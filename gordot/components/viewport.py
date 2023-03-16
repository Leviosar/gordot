from typing import List, Tuple

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPen, QPalette
from PyQt5.QtCore import Qt

from gordot.shapes import Shape, Point, Line, Triangle
from gordot.utils import Coord
from gordot.structures.view import View

test_shapes = [
    Point(Coord(0, 0), "Pontinho", (0, 0 , 0)),
    Line(
        Coord(250, 250),
        Coord(300, 300),
        "Minha linhazinha"
    ),
    # Triangle(
    #     Coord(150, 200),
    #     Coord(300, 200),
    #     Coord(250, 100),
    #     "Meu trigozinho"
    # )
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

            shape.draw(self.painter, self.viewport_dimensions, self.window_dimensions)

        self.painter.end()

    
    def resizeEvent(self, event) -> None:
        super().resizeEvent(event)
        
        self.viewport_dimensions = View(0, 0, self.width(), self.height())
        self.window_dimensions = View(0, 0, self.width(), self.height())

        # self.display_file.append(Line(
        #     Coord(0, 0),
        #     Coord(self.width() / 2, self.height() / 2),
        #     'Linha diagonal'
        # ))

    def setBackgroundColor(self, red: int, green: int, blue: int):
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(red, green, blue))

        self.setPalette(palette)

    def zoom_in(self, factor):
        w = self.window_dimensions.width() * factor / 2
        h = self.window_dimensions.height() * factor / 2
        self.window_dimensions.xmin += w
        self.window_dimensions.xmax -= w
        self.window_dimensions.ymin += h
        self.window_dimensions.ymax -= h
        self.repaint()

    def zoom_out(self, factor):
        w = self.window_dimensions.width() * factor / 2
        h = self.window_dimensions.height() * factor / 2
        self.window_dimensions.xmin -= w
        self.window_dimensions.xmax += w
        self.window_dimensions.ymin -= h
        self.window_dimensions.ymax += h
        self.repaint()

def initPen(color: Tuple[int, int, int]) -> QPen:
    pen = QPen()
    pen.setWidth(4)
    pen.setCapStyle(Qt.RoundCap)

    pen.setColor(QColor(*color))

    return pen

def initBrush(color: Tuple[int, int, int]) -> QBrush:
    brush = QBrush()
    brush.setStyle(1)

    brush.setColor(QColor(*color))

    return brush
