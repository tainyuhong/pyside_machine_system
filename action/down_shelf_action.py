import sys
from ui.down_shelf import *
from PySide6 import QtWidgets
from db.db_orm import *
# import logging
#
#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class UiDownShelf(Ui_down_shelf, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiDownShelf, self).__init__(parent)
        self.setupUi(self)

        # 定义按钮功能
        self.bt_select.clicked.connect(self.display)  # 查询内容
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容

        # 设置下架时间默认为系统当天
        self.down_time.setDate(QDate.currentDate())  # 设置默认为系统当天
        self.bt_donw_shelf.clicked.connect(self.select_machine)     # 设置为下架状态

    def display(self):
        machine_name = self.machine_name.text().strip()
        mg_ip = self.mg_ip.text().strip()
        self.tb_display.clearContents()         # 清空表格中内容
        # 查询结果数据处理
        if machine_name != '' or mg_ip != '':
            # print('machine_name', machine_name, 'mg_ip', mg_ip)
            if machine_name == '':
                # print('设备名为空')
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn,  MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1, MachineInfos.comments) \
                    .where((MachineInfos.mg_ip.contains(mg_ip)) & (MachineInfos.run_state != 4)).prefetch(MachineRoom, Cabinet, CabPosition)
                # print('查询IP SQL', data_model, len(data_model))
                data = [(i.machine_id, i.machine_roomid.room_id,
                         i.cabinet_name.cab_num, i.start_position.num,
                         i.end_position.num, i.machine_name,
                         i.machine_sort_name.sort_name, i.machine_factory,
                         i.model, i.machine_sn, i.work_are,
                         i.machine_admin, i.app_admin, i.mg_ip,
                         i.app_ip1, i.comments) for i in data_model]
                # print(data)
                data_count = len(data)
                self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
                self.lb_status.setStyleSheet('color:blue')
                self.tb_display.setRowCount(data_count)  # 根据内容设置行数
                self.tb_display.clearContents()
                for row, d1 in enumerate(data):
                    for col, d2 in enumerate(d1):
                        if col == 0:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                            self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)  # 第一列添加复选框按钮
                        else:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                self.tb_display.resizeColumnsToContents()
            elif mg_ip == '':
                # print('IP为空')
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn, MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1, MachineInfos.comments) \
                    .where((MachineInfos.machine_name.contains(machine_name)) & (MachineInfos.run_state != 4)).prefetch(MachineRoom, Cabinet, CabPosition)
                data = [(i.machine_id, i.machine_roomid.room_id,
                         i.cabinet_name.cab_num, i.start_position.num,
                         i.end_position.num, i.machine_name,
                         i.machine_sort_name.sort_name, i.machine_factory,
                         i.model, i.machine_sn, i.work_are,
                         i.machine_admin, i.app_admin, i.mg_ip,
                         i.app_ip1, i.comments) for i in data_model]
                # print(data)
                data_count = len(data)
                self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
                self.lb_status.setStyleSheet('color:blue')
                self.tb_display.setRowCount(data_count)  # 根据内容设置行数
                for row, d1 in enumerate(data):
                    for col, d2 in enumerate(d1):
                        if col == 0:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                            self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)  # 第一列添加复选框按钮
                        else:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                self.tb_display.resizeColumnsToContents()  # 设置自适应列宽

            elif machine_name != '' and mg_ip != '':
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn,  MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1,  MachineInfos.comments) \
                    .where(
                    (MachineInfos.machine_name.contains(machine_name)) & (MachineInfos.mg_ip.contains(mg_ip)) & (MachineInfos.run_state!=4)).prefetch(
                    MachineRoom, Cabinet, CabPosition)
                data = [(i.machine_id, i.machine_roomid.room_id,
                         i.cabinet_name.cab_num, i.start_position.num,
                         i.end_position.num, i.machine_name,
                         i.machine_sort_name.sort_name, i.machine_factory,
                         i.model, i.machine_sn, i.work_are,
                         i.machine_admin, i.app_admin, i.mg_ip,
                         i.app_ip1, i.comments) for i in data_model]
                # print(data)
                data_count = len(data)
                self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
                self.lb_status.setStyleSheet('color:blue')
                self.tb_display.setRowCount(data_count)  # 根据内容设置行数
                for row, d1 in enumerate(data):
                    for col, d2 in enumerate(d1):
                        if col == 0:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                            self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)  # 第一列添加复选框按钮
                        else:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                self.tb_display.resizeColumnsToContents()
        else:
            print('请输入查询条件')
        # 在数据未修改或已经保存后才能发送信号

    # 钩选的要下架的设备
    def select_machine(self):
        rowconut = self.tb_display.rowCount()       # 获取表格中总行数
        select_data = []                            # 定义钩选的设备列表
        # 遍历所有行的第一列，将钩选的设备ID添加到select_data设备列表中
        for i in range(rowconut):
            select_row = self.tb_display.item(i, 0)     # 每行的第一列
            if select_row is not None:
                if select_row.checkState() == Qt.Checked:   # 判断是否钩选
                    print('设备id:',select_row.text())
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
                print('选择的设备：', select_data)
                if QtWidgets.QMessageBox.question(self, '设备下架', '是否确认要下架选择的设备？') == QtWidgets.QMessageBox.Yes:
                    # 按格式生成下架数据（machine_id,up_or_down,operator, down_time, comments）
                    data = []  # 定义下架数据
                    for _ in select_data:
                        data.append((_, 2, operator, down_time, comments))
                    try:
                        with database.atomic():
                            res = ShelfManage.insert_many(data,fields=('machine_id','up_or_down','operator', 'date', 'comments'))
                            print(res)
                            res.execute()
                    except Exception as e:
                        print('执行下架出错：',e)
                    else:
                        try:
                            ret = MachineInfos.update(run_state=4,uninstall_date=down_time).where(MachineInfos.machine_id.in_(select_data)) # 修改设备表运行状态为下架
                            print(ret)
                            ret.execute()
                        except Exception as e:
                            print('修改状态出错：',e)
                        else:
                            print('状态修改成功！')
                        QtWidgets.QMessageBox.information(self, '设备下架成功', '成功下架设备！')
                        self.tb_display.clearContents()
                else:
                    pass

    def clear(self):
        """
        清除条件框中内容
        :return:
        """
        self.machine_name.setText('')
        self.mg_ip.setText('')




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    down_win = UiDownShelf()
    down_win.show()
    sys.exit(app.exec())

