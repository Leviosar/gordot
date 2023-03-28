import qtawesome as qta

from gordot.components import Viewport

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QMouseEvent, QIcon
from PyQt5.QtCore import Qt

class ZoomTool(QWidget):

    icon: QIcon

    def __init__(self, viewport: Viewport):
        super().__init__()
        
        self.icon = qta.icon('fa5s.search-plus')

        self.viewport = viewport
        
        self.viewport.on_mouse_double_clicked.connect(self.handle)
        
    def handle(self, event: QMouseEvent):
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.viewport.zoom_in(0.25)
        else:
            self.viewport.zoom_out(0.25)
