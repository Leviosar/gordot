from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QWidget

from gordot.components.sidebar import Sidebar
from gordot.components.viewport import Viewport

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Gordot")
        
        window = QWidget()

        horizontal_layout = QHBoxLayout(window)

        viewport = Viewport()

        horizontal_layout.addWidget(Sidebar(viewport), 1)
        horizontal_layout.addWidget(viewport, 3)
        # horizontal_layout.addWidget(Sidebar(viewport), 1)

        self.resize(1920 // 2, 1080 // 2)

        self.setCentralWidget(window)

