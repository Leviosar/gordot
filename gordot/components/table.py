from PyQt5.QtWidgets import QTreeView
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QStandardItemModel

class Table(QTreeView):
    itemSelected = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = QStandardItemModel(0, 3)
        self.setModel(self.model)

    def setHorizontalHeaderLabels(self, *args, **kwargs):
        self.model.setHorizontalHeaderLabels(*args, **kwargs)

    def appendRow(self, *args, **kwargs):
        self.model.appendRow(*args, **kwargs)

    def clearRows(self):
        self.model.removeRows(0, self.model.rowCount())

    def selectionChanged(self, selected, deselected):
        super().selectionChanged(selected, deselected)
        self.itemSelected.emit()
