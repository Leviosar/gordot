from PyQt5.QtWidgets import QLineEdit, QFormLayout

from gordot import state
from gordot.shapes import Point
from gordot.structures import Vector
from gordot.tools import ObjectTool
from gordot.components import Viewport

class PointTool(ObjectTool):
    def __init__(self, viewport: Viewport):
        super().__init__(viewport)

        self.x_input = QLineEdit()
        self.y_input = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Name", self.name_input)
        layout.addRow("X", self.x_input)
        layout.addRow("Y", self.y_input)
        layout.addRow(self.create_button)

        self.setLayout(layout)

    def create_callback(self):
        x = int(self.x_input.text())
        y = int(self.y_input.text())

        point = Point(
            Vector(x, y),
            self.name_input.text(),
            state.primary_color
        )

        self.add_shape(point)