from typing import Tuple, List

from PyQt5.QtGui import QPainter, QColor

from gordot.structures import Vector
from gordot.utils import Transform

class Shape:
    def __init__(self, name, color: QColor = QColor(0,0,0)):
        self.name = name
        self.color = color

    def points(self) -> List[Vector]:
        return []
    
    def transform(self, matrix):
        for point in self.points():
            point.transform(matrix)

    def center(self):
        s = Vector(0,0,0)

        for point in self.points():
            s += point
        
        if self.points():
            s /= len(self.points())
        
        return s 
    
    def move(self, vector):
        matrix = Transform.translate(vector)
        self.transform(matrix)

    def scale(self, vector, around=Vector(0,0)):    
        matrix = Transform.translate(-around) @ Transform.scale(vector) @ Transform.translate(around)
        self.transform(matrix)

    def rotate(self, angle, around=Vector(0,0)):
        matrix = Transform.translate(-around) @ Transform.rotate(angle) @ Transform.translate(around)
        self.transform(matrix)
        
    def viewport_transform(self, origin: 'View', destiny: 'View') -> 'Shape':
        raise "Implementa ai fera"

    def draw(self, painter: QPainter, viewport, window):
        raise "Implementa ai fera"

    def transform(self, matrix: Vector):
        raise "Implementa ai fera"

    def export(self, index: int):
        raise "Implementa ai fera"
    
    def clip(self, view: 'View'):
        return self
