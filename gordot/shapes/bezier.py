from typing import List, Iterator

from PyQt5.QtGui import QPainter, QColor

from gordot.shapes import Shape, Wireframe
from gordot.shapes.shape import Shape
from gordot.structures import Vector, View

from gordot.utils import make_bezier_points

BEZIER_RESOLUTION = 25

class Bezier(Shape):

    control_points: List[Vector]

    def __init__(self, control_points: List[Vector], name: str, color: QColor = QColor(0, 0, 0)):
        super().__init__(name, color)

        self.control_points = control_points

    def draw(self, painter: QPainter):
        drawable_points = self.make_drawable_points()

        w = Wireframe(drawable_points, self.name, self.color, Wireframe.OPEN)
        w.draw(painter)

    ## Given the control_points, create the points that will be actually drawn
    def make_drawable_points(self) -> List[Vector]:
        drawable_points: List[Vector] = []

        for points in self.packed_points():
            for i in range(BEZIER_RESOLUTION + 1):
                x, y, z = make_bezier_points(i / BEZIER_RESOLUTION, points)
                drawable_points.append(Vector(x, y, z))

        return drawable_points

    ## Pack the control points in packs of 4
    def packed_points(self) -> Iterator[List[Vector]]:
        for i in range(0, len(self.control_points) - 1, 3):
            yield self.control_points[i : (i + 4)]

    def transform(self, matrix: Vector):
        for coord in self.control_points:
            coord @= matrix

    def viewport_transform(self, origin: View, destiny: View) -> 'Bezier':
        points = [point.viewport_transform(origin, destiny) for point in self.control_points]
        return Bezier(points, self.name, self.color)
