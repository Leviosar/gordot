from typing import Tuple

from PyQt5.QtGui import QPainter

from gordot.structures.view import View

class Shape:
    def __init__(self, name, color: Tuple[int, int, int] = (0,0,0)):
        self.name = name
        self.color = color

    def draw(self, painter: QPainter, viewport: View, window: View) -> None:
        raise "Implementa ai fera"