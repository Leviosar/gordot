from typing import List, Tuple

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.structures import Vector
from gordot.structures import View

class Bezier(Shape):

    coords: List[Vector]

    def __init__(self, coords: List[Vector], name: str, color: QColor = QColor(0, 0, 0)):
        super().__init__(name, color)

        self.coords = coords

    def draw(self, painter: QPainter):
        num_coords = len(self.coords)

        for i in range(num_coords):
            current = self.coords[i]
            next = self.coords[(i + 1) % num_coords]

            painter.drawLine(
                int(current.x), int(current.y),
                int(next.x), int(next.y)
            )


    def transform(self, matrix: Vector):
        for coord in self.coords:
            coord @= matrix