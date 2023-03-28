import sys
import qdarktheme

from PyQt5.QtWidgets import QApplication, QWidget
from gordot.views.main_window import MainWindow

app = QApplication(sys.argv)

qdarktheme.setup_theme()

window = MainWindow()

window.show()

app.exec()
# sys.exit(app.exec_())