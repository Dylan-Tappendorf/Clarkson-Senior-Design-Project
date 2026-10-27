
"""
Data Processing and Routing (Middleman Thread).

Role:
- Consumes raw bytes from the hardware RawDataQueue.
- Decodes, validates, and parses the byte stream into structured Python objects.
- Applies any necessary mathematical scaling or filtering.
- Distributes the clean data to the UI ring buffer and the file writer queue.
"""