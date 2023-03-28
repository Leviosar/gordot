import numpy as np

from gordot.structures import View, Vec2D

class Coord:

    def __init__(self, x: float, y: float, z: float = 1):
        self.arr = np.array([x,y,z], dtype=float)


    @property
    def x(self):
        return self.arr[0]
    

    @property
    def y(self):
        return self.arr[1]


    @property
    def z(self):
        return self.arr[2]


    def transform(self, origin: View, destiny: View):
        x = (self.x - origin.xmin) / (origin.xmax - origin.xmin) * (destiny.xmax - destiny.xmin)
        y = (1 - (self.y - origin.ymin) / (origin.ymax - origin.ymin)) * (destiny.ymax - destiny.ymin)

        return Coord(x, y)


    def __add__(self, other):
        if isinstance(other, Coord):
            other = other.arr  
        v = self.arr + other
        
        return Coord(*v)
    

    def __sub__(self, other):
        if isinstance(other, Coord):
            other = other.arr  
        v = self.arr - other
        
        return Coord(*v)
      

    def __iadd__(self, other):
        self.arr = (self + other).arr
        return self


    def __mul__(self, other):
        v = self.arr * other
        return Coord(*v)


    def __imul__(self, other):
        self.arr = (self * other).arr
        return self


    def __truediv__(self, other):
        v = self.arr / other
        return Coord(*v)


    def __itruediv__(self, other):
        self.arr = (self / other).arr
        return self


    def __matmul__(self, other):
        v = self.arr @ other
        return Coord(*v)


    def __imatmul__(self, other):
        self.arr = (self @ other).arr
        return self


    def __neg__(self):
        return Coord(-self.x, -self.y)


    def __str__(self):
        return f'Coord({self.x}, {self.y}, {self.z})'


    def __repr__(self):
        return str(self)


    def __str__(self):
        return f"(x: {self.x}, y: {self.y})"
