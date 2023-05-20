import qtawesome as qta

from PyQt5.QtWidgets import QWidget, QLineEdit, QFormLayout, QVBoxLayout, QHBoxLayout, QPushButton

from typing import List

from gordot import state
from gordot.shapes import Wireframe
from gordot.structures import Vector
from gordot.tools import ObjectTool
from gordot.components import Viewport

class WireframeTool(ObjectTool):

    fields: List[List[QLineEdit]] = []

    min_points: int = 3

    current_points: int = 0

    fields_layout: QFormLayout

    def __init__(self, viewport):
        super().__init__(viewport)

        self.fields_layout = QFormLayout()
        
        for i in range(self.min_points):
            self.add_point_row(i)

        add_button = QPushButton(qta.icon('fa5s.plus'), '')
        add_button.clicked.connect(self.add_row_callback)

        layout = QVBoxLayout()
        layout.addWidget(self.name_input)
        layout.addLayout(self.fields_layout)
        layout.addWidget(add_button)
        layout.addWidget(self.create_button)

        self.setLayout(layout)

    def add_point_row(self, index: int, defaults = ['', '']):
        self.current_points += 1

        row = QHBoxLayout()
            
        x_input = QLineEdit()
        x_input.setPlaceholderText("X")
        x_input.setText(defaults[0])
        
        y_input = QLineEdit()
        y_input.setPlaceholderText("Y")
        y_input.setText(defaults[1])

        delete_button = QPushButton(qta.icon('fa5s.trash'), '')
        delete_button.clicked.connect(lambda: self.delete_row_callback(row))

        row.addWidget(x_input, 5)
        row.addWidget(y_input, 5)
        row.addWidget(delete_button, 2)

        self.fields.append([x_input, y_input])

        self.fields_layout.addRow(row)


    def add_row_callback(self):
        self.add_point_row(len(self.fields))


    def delete_row_callback(self, index: int, row: QWidget):
        if self.current_points <= 3:
            return
        
        self.fields.pop(index)
        self.fields_layout.removeRow(row)


    def create_callback(self):
        coords = [
            Vector(
                int(self.fields[i][0].text()),
                int(self.fields[i][1].text())
            )

            for i in range(len(self.fields))
        ]

        wireframe = Wireframe(coords, self.name_input.text(), state.primary_color)

        self.add_shape(wireframe)
