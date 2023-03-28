from typing import Tuple

from PyQt5.QtGui import QPainter, QColor

from gordot.structures.view import View
from gordot.utils import Coord

class Shape:
    def __init__(self, name, color: QColor = QColor(0,0,0)):
        self.name = name
        self.color = color


    def draw(self, painter: QPainter, viewport: View, window: View):
        raise "Implementa ai fera"


    def transform(self, matrix: Coord):
        raise "Implementa ai fera"
