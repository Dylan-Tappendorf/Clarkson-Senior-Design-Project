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



def open_port(port = SERIAL_PORT, baudrate = BAUD_RATE, timeout = 1):
    """
    Open the serial port with the given parameters.

    Args:
        port (str): The COM port to open (e.g., "COM3").
        baudrate (int): The baud rate for the connection.
        timeout (float): The timeout for the connection.

    Returns:
        serial.Serial: The opened serial port object.
    """

    try:
        ser = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        return ser
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return None

    