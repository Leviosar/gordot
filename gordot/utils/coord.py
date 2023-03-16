from dataclasses import dataclass

from gordot.structures.view import View

@dataclass
class Coord:
    x: float
    y: float
    z: float = 0

    def transform(self, origin: View, destiny: View) -> 'Coord':
        x = (self.x - origin.xmin) / (origin.xmax - origin.xmin) * (destiny.xmax - destiny.xmin)
        # x = (destiny.xmax - destiny.xmin)
        # x *= (self.x - origin.xmin)
        # x /= (origin.xmax - origin.xmin)
        y = (1 - (self.y - origin.ymin) / (origin.ymax - origin.ymin)) * (destiny.ymax - destiny.ymin)
        # y = (self.y - origin.ymin) / (origin.ymax - origin.ymin)
        # y *= (destiny.ymax - destiny.ymin)

        return Coord(x, y)
    
    def __str__(self) -> str:
        return f"(x: {self.x}, y: {self.y})"