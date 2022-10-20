import sys
from PySide6 import QtWidgets
from ui.check_config_ui import *
from db.db_orm import database, CmdFile, MachineCheckUser, MachineList, ViewCheckCmd
# import logging
#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class UiCconfigCheck(Ui_check_config, QtWidgets.QWidget):
    """
    添加设备窗口类
    """
    room_and_id = None  # 定义一个机房ID与机房名称的映射，后用于字典

    def __init__(self, parent=None):
        super(UiCconfigCheck, self).__init__(parent)
        self.setupUi(self)

        self.selected_shell_id = None

        # 初始化巡检类型下拉菜单数据
        self.get_check_sort()
        self.display_machine()
        self.display_cmd()  # 加载shell信息

        # 定义按钮功能
        self.bt_add_check.clicked.connect(self.add_config)  # 添加巡检设备按钮
        self.bt_select.clicked.connect(self.query_by_condition)  # 查询按钮
        self.bt_query_select.clicked.connect(self.query_check_machine)  # 巡检配置查询
        self.bt_query_del.clicked.connect(self.del_check_machine)       # 删除巡检配置信息
        self.bt_add_shell.clicked.connect(self.add_shell)  # 添加命令脚本
        self.bt_del_shell.clicked.connect(self.del_shell)  # 删除命令脚本
        self.bt_modify_shell.clicked.connect(self.modify_shell)  # 修改脚本

        self.tb_display_shell.doubleClicked.connect(self.get_table_row)  # 定义双击事件

    # 巡检配置窗口界面
    # 获取巡检类型
    def get_check_sort(self):
        sort_model = CmdFile.select(CmdFile.cmd_name).execute()
        sort = [i.cmd_name for i in sort_model]
        # print(sort)
        self.cb_check_sort.clear()
        self.cb_check_sort.addItems(sort)

    # 查询并显示设备信息
    def display_machine(self):
        data_model = MachineList.select(MachineList.machine_id, MachineList.room_name, MachineList.cab_name,
                                        MachineList.start_position, MachineList.postion_u, MachineList.machine_name,
                                        MachineList.mg_ip, MachineList.machine_factory, MachineList.model).execute()
        self.tb_display.setRowCount(len(data_model))  # 设置行数
        # 写入表格内容
        for row, item in enumerate(data_model):
            for col, cell in enumerate((item.machine_id, item.room_name, item.cab_name, item.start_position,
                                        item.postion_u, item.machine_name, item.mg_ip, item.machine_factory,
                                        item.model)):
                cell_data = QtWidgets.QTableWidgetItem(str(cell))
                if col == 0:
                    cell_data.setCheckState(Qt.Unchecked)
                self.tb_display.setItem(row, col, cell_data)
        self.tb_display.resizeColumnsToContents()  # 设置单元格

    # 按条件进行查询设备
    def query_by_condition(self):
        machine_name = self.machine_name.text().strip()
        mg_ip = self.mg_ip.text().strip()
        if machine_name == '' and mg_ip == '':
            data_model = MachineList.select(MachineList.machine_id, MachineList.room_name, MachineList.cab_name,
                                            MachineList.start_position, MachineList.postion_u, MachineList.machine_name,
                                            MachineList.mg_ip, MachineList.machine_factory, MachineList.model).execute()
        else:
            data_model = MachineList.select(MachineList.machine_id, MachineList.room_name, MachineList.cab_name,
                                            MachineList.start_position, MachineList.postion_u, MachineList.machine_name,
                                            MachineList.mg_ip, MachineList.machine_factory, MachineList.model).orwhere(
                MachineList.machine_name.contains(machine_name)).orwhere(MachineList.mg_ip == mg_ip).execute()
        self.tb_display.setRowCount(len(data_model))  # 设置行数
        # 写入表格内容
        for row, item in enumerate(data_model):
            for col, cell in enumerate((item.machine_id, item.room_name, item.cab_name, item.start_position,
                                        item.postion_u, item.machine_name, item.mg_ip, item.machine_factory,
                                        item.model)):
                cell_data = QtWidgets.QTableWidgetItem(str(cell))
                if col == 0:
                    cell_data.setCheckState(Qt.Unchecked)
                self.tb_display.setItem(row, col, cell_data)
        self.tb_display.resizeColumnsToContents()  # 设置单元格
        self.lb_check_status.setText('查询到 {} 条记录'.format(len(data_model)))  # 巡检配置窗口状态栏信息设置

    # 获取选择的设备并添加配置
    def add_config(self):
        # 获取巡检用户及密码
        user = self.le_user.text().strip()  # 巡检用户
        passwd = self.le_passwd.text().strip()  # 巡检密码
        check_sort = self.cb_check_sort.currentText()  # 选择的巡检类型
        # 从数据库获取巡检分类信息
        check_sort_model = CmdFile.select(CmdFile.cmd_name, CmdFile.cmd_id).tuples().execute()  # 查询分类信息及ID
        check_sor_data = dict([i for i in check_sort_model])  # 将查询到的命令类型名称与ID组合成字典

        # 校验输入数据
        if user == '' or passwd == '' or check_sort == '无':
            QtWidgets.QMessageBox.warning(self, '添加巡检用户信息', '请输入巡检用户及密码，并选择巡检类型！')
        else:
            if QtWidgets.QMessageBox.question(self, '添加巡检配置信息', '你确定要添加巡检配置信息吗？') == QtWidgets.QMessageBox.Yes:
                # 获取钩择的设备信息
                row = self.tb_display.rowCount()  # 表格的总行数
                checked_cell = []  # 钩选的单元格
                for i in range(row):
                    cell = self.tb_display.item(i, 0)
                    if cell.checkState():
                        checked_cell.append(cell.text())
                # print('当前选择单元格：',checked_cell)

                # 判断是否有选择设备
                if checked_cell:
                    # print('用户名和密码：{}-->{},{},{}'.format(user, passwd, check_sor_data[check_sort], checked_cell))
                    with database.atomic():
                        for ma in checked_cell:
                            MachineCheckUser.insert_many([(user, passwd, check_sor_data[check_sort], ma)], (
                                MachineCheckUser.user, MachineCheckUser.password, MachineCheckUser.cmd_id,
                                MachineCheckUser.machine)).execute()
                        QtWidgets.QMessageBox.information(self, '添加巡检配置信息', '保存成功!')
                        self.le_user.clear()        # 清空文本框
                        self.le_passwd.clear()      # 清空文本框
                        self.cb_check_sort.setCurrentIndex(0)
                        self.display_machine()     # 取消选择
                else:
                    QtWidgets.QMessageBox.warning(self, '添加巡检配置信息', '请选择需要配置的主机!')
            else:
                pass

    # 巡检查询窗口界面
    def query_check_machine(self):
        machine_name = self.query_machine_name.text().strip()
        mg_ip = self.query_mg_ip.text().strip()
        if machine_name == '' and mg_ip == '':
            data_model = ViewCheckCmd.select(ViewCheckCmd.id, ViewCheckCmd.machine_id, ViewCheckCmd.hostname,
                                             ViewCheckCmd.ip, ViewCheckCmd.user, ViewCheckCmd.password,
                                             ViewCheckCmd.cmd_name, ViewCheckCmd.cmd).execute()
        else:
            data_model = ViewCheckCmd.select(ViewCheckCmd.id, ViewCheckCmd.machine_id, ViewCheckCmd.hostname,
                                             ViewCheckCmd.ip, ViewCheckCmd.user, ViewCheckCmd.password,
                                             ViewCheckCmd.cmd_name, ViewCheckCmd.cmd).orwhere(
                ViewCheckCmd.hostname.contains(machine_name)).orwhere(ViewCheckCmd.machine_id == mg_ip).execute()
        self.tb_query_display.setRowCount(len(data_model))  # 设置行数
        # 写入表格内容
        for row, item in enumerate(data_model):
            for col, cell in enumerate((item.song_id, item.machine_id, item.hostname, item.ip, item.user,
                                        item.password, item.cmd_name, item.cmd)):
                cell_data = QtWidgets.QTableWidgetItem(str(cell))
                self.tb_query_display.setItem(row, col, cell_data)
        # self.tb_query_display.resizeColumnsToContents()  # 设置单元格
        self.tb_query_display.resizeRowsToContents()  # 设置单元格
        self.tb_query_display.horizontalHeader().setStretchLastSection(True)  # 最后一列拉宽
        self.lb_query_check_status.setText('查询到 {} 条记录'.format(len(data_model)))  # 巡检配置窗口状态栏信息设置

    # 删除巡检配置信息
    def del_check_machine(self):
        item = self.tb_query_display.selectedItems()  # 获取选择的行
        if not item:
            QtWidgets.QMessageBox.warning(self, '删除巡检配置信息', '请先选择需要删除巡检配置信息的行！')
        else:
            check_id = item[0].text()  # 获取id
            # print('选择的行的内容', check_id)
            if QtWidgets.QMessageBox.question(self, '删除巡检配置信息', '你确定要删除巡检配置信息吗？') == QtWidgets.QMessageBox.Yes:
                try:
                    MachineCheckUser.delete_by_id(check_id) # 根据id进行删除
                except Exception as e:
                    print('删除巡检配置信息错误：',e)
                else:
                    QtWidgets.QMessageBox.information(self, '删除巡检配置信息', '删除成功！')
                    self.query_check_machine()
            else:
                pass

    # 巡检命令配置界面
    # 添加SHELL
    def add_shell(self):
        shell_name = self.le_shell_name.text().strip()
        shell_content = self.text_shell.toPlainText().strip()
        if shell_name == '' or shell_content == '':
            QtWidgets.QMessageBox.warning(self, '添加shell命令', '请填写完整的shell名及shell内容！')
        else:
            input_data = (shell_name, shell_content)
            # print(input_data)
            if QtWidgets.QMessageBox.question(self, '添加shell命令', '你确定要添加shell吗？') == QtWidgets.QMessageBox.Yes:
                try:
                    with database.atomic():
                        CmdFile.insert_many([input_data], fields=(CmdFile.cmd_name, CmdFile.cmd)).execute()
                except Exception as e:
                    print('添加shell出错：', e)
                else:
                    QtWidgets.QMessageBox.information(self, '添加shell命令', '添加成功！')
                    self.display_cmd()  # 刷新表内容
                    self.le_shell_name.clear()
                    self.text_shell.clear()
                    self.get_check_sort()       # 刷新巡检分类信息
            else:
                pass

    # 显示shell命令
    def display_cmd(self):
        shell_data_model = CmdFile.select(CmdFile.cmd_id, CmdFile.cmd_name, CmdFile.cmd).tuples().execute()
        self.tb_display_shell.setRowCount(len(shell_data_model))  # 设置表格的行
        # 显示到表格中
        for row, row_data in enumerate(shell_data_model):
            for col, cell_data in enumerate(row_data):
                self.tb_display_shell.setItem(row, col, QTableWidgetItem(str(cell_data)))
        self.tb_display_shell.resizeRowsToContents()  # 根据内容自定义行高
        self.lb_shell_status.setText('查询到 {} 条记录'.format(len(shell_data_model)))  # 巡检配置窗口状态栏信息设置

    # 删除shell
    def del_shell(self):
        item = self.tb_display_shell.selectedItems()  # 获取选择的行
        if not item:
            QtWidgets.QMessageBox.warning(self, '删除shell命令', '请先选择需要删除的shell的行！')
        else:
            shell_id = item[0].text()  # 获取id
            # print('选择的行的内容', shell_id)
            # 判断该shell是否有被主机使用
            if ViewCheckCmd.get_or_none(ViewCheckCmd.cmd_id == shell_id) is None:
                CmdFile.delete_by_id(shell_id)  # 根据id进行删除
                QtWidgets.QMessageBox.information(self, '删除shell命令', '删除成功！')
                self.display_cmd()  # 刷新表内容
                self.get_check_sort()  # 刷新巡检分类信息
            else:
                QtWidgets.QMessageBox.warning(self, '删除shell命令', '该shell已被使用，不能删除！')

    # 修改shell
    def modify_shell(self):
        shell_name = self.le_shell_name.text().strip()
        shell_content = self.text_shell.toPlainText().strip()
        if self.selected_shell_id is not None:
            if shell_name == '' or shell_content == '':
                QtWidgets.QMessageBox.warning(self, '修改shell命令', '请填写完整的shell名及shell内容！')
            else:
                # input_data = [shell_name, shell_content]
                if QtWidgets.QMessageBox.question(self, '修改shell命令', '你确定要修改shell吗？') == QtWidgets.QMessageBox.Yes:
                    try:
                        with database.atomic():
                            CmdFile.update(cmd_name=shell_name, cmd=shell_content).where(
                                CmdFile.cmd_id == self.selected_shell_id).execute()
                    except Exception as e:
                        print('添加shell出错：', e)
                    else:
                        QtWidgets.QMessageBox.information(self, '修改shell命令', '修改成功！')
                        self.display_cmd()  # 刷新表内容
                        self.le_shell_name.clear()
                        self.text_shell.clear()
                        self.selected_shell_id = None
                        self.tb_display_shell.setCurrentItem(None)      # 设置为非选择状态
                else:
                    pass
        else:
            QtWidgets.QMessageBox.warning(self, '修改shell命令', '请双击需要修改shell所在的行！')

    # 双击单元格获取行内容
    def get_table_row(self):
        item = self.tb_display_shell.selectedItems()  # 获取选择的行
        if item:
            self.selected_shell_id = item[0].text()
            self.le_shell_name.setText(item[1].text())  # 获取id
            self.text_shell.setPlainText(item[2].text())
        else:
            pass

    # 重新定义键盘esc键事件，退出修改模式
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # 当在巡检命令配置窗口时，退出修改模式
            if self.tabWidg_check.currentIndex() == 2:
                # print('巡检命令配置窗口，按了ESC键')
                self.le_shell_name.clear()
                self.text_shell.clear()
                self.selected_shell_id = None
                self.tb_display_shell.setCurrentItem(None)  # 设置为非选择状态
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    check_conf_win = UiCconfigCheck()
    check_conf_win.show()
    sys.exit(app.exec())
