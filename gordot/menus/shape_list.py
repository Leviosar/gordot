from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtGui import QStandardItem, QBrush, QColor

from gordot import state
from gordot.components import Table
from gordot.components import Viewport

class ShapeList(QWidget):
    def __init__(self, viewport: Viewport):
        super().__init__()

        self.viewport = viewport
        self.viewport.display_file_changed.connect(self.update)

        self.table = Table()
        self.table.setHorizontalHeaderLabels(["NAME", "SHAPE", "COLOR"])
        self.table.itemSelected.connect(self.selection_callback)

        layout = QVBoxLayout()
        layout.addWidget(self.table)

        self.setLayout(layout)
        self.update()

    def selected_index(self):
        return self.table.currentIndex().row()

    def selection_callback(self):
        i = self.table.currentIndex().row()
        state.selected_shape = self.viewport.display_file[i]

    def delete_callback(self):
        selected = self.viewport.selected_shape
        self.viewport.remove_shape(selected)

    def populate_tree(self):
        self.table.clearRows()

        for shape in self.viewport.display_file:
            name = QStandardItem(str(shape.name))
            types = QStandardItem(shape.__class__.__name__)
            color = QStandardItem()
            color.setBackground(QBrush(shape.color))
            self.table.appendRow([name, types, color])

    def update(self):
        self.populate_tree()
        super().update()
