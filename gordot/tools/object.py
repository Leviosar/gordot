from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton

from gordot.shapes import Shape
from gordot.components import Viewport

class ObjectTool(QWidget):

    viewport: Viewport

    name_input: QLineEdit

    create_button: QPushButton

    def __init__(self, viewport):
        super().__init__()

        self.viewport = viewport

        self.name_input = QLineEdit()

        self.create_button = QPushButton("Create")

        self.create_button.pressed.connect(self.create_callback)

    def add_shape(self, shape: Shape):
        self.viewport.add_shape(shape)

    def create_callback(self):
        raise "Implementa ai fera"
