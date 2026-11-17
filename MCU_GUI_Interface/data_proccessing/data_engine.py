import numpy as np
import scipy.signal as signal
import struct
import Config.settings as settings
from hardware.uart_recv import raw_data

"""
Data Processing and Routing (Middleman Thread).

Role:
- Consumes raw bytes from the hardware RawDataQueue.
- Decodes, validates, and parses the byte stream into structured Python objects.
- Applies any necessary mathematical scaling or filtering.
- Distributes the clean data to the UI ring buffer and the file writer queue.
"""
header_format = f"BHIi"
data_format = f"{settings.NUM_SAMPLES}h"

if len(raw_data) == settings.BYTES_TO_READ:
    header = struct.unpack(header_format, raw_data[:8])
    data = struct.unpack(data_format, raw_data[8:])
    v_i = (data.astype(np.float32) * 3.3 / 4095.0) - 1.65


N = len(v_i)
dt = 1.0 / settings.ADC_SAMPLE_RATE_HZ
t = np.arange(N) * dt

analitical_signal = signal.hilbert(v_i)
phase = np.unwrap(np.angle(analitical_signal))
