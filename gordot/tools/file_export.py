from PyQt5.QtWidgets import QAction, QFileDialog

from gordot.components import Viewport
from gordot.io import OBJExporter

class FileExportTool(QAction):
    
    viewport: Viewport
    
    def  __init__(self, parent, viewport: Viewport):
        QAction.__init__(self, "&Export", parent)

        self.viewport = viewport
        self.triggered.connect(self.handle)

    def handle(self):
        path, _ = QFileDialog.getSaveFileName(None, 'Save File', 'scene.obj', 'Wavefront *.obj')
        
        if path:
            OBJExporter(self.viewport.display_file.items).write(path)