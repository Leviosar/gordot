from typing import Tuple, List

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.utils.coord import Vector
from gordot.structures import View, Vector

class Point(Shape):

    coord: Vector

    def __init__(self, coord: Vector, name: str, color: QColor = QColor(0,0,0)):
        self.coord = coord
        super().__init__(name, color)
        
    def points(self) -> List[Vector]:
        return [self.coord]
    
    def draw(self, painter: QPainter) -> None:
        coord = self.coord

        painter.drawPoint(int(coord.x), int(coord.y))

    def move(self, vec: Vector) -> None:
        self.coord += vec

    def transform(self, matrix: Vector):
        self.coord @= matrix
        
    def export(self, index = 1):
        p = self.coord
        string  = f'v {p.x} {p.y} {p.z} \n'
        string += f'o {self.name} \n'
        string += f'p {index} \n'
        return string
        
    def viewport_transform(self, origin: 'View', destiny: 'View'):
        return Point(self.coord.viewport_transform(origin, destiny), self.name, self.color)
    
    def clip(self, view: 'View'):
        in_x = view.min().x < self.coord.x < view.max().x
        in_y = view.min().y < self.coord.y < view.max().y

        if in_x and in_y:
            return self
        else:
            return None