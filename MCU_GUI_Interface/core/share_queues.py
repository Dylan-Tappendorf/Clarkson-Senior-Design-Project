"""
Shared Memory and Thread Synchronization.

Role:
- Hosts the thread-safe queues connecting the Producer (UART) and Consumer (UI).
- Defines the raw byte Queue for incoming hardware data.
- Defines the high-speed ring buffer (deque) for real-time plotting.
- Holds threading.Event() flags for inter-module signaling (e.g., 'stop_event', 'save_event').
"""