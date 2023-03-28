from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout, QPushButton, QHBoxLayout

from gordot import state
from gordot.components import Viewport
from gordot.utils import Transform, Coord

class TranslateTool(QWidget):
    def  __init__(self, viewport: Viewport):
        QWidget.__init__(self)

        self.viewport = viewport

        self.x_field = QLineEdit()
        self.x_field.setPlaceholderText("X")
        
        self.y_field = QLineEdit()
        self.y_field.setPlaceholderText("Y")

        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.handle)

        row = QHBoxLayout()

        row.addWidget(self.x_field)
        row.addWidget(self.y_field)
        row.addWidget(self.apply_button)

        self.setLayout(row)

    def handle(self):
        if state.selected_shape is None:
            return
        
        x = self.x_field.text()
        y = self.y_field.text()

        delta = Coord(x, y)
        matrix = Transform.translate(delta)
        state.selected_shape.transform(matrix)
        self.viewport.repaint()