from typing import Tuple

from PyQt5.QtGui import QPainter

from gordot.shapes.shape import Shape
from gordot.utils.coord import Coord

class Point(Shape):

    coord: Coord

    def __init__(self, coord: Coord, name: str, color: Tuple[int, int, int] = (0,0,0)):
        self.coord = coord
        super().__init__(name, color)

    def draw(self, painter: QPainter) -> None:
        painter.drawPoint(self.coord.x, self.coord.y)
