import sys
from ui.password_mg import *
from PySide6 import QtWidgets
from db.db_orm import *


# import logging
#
#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class UiPassword(Ui_password_form, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiPassword, self).__init__(parent)
        self.setupUi(self)

        self.le_current_ip.setDisabled(True)  # 设置默认物理设备，IP不可手动输入，需要查询来获得
        self.grp_is_vm.toggled.connect(self.is_vm)  # 判断当前是否选择
        self.btn_add.clicked.connect(self.add_passwd)  # 添加用户、密码
        self.bt_select_mg.clicked.connect(self.get_machine)  # 查询设备信息
        self.bt_current.clicked.connect(self.get_current_machine)  # 当前选择的设备

    # 查看密码窗口

    # 维护密码窗口
    # 判断维护的是物理设备还是虚拟机
    def is_vm(self):
        stat = self.grp_is_vm.isChecked()
        print(stat)
        if not stat:
            self.grp_is_vm.setTitle('虚拟机')
            self.le_current_ip.setDisabled(False)
            self.le_current_ip.setText('')
            self.lb_ma_conut.setText('')
        else:
            self.grp_is_vm.setTitle('物理机')
            self.le_current_ip.setDisabled(True)

    # 查询主机信息
    def get_machine(self):
        ip = self.le_ip.text().strip()
        # 从数据库中获取数据
        data_model = MachineList.select(MachineList.machine_id, MachineList.machine_name, MachineList.room_name,
                                        MachineList.machine_sn, MachineList.mg_ip, MachineList.bmc_ip).where(
            MachineList.mg_ip == ip).orwhere(MachineList.bmc_ip == ip).tuples().execute()
        # 将查询数据显示到表格中
        self.tb_query_ma.setRowCount(len(data_model))  # 表格数据行数
        self.lb_ma_conut.setText('查询到 {} 条记录'.format(len(data_model)))
        for row, row_data in enumerate(data_model):
            for col, item in enumerate(row_data):
                self.tb_query_ma.setItem(row, col, QTableWidgetItem(str(item)))
            print('查询到的设备', row_data)

    # 选择需要配置的主机
    def get_current_machine(self):
        item = self.tb_query_ma.currentItem()  # 获取选择的单元格
        row = self.tb_query_ma.currentRow()  # 获取行号
        # print('当前选择ITEM',item.text(),item.column(),'当前选择行：',row,self.tb_query_ma.item(row,0).text())
        # 判断是否选择的是IP地址一列，IP在第5，6列
        if item.column() in (4, 5):
            self.le_current_ip.setText(item.text())  # 将获取的IP写入到当前选择的IP地址栏中
            machine_id = self.tb_query_ma.item(row, 0).text()  # 获取设备的ID，为第1列信息
            print('当前设备的ID', self.tb_query_ma.item(row, 0).text())
        else:
            print('未选择到IP')

    # 添加用户密码
    def add_passwd(self):
        user = self.le_user.text().strip()
        passwd = self.le_password.text().strip()
        ip = self.le_current_ip.text().strip()
        remark = self.te_remark.toPlainText().strip()
        if user == '':
            QtWidgets.QMessageBox.warning(self, '添加用户密码', '用户名未输入')
        elif passwd == '':
            QtWidgets.QMessageBox.warning(self, '添加用户密码', '密码未输入')
        elif ip == '':
            QtWidgets.QMessageBox.warning(self, '添加用户密码', 'IP未选择或未输入')
        else:
            value = (user, passwd, ip, remark)
            print('输入信息：', value)
            # 添加到数据库中
            MachinePassword.insert_many([value], [MachinePassword.machine_name, MachinePassword.ip, MachinePassword.sn,
                                                  MachinePassword.room, MachinePassword.user, MachinePassword.password,
                                                  MachinePassword.machine_type, MachinePassword.machine_id,
                                                  MachinePassword.remark]).execute()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    passwd_win = UiPassword()
    passwd_win.show()
    sys.exit(app.exec())
