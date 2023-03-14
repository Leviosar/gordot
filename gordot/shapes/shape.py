from typing import Tuple

from PyQt5.QtGui import QPainter

class Shape:
    def __init__(self, name, color: Tuple[int, int, int] = (0,0,0)):
        self.name = name
        self.color = color

    def draw(self, painter: QPainter) -> None:
        raise "Implementa ai fera"