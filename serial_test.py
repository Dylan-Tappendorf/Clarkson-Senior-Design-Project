import threading
import time
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as signal
import serial

# --- CONFIGURATION (Must match your firmware in app.c / main.c) ---
SERIAL_PORT = "COM3"
BAUD_RATE = 115200  # Match init_usart4() in main.c
ADC_SAMPLE_RATE_HZ = 1_000_000.0  # 1.000 MHz
NUM_SAMPLES = 100_000  # Match NUM_SAMPLES in app.c (e.g. 100000 or 2048)
BYTES_TO_READ = NUM_SAMPLES * 2
SYNC_HEADER = b"\xaa\x55\xaa\x55"
CYCLES_TO_DISPLAY = 5

# Shared thread-safe state for the latest frame
latest_v_i = None
frame_counter = 0
data_lock = threading.Lock()
stop_event = threading.Event()


def serial_reader_worker():
    """Background thread that continuously syncs and reads full sample bursts."""
    global latest_v_i, frame_counter
    ser = None

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
        ser.reset_input_buffer()
        print(
            f"[Reader] Connected to {SERIAL_PORT} at {BAUD_RATE} baud. Listening for frames..."
        )

        while not stop_event.is_set():
            # 1. Hunt for the 4-byte sync header (0xAA 0x55 0xAA 0x55)
            window = bytearray()
            synced = False
            while not stop_event.is_set():
                b = ser.read(1)
                if not b:
                    continue
                window += b
                if len(window) > 4:
                    window.pop(0)
                if bytes(window) == SYNC_HEADER:
                    synced = True
                    break

            if not synced or stop_event.is_set():
                break

            # 2. Read the full binary payload for this burst
            raw_buffer = bytearray()
            while len(raw_buffer) < BYTES_TO_READ and not stop_event.is_set():
                chunk = ser.read(min(8192, BYTES_TO_READ - len(raw_buffer)))
                if not chunk:
                    break
                raw_buffer.extend(chunk)

            # 3. Unpack and hand off to the plotting thread if complete
            if len(raw_buffer) == BYTES_TO_READ:
                data = np.frombuffer(raw_buffer, dtype="<u2")
                v_i = (data.astype(np.float32) * 3.3 / 4095.0) - 1.65

                with data_lock:
                    latest_v_i = v_i
                    frame_counter += 1
                print(
                    f"[Reader] Frame #{frame_counter} received ({len(v_i)} samples)."
                )

    except serial.SerialException as e:
        print(f"[Reader] Serial error: {e}")
    except PermissionError:
        print(
            "[Reader] Permission denied. Make sure COM3 isn't open in another program."
        )
    finally:
        if ser is not None and ser.is_open:
            ser.close()
            print("[Reader] Serial port closed.")


# Start background serial acquisition thread
reader_thread = threading.Thread(target=serial_reader_worker, daemon=True)
reader_thread.start()

# --- SETUP MATPLOTLIB FIGURE ---
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 8))
fig.suptitle("Real-Time 1 MSPS Sine Wave & Unwrapped Phase Monitor")

# 1. Top Plot: Sampled Sine Wave + Fitted Wave
(line_vi,) = ax1.plot([], [], "-o", markersize=3, label="Sampled Vi")
(line_fit,) = ax1.plot(
    [], [], "--", color="red", alpha=0.8, label="Unwrapped Fit"
)
ax1.set_ylabel("Amplitude (V)")
ax1.grid(True)
ax1.legend(loc="upper right")

# 2. Middle Plot: Continuous Unwrapped Phase Ramp
(line_unwrapped,) = ax2.plot(
    [], [], "-", linewidth=2, color="tab:purple", label="Unwrapped Phase Φ(t)"
)
ax2.set_ylabel("Unwrapped Phase (deg)")
ax2.grid(True)
ax2.legend(loc="upper left")

# 3. Bottom Plot: Detrended Phase Offset
(line_offset,) = ax3.plot(
    [], [], "-", color="tab:green", label="Detrended Phase Offset φ(t)"
)
(line_mean_offset,) = ax3.plot(
    [], [], "--", color="red", label="Mean Phase Offset"
)
ax3.set_ylabel("Phase Offset (deg)")
ax3.set_ylim(0, 360)
ax3.grid(True)
ax3.legend(loc="upper right")

last_plotted_frame = -1


