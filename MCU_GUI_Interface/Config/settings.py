"""
Global Configuration and Constants.

Role:
- Acts as the single source of truth for hardcoded settings.
- Contains hardware parameters (BAUD_RATE, PORT).
- Contains software parameters (MAX_PLOT_POINTS, REFRESH_RATE_MS).
- Contains storage paths and UI theme colors.
"""

SERIAL_PORT = "COM3"
BAUD_RATE = 115200  # Match init_usart4() in main.c
ADC_SAMPLE_RATE_HZ = 1_000_000.0  # 1.000 MHz
NUM_SAMPLES = 2048  # Match NUM_SAMPLES in app.c (e.g. 100000 or 2048)
BYTES_TO_READ = NUM_SAMPLES * 2
SYNC_HEADER = b"\xaa\x55\xaa\x55"
CYCLES_TO_DISPLAY = 5

