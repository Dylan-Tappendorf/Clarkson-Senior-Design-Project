import tkinter as tk
from tkinter import ttk, messagebox
import serial
import serial.tools.list_ports
import threading
import queue
import re
from collections import deque

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class LiveLidarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("EFM32 Live UART LiDAR Dashboard")
        self.root.geometry("950x650")
        self.root.configure(bg="#1e1e2e")

        self.serial_port = None
        self.is_connected = False
        self.data_queue = queue.Queue()

        self.max_pts = 50
        self.x_data = deque(maxlen=self.max_pts)
        self.phase_data = deque(maxlen=self.max_pts)
        self.vi_data = deque(maxlen=self.max_pts)
        self.vq_data = deque(maxlen=self.max_pts)
        self.sample_index = 0

        self.pattern = re.compile(
            r"Vi:[ \t]*([+-]?\d+(?:\.\d+)?)\s*V"
            r".*?Vq:[ \t]*([+-]?\d+(?:\.\d+)?)\s*V"
            r".*?Vctrl:[ \t]*([+-]?\d+(?:\.\d+)?)\s*V"
            r".*?Phase:[ \t]*([+-]?\d+(?:\.\d+)?)\s*deg",
            re.IGNORECASE
        )

        self._build_ui()
        self._poll_uart_queue()
        self.root.protocol("WM_DELETE_WINDOW", self._on_close)

    def _build_ui(self):
        top_frame = tk.Frame(self.root, bg="#2b2b3b", pady=10, padx=15)
        top_frame.pack(fill="x")

        tk.Label(top_frame, text="Port:", fg="#cdd6f4", bg="#2b2b3b", font=("Segoe UI", 10, "bold")).pack(side="left", padx=5)

        self.port_cb = ttk.Combobox(top_frame, width=10, state="normal")
        self.port_cb.pack(side="left", padx=5)
        self._refresh_com_ports()

        self.btn_connect = tk.Button(
            top_frame,
            text="Connect COM3",
            bg="#a6e3a1",
            fg="#11111b",
            font=("Segoe UI", 10, "bold"),
            command=self.toggle_uart_connection,
        )
        self.btn_connect.pack(side="left", padx=10)

        self.btn_refresh = tk.Button(
            top_frame,
            text="Refresh Ports",
            bg="#89b4fa",
            fg="#11111b",
            font=("Segoe UI", 9, "bold"),
            command=self._refresh_com_ports,
        )
        self.btn_refresh.pack(side="left", padx=5)

        self.status_label = tk.Label(
            top_frame,
            text="UART Disconnected",
            fg="#f38ba8",
            bg="#2b2b3b",
            font=("Segoe UI", 10, "italic"),
        )
        self.status_label.pack(side="right", padx=10)

        cards_frame = tk.Frame(self.root, bg="#1e1e2e", pady=10)
        cards_frame.pack(fill="x", padx=15)

        self.val_phase = self._add_card(cards_frame, "PHASE SHIFT", "-- °", "#f9e2af", 0)
        self.val_vi = self._add_card(cards_frame, "IN-PHASE (Vi)", "-- V", "#89b4fa", 1)
        self.val_vq = self._add_card(cards_frame, "QUADRATURE (Vq)", "-- V", "#cba6f7", 2)
        self.val_vctrl = self._add_card(cards_frame, "CONTROL (Vctrl)", "-- V", "#74c7ec", 3)

        plt.style.use("dark_background")
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(8, 4), sharex=True)
        self.fig.patch.set_facecolor("#1e1e2e")

        self.ax1.set_facecolor("#181825")
        self.ax2.set_facecolor("#181825")

        (self.line_phase,) = self.ax1.plot([], [], color="#f9e2af", lw=2, label="Phase Shift (°)")
        (self.line_vi,) = self.ax2.plot([], [], color="#89b4fa", lw=1.5, label="Vi (V)")
        (self.line_vq,) = self.ax2.plot([], [], color="#cba6f7", lw=1.5, label="Vq (V)")

        self.ax1.set_ylabel("Phase (°)", color="#cdd6f4")
        self.ax1.grid(True, color="#313244", linestyle="--", alpha=0.5)
        self.ax1.legend(loc="upper left")

        self.ax2.set_ylabel("Voltage (V)", color="#cdd6f4")
        self.ax2.set_xlabel("UART Samples Received", color="#cdd6f4")
        self.ax2.grid(True, color="#313244", linestyle="--", alpha=0.5)
        self.ax2.legend(loc="upper left")

        self.fig.tight_layout()

        plot_container = tk.Frame(self.root, bg="#1e1e2e")
        plot_container.pack(fill="both", expand=True, padx=15, pady=5)

        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_container)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def _add_card(self, parent, title, text_init, text_color, col_idx):
        box = tk.Frame(parent, bg="#2b2b3b", padx=15, pady=10)
        box.grid(row=0, column=col_idx, sticky="nsew", padx=5)
        parent.grid_columnconfigure(col_idx, weight=1)

        tk.Label(box, text=title, fg="#a6adc8", bg="#2b2b3b", font=("Segoe UI", 9, "bold")).pack(anchor="w")
        lbl = tk.Label(box, text=text_init, fg=text_color, bg="#2b2b3b", font=("Segoe UI", 18, "bold"))
        lbl.pack(anchor="w", pady=(2, 0))
        return lbl

    def _refresh_com_ports(self):
        available_ports = [p.device for p in serial.tools.list_ports.comports()]
        if "COM3" not in available_ports:
            available_ports.append("COM3")
        self.port_cb["values"] = available_ports
        self.port_cb.set("COM3")

    def toggle_uart_connection(self):
        if not self.is_connected:
            selected_port = self.port_cb.get().strip()
            if not selected_port:
                messagebox.showerror("Port Error", "No COM port specified.")
                return

            try:
                self.serial_port = serial.Serial(selected_port, 115200, timeout=1)
                self.serial_port.reset_input_buffer()

                self.is_connected = True
                self.btn_connect.config(text="Disconnect", bg="#f38ba8")
                self.status_label.config(
                    text=f"Receiving live stream on {selected_port}", fg="#a6e3a1"
                )

                threading.Thread(target=self._uart_read_thread, daemon=True).start()
            except Exception as err:
                messagebox.showerror(
                    "Serial Connection Failed", f"Could not open {selected_port}:\n{str(err)}"
                )
        else:
            self._disconnect_uart()

    def _disconnect_uart(self):
        self.is_connected = False
        if self.serial_port and self.serial_port.is_open:
            try:
                self.serial_port.close()
            except Exception:
                pass
        self.btn_connect.config(text="Connect COM3", bg="#a6e3a1")
        self.status_label.config(text="UART Disconnected", fg="#f38ba8")

    def _uart_read_thread(self):
        while self.is_connected and self.serial_port and self.serial_port.is_open:
            try:
                if self.serial_port.in_waiting > 256:
                    self.serial_port.reset_input_buffer()

                raw_line = self.serial_port.readline().decode("utf-8", errors="ignore").strip()
                if raw_line:
                    self.data_queue.put(raw_line)
            except Exception:
                break

    def _poll_uart_queue(self):
        while not self.data_queue.empty():
            raw_line = self.data_queue.get()
            self._update_gui_from_uart_string(raw_line)

        self.root.after(30, self._poll_uart_queue)

    def _update_gui_from_uart_string(self, raw_line):
        match = self.pattern.search(raw_line)
        if match:
            vi_val = float(match.group(1))
            vq_val = float(match.group(2))
            vctrl_val = float(match.group(3))
            phase_val = float(match.group(4))

            self.val_phase.config(text=f"{phase_val:.2f} °")
            self.val_vi.config(text=f"{vi_val:.2f} V")
            self.val_vq.config(text=f"{vq_val:.2f} V")
            self.val_vctrl.config(text=f"{vctrl_val:.2f} V")

            self.sample_index += 1
            self.x_data.append(self.sample_index)
            self.phase_data.append(phase_val)
            self.vi_data.append(vi_val)
            self.vq_data.append(vq_val)

            self.line_phase.set_data(self.x_data, self.phase_data)
            self.line_vi.set_data(self.x_data, self.vi_data)
            self.line_vq.set_data(self.x_data, self.vq_data)

            self.ax1.relim()
            self.ax1.autoscale_view()
            self.ax2.relim()
            self.ax2.autoscale_view()

            self.canvas.draw_idle()

    def _on_close(self):
        self._disconnect_uart()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = LiveLidarGUI(root)
    root.mainloop()