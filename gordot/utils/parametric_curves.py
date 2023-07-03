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

def make_delta_matrix(d: float):
    d2 = d * d
    d3 = d * d * d
    matrix = np.array(
        [[0, 0, 0, 1], [d3, d2, d, 0], [6 * d3, 2 * d2, 0, 0], [6 * d3, 0, 0, 0]]
    )

    return matrix

def make_bspline_matrix():
    matrix = np.array([[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 0, 3, 0], [1, 4, 1, 0]]) / 6
    return matrix

def make_fd_bspline_points(control_points: List['Vector'], resolution: int) -> Tuple[float, float, float]:
    E = make_delta_matrix(1 / resolution)
    bspline_matrix = make_bspline_matrix()

    px = np.array([p.x for p in control_points])
    py = np.array([p.y for p in control_points])
    pz = np.array([p.z for p in control_points])

    x, dx, dx2, dx3 = E @ bspline_matrix @ px
    y, dy, dy2, dy3 = E @ bspline_matrix @ py
    z, dz, dz2, dz3 = E @ bspline_matrix @ pz

    for x, y, z in forward_difference(resolution, x, y, z, dx, dy, dz, dx2, dy2, dz2, dx3, dy3, dz3):
        yield x, y, z

def forward_difference(n, x, y, z, dx, dy, dz, dx2, dy2, dz2, dx3, dy3, dz3):
    yield (x, y, z)

    for i in range(n):
        x = x + dx
        y = y + dy
        z = z + dz

        dx = dx + dx2
        dy = dy + dy2
        dz = dz + dz2

        dx2 = dx2 + dx3
        dy2 = dy2 + dy3
        dz2 = dz2 + dz3

        yield (x, y, z)
