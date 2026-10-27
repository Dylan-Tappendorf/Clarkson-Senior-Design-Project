"""
Asynchronous File I/O and Export.

Role:
- Monitors the 'save_event' flag triggered by the UI.
- When active, pulls formatted data from the storage queue.
- Handles safe file writing (CSV/binary) without blocking the hardware 
  reader or freezing the UI.
"""