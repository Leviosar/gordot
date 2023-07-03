from typing import List, Tuple

from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QColor, QFont, QBrush, QPen, QPalette, QMouseEvent
from PyQt5.QtCore import Qt, pyqtSignal

from gordot import state
from gordot.shapes import Shape, Wireframe
from gordot.structures import Vector
from gordot.structures import View, DisplayFile

class Viewport(QWidget):

    display_file_changed = pyqtSignal()
    on_mouse_pressed = pyqtSignal(QMouseEvent)
    on_mouse_moved = pyqtSignal(QMouseEvent)
    on_mouse_released = pyqtSignal(QMouseEvent)
    on_mouse_double_clicked = pyqtSignal(QMouseEvent)
    
    def __init__(self):
        super(Viewport, self).__init__()
        
        self.display_file = DisplayFile()
        self.display_file.items.append(Wireframe([
                Vector(0, 0),
                Vector(0, 100),
                Vector(100, 0),
                Vector(100, 100),
            ], "A", state.primary_color)
        )

        self.painter = QPainter()


    def add_shape(self, shape: Shape):
        self.display_file.items.append(shape)
        self.display_file_changed.emit()
        self.repaint()

    def paintEvent(self, event):
        self.painter.begin(self)

        for shape in self.display_file.projected_shapes(self.window_dimensions, self.viewport_dimensions):
            self.painter.setPen(initPen(shape.color))
            self.painter.setBrush(initBrush(shape.color))

            shape.draw(self.painter)

        self.painter.end()

    def resizeEvent(self, event):
        super().resizeEvent(event)

        self.viewport_dimensions = View(
            Vector(0, self.height()),
            Vector(self.width(), self.height()),
            Vector(0, 0),
            Vector(self.width(), 0),
        )
        
        self.window_dimensions = View(
            Vector(0, self.height()),
            Vector(self.width(), self.height()),
            Vector(0, 0),
            Vector(self.width(), 0),
        )

    def mouseMoveEvent(self, event: QMouseEvent):
        self.on_mouse_moved.emit(event)

    def mousePressEvent(self, event: QMouseEvent):
        self.on_mouse_pressed.emit(event)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.on_mouse_released.emit(event)

    def mouseDoubleClickEvent(self, event: QMouseEvent):
        self.on_mouse_double_clicked.emit(event)


    def setBackgroundColor(self, red: int, green: int, blue: int):
        self.setAutoFillBackground(True)

        palette = QPalette()
        palette.setColor(self.backgroundRole(), QColor(red, green, blue))

        self.setPalette(palette)

    def move_up(self, pixels: int):
        self.window_dimensions.move(Vector(0, -pixels))
        self.repaint()

    def move_down(self, pixels: int):
        self.window_dimensions.move(Vector(0, pixels))
        self.repaint()

    def move_left(self, pixels: int):
        self.window_dimensions.move(Vector(pixels, 0))
        self.repaint()
    
    def move_right(self, pixels: int):
        self.window_dimensions.move(Vector(-pixels, 0))
        self.repaint()

    def pan(self, direction: Vector):
        self.window_dimensions.move(direction)
        self.repaint()

    def zoom_in(self, factor):
        self.window_dimensions.zoom(1 / factor)
        self.repaint()

    def zoom_out(self, factor):
        self.window_dimensions.zoom(factor)
        self.repaint()

    def rotate(self, angle):
        self.window_dimensions.rotate(angle)
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
