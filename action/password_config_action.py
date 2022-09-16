import sys
from ui.password_mg import *
from PySide6 import QtWidgets
from db.db_orm import *

# import logging
#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)

"""
记录设备常用登录密码
"""
# 获取机房信息
def get_room():
    data_model = MachineRoom.select(MachineRoom.room_name).order_by(MachineRoom.room_id).execute()
    room = [i.room_name for i in data_model]
    # print(room)
    return room


class UiPassword(Ui_password_form, QtWidgets.QWidget):
    pass_flag = None
    selected_data = None  # 修改页面获取的选择信息

    def __init__(self, parent=None):
        super(UiPassword, self).__init__(parent)
        self.setupUi(self)
        self.tb_select.setColumnWidth(0, 50)  # 设置第一列的列宽
        self.tb_select.hideColumn(5)  # 默认隐藏密码一列
        self.btn_select.clicked.connect(self.display_userdata)  # 查询密码信息
        self.btn_show_pass.clicked.connect(self.show_password)  # 双击显示内容

        self.cb_room.addItems(get_room())     # 显示机房
        self.machine_info = None  # 自定义设备信息
        self.le_current_ip.setDisabled(True)  # 设置默认物理设备，IP不可手动输入，需要查询来获得
        self.le_machine_name.setDisabled(True)  # 设置默认物理设备，设备名不可手动输入，需要查询来获得
        self.cb_room.setDisabled(True)  # 设置默认物理设备，机房名不可手动输入，需要查询来获得
        self.grp_is_vm.toggled.connect(self.is_vm)  # 判断当前是否选择
        self.btn_add.clicked.connect(self.add_passwd)  # 添加用户、密码
        self.bt_select_mg.clicked.connect(self.get_machine)  # 查询设备信息
        self.btn_current.clicked.connect(self.get_current_machine)  # 当前选择的设备

        # 修改/删除页
        self.cb_modify_room.addItems(get_room())        # 获取机房信息
        self.btn_modify_select.clicked.connect(self.display_userdata_modify)  # 查询密码信息
        self.tb_modify_select.doubleClicked.connect(self.get_select_row)  # 获取选择行信息
        self.btn_modify.clicked.connect(self.commit_modify)  # 提交修改
        self.btn_del_pass.clicked.connect(self.del_user_passwd)  # 删除选择的用户信息

    # 查看密码窗口
    # 从数据库中获取数据
    def display_userdata(self):
        ip = self.le_display_ip.text().strip()
        if ip == '':
            data_model = MachinePassword.select(MachinePassword.pid, MachinePassword.machine_name,
                                                MachinePassword.ip, MachinePassword.room, MachinePassword.user,
                                                MachinePassword.password, MachinePassword.sn,
                                                Case(MachinePassword.machine_type, [(0, '物理机'), (1, '虚拟机')]),
                                                MachinePassword.machine_id, MachinePassword.remark).tuples().execute()
        else:
            data_model = MachinePassword.select(MachinePassword.pid, MachinePassword.machine_name,
                                                MachinePassword.ip, MachinePassword.room, MachinePassword.user,
                                                MachinePassword.password, MachinePassword.sn,
                                                Case(MachinePassword.machine_type, [(0, '物理机'), (1, '虚拟机')]),
                                                MachinePassword.machine_id, MachinePassword.remark).where(
                MachinePassword.ip.startswith(ip)).tuples().execute()
        # 将查询数据显示到表格中
        self.tb_select.setRowCount(len(data_model))  # 表格数据行数
        self.lb_status.setText('查询到 {} 条记录'.format(len(data_model)))
        self.pass_flag = False
        for row, row_data in enumerate(data_model):
            for col, item in enumerate(row_data):
                if col == 5:
                    self.tb_select.setItem(row, col, QTableWidgetItem(str(str(item))))
                    # self.tb_select.item(row, 5).setCheckState(Qt.Unchecked)  # 第六列添加复选框按钮
                else:
                    if item is None:
                        item = ''
                        self.tb_select.setItem(row, col, QTableWidgetItem(str(item)))
                    else:
                        cell_data = QTableWidgetItem(str(item))
                        # cell_data.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)     # 水平垂直居中
                        self.tb_select.setItem(row, col, cell_data)
            # print('查询到的设备', row_data)

    # 显示或隐藏密码
    def show_password(self):
        print(self.pass_flag)

        if self.pass_flag:
            print('隐藏密码')
            self.tb_select.hideColumn(5)
            self.btn_show_pass.setText('显示密码')
            self.pass_flag = False
        elif self.pass_flag == False:
            print('显示密码')
            self.tb_select.showColumn(5)
            self.btn_show_pass.setText('隐藏密码')
            self.pass_flag = True

    # 维护密码窗口
    # 判断维护的是物理设备还是虚拟机
    def is_vm(self):
        stat = self.grp_is_vm.isChecked()
        if not stat:
            self.grp_is_vm.setTitle('虚拟机')
            self.le_current_ip.setDisabled(False)
            self.le_machine_name.setDisabled(False)
            self.cb_room.setDisabled(False)
            self.le_current_ip.clear()
            self.lb_ma_conut.clear()
            self.le_machine_name.clear()
            self.cb_room.setCurrentIndex(-1)
            self.machine_info = None  # 自定义设备信息
        else:
            self.grp_is_vm.setTitle('物理机')
            self.le_current_ip.setDisabled(True)  # 设置默认物理设备，IP不可手动输入，需要查询来获得
            self.le_machine_name.setDisabled(True)  # 设置默认物理设备，设备名不可手动输入，需要查询来获得
            self.cb_room.setDisabled(True)  # 设置默认物理设备，机房名不可手动输入，需要查询来获得

    # 查询主机信息
    def get_machine(self):
        ip = self.le_ip.text().strip()
        # 从数据库中获取数据
        data_model = MachineList.select(MachineList.machine_id, MachineList.machine_name, MachineList.room_name,
                                        MachineList.machine_sn, MachineList.mg_ip, MachineList.bmc_ip).where(
            MachineList.mg_ip.startswith(ip)).orwhere(MachineList.bmc_ip.startswith(ip)).tuples().execute()
        # 将查询数据显示到表格中
        self.tb_query_ma.setRowCount(len(data_model))  # 表格数据行数
        self.lb_ma_conut.setText('查询到 {} 条记录'.format(len(data_model)))
        for row, row_data in enumerate(data_model):
            for col, item in enumerate(row_data):
                self.tb_query_ma.setItem(row, col, QTableWidgetItem(str(item)))
            # print('查询到的设备', row_data)

    # 选择需要配置的主机
    def get_current_machine(self):
        item = self.tb_query_ma.currentItem()  # 获取选择的单元格
        row = self.tb_query_ma.currentRow()  # 获取行号
        # print('当前选择ITEM',item.text(),item.column(),'当前选择行：',row,self.tb_query_ma.item(row,0).text())
        # 判断是否选择的是IP地址一列，IP在第5，6列
        if item.column() in (4, 5):
            machine_id = self.tb_query_ma.item(row, 0).text()  # 获取设备的ID，为第1列信息
            machine_name = self.tb_query_ma.item(row, 1).text()  # 获取设备名，为第2列信息
            machine_room = self.tb_query_ma.item(row, 2).text()  # 获取机房名，为第3列信息
            machine_sn = self.tb_query_ma.item(row, 3).text()  # 获取设备的SN，为第4列信息
            self.le_current_ip.setText(item.text())  # 将获取的IP写入到当前选择的IP地址栏中
            self.le_machine_name.setText(machine_name)  # 将获取的设备名写入到当前选择的设备名中
            self.cb_room.setCurrentText(machine_room)  # 将获取的机房名写入到当前选择的机房名中
            self.machine_info = [machine_id, machine_name, machine_room, machine_sn]
            # print('当前设备的信息：', self.machine_info)
        else:
            QtWidgets.QMessageBox.warning(self, '选择主机', '未选择到IP！')
            self.le_current_ip.clear()
            self.le_user.clear()
            self.le_password.clear()
            self.le_machine_name.clear()
            self.cb_room.setCurrentIndex(-1)
            self.te_remark.clear()
            self.machine_info = None  # 自定义设备信息

    # 添加用户密码
    def add_passwd(self):
        username = self.le_user.text().strip()
        passwd = self.le_password.text().strip()
        ip = self.le_current_ip.text().strip()
        remark = self.te_remark.toPlainText().strip()
        machine_name = self.le_machine_name.text().strip()
        machine_room = self.cb_room.currentText()
        if username == '':
            QtWidgets.QMessageBox.warning(self, '添加用户密码', '用户名未输入')
        elif passwd == '':
            QtWidgets.QMessageBox.warning(self, '添加用户密码', '密码未输入')
        elif ip == '':
            QtWidgets.QMessageBox.warning(self, '添加用户密码', 'IP未选择或未输入')
        else:
            if self.machine_info:
                value = [username, passwd, ip, remark] + self.machine_info  #
                # print('输入信息：', value, '选择的设备信息：', self.machine_info)
                # 添加到数据库中
                try:
                    MachinePassword.insert_many([value],
                                                [MachinePassword.user, MachinePassword.password, MachinePassword.ip,
                                                 MachinePassword.remark,
                                                 MachinePassword.machine_id, MachinePassword.machine_name,
                                                 MachinePassword.room, MachinePassword.sn]).execute()
                except Exception as e:
                    print('添加用户密码错误：', e)
                else:
                    QtWidgets.QMessageBox.information(self, '添加用户密码信息', '添加成功！')
                    # 清空输入框信息
                    self.le_current_ip.clear()
                    self.le_user.clear()
                    self.le_password.clear()
                    self.te_remark.clear()
                    self.le_machine_name.clear()
                    self.cb_room.setCurrentIndex(-1)
                    self.machine_info = None  # 自定义设备信息
            else:
                value = [username, passwd, ip, remark, machine_name, machine_room, 1]  # 输入的信息
                # print('虚拟机设备信息：', value)
                # # 添加到数据库中
                try:
                    MachinePassword.insert_many([value],
                                                [MachinePassword.user, MachinePassword.password, MachinePassword.ip,
                                                 MachinePassword.remark, MachinePassword.machine_name,
                                                 MachinePassword.room, MachinePassword.machine_type]).execute()
                except Exception as e:
                    print('添加用户密码错误：', e)
                else:
                    QtWidgets.QMessageBox.information(self, '添加用户密码信息', '添加成功！')
                    # 清空输入框信息
                    self.le_current_ip.clear()
                    self.le_user.clear()
                    self.le_password.clear()
                    self.te_remark.clear()
                    self.le_machine_name.clear()
                    self.cb_room.setCurrentIndex(-1)
                    self.machine_info = None  # 自定义设备信息

    # 修改删除页面
    # 获取查询信息
    def display_userdata_modify(self):
        ip = self.le_modify_display_ip.text().strip()
        if ip == '':
            data_model = MachinePassword.select(MachinePassword.pid, MachinePassword.machine_name,
                                                MachinePassword.ip, MachinePassword.room, MachinePassword.user,
                                                MachinePassword.password, MachinePassword.sn,
                                                Case(MachinePassword.machine_type, [(0, '物理机'), (1, '虚拟机')]),
                                                MachinePassword.machine_id, MachinePassword.remark).tuples().execute()
        else:
            data_model = MachinePassword.select(MachinePassword.pid, MachinePassword.machine_name,
                                                MachinePassword.ip, MachinePassword.room, MachinePassword.user,
                                                MachinePassword.password, MachinePassword.sn,
                                                Case(MachinePassword.machine_type, [(0, '物理机'), (1, '虚拟机')]),
                                                MachinePassword.machine_id, MachinePassword.remark).where(
                MachinePassword.ip == ip).tuples().execute()
        # 将查询数据显示到表格中
        self.tb_modify_select.setRowCount(len(data_model))  # 表格数据行数
        self.lb_status_2.setText('查询到 {} 条记录'.format(len(data_model)))
        for row, row_data in enumerate(data_model):
            for col, item in enumerate(row_data):
                if item is None:
                    item = ''
                    self.tb_modify_select.setItem(row, col, QTableWidgetItem(str(item)))
                else:
                    cell_data = QTableWidgetItem(str(item))
                    # cell_data.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)     # 水平垂直居中
                    self.tb_modify_select.setItem(row, col, cell_data)
            # print('查询到的设备', row_data)
        self.tb_modify_select.resizeColumnsToContents()
        self.selected_data = None  # 清除选择状态
        # 清空输入框
        self.le_modify_user.clear()
        self.le_modify_password.clear()
        self.le_modify_ip.clear()
        self.le_modify_machine_name.clear()
        self.cb_modify_room.setCurrentIndex(-1)
        self.te_modify_remark.clear()
        self.le_modify_machine_name.setDisabled(False)
        self.cb_modify_room.setDisabled(False)

    # 获取选择的行信息
    def get_select_row(self):
        row_num = self.tb_modify_select.currentRow()
        machine_type = self.tb_modify_select.item(row_num, 7).text()
        pass_id = self.tb_modify_select.item(row_num, 0).text()
        machine_name = self.tb_modify_select.item(row_num, 1).text()
        ip = self.tb_modify_select.item(row_num, 2).text()
        room = self.tb_modify_select.item(row_num, 3).text()
        username = self.tb_modify_select.item(row_num, 4).text()
        user_passwd = self.tb_modify_select.item(row_num, 5).text()
        remark = self.tb_modify_select.item(row_num, 9).text()
        # value = (machine_type,pass_id,machine_name,ip,room,username,user_passwd,remark)
        # print('当前选择行：', value)
        if machine_type == '虚拟机':
            self.le_modify_user.setText(username)
            self.le_modify_password.setText(user_passwd)
            self.le_modify_ip.setText(ip)
            self.le_modify_machine_name.setText(machine_name)
            # self.cb_modify_room.setCurrentText(room)
            self.te_modify_remark.setText(remark)
            # 判断机房信息是否为空
            if room == '':
                self.cb_modify_room.setCurrentIndex(-1)
            else:
                self.cb_modify_room.setCurrentText(room)
            self.selected_data = (machine_type, pass_id)
            # 设置窗口状态
            self.le_modify_ip.setDisabled(False)
            self.le_modify_machine_name.setDisabled(False)
            self.cb_modify_room.setDisabled(False)

        elif machine_type == '物理机':
            self.le_modify_user.setText(username)
            self.le_modify_password.setText(user_passwd)
            self.le_modify_ip.setText(ip)
            self.le_modify_machine_name.setText(machine_name)
            self.te_modify_remark.setText(remark)
            # 判断机房信息是否为空
            if room == '':
                self.cb_modify_room.setCurrentIndex(-1)
            else:
                self.cb_modify_room.setCurrentText(room)
            self.selected_data = (machine_type, pass_id)
            # 设置窗口状态
            self.le_modify_ip.setDisabled(True)
            self.le_modify_machine_name.setDisabled(True)
            self.cb_modify_room.setDisabled(True)

    # 提交修改
    def commit_modify(self):
        username = self.le_modify_user.text().strip()
        user_passwd = self.le_modify_password.text().strip()
        machine_name = self.le_modify_machine_name.text().strip()
        room = self.cb_modify_room.currentText()
        ip = self.le_modify_ip.text().strip()
        remark = self.te_modify_remark.toPlainText()
        # 判断是否有选择行，并获取到行数据
        if self.selected_data:
            # 判断为物理机
            if self.selected_data[0] == '物理机':
                # data = (username,user_passwd)
                pid = self.selected_data[1]
                # print(pid,data)
                try:
                    MachinePassword.update(user=username, password=user_passwd).where(
                        MachinePassword.pid == pid).execute()
                except Exception as e:
                    print('修改用户密码信息错误：', e)
                else:
                    QtWidgets.QMessageBox.information(self, '修改用户密码信息', '修改成功！')
                    self.selected_data = None  # 清除选择状态
                    self.display_userdata_modify()  # 刷新查询列表
                    # 清空输入框
                    self.le_modify_user.clear()
                    self.le_modify_password.clear()
                    self.le_modify_ip.clear()
                    self.le_modify_machine_name.clear()
                    self.cb_modify_room.setCurrentIndex(-1)
                    self.te_modify_remark.clear()
                    self.le_modify_machine_name.setDisabled(False)
                    self.cb_modify_room.setDisabled(False)
            # 判断为虚拟机
            else:
                # data = (username, user_passwd, machine_name, room, remark)
                pid = self.selected_data[1]
                # print(pid, data)
                try:
                    MachinePassword.update(user=username, password=user_passwd, machine_name=machine_name, room=room,
                                           ip=ip,remark=remark).where(MachinePassword.pid == pid).execute()
                except Exception as e:
                    print('修改用户密码信息错误：', e)
                else:
                    QtWidgets.QMessageBox.information(self, '修改用户密码信息', '修改成功！')
                    self.selected_data = None  # 清除选择状态
                    self.display_userdata_modify()  # 刷新查询列表
                    # 清空输入框
                    self.le_modify_user.clear()
                    self.le_modify_password.clear()
                    self.le_modify_ip.clear()
                    self.le_modify_machine_name.clear()
                    self.cb_modify_room.setCurrentIndex(-1)
                    self.te_modify_remark.clear()
                    self.le_modify_machine_name.setDisabled(False)
                    self.cb_modify_room.setDisabled(False)
        else:
            QtWidgets.QMessageBox.warning(self, '修改用户密码信息', '未选择需要修改的用户信息！')

    # 删除用户密码信息
    def del_user_passwd(self):
        row_num = self.tb_modify_select.currentRow()  # 当前选择的行
        # print('row_num', row_num)
        # 判断是否选择了行
        if row_num != -1:
            pid = self.tb_modify_select.item(row_num, 0).text()
            # print('选择的行ID', pid)
            if QtWidgets.QMessageBox.question(self, '删除用户信息',
                                              '确定要删除用户密码吗？') == QtWidgets.QMessageBox.Yes:
                try:
                    MachinePassword.delete().where(MachinePassword.pid == pid).execute()
                except Exception as e:
                    print('删除用户密码错误：', e)
                else:
                    QtWidgets.QMessageBox.information(self, '删除用户信息', '删除用户密码信息成功！')
                    self.display_userdata_modify()  # 刷新查询列表
            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self, '删除用户信息', '请选择需要删除用户！')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    passwd_win = UiPassword()
    passwd_win.show()
    sys.exit(app.exec())
