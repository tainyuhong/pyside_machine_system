import sys
from ui.down_shelf import *
from PySide6 import QtWidgets
from db.db_orm import *
from action.pub_infos import PubSwitch


class UiDownShelf(Ui_down_shelf, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiDownShelf, self).__init__(parent)
        self.pub_infos = PubSwitch()
        self.setupUi(self)

        self.display_room()  # 显示机房下拉菜单内容
        self.cb_room.currentIndexChanged.connect(self.display_cabinet)  # 定义机房下拉菜单触发事件

        # 定义按钮功能
        self.bt_select.clicked.connect(self.display)  # 查询内容
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容

        # 设置下架时间默认为系统当天
        self.down_time.setDate(QDate.currentDate())  # 设置默认为系统当天
        self.bt_donw_shelf.clicked.connect(self.select_machine)  # 设置为下架状态

    # 获取机房机柜信息并显示在下拉菜单中
    def display_room(self):
        room = self.pub_infos.get_room().values()
        self.cb_room.addItems(room)

    # 获取并显示机柜信息至下拉菜单中
    def display_cabinet(self):
        cabinet = self.pub_infos.get_cabinet_infos(self.cb_room.currentText())
        self.cb_cabinet.clear()
        self.cb_cabinet.addItem('所有')
        self.cb_cabinet.addItems(cabinet)

    # 显示查询结果
    def display(self):
        self.tb_display.clearContents()  # 清空表格中内容
        room = self.cb_room.currentText()
        cabinet = self.cb_cabinet.currentText()
        machine_name = self.machine_name.text().strip()
        sn = self.le_sn.text().strip()
        mg_ip = self.mg_ip.text().strip()

        # 查询结果数据处理
        query = MachineList.select(MachineList.machine_id, MachineList.room_name,
                                   MachineList.cab_name, MachineList.start_position,
                                   MachineList.start_position + MachineList.postion_u - 1,
                                   Case(None, ((MachineList.machine_name.is_null(True), ''),
                                               (MachineList.machine_name.is_null(False), MachineList.machine_name))),
                                   MachineList.machine_sort_name, MachineList.machine_factory, MachineList.model,
                                   Case(None, ((MachineList.machine_sn.is_null(True), ''),
                                               (MachineList.machine_sn.is_null(False), MachineList.machine_sn))),
                                   Case(None, ((MachineList.machine_admin.is_null(True), ''), (
                                       MachineList.machine_admin.is_null(False), MachineList.machine_admin)), ),
                                   Case(None, ((MachineList.mg_ip.is_null(True), ''),
                                               (MachineList.mg_ip.is_null(False), MachineList.mg_ip)), ),
                                   Case(None, ((MachineList.bmc_ip.is_null(True), ''),
                                               (MachineList.bmc_ip.is_null(False), MachineList.bmc_ip))),
                                   Case(None, ((MachineList.comments.is_null(True), ''),
                                               (MachineList.comments.is_null(False), MachineList.comments))))
        cond_room = MachineList.room_name == self.cb_room.currentText()
        cond_cabinet = MachineList.cab_name == self.cb_cabinet.currentText()
        cond_machine_name = MachineList.machine_name.contains(machine_name)
        cond_sn = MachineList.machine_sn == self.le_sn.text().strip()
        # 判断是否选择带内IP
        if self.rd_mg_ip.isChecked():
            cond_mg_ip = MachineList.mg_ip.contains(mg_ip)
        else:
            cond_mg_ip = MachineList.bmc_ip.contains(mg_ip)

        cond_query = None  # 设置查询条件初始值为空，即查询所有
        # 机房为所有
        if room == '所有':
            # print('machine_name', machine_name, 'mg_ip', mg_ip)
            if machine_name != '' and mg_ip == '' and sn == '':
                cond_query = cond_machine_name
            elif machine_name == '' and mg_ip != '' and sn == '':
                cond_query = cond_mg_ip
            elif machine_name == '' and mg_ip == '' and sn != '':
                cond_query = cond_sn
            elif machine_name != '' and mg_ip != '' and sn == '':
                cond_query = cond_machine_name & cond_mg_ip
            elif machine_name != '' and mg_ip == '' and sn != '':
                cond_query = cond_machine_name & cond_sn
            elif machine_name == '' and mg_ip != '' and sn != '':
                cond_query = cond_mg_ip & cond_sn
            elif machine_name != '' and mg_ip != '' and sn != '':
                cond_query = cond_machine_name & cond_mg_ip & cond_sn
        elif room != '所有' and cabinet == '所有':
            if machine_name != '' and mg_ip == '' and sn == '':
                cond_query = cond_room & cond_machine_name
            elif machine_name == '' and mg_ip == '' and sn != '':
                cond_query = cond_room & cond_sn
            elif machine_name == '' and mg_ip != '' and sn == '':
                cond_query = cond_room & cond_mg_ip
            elif machine_name != '' and mg_ip == '' and sn != '':
                cond_query = cond_room & cond_machine_name & cond_sn
            elif machine_name != '' and mg_ip != '' and sn == '':
                cond_query = cond_room & cond_machine_name & cond_mg_ip
            elif machine_name == '' and mg_ip != '' and sn != '':
                cond_query = cond_room & cond_mg_ip & cond_sn
            elif machine_name != '' and mg_ip != '' and sn != '':
                cond_query = cond_room & cond_machine_name & cond_mg_ip & cond_sn
            else:
                cond_query = cond_room
        elif room != '所有' and cabinet != '所有':
            if machine_name != '' and mg_ip == '' and sn == '':
                cond_query = cond_room & cond_cabinet & cond_machine_name
            elif machine_name == '' and mg_ip == '' and sn != '':
                cond_query = cond_room & cond_cabinet & cond_sn
            elif machine_name == '' and mg_ip != '' and sn == '':
                cond_query = cond_room & cond_cabinet & cond_mg_ip

            elif machine_name != '' and mg_ip == '' and sn != '':
                cond_query = cond_room & cond_cabinet & cond_machine_name & cond_sn
            elif machine_name == '' and mg_ip != '' and sn != '':
                cond_query = cond_room & cond_cabinet & cond_mg_ip & cond_sn
            elif machine_name != '' and mg_ip != '' and sn == '':
                cond_query = cond_room & cond_cabinet & cond_machine_name & cond_mg_ip

            elif machine_name != '' and mg_ip != '' and sn != '':
                cond_query = cond_room & cond_cabinet & cond_machine_name & cond_mg_ip & cond_sn
            else:
                cond_query = cond_room & cond_cabinet
        data_model = query.where(cond_query).tuples()
        print(data_model.sql())
        data = [i for i in data_model]
        # print(data)
        data_count = len(data)
        self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_status.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                # 当为第一列时添加复选框按钮
                if col == 0:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                    self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)
                else:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        self.tb_display.resizeColumnsToContents()   # 自适应列宽

    # 下架操作---钩选的要下架的设备
    def select_machine(self):
        rowcount = self.tb_display.rowCount()  # 获取表格中总行数
        select_data = []  # 定义钩选的设备列表
        # 遍历所有行的第一列，将钩选的设备ID添加到select_data设备列表中
        for i in range(rowcount):
            select_row = self.tb_display.item(i, 0)  # 每行的第一列
            if select_row is not None:
                if select_row.checkState() == Qt.Checked:  # 判断是否钩选
                    # print('设备id:', select_row.text())
                    select_data.append(select_row.text())
                else:
                    pass
            else:
                pass

        # 获取并提交数据
        if len(select_data) == 0:
            QtWidgets.QMessageBox.warning(self, '设备下架', '请选择要下架的设备！')
        else:
            # 获取输入的下架信息
            comments = self.comments.toPlainText().strip()  # 下架情况说明
            operator = self.le_down_operator.text().strip()  # 下架执行人
            down_time = self.down_time.date().toString('yyyy/M/d')  # 下架时间
            if comments == '' or operator == '':
                QtWidgets.QMessageBox.warning(self, '设备下架', '请填写下架情况说明和执行人员！')
            else:
                # print('选择的设备：', select_data)
                if QtWidgets.QMessageBox.question(self, '设备下架',
                                                  '是否确认要下架选择的设备？') == QtWidgets.QMessageBox.Yes:
                    # 按格式生成下架数据（machine_id,up_or_down,operator, down_time, comments）
                    data = []  # 定义下架数据
                    for _ in select_data:
                        data.append((_, 2, operator, down_time, comments))
                    try:
                        with db.atomic():
                            ShelfManage.insert_many(data, fields=(
                                'machine_id', 'up_or_down', 'operator', 'date', 'comments')).execute()  # 插入下架设备信息到下架表中
                            MachineInfos.update(run_state=4, uninstall_date=down_time).where(
                                MachineInfos.machine_id.in_(select_data)).execute()  # 修改设备表运行状态为下架
                    except Exception as e:
                        logging.critical('执行下架出错：'.format(e))
                    else:
                        QtWidgets.QMessageBox.information(self, '设备下架成功', '成功下架设备！')
                        self.tb_display.clearContents()  # 清空表格插件内容
                else:
                    pass

    def clear(self):
        """
        清除条件框中内容
        :return:
        """
        self.machine_name.clear()
        self.mg_ip.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    down_win = UiDownShelf()
    down_win.show()
    sys.exit(app.exec())
