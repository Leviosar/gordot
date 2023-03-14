from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton


class Sidebar(QWidget):
    def __init__(self):
        super(Sidebar, self).__init__()

        self.sidebar_layout = QVBoxLayout()

        self.sidebar_layout.addWidget(QPushButton("Aperta o gordin"))

        widgets = [QPushButton(f'butao {i}') for i in range(10)]
        for w in widgets:
            self.sidebar_layout.addWidget(w)

        self.setLayout(self.sidebar_layout)

