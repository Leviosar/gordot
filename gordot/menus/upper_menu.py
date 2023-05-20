from PyQt5.QtWidgets import QMenuBar, QMenu
from gordot.tools import FileExportTool, FileImportTool

class UpperMenu(QMenuBar):
    def __init__(self, parent, viewport: 'Viewport'):
        super().__init__(parent)
        
        self.viewport = viewport
        
        items = [
            self.file()
        ]
        
        for item in items:
            self.addMenu(item)
            
    def file(self):
        menu = QMenu('&File', self)
        
        export = FileExportTool(menu, self.viewport)
        import_ = FileImportTool(menu, self.viewport)
        
        menu.addAction(export)
        menu.addAction(import_)
        
        return menu