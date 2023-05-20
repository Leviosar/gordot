from PyQt5.QtWidgets import QLineEdit, QFormLayout

from gordot import state
from gordot.shapes import Line
from gordot.structures import Vector
from gordot.tools import ObjectTool
from gordot.components import Viewport

class LineTool(ObjectTool):
    def __init__(self, viewport: Viewport):
        super().__init__(viewport)

        self.x1_input = QLineEdit()
        self.y1_input = QLineEdit()
        self.x2_input = QLineEdit()
        self.y2_input = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Name", self.name_input)
        layout.addRow("X0", self.x1_input)
        layout.addRow("Y0", self.y1_input)
        layout.addRow("X1", self.x2_input)
        layout.addRow("Y1", self.y2_input)
        layout.addRow(self.create_button)

        self.setLayout(layout)

    def create_callback(self):
        x1 = int(self.x1_input.text())
        y1 = int(self.y1_input.text())
        x2 = int(self.x2_input.text())
        y2 = int(self.y2_input.text())

        line = Line(
            Vector(x1, y1),
            Vector(x2, y2),
            self.name_input.text(),
            state.primary_color
        )

        self.add_shape(line)