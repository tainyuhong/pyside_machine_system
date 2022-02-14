import os
import sys
import openpyxl
from PySide6 import QtWidgets, QtGui, QtCore
from ui.check import *
from db.db_handler import *


class UiCheck(Ui_Form,QtWidgets.QFrame):
    def __init__(self,parent=None):
        super(UiCheck, self).__init__(parent)
        self.setupUi(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiCheck()
    import_win.show()
    sys.exit(app.exec())
