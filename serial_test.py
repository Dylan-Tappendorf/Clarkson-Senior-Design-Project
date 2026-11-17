import serial
import struct
import time

# Configure these to match your system
SERIAL_PORT = 'COM3'  # e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux
BAUD_RATE = 115200
MSG_TYPE_ADC_BURST = 0x01

def main():
    # Open the serial port
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2.0)
        print(f"Listening on {SERIAL_PORT} at {BAUD_RATE} baud...")
    except serial.SerialException as e:
        print(f"Error opening serial port: {e}")
        return

    while True:
        try:
            # 1. Sync to the message type byte
            sync_byte = ser.read(1)
            if not sync_byte:
                continue # Timeout, try again
                
            if sync_byte[0] != MSG_TYPE_ADC_BURST:
                # If we get out of sync, discard bytes until we find the 0x01 header
                continue

            # 2. Read the rest of the 11-byte header (10 bytes remaining)
            header_rest = ser.read(10)
            if len(header_rest) != 10:
                print("Warning: Incomplete header received")
                continue

            # Unpack the 10 bytes:
            # < = Little Endian
            # H = unsigned short (16-bit) -> Message Number
            # I = unsigned int (32-bit)   -> Number of Samples
            # I = unsigned int (32-bit)   -> Timestamp
            msg_num, num_samples, timestamp_ms = struct.unpack('<HII', header_rest)

            # 3. Read the payload (Number of samples * 2 bytes per 16-bit sample)
            expected_payload_bytes = num_samples * 2
            payload_data = ser.read(expected_payload_bytes)

            if len(payload_data) != expected_payload_bytes:
                print(f"Warning: Expected {expected_payload_bytes} payload bytes, got {len(payload_data)}")
                continue

            # 4. Unpack the payload into a tuple of 16-bit signed integers
            # < = Little Endian
            # h = signed short (16-bit)
            # We dynamically build the format string based on num_samples (e.g., '<512h')
            samples = struct.unpack(f'<{num_samples}h', payload_data)

            # 5. Process or display the data
            print(f"--- Message {msg_num} ---")
            print(f"Time: {timestamp_ms} ms")
            print(f"Samples received: {len(samples)}")
            print(f"First 5 samples: {samples[:5]}")
            print(f"Last 5 samples:  {samples[-5:]}\n")

        except KeyboardInterrupt:
            print("Stopping...")
            break
        except Exception as e:
            print(f"Error reading stream: {e}")
            break

    ser.close()

if __name__ == '__main__':
    main()