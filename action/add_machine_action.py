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
        self.clear.clicked.connect(self.clear_all)

    def save_infos(self):
        '''
        提交设备信息至数据库中
        :return:
        '''
        pass

    def clear_all(self):
        '''
        清空所填内容
        :return:
        '''
        self.machine_name.setText('')

        self.sort_name.setItemText(0,'')

        self.room.setItemText(0,'')

        self.cabinet.setItemText(0,'')

        self.up_position.setItemText(0,'')

        self.machine_factory.setText('')

        self.model.setText('')

        self.down_position.setItemText(0,'')

        self.machine_sn.setText('')

        self.lmg_ip.setText('')

        self.work_are.setText('')

        self.machine_admin.setText('')

        self.admin.setText('')

        self.app_ip.setText('')

        self.factory_date.setDate(QDate.getDate())

        self.end_ma_date.setText('')

        self.install_date.setText('')

        self.comments.setText('')



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiAdd()
    add_win.show()
    sys.exit(app.exec())
