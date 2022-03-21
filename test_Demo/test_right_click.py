import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class RightClick(QWidget):
    def __init__(self,parent=None):
        super(RightClick, self).__init__(parent)
        self.frame = QFrame()
        self.setWindowTitle('右键菜单测试')
        lb = QLabel('文件目录树')
        self.treewidget = QTreeWidget()
        layout = QVBoxLayout()
        layout.addWidget(lb)
        layout.addWidget(self.treewidget)
        self.setLayout(layout)
        self.treewidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.treewidget.customContextMenuRequested.connect(self.menu_file)

    def menu_file(self,pos):
        # item = self.treewidget.currentItem()
        filemenu = QMenu()
        addfile = QAction('增加文件')
        delfile = QAction('删除文件')
        altfile = QAction('修改文件')
        filemenu.addAction(addfile)
        filemenu.addAction(delfile)
        filemenu.addAction(altfile)
        filemenu.exec(self.mapToGlobal(pos))
        filemenu.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = RightClick()
    win.show()
    sys.exit(app.exec())