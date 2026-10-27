"""
Main Application Entry Point.

Role:
- Initializes thread-safe queues and shared memory buffers.
- Spawns and manages the UART background thread and Data Processing thread.
- Launches the main GUI event loop.
- Catches exit events to safely close threads, release the COM port, and terminate.
"""