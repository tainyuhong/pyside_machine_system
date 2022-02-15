import os
import sys
import openpyxl
from PySide6 import QtWidgets, QtGui, QtCore
from ui.check import *
from ui.addhost_win import *
from db.db_handler import *


# SQL查询语句
hosts_sql = ''' select m.machine_name,m.mg_ip from machine_list m where m.mg_ip is not Null;'''

class UiCheck(Ui_check_form,QtWidgets.QFrame):
    def __init__(self,parent=None):
        super(UiCheck, self).__init__(parent)
        self.setupUi(self)
        self.addhost_btn.clicked.connect(self.select_hosts)     # 查询所有设备

    def select_hosts(self):
        db = DBMysql()
        host_win = Ui_addhost_win()
        win = host_win.setupUi(QDialog)
        win.show()
        hosts_infos = db.query_single(hosts_sql)
        print(hosts_infos)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiCheck()
    import_win.show()
    sys.exit(app.exec())
