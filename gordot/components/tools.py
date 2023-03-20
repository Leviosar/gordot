from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QLabel

class ToolsMenu(QWidget):
    def __init__(self, viewport):
        super().__init__()

        tabs = [
            { "widget": ZoomTool(viewport), "name": "Zoom"},
            { "widget": PanTool(viewport), "name": "Move"},
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

