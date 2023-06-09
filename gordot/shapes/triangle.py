from typing import Tuple

from PyQt5.QtGui import QPainter

from gordot.shapes import Shape
from gordot.structures import Vector

class Triangle(Shape):

    coord1: Vector
    coord2: Vector
    coord3: Vector

    def __init__(self, coord1: Vector, coord2: Vector, coord3: Vector, name: str, color: Tuple[int, int, int] = (0, 0, 0)):
        super().__init__(name, color)

        self.coord1 = coord1
        self.coord2 = coord2
        self.coord3 = coord3

    def draw(self, painter: QPainter):
        painter.drawLine(
            self.coord1.x, self.coord1.y,
            self.coord2.x, self.coord2.y
        )

        painter.drawLine(
            self.coord2.x, self.coord2.y,
            self.coord3.x, self.coord3.y
        )

        painter.drawLine(
            self.coord3.x, self.coord3.y,
            self.coord1.x, self.coord1.y
        )



