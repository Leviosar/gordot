from typing import Tuple, List

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.structures import Vector
from gordot.structures import View, Vector

class Line(Shape):

    start: Vector
    end: Vector

    def __init__(self, start: Vector, end: Vector, name: str, color: QColor = QColor(0, 0, 0)):
        super().__init__(name, color)

        self.start = start
        self.end = end
    
    def points(self) -> List[Vector]:
        return [self.start, self.end]

    def draw(self, painter: QPainter):
        start = self.start
        end = self.end

        painter.drawLine(
            int(start.x), int(start.y),
            int(end.x), int(end.y)
        )

    def move(self, vec: Vector):
        self.start += vec
        self.end += vec

    def transform(self, matrix: Vector):
        self.start @= matrix
        self.end @= matrix
        
    def export(self, index = 1):
        s = self.start
        e = self.end
        string  = f'v {e.x} {e.y} {e.z} \n'
        string += f'v {s.x} {s.y} {s.z} \n'
        string += f'o {self.name} \n'
        string += f'l {index} {index+1} \n'
        return string

    def viewport_transform(self, origin: 'View', destiny: 'View'):
        start = self.start.viewport_transform(origin, destiny)
        end = self.end.viewport_transform(origin, destiny)
        return Line(start, end, self.name, self.color)