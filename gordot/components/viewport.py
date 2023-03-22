from typing import List, Tuple

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPen, QPalette
from PyQt5.QtCore import Qt, pyqtSignal

from gordot.shapes import Shape, Point, Line, Triangle
from gordot.utils import Coord
from gordot.structures import View

class Viewport(QWidget):

    display_file_changed = pyqtSignal()
    
    def __init__(self):
        super(Viewport, self).__init__()
        
        self.display_file: List[Shape] = []

        self.painter = QPainter()


    def add_shape(self, shape: Shape):
        self.display_file.append(shape)
        self.display_file_changed.emit()
        self.repaint()

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

    def setBackgroundColor(self, red: int, green: int, blue: int):
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(red, green, blue))

        self.setPalette(palette)

    def move_up(self, pixels: int):
        self.window_dimensions.ymin -= pixels
        self.window_dimensions.ymax -= pixels

        self.repaint()

    def move_down(self, pixels: int):
        self.window_dimensions.ymin += pixels
        self.window_dimensions.ymax += pixels

        self.repaint()

    def move_left(self, pixels: int):
        self.window_dimensions.xmin += pixels
        self.window_dimensions.xmax += pixels

        self.repaint()
    
    def move_right(self, pixels: int):
        self.window_dimensions.xmin -= pixels
        self.window_dimensions.xmax -= pixels

        self.repaint()

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
