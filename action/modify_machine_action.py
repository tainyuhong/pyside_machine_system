import sys
from ui.modify import *
from PySide6 import QtWidgets, QtGui, QtCore
from ui.add_machine import *
from db.db_orm import *


class UiModifyMachine(Ui_modify, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiModifyMachine, self).__init__(parent)
        self.setupUi(self)

        # 定义下拉菜单柜机房、机柜根据条件进行显示
        self.room.addItems(self.display_room())
        self.room.activated.connect(self.display_cabinet)

        # 定义按钮功能
        self.bt_select.clicked.connect(self.select)

    def display_room(self):
        """
        查询并显示机房信息
        :return: 机房信息列表
        """
        room_data = MachineRoom.select(MachineRoom.room_name)
        room_item = [item.room_name for item in room_data]
        print('机房列表', room_item)
        return room_item

    def display_cabinet(self):
        """
        查询并显示相应机房的机柜信息
        :return:
        """
        cabinet_data = Cabinet.select(Cabinet.cab_num).where(Cabinet.room == self.room.currentIndex())
        # print('SQL',cabinet_data)
        cabinet_item = [item.cab_num for item in cabinet_data]
        print(cabinet_item)
        # return cabinet_item
        self.cabinet.clear()
        self.cabinet.addItem('所有')
        self.cabinet.addItems(cabinet_item)

    def select(self):
        machine_name = self.machine_name.text().strip()
        mg_ip = self.mg_ip.text().strip()
        room = self.room.currentIndex()
        cabinet = self.cabinet.currentText()
        print('name：{},ip:{},romm:{},cabinet:{}'.format(machine_name, mg_ip, room, cabinet))
        if machine_name != '':
            data_model = MachineInfos.select('machine_id', 'machine_roomid', 'cabinet_name', 'start_position',
                                             'end_position', 'machine_name', 'machine_sort_name', 'machine_factory',
                                             'model', 'machine_sn', 'factory_date', 'end_ma_date', 'work_are',
                                             'machine_admin', 'app_admin', 'mg_ip', 'app_ip1', 'bmc_ip',
                                             'comments').where(
                MachineInfos.machine_name == machine_name)
            print('查询设备名 SQL', data_model)
        if mg_ip != '':
            data_model = MachineInfos.select('machine_id', 'machine_roomid', 'cabinet_name', 'start_position',
                                             'end_position', 'machine_name', 'machine_sort_name', 'machine_factory',
                                             'model', 'machine_sn', 'factory_date', 'end_ma_date', 'work_are',
                                             'machine_admin', 'app_admin', 'mg_ip', 'app_ip1', 'bmc_ip',
                                             'comments').where(
                MachineInfos.mg_ip == mg_ip)
            print('查询IP SQL', data_model)
        if room != 0:  # 所有机房，采用索引进行查询
            data_model = MachineInfos.select('machine_id', 'machine_roomid', 'cabinet_name', 'start_position',
                                             'end_position', 'machine_name', 'machine_sort_name', 'machine_factory',
                                             'model', 'machine_sn', 'factory_date', 'end_ma_date', 'work_are',
                                             'machine_admin', 'app_admin', 'mg_ip', 'app_ip1', 'bmc_ip',
                                             'comments').where(
                MachineInfos.machine_roomid == self.room.currentIndex())
            print('查询机房SQL', data_model)
        if cabinet != '所有':  # 所有机柜，采用项名 进行查询
            data_model = MachineInfos().select('machine_id', 'machine_roomid', 'cabinet_name', 'start_position',
                                               'end_position', 'machine_name', 'machine_sort_name', 'machine_factory',
                                               'model', 'machine_sn', 'factory_date', 'end_ma_date', 'work_are',
                                               'machine_admin', 'app_admin', 'mg_ip', 'app_ip1', 'bmc_ip',
                                               'comments').where(
                MachineInfos.cabinet_name == self.cabinet.currentText())
            print('查询机柜SQL', data_model)
        else:
            data_model = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid,
                                             MachineInfos.cabinet_name, MachineInfos.start_position,
                                             MachineInfos.end_position, MachineInfos.machine_name,
                                             MachineInfos.machine_sort_name, MachineInfos.machine_factory,
                                             MachineInfos.model, MachineInfos.machine_sn, MachineInfos.factory_date,
                                             MachineInfos.end_ma_date, MachineInfos.work_are,
                                             MachineInfos.machine_admin, MachineInfos.app_admin, MachineInfos.mg_ip,
                                             MachineInfos.app_ip1, MachineInfos.bmc_ip, MachineInfos.comments)
            print('查询所有SQL', data_model)
            data = [(i.machine_id, i.machine_roomid,
                                               i.cabinet_name, i.start_position,
                                               i.end_position, i.machine_name,
                                               i.machine_sort_name, i.machine_factory,
                                               i.model, i.machine_sn, i.factory_date,
                                               i.end_ma_date, i.work_are,
                                               i.machine_admin, i.app_admin, i.mg_ip,
                                               i.app_ip1, i.bmc_ip, i.comments) for i in data_model]
            print(data)
            # for i in data_model:
            #     print(i.machine_id, i.machine_roomid,
            #           i.cabinet_name, i.start_position,
            #           i.end_position, i.machine_name,
            #           i.machine_sort_name, i.machine_factory,
            #           i.model, i.machine_sn, i.factory_date,
            #           i.end_ma_date, i.work_are,
            #           i.machine_admin, i.app_admin, i.mg_ip,
            #           i.app_ip1, i.bmc_ip, i.comments)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiModifyMachine()
    add_win.show()
    sys.exit(app.exec())
