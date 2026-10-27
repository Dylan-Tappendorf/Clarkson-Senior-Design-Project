"""
Real-Time Visualization Engine.

Role:
- Manages the high-performance plotting canvases (e.g., PyQtGraph).
- Runs a QTimer synchronized with the GUI event loop.
- Periodically samples the shared ring buffer (deque) and updates the plot curves.
- Isolated from hardware delays to ensure 60FPS UI rendering.
"""