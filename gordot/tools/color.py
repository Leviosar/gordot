from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QColorDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor

from gordot import state
from gordot.components import Viewport

from typing import Dict


class ColorTool(QWidget):

    primary_button: QPushButton

    secondary_button: QPushButton

    sliders: Dict[str, QSlider] = {
        "red": None,
        "green": None,
        "blue": None,
    }

    def __init__(self, viewport: Viewport):
        super().__init__()

        self.viewport = Viewport

        layout = QHBoxLayout()

        colors_column = QVBoxLayout()
        
        self.primary_button = QPushButton()
        self.primary_button.clicked.connect(self.select_primary)
        
        self.secondary_button = QPushButton()
        self.secondary_button.clicked.connect(self.select_secondary)
        
        self.update_button_styles()

        colors_column.addWidget(self.primary_button)
        colors_column.addWidget(self.secondary_button)
        
        sliders_column = QVBoxLayout()

        self.sliders["red"] = QSlider(Qt.Orientation.Horizontal)
        self.sliders["green"] = QSlider(Qt.Orientation.Horizontal)
        self.sliders["blue"] = QSlider(Qt.Orientation.Horizontal)

        sliders_column.addWidget(self.sliders["red"])
        sliders_column.addWidget(self.sliders["green"])
        sliders_column.addWidget(self.sliders["blue"])

        layout.addLayout(colors_column)
        layout.addLayout(sliders_column)

        self.setLayout(layout)

    def select_primary(self):
        state.primary_color = QColorDialog.getColor()
        self.update_button_styles()

    def select_secondary(self):
        state.secondary_color = QColorDialog.getColor()
        self.update_button_styles()

    def update_button_styles(self):
        self.primary_button.setStyleSheet(f"""
            QPushButton {{ 
                background-color:rgb(
                    {state.primary_color.red()},
                    {state.primary_color.green()},
                    {state.primary_color.blue()}
                )
            }}
        """)

        self.secondary_button.setStyleSheet(f"""
            QPushButton {{ 
                background-color:rgb(
                    {state.secondary_color.red()},
                    {state.secondary_color.green()},
                    {state.secondary_color.blue()}
                )
            }}
        """)