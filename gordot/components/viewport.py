from typing import List, Tuple

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPen, QPalette, QMouseEvent
from PyQt5.QtCore import Qt, pyqtSignal

from gordot.shapes import Shape, Point, Line, Triangle
from gordot.utils import Coord
from gordot.structures import View

class Viewport(QWidget):

    display_file_changed = pyqtSignal()
    on_mouse_pressed = pyqtSignal(QMouseEvent)
    on_mouse_moved = pyqtSignal(QMouseEvent)
    on_mouse_released = pyqtSignal(QMouseEvent)
    on_mouse_double_clicked = pyqtSignal(QMouseEvent)
    
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

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.on_mouse_moved.emit(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.on_mouse_pressed.emit(event)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        self.on_mouse_released.emit(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.on_mouse_double_clicked.emit(event)


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

    def pan(self, direction: Coord):
        self.window_dimensions.xmin -= direction.x
        self.window_dimensions.xmax -= direction.x
        self.window_dimensions.ymin += direction.y
        self.window_dimensions.ymax += direction.y
        
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


def initPen(color: QColor) -> QPen:
    pen = QPen()
    pen.setWidth(4)
    pen.setCapStyle(Qt.RoundCap)

    pen.setColor(color)

    return pen

def initBrush(color: QColor) -> QBrush:
    brush = QBrush()
    brush.setStyle(1)

    brush.setColor(color)

    return brush
