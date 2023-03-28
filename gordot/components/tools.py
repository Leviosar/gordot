import qtawesome as qta

from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QFormLayout, QTableWidget, QTableWidgetItem, QTreeView
from PyQt5.QtGui import QStandardItemModel, QColor, QBrush, QStandardItem, QMouseEvent, QIcon
from PyQt5.QtCore import QSize

from gordot import state
from gordot.utils import Coord
from gordot.shapes import Point, Line, Shape, Wireframe
from gordot.tools import PanTool, ZoomTool
from gordot.components import VerticalTabWidget
from PyQt5.QtCore import Qt, pyqtSignal

from typing import List

class ToolsMenu(QWidget):
    def __init__(self, viewport):
        super().__init__()

        tabs = [
            { "widget": ObjectsCreationTool(viewport), "name": "Objects"},
            { "widget": ZoomTool(viewport), "name": "Zoom"},
            { "widget": PanTool(viewport), "name": "Move"},
        ]

        tab_bar = VerticalTabWidget()
        tab_bar.setIconSize(QSize(24, 24))

        for tab in tabs:
            tab_bar.addTab(tab["widget"], tab["widget"].icon, "")

        layout = QVBoxLayout()
        layout.addWidget(tab_bar)

        self.setLayout(layout)

class ObjectsCreationTool(QWidget):

    icon: QIcon

    def __init__(self, viewport):
        super().__init__()

        self.icon = qta.icon('fa5s.cube')

        tabs = [
            { "widget": PointTab(viewport), "name": "Point"},
            { "widget": LineTab(viewport), "name": "Line"},
            { "widget": WireframeTab(viewport), "name": "Wireframe"},
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
            self.name_lineEdit.text(),
            state.primary_color
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
            self.name_lineEdit.text(),
            state.primary_color
        )

        self.add_shape(line)


class WireframeTab(ObjectCreatorTab):

    fields: List[List[QLineEdit]] = []

    min_points: int = 3

    current_points: int = 0

    fields_layout: QFormLayout

    def __init__(self, viewport):
        super().__init__(viewport)

        self.fields_layout = QFormLayout()
        
        for i in range(self.min_points):
            self.add_point_row(i)

        add_button = QPushButton(qta.icon('fa5s.plus'), '')
        add_button.clicked.connect(self.add_row_callback)

        layout = QVBoxLayout()
        layout.addWidget(self.name_lineEdit)
        layout.addLayout(self.fields_layout)
        layout.addWidget(add_button)
        layout.addWidget(self.create_button)

        self.setLayout(layout)

    def add_point_row(self, index: int, defaults = ['', '']):
        self.current_points += 1

        row = QHBoxLayout()
            
        x_input = QLineEdit()
        x_input.setPlaceholderText("X")
        x_input.setText(defaults[0])
        
        y_input = QLineEdit()
        y_input.setPlaceholderText("Y")
        y_input.setText(defaults[1])

        delete_button = QPushButton(qta.icon('fa5s.trash'), '')
        delete_button.clicked.connect(lambda: self.delete_row_callback(row))

        row.addWidget(x_input, 5)
        row.addWidget(y_input, 5)
        row.addWidget(delete_button, 2)

        self.fields.append([x_input, y_input])

        self.fields_layout.addRow(row)


    def add_row_callback(self):
        self.add_point_row(len(self.fields))


    def delete_row_callback(self, index: int, row: QWidget):
        if self.current_points <= 3:
            return
        
        self.fields.pop(index)
        self.fields_layout.removeRow(row)


    def create_callback(self):
        coords = [
            Coord(
                int(self.fields[i][0].text()),
                int(self.fields[i][1].text())
            )

            for i in range(len(self.fields))
        ]

        wireframe = Wireframe(coords, self.name_lineEdit.text(), state.primary_color)

        self.add_shape(wireframe)
