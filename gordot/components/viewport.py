from typing import List, Tuple

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPen, QPalette
from PyQt5.QtCore import Qt

from gordot.shapes import Shape, Point, Line, Triangle
from gordot.utils import Coord

test_shapes = [
    Point(Coord(100, 100), "Pontinho", (0, 255 , 0)),
    Line(
        Coord(250, 250),
        Coord(300, 300),
        "Minha linhazinha"
    ),
    Triangle(
        Coord(150, 200),
        Coord(300, 200),
        Coord(250, 100),
        "Meu trigozinho"
    )
]

class Viewport(QWidget):
    def __init__(self):
        super(Viewport, self).__init__()
        
        self.display_file: List[Shape] = test_shapes

        self.painter = QPainter()

        self.setBackgroundColor(255, 255, 0)


    def paintEvent(self, event):
        self.painter.begin(self)

        for shape in self.display_file:
            self.painter.setPen(initPen(shape.color))
            self.painter.setBrush(initBrush(shape.color))

            shape.draw(self.painter)

        self.painter.end()


    def setBackgroundColor(self, red: int, green: int, blue: int):
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(red, green, blue))

        self.setPalette(palette)

def initPen(color: Tuple[int, int, int]) -> QPen:
    pen = QPen()
    pen.setWidth(11)
    pen.setCapStyle(Qt.RoundCap)

    pen.setColor(QColor(*color))

    return pen

def initBrush(color: Tuple[int, int, int]) -> QBrush:
    brush = QBrush()
    brush.setStyle(1)

    brush.setColor(QColor(*color))

    return brush
