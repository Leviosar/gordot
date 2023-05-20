import qtawesome as qta
import math

from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton, QFormLayout
from PyQt5.QtGui import QIcon

from gordot.shapes import Shape
from gordot.components import Viewport

class RotateViewportTool(QWidget):

    viewport: Viewport

    angle_input: QLineEdit

    action_button: QPushButton
    
    icon: QIcon

    def __init__(self, viewport):
        super().__init__()

        self.viewport = viewport
        
        self.icon = qta.icon('fa5s.sync')
        
        self.angle_input = QLineEdit()

        self.action_button = QPushButton("Rotate")
        
        self.action_button.pressed.connect(self.handle)
        
        layout = QFormLayout()
        layout.addRow("Angle (degrees)", self.angle_input)
        layout.addRow(self.action_button)

        self.setLayout(layout)

    def handle(self):
        angle = math.radians(float(self.angle_input.text()))
        self.viewport.rotate(angle)

