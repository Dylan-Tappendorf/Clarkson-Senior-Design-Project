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
NUM_SAMPLES = 512
BYTES_TO_READ = 1035
SYNC_HEADER = b"\xaa\x55\xaa\x55"
CYCLES_TO_DISPLAY = 5
TUNING_CURVE_FILE = 'ZOS-150+_Tuning_Data.xlsx'


