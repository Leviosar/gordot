from typing import Tuple

from PyQt5.QtGui import QPainter

from gordot.shapes import Shape
from gordot.utils import Coord

class Line(Shape):

    start: Coord
    end: Coord

    def __init__(self, start: Coord, end: Coord, name: str, color: Tuple[int, int, int] = (0, 0, 0)):
        super().__init__(name, color)

        self.start = start
        self.end = end

    def draw(self, painter: QPainter):
        painter.drawLine(
            self.start.x, self.start.y,
            self.end.x, self.end.y
        )
