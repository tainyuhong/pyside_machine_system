import sys
from PySide6 import QtWidgets, QtGui, QtCore
from ui.add_machine import *
from db.db_handler import *

class UiAdd(Ui_add_machine_form, QtWidgets.QDialog, QObject):
    '''
    添加设备窗口类
    '''

    def __init__(self, parent=None):
        super(UiAdd, self).__init__(parent)
        self.setupUi(self)
        self.db = DBMysql()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiAdd()
    import_win.show()
    sys.exit(app.exec())
