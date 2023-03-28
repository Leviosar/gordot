import qtawesome as qta

from gordot.components import Viewport
from gordot.utils import Coord

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QMouseEvent, QIcon
from PyQt5.QtCore import Qt

class PanTool(QWidget):
    
    enabled: bool = False
    started: bool = False
    icon: QIcon

    def __init__(self, viewport: Viewport):
        super().__init__()

        self.icon = qta.icon('fa5s.arrows-alt')

        self.viewport = viewport

        self.viewport.on_mouse_pressed.connect(self.start)
        self.viewport.on_mouse_moved.connect(self.move_)

    def start(self, event: QMouseEvent):
        self.started = True
        self.last_point = Coord(event.x(), event.y())

    def move_(self, event: QMouseEvent):
        if not self.started:
            return
        
        current = Coord(event.x(), event.y())

        self.viewport.pan(current - self.last_point)
        
        self.last_point = current