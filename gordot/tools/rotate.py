from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout, QPushButton, QHBoxLayout

from gordot import state
from gordot.components import Viewport
from gordot.utils import Transform, Coord

class RotateTool(QWidget):
    def  __init__(self, viewport: Viewport):
        QWidget.__init__(self)

        self.viewport = viewport

        self.angle_field = QLineEdit()
        self.angle_field.setPlaceholderText("Angle")

        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.handle)

        row = QHBoxLayout()

        row.addWidget(self.angle_field)
        row.addWidget(self.apply_button)

        self.setLayout(row)

    def handle(self):
        if state.selected_shape is None:
            return
        
        angle = self.angle_field.text()

        matrix = Transform.rotate(float(angle))
        state.selected_shape.transform(matrix)
        self.viewport.repaint()