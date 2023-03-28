from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget

from gordot.tools import TranslateTool, ScaleTool, RotateTool
from gordot.components import Viewport

class ShapeEdit(QWidget):
    def __init__(self, viewport: Viewport):
        super().__init__()

        tabs = [
            { "widget": TranslateTool(viewport), "name": "Translate"},
            { "widget": ScaleTool(viewport), "name": "Scale"},
            { "widget": RotateTool(viewport), "name": "Rotate"},
        ]

        tab_bar = QTabWidget()

        for tab in tabs:
            tab_bar.addTab(tab["widget"], tab["name"])

        layout = QVBoxLayout()
        layout.addWidget(tab_bar)

        self.setLayout(layout)
