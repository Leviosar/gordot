from typing import List, Tuple

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.utils import Coord
from gordot.structures import View

class Wireframe(Shape):

    coords: List[Coord]

    def __init__(self, coords: List[Coord], name: str, color: QColor = QColor(0, 0, 0)):
        super().__init__(name, color)

        self.coords = coords

    def draw(self, painter: QPainter, viewport: View, window: View):
        num_coords = len(self.coords)

        for i in range(num_coords):
            current = self.coords[i].transform(window, viewport)
            next = self.coords[(i + 1) % num_coords].transform(window, viewport)

            painter.drawLine(
                int(current.x), int(current.y),
                int(next.x), int(next.y)
            )


    def transform(self, matrix: Coord):
        for coord in self.coords:
            coord @= matrix