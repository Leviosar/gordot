from typing import List, Tuple

import numpy as np
from numpy._typing import NDArray


def make_bezier_matrix() -> NDArray:
    return np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]])

def make_bezier_points(t: float, control_points: List['Vector']) -> Tuple[float, float, float]:
    bezier_matrix = make_bezier_matrix()

    t = np.array([t ** 3, t ** 2, t, 1])

    px = [point.x for point in control_points]
    py = [point.y for point in control_points]
    pz = [point.z for point in control_points]

    x = t @ bezier_matrix @ px
    y = t @ bezier_matrix @ py
    z = t @ bezier_matrix @ pz

    return (x, y, z)
