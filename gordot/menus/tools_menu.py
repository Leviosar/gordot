import qtawesome as qta

from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel, QLineEdit, QFormLayout, QTableWidget, QTableWidgetItem, QTreeView
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

from gordot.structures import Vector
from gordot.tools import PanTool, ZoomTool, PointTool, LineTool, WireframeTool, BezierTool, RotateViewportTool
from gordot.components import VerticalTabWidget

from typing import List

class ToolsMenu(QWidget):
    def __init__(self, viewport):
        super().__init__()

        tabs = [
            { "widget": ObjectsCreationTool(viewport), "name": "Objects"},
            { "widget": ZoomTool(viewport), "name": "Zoom"},
            { "widget": PanTool(viewport), "name": "Move"},
            { "widget": RotateViewportTool(viewport), "name": "Rotate"},
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
            { "widget": PointTool(viewport), "name": "Point"},
            { "widget": LineTool(viewport), "name": "Line"},
            { "widget": WireframeTool(viewport), "name": "Wireframe"},
            { "widget": BezierTool(viewport), "name": "Bezier"},
        ]

        tab_bar = QTabWidget()

        for tab in tabs:
            tab_bar.addTab(tab["widget"], tab["name"])

        layout = QVBoxLayout()
        layout.addWidget(tab_bar)

        self.setLayout(layout)