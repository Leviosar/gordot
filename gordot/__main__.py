import sys

from PyQt5.QtWidgets import QApplication, QWidget
from gordot.views.main_window import MainWindow

app = QApplication(sys.argv)

window = MainWindow()

window.show()

app.exec()
# sys.exit(app.exec_())