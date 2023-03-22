from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

from gordot.components.tools import ToolsMenu

from typing import List

class Sidebar(QWidget):
    def __init__(self, items: List[QWidget]):
        super(Sidebar, self).__init__()

        self.sidebar_layout = QVBoxLayout()

        for item in items:
            self.sidebar_layout.addWidget(item)
        # self.sidebar_layout.addWidget(ToolsMenu(viewport))

        self.setLayout(self.sidebar_layout)

