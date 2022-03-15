import sys
from test_Demo.untitled import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


class MainUi(Ui_MainWindow,QMainWindow):

    def __init__(self,parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        # self.setCentralWidget(self.splitter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()
    sys.exit(app.exec())