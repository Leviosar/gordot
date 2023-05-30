from gordot.structures import View, Vector
from gordot.shapes.line import Line

def liang_barsky(line: Line, window: View):
    delta = line.end - line.start

    p = [
        -delta.x,
        delta.x,
        -delta.y,
        delta.y,
    ]

    q = [
        line.start.x - window.min().x,
        window.max().x - line.start.x,
        line.start.y - window.min().y,
        window.max().y - line.start.y,
    ]

    for i in range(4):
        if p[i] == 0 and q[i] < 0:
            return None

    r = [(qk / pk if pk != 0 else 0) for qk, pk in zip(q, p)]

    u = [
        max(0, *[r[k] for k in range(4) if p[k] < 0]),
        min(1, *[r[k] for k in range(4) if p[k] > 0]),
    ]

    if u[0] > u[1]:
        return None

    points = []

    if u[0] == 0:
        points.append(line.start)
    else:
        x = line.start.x + delta.x * u[0]
        y = line.start.y + delta.y * u[0]
        points.append(Vector(x, y))

    if u[1] == 1:
        points.append(line.end)
    else:
        x = line.start.x + delta.x * u[1]
        y = line.start.y + delta.y * u[1]
        points.append(Vector(x, y))

    return Line(points[0], points[1], line.name, line.color)