import sys, time
from ui.modify import *
from PySide6 import QtWidgets, QtGui, QtCore
from ui.add_machine import *
from db.db_orm import *
import logging


# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class UiModifyMachine(Ui_modify, QtWidgets.QWidget):
    save_flag = True  # 判断是否有修改
    is_selected = False  # 是否再次查询
    modify_data = []
    modify_item = dict()

    def __init__(self, parent=None):
        super(UiModifyMachine, self).__init__(parent)
        self.setupUi(self)

        # 定义按钮功能
        self.bt_select.clicked.connect(self.select)  # 查询内容
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容
        self.bt_modify.clicked.connect(self.submit_modify)

    def select(self):
        machine_name = self.machine_name.text().strip()
        mg_ip = self.mg_ip.text().strip()
        # print('是否保存的状态：', self.save_flag)
        # 判断是否进行过一次查询
        if self.is_selected:
            self.tb_display.cellChanged.disconnect(self.display_changed)  # 启用单元格式信号
        else:
            pass
        # 查询结果数据处理
        if machine_name != '' or mg_ip != '':
            # print('machine_name', machine_name, 'mg_ip', mg_ip)

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
                print('查询IP SQL', data_model, len(data_model))
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
                self.tb_display.resizeColumnsToContents()  # 设置自适应列宽

            elif machine_name != '' and mg_ip != '':
                print('两个都不为空', machine_name, mg_ip)
                data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                                 MachineInfos.cabinet_name, MachineInfos.start_position,
                                                 MachineInfos.end_position, MachineInfos.machine_name,
                                                 MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                                 MachineInfos.model, MachineInfos.machine_sn, MachineInfos.factory_date,
                                                 MachineInfos.end_ma_date, MachineInfos.work_are,
                                                 MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                                 MachineInfos.app_ip1, MachineInfos.bmc_ip, MachineInfos.comments) \
                    .where(
                    MachineInfos.machine_name.contains(machine_name) & MachineInfos.mg_ip.contains(mg_ip)).prefetch(
                    MachineRoom, Cabinet, CabPosition)
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
                self.tb_display.resizeColumnsToContents()
        else:
            print('请输入查询条件')
        # 在数据未修改或已经保存后才能发送信号
        # print('是否保存的状态,查询显示完后状态：', self.save_flag)
        self.tb_display.cellChanged.connect(self.display_changed)  # 启用单元格修改信号
        self.is_selected = True  # 标记为已查询状态

    def clear(self):
        """
        清除条件框中内容
        :return:
        """
        self.machine_name.setText('')
        self.mg_ip.setText('')

    def display_changed(self):
        changed_item = self.tb_display.currentItem()  # 获取当前修改的单元格信息
        item_row = changed_item.row()  # 所在行
        item_col = changed_item.column()  # 所在列
        item_name = changed_item.text()  # 修改后项的值
        machine_id = self.tb_display.item(item_row, 0).text()  # 修改数据所属的设备id
        print('修改后的内容：', item_row, item_col, item_name, machine_id)
        table_list = (MachineInfos.machine_id, MachineInfos.machine_roomid,
                      MachineInfos.cabinet_name, MachineInfos.start_position,
                      MachineInfos.end_position, MachineInfos.machine_name,
                      MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                      MachineInfos.model, MachineInfos.machine_sn, MachineInfos.factory_date,
                      MachineInfos.end_ma_date, MachineInfos.work_are,
                      MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                      MachineInfos.app_ip1, MachineInfos.bmc_ip, MachineInfos.comments)
        print('表结构中字段名：', table_list[item_col])
        self.modify_item['id'] = machine_id
        self.modify_item['data'] = table_list[item_col] = item_name
        self.modify_data[table_list[item_col]] = item_name
        print('修改的数据内容：', self.modify_data)
        # a = [{'id': '1', 'data': {'ip': '192.168','name':'服务器'}},{'id': '2', 'data': {'ip': '192.1','name':'小型机'}}]   # 要生成的数据格式
        self.save_flag = False  # 设置为未保存

    def submit_modify(self):
        print('提交修改')
        if not self.save_flag:
            self.tb_display.cellChanged.disconnect(self.display_changed)  # 启用单元格式信号
            # print('断开连接')
            self.save_flag = True  # 设置为已保存
            self.is_selected = False  # 设置为未查询过
        else:
            print('没有数据需要保存！')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiModifyMachine()
    add_win.show()
    sys.exit(app.exec())

"""
业务判断逻辑
1、查询逻辑
    根据设备名称、MG_IP自由组合查询，包含任务一个字段就进行查询
2、修改判断逻辑
    使用了两个标志参数，save_flag、is_selected
    save_flag = True  # 判断是否有修改
    is_selected = False  # 在点击了查询按钮后设置为True，表示已经进行了查询
    + 在点击了查询按钮后，先判断查询状态，为是时，先断开信号，为否时，进入后续操作、发送单元格修改信号给槽display_changed，并将is_selected设置为True
    + 保存修改：将save_flag标志设置为True,同时将is_selected设置为未查询
    
    
"""
