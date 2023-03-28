from typing import Tuple

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.utils import Coord
from gordot.structures import View, Vec2D

class Line(Shape):

    start: Coord
    end: Coord

    def __init__(self, start: Coord, end: Coord, name: str, color: QColor = QColor(0, 0, 0)):
        super().__init__(name, color)

        self.start = start
        self.end = end

    def draw(self, painter: QPainter, viewport: View, window: View):
        start = self.start.transform(window, viewport)
        end = self.end.transform(window, viewport)

        painter.drawLine(
            int(start.x), int(start.y),
            int(end.x), int(end.y)
        )

    def move(self, vec: Vec2D):
        self.start += vec
        self.end += vec

    def transform(self, matrix: Coord):
        self.start @= matrix
        self.end @= matrix
