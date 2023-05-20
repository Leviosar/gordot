import numpy as np

from gordot.utils import Transform
# from gordot.structures import View

class Vector:
    x: float
    y: float
    z: float
    
    def __init__(self, x: float, y: float, z: float = 1):
        self.x = x
        self.y = y
        self.z = z
        
    @property
    def data(self):
        return np.array([self.x, self.y, self.z], dtype=float)

    @data.setter
    def data(self, sequence):
        self.x = sequence[0]
        self.y = sequence[1]
        self.z = sequence[2]
    
    def transform(self, matrix):
        self @= matrix
    
    def translate(self, delta: 'Vector'):
        self.transform(Transform.translate(delta))

    def scale(self, vector, around=None):
        if around is None:
            around = Vector(0,0)

        matrix = Transform.translate(-around) @ Transform.scale(vector) @ Transform.translate(around)
        
        self.transform(matrix)

    def rotate(self, angle, around=None):
        if around is None:
            around = Vector(0,0)

        matrix = Transform.translate(-around) @ Transform.rotate(angle) @ Transform.translate(around)
        
        self.transform(matrix)
    
    def size(self) -> float:
        return np.sqrt(self.x * self.x + self.y * self.y)
    
    def angle(self, other: 'Vector'):
        uv0 = self.data / np.linalg.norm(self.data)
        uv1 = other.data / np.linalg.norm(other.data)
        cos = np.dot(uv0, uv1)
        return np.arccos(cos)

    def viewport_transform(self, origin: 'View', destiny: 'View'):
        x = self.x - origin.min().x
        x /= origin.max().x - origin.min().x
        x *= destiny.max().x - destiny.min().x

        y = self.y - origin.min().y
        y /= origin.max().y - origin.min().y
        y = 1 - y
        y *= destiny.max().y - destiny.min().y

        self.x = x
        self.y = y
        return self

    def __add__(self, other):
        if isinstance(other, Vector):
            other = other.data  
        v = self.data + other
        return Vector(*v)

    def __iadd__(self, other):
        self.data = (self + other).data
        return self
    
    def __sub__(self, other):
        if isinstance(other, Vector):
            other = other.data  
        v = self.data - other
        return Vector(*v)

    def __isub__(self, other):
        self.data = (self - other).data
        return self

    def __mul__(self, other):
        v = self.data * other
        return Vector(*v)
    
    def __imul__(self, other):
        self.data = (self * other).data
        return self
    
    def __truediv__(self, other):
        v = self.data / other
        return Vector(*v)

    def __itruediv__(self, other):
        self.data = (self / other).data
        return self

    def __matmul__(self, other):
        v = self.data @ other
        return Vector(*v)
    
    def __imatmul__(self, other):
        self.data = (self @ other).data
        return self

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'
    
    def __repr__(self):
        return str(self)