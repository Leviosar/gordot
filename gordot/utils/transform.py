import numpy as np

from gordot.utils import Coord

class Transform:
    @classmethod
    def translate(cls, delta: Coord):
        matrix = np.identity(3)
        matrix[2, 0] = delta.x
        matrix[2, 1] = delta.y
        return matrix

    @classmethod
    def scale(cls, delta: Coord):
        matrix = np.identity(3)
        matrix[0,0] = delta.x
        matrix[1,1] = delta.y
        return matrix

    @classmethod
    def rotate(cls, angle: float):
        matrix = np.identity(3)
        matrix[0,0] = np.cos(angle)
        matrix[0,1] = -np.sin(angle)
        matrix[1,0] = np.sin(angle)
        matrix[1,1] = np.cos(angle)
        return matrix