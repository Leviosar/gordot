from PyQt5.QtWidgets import QAction, QFileDialog

from gordot import state
from gordot.components import Viewport
from gordot.utils import Transform
from gordot.structures import Vector

class FileImportTool(QAction):
    
    viewport: Viewport
    
    def  __init__(self, parent, viewport: Viewport):
        QAction.__init__(self, "&Import", parent)

        self.viewport = viewport
        self.triggered.connect(self.handle)

    def handle(self):
        path, _ = QFileDialog.getOpenFileName(self, 'Import File', '', 'Wavefront *.obj')
        
        if path:
            self.viewport.scene.save(path)