from typing import Tuple

from PyQt5.QtGui import QPainter

from gordot.shapes import Shape
from gordot.utils import Coord
from gordot.structures.view import View

class Line(Shape):

    start: Coord
    end: Coord

    def __init__(self, start: Coord, end: Coord, name: str, color: Tuple[int, int, int] = (0, 0, 0)):
        super().__init__(name, color)

        self.start = start
        self.end = end

    def draw(self, painter: QPainter, viewport: View, window: View):
        print(self.name)
        print([self.start, self.end])
        start = self.start.transform(window, viewport)
        end = self.end.transform(window, viewport)
        print([start, end])

        painter.drawLine(
            int(start.x), int(start.y),
            int(end.x), int(end.y)
        )
