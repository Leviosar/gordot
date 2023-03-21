from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from gordot.components.tools import ToolsMenu

class Sidebar(QWidget):
    def __init__(self, viewport):
        super(Sidebar, self).__init__()

        self.sidebar_layout = QVBoxLayout()

        self.sidebar_layout.addWidget(ToolsMenu(viewport))

        self.setLayout(self.sidebar_layout)

