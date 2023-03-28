from typing import Tuple

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.utils.coord import Coord
from gordot.structures import View, Vec2D

class Point(Shape):

    coord: Coord

    def __init__(self, coord: Coord, name: str, color: QColor = QColor(0,0,0)):
        self.coord = coord
        super().__init__(name, color)

    def draw(self, painter: QPainter, viewport: View, window: View) -> None:
        coord = self.coord.transform(window, viewport)

        painter.drawPoint(int(coord.x), int(coord.y))

    def move(self, vec: Vec2D) -> None:
        self.coord += vec

    def transform(self, matrix: Coord):
        self.coord @= matrix