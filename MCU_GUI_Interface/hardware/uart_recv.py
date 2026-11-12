"""
UART Hardware Interface (Producer Thread).

Role:
- Opens and manages the PySerial connection to the hardware.
- Runs in an isolated background thread to prevent UI blocking.
- Reads raw bytes from the buffer and pushes them directly into the RawDataQueue.
- Does NOT parse data; only extracts hardware bytes.
"""

import serial
import threading
import numpy as np
from Config.settings import SERIAL_PORT, BAUD_RATE, BYTES_TO_READ, SYNC_HEADER







    