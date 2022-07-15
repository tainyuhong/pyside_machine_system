import sys
from ui.modify import *
from PySide6 import QtWidgets, QtGui, QtCore
from ui.add_machine import *
from db.db_orm import *


class UiModifyMachine(Ui_modify, QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(UiModifyMachine, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiModifyMachine()
    add_win.show()
    sys.exit(app.exec())
