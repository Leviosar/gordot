from typing import List, Tuple

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape
from gordot.structures import Vector
from gordot.structures import View

class Wireframe(Shape):

    coords: List[Vector]

    def __init__(self, coords: List[Vector], name: str, color: QColor = QColor(0, 0, 0)):
        super().__init__(name, color)

        self.coords = coords

    def points(self) -> List[Vector]:
        return self.coords
    
    def draw(self, painter: QPainter):
        num_coords = len(self.coords)

        for i in range(num_coords):
            current = self.coords[i]
            next = self.coords[(i + 1) % num_coords]

            painter.drawLine(
                int(current.x), int(current.y),
                int(next.x), int(next.y)
            )

    def viewport_transform(self, origin: 'View', destiny: 'View'):
        points = [point.viewport_transform(origin, destiny) for point in self.points()]
        return Wireframe(points, self.name, self.color)
    
    def export(self, index = 1):
        points = self.points()
        string = ''

        for p in points:
            string += f'v {p.x} {p.y} {p.z} \n'
        
        string += f'o {self.name} \n'
        string += 'l '
        string += ''.join(f'{p + index} ' for p in range(len(points)))
        string += f'{index} \n'

        return string

    def transform(self, matrix: Vector):
        for coord in self.coords:
            coord @= matrix

    def clip(self, view: View):
        from gordot.clipping.sutherland_hodgeman import sutherland_hodgeman
        
        return sutherland_hodgeman(self, view)