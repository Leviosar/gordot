from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QWidget

from gordot.components import Sidebar
from gordot.components import Viewport
from gordot.menus import ShapeList, ShapeEdit, ToolsMenu
from gordot.tools import ColorTool

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gordot")
        
        window = QWidget()

        horizontal_layout = QHBoxLayout(window)

        viewport = Viewport()

        horizontal_layout.addWidget(
            Sidebar([
                ToolsMenu(viewport)
            ])
        )

        horizontal_layout.addWidget(viewport, 3)
        
        horizontal_layout.addWidget(
            Sidebar([
                ColorTool(viewport),
                ShapeList(viewport),
                ShapeEdit(viewport)
            ])
        )

        self.resize(1920, 1080)

        self.setCentralWidget(window)