def update_plot( _ ):
    global last_plotted_frame

    with data_lock:
        if latest_v_i is None or frame_counter == last_plotted_frame:
            return (
                line_vi,
                line_fit,
                line_unwrapped,
                line_offset,
                line_mean_offset,
            )
        v_i = latest_v_i.copy()
        current_frame = frame_counter
        last_plotted_frame = current_frame

    N = len(v_i)
    dt = 1.0 / ADC_SAMPLE_RATE_HZ
    t = np.arange(N) * dt

    # 1. Remove residual DC offset
    v_i_ac = v_i - np.mean(v_i)

    # 2. Compute Analytic Signal via Hilbert Transform
    analytic_signal = signal.hilbert(v_i_ac)

    # 3. Extract and UNWRAP Phase (referenced to a Sine wave by adding pi/2)
    wrapped_phase_rad = np.angle(analytic_signal) + (np.pi / 2.0)
    unwrapped_phase_rad = np.unwrap(wrapped_phase_rad)
    unwrapped_phase_deg = np.degrees(unwrapped_phase_rad)

    # 4. Linear Least-Squares Fit on interior 80% (avoids Hilbert edge ringing)
    trim = max(1, N // 10)
    slope_rad_s, intercept_rad = np.polyfit(
        t[trim:-trim], unwrapped_phase_rad[trim:-trim], 1
    )

    detected_freq_hz = abs(slope_rad_s) / (2.0 * np.pi)
    initial_phase_deg_360 = np.degrees(intercept_rad) % 360.0

    # Detrended phase offset trace
    phase_offset_trace_deg = (
        np.degrees(unwrapped_phase_rad - (slope_rad_s * t)) % 360.0
    )

    # Auto-select time axis unit (µs vs ms)
    if detected_freq_hz >= 10_000:
        time_scale, time_unit = 1e6, "µs"
    else:
        time_scale, time_unit = 1e3, "ms"

    t_scaled = t * time_scale
    period_scaled = (
        (1.0 / detected_freq_hz) * time_scale
        if detected_freq_hz > 0
        else t_scaled[-1]
    )
    max_x = min(t_scaled[-1], CYCLES_TO_DISPLAY * period_scaled)
    zoom_mask = t_scaled <= max_x

    t_zoom = t_scaled[zoom_mask]
    vi_zoom = v_i_ac[zoom_mask]
    unwrapped_zoom = unwrapped_phase_deg[zoom_mask]
    offset_zoom = phase_offset_trace_deg[zoom_mask]

    # Reconstructed sine fit over zoom window
    amp_est = np.std(v_i_ac) * np.sqrt(2.0)
    fitted_sine = amp_est * np.sin(slope_rad_s * t[zoom_mask] + intercept_rad)

    # Update Top Subplot (Wave + Fit)
    line_vi.set_data(t_zoom, vi_zoom)
    line_fit.set_data(t_zoom, fitted_sine)
    ax1.set_xlim(0, max_x)
    y_max = max(0.1, np.max(np.abs(vi_zoom)) * 1.25)
    ax1.set_ylim(-y_max, y_max)
    ax1.set_title(
        f"Frame #{current_frame} | Freq: {detected_freq_hz / 1e3:.2f} kHz | "
        f"Initial Sine Phase (t=0): {initial_phase_deg_360:.2f}°"
    )
    ax1.set_xlabel(f"Time ({time_unit})")

    # Update Middle Subplot (Unwrapped Phase)
    line_unwrapped.set_data(t_zoom, unwrapped_zoom)
    ax2.set_xlim(0, max_x)
    ax2.set_ylim(np.min(unwrapped_zoom) - 20, np.max(unwrapped_zoom) + 20)
    ax2.set_title(
        f"Unwrapped Phase Φ(t) = 360·f·t + φ₀ (Intercept φ₀ = {initial_phase_deg_360:.2f}°)"
    )
    ax2.set_xlabel(f"Time ({time_unit})")

    # Update Bottom Subplot (Detrended Phase Offset)
    line_offset.set_data(t_zoom, offset_zoom)
    line_mean_offset.set_data(
        [0, max_x], [initial_phase_deg_360, initial_phase_deg_360]
    )
    ax3.set_xlim(0, max_x)
    ax3.set_title(
        f"Extracted Phase Offset (Mean: {initial_phase_deg_360:.2f}°)"
    )
    ax3.set_xlabel(f"Time ({time_unit})")

    return line_vi, line_fit, line_unwrapped, line_offset, line_mean_offset


ani = animation.FuncAnimation(
    fig, update_plot, interval=100, blit=False, cache_frame_data=False
)

try:
    plt.tight_layout()
    plt.show()
finally:
    stop_event.set()
    reader_thread.join(timeout=2.0)