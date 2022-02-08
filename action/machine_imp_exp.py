import os
import sys
from PySide6 import QtWidgets, QtGui, QtCore
from ui.machine_import import *
from db.db_handler import *


class import_ui(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(import_ui, self).__init__(parent)
        self.setupUi(self)
        self.import_btn.clicked.connect(self.open_file)

    def open_file(self):
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(),
                                                                   'xls files (*.xls) ;; xlsx files (*.xlsx)')
        print(filename)
        self.path_le.setText(filename)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = import_ui()
    import_win.show()
    sys.exit(app.exec())
