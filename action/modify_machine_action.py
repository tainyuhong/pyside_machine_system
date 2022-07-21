import sys,time
from ui.modify import *
from PySide6 import QtWidgets, QtGui, QtCore
from ui.add_machine import *
from db.db_orm import *
import logging
logger = logging.getLogger('peewee')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


class UiModifyMachine(Ui_modify, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiModifyMachine, self).__init__(parent)
        self.setupUi(self)

        # 定义按钮功能
        self.bt_select.clicked.connect(self.select)       # 查询内容
        self.bt_clear.clicked.connect(self.clear)       # 清空条件框内容
        self.bt_modify.clicked.connect(self.submit_modify)


    def select(self):
        machine_name = self.machine_name.text().strip()
        mg_ip = self.mg_ip.text().strip()

        print('name：{},ip:{}'.format(machine_name, mg_ip))
        if machine_name != '' or mg_ip != '':
            print('设备名或IP有一项不为空')
            print('machine_name',machine_name,'mg_ip',mg_ip)

            if machine_name == '':
                print('设备名为空')
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn, MachineInfos.factory_date,
                                                 MachineInfos.end_ma_date, MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1, MachineInfos.bmc_ip, MachineInfos.comments) \
                    .where(MachineInfos.mg_ip.contains(mg_ip)).prefetch(MachineRoom, Cabinet, CabPosition)
                print('查询IP SQL',data_model,len(data_model))
                data = [(i.machine_id, i.machine_roomid.room_id,
                         i.cabinet_name.cab_num, i.start_position.num,
                         i.end_position.num, i.machine_name,
                         i.machine_sort_name.sort_name, i.machine_factory,
                         i.model, i.machine_sn, i.factory_date,
                         i.end_ma_date, i.work_are,
                         i.machine_admin, i.app_admin, i.mg_ip,
                         i.app_ip1, i.bmc_ip, i.comments) for i in data_model]
                # print(data)
                data_count = len(data)
                self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
                self.lb_status.setStyleSheet('color:blue')
                self.tb_display.setRowCount(data_count)      # 根据内容设置行数
                self.tb_display.clearContents()
                for row, d1 in enumerate(data):
                    for col, d2 in enumerate(d1):
                        if col == 0:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                            self.tb_display.item(row, 0).setFlags(Qt.ItemIsEnabled)  # 第一列设置为不可编辑
                        else:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                self.tb_display.resizeColumnsToContents()
            elif mg_ip == '':
                print('IP为空')
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn, MachineInfos.factory_date,
                                                 MachineInfos.end_ma_date, MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1, MachineInfos.bmc_ip, MachineInfos.comments) \
                    .where(MachineInfos.machine_name.contains(machine_name)).prefetch(MachineRoom, Cabinet, CabPosition)
                print('查询设备SQL', data_model, len(data_model))
                data = [(i.machine_id, i.machine_roomid.room_id,
                         i.cabinet_name.cab_num, i.start_position.num,
                         i.end_position.num, i.machine_name,
                         i.machine_sort_name.sort_name, i.machine_factory,
                         i.model, i.machine_sn, i.factory_date,
                         i.end_ma_date, i.work_are,
                         i.machine_admin, i.app_admin, i.mg_ip,
                         i.app_ip1, i.bmc_ip, i.comments) for i in data_model]
                # print(data)
                data_count = len(data)
                self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
                self.lb_status.setStyleSheet('color:blue')
                self.tb_display.setRowCount(data_count)  # 根据内容设置行数
                for row, d1 in enumerate(data):
                    for col, d2 in enumerate(d1):
                        if col == 0:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                            self.tb_display.item(row, 0).setFlags(Qt.ItemIsEnabled)  # 第一列设置为不可编辑
                        else:
                            self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                self.tb_display.resizeColumnsToContents()       # 设置自适应列宽

            elif machine_name != '' and mg_ip != '':
                print('两个都不为空',machine_name,mg_ip)
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn, MachineInfos.factory_date,
                                                 MachineInfos.end_ma_date, MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1, MachineInfos.bmc_ip, MachineInfos.comments) \
                    .where(MachineInfos.machine_name.contains(machine_name) & MachineInfos.mg_ip.contains(mg_ip)).prefetch(MachineRoom, Cabinet, CabPosition)
                print('查询设备SQL', data_model, len(data_model))
                data = [(i.machine_id, i.machine_roomid.room_id,
                                       i.cabinet_name.cab_num, i.start_position.num,
                                       i.end_position.num, i.machine_name,
                                       i.machine_sort_name.sort_name, i.machine_factory,
                                       i.model, i.machine_sn, i.factory_date,
                                       i.end_ma_date, i.work_are,
                                       i.machine_admin, i.app_admin, i.mg_ip,
                                       i.app_ip1, i.bmc_ip, i.comments) for i in data_model]
                             # print(data)
                data_count = len(data)
                self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
                self.lb_status.setStyleSheet('color:blue')
                self.tb_display.setRowCount(data_count)  # 根据内容设置行数
                for row,d1 in enumerate(data):
                    for col,d2 in enumerate(d1):
                        if col == 0:
                            self.tb_display.setItem(row,col,QTableWidgetItem(str(data[row][col])))
                            self.tb_display.item(row, 0).setFlags(Qt.ItemIsEnabled)  # 第一列设置为不可编辑
                        else:
                            self.tb_display.setItem(row,col,QTableWidgetItem(str(data[row][col])))
                self.tb_display.resizeColumnsToContents()
        else:
            print('请输入查询条件')
        self.tb_display.cellChanged.connect(self.display_changed)  # 启用单元格式信号

    def clear(self):
        """
        清除条件框中内容
        :return:
        """
        self.machine_name.setText('')
        self.mg_ip.setText('')

    def display_changed(self):
        print('有变化')


    def submit_modify(self):
        print('提交修改')
        self.tb_display.cellChanged.disconnect(self.display_changed)  # 启用单元格式信号
        # self.tb_display.blockSignals(True)    # 进入阻塞模式
        print('断开连接')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiModifyMachine()
    add_win.show()
    sys.exit(app.exec())
