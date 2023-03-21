from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QFormLayout

from gordot.utils import Coord
from gordot.shapes import Point, Line, Shape

class ToolsMenu(QWidget):
    def __init__(self, viewport):
        super().__init__()

        tabs = [
            { "widget": ZoomTool(viewport), "name": "Zoom"},
            { "widget": PanTool(viewport), "name": "Move"},
            { "widget": ObjectsCreationTool(viewport), "name": "Objects"},
        ]

        tab_bar = QTabWidget()
        
        for tab in tabs:
            tab_bar.addTab(tab["widget"], tab["name"])

        layout = QVBoxLayout()
        layout.addWidget(tab_bar)

        self.setLayout(layout)

class ZoomTool(QWidget):
    def __init__(self, viewport):
        super().__init__()
        
        self.viewport = viewport
        
        self.zoom_in = QPushButton("+")
        self.zoom_out = QPushButton("-")
        
        self.zoom_in.clicked.connect(lambda: self.viewport.zoom_in(0.1))
        self.zoom_out.clicked.connect(lambda: self.viewport.zoom_out(0.1))

        layout = QHBoxLayout()
        layout.addWidget(self.zoom_out)
        layout.addWidget(QLabel("<center><h6>Zoom</h6><\center>"))
        layout.addWidget(self.zoom_in)

        self.setLayout(layout)

class PanTool(QWidget):
    def __init__(self, viewport):
        super().__init__()

        self.viewport = viewport

        self.up = QPushButton("Up")
        self.down = QPushButton("Down")
        self.left = QPushButton("Left")
        self.right = QPushButton("Right")

        self.up.clicked.connect(lambda: self.viewport.move_up(15))
        self.down.clicked.connect(lambda: self.viewport.move_down(15))
        self.left.clicked.connect(lambda: self.viewport.move_left(15))
        self.right.clicked.connect(lambda: self.viewport.move_right(15))

        layout = QVBoxLayout()
        layout.addWidget(self.up)
        layout.addWidget(self.down)
        layout.addWidget(self.left)
        layout.addWidget(self.right)

        self.setLayout(layout)

class ObjectsCreationTool(QWidget):
    def __init__(self, viewport):
        super().__init__()

        tabs = [
            { "widget": PointTab(viewport), "name": "Point"},
            { "widget": LineTab(viewport), "name": "Line"},
        ]

        tab_bar = QTabWidget()

        for tab in tabs:
            tab_bar.addTab(tab["widget"], tab["name"])

        layout = QVBoxLayout()
        layout.addWidget(tab_bar)

        self.setLayout(layout)

class ObjectCreatorTab(QWidget):
    def __init__(self, viewport):
        super().__init__()

        self.viewport = viewport

        self.name_lineEdit = QLineEdit()
        self.create_button = QPushButton("Create")

        self.create_button.pressed.connect(self.create_callback)

    def add_shape(self, shape: Shape):
        self.viewport.add_shape(shape)

    def create_callback(self):
        raise "Implementa ai fera"


class PointTab(ObjectCreatorTab):
    def __init__(self, viewport):
        super().__init__(viewport)

        self.x_lineEdit = QLineEdit()
        self.y_lineEdit = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Name", self.name_lineEdit)
        layout.addRow("X", self.x_lineEdit)
        layout.addRow("Y", self.y_lineEdit)
        layout.addRow(self.create_button)

        self.setLayout(layout)

    def create_callback(self):
        x = int(self.x_lineEdit.text())
        y = int(self.y_lineEdit.text())

        point = Point(
            Coord(x, y),
            self.name_lineEdit.text()
        )

        self.add_shape(point)


class LineTab(ObjectCreatorTab):
    def __init__(self, viewport):
        super().__init__(viewport)

        self.x1_lineEdit = QLineEdit()
        self.y1_lineEdit = QLineEdit()
        self.x2_lineEdit = QLineEdit()
        self.y2_lineEdit = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Name", self.name_lineEdit)
        layout.addRow("X0", self.x1_lineEdit)
        layout.addRow("Y0", self.y1_lineEdit)
        layout.addRow("X1", self.x2_lineEdit)
        layout.addRow("Y1", self.y2_lineEdit)
        layout.addRow(self.create_button)

        self.setLayout(layout)

    def create_callback(self):
        x1 = int(self.x1_lineEdit.text())
        y1 = int(self.y1_lineEdit.text())
        x2 = int(self.x2_lineEdit.text())
        y2 = int(self.y2_lineEdit.text())

        line = Line(
            Coord(x1, y1),
            Coord(x2, y2),
            self.name_lineEdit.text()
        )

        self.add_shape(line)
