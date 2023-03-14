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

        horizontal_layout.addWidget(Sidebar())
        horizontal_layout.addWidget(Viewport())

        self.setCentralWidget(window)

