import sys
from ui.top import Ui_top
from PySide6 import QtWidgets, QtGui, QtCore
from db.db_orm import *

"""
设备位图

"""


class DisplayTop(QtWidgets.QWidget, Ui_top):
    room_and_id = None  # 定义一个机房ID与机房名称的映射，后用于字典
    rooms = None

    def __init__(self, parent=None):
        super(DisplayTop, self).__init__(parent)
        self.setupUi(self)
        self.setWindowState(QtCore.Qt.WindowMaximized)  # 最大化打开窗口
        self.create_room_win()  # 创建机房窗口视图

    # 获取机房信息
    def get_room(self):
        room_model = MachineRoom.select(MachineRoom.room_id, MachineRoom.room_name).order_by(
            MachineRoom.room_id).execute()  # 查询有几个机房数据
        # 将机房信息取出作为公共变量
        self.room_and_id = {}  # 定义一个机房ID与机房名称的映射字典
        # 生成机房ID与机房名称的映射字典
        for i in room_model:
            self.room_and_id[i.room_id] = i.room_name
        # print('机房信息字典',self.room_and_id)
        self.rooms = [i.room_name for i in room_model]
        # print(self.rooms)

    # 生成每个机房的页面窗口视图
    def create_room_win(self):
        # cell_bg_color = QtGui.QBrush(QtGui.QColor(85, 170, 255, 255))  # 定义表格单元格画刷颜色
        cell_bg_color = QtGui.QBrush(QtGui.QColor(250, 250, 210))  # 定义表格单元格画刷颜色
        self.get_room()  # 获取机房数据
        for tab_name in self.rooms:
            tab = QtWidgets.QWidget()
            tab.setObjectName(tab_name)
            self.tabWidget.addTab(tab, tab_name)  # 添加到tab控件中
            vertlayout = QtWidgets.QVBoxLayout(tab)  # 在tab页面上创建垂直布局层
            table = QtWidgets.QTableWidget()  # 定义表格控件
            vertlayout.addWidget(table)  # 将表格添加到垂直布局中

            # 对每个机房机房数据进行处理,生成机柜模型
            room_id = self.room_to_id(name=tab_name)  # 机房名转换成ID
            cabinet = self.get_cabinet(room_id)  # 机柜数据
            # print('机柜信息', cabinet)
            u_pos = self.get_u_pos()  # U位信息
            table.setRowCount(len(u_pos))  # U数
            table.setVerticalHeaderLabels(u_pos)
            table.setColumnCount(len(cabinet))  # 每页列数
            table.setAlternatingRowColors(True)  # 每行颜色交叉显示
            table.setHorizontalHeaderLabels(cabinet)  # 将机柜名设置为每列的列名

            # 将设备放入机柜对应位置上
            room_machine_datas = self.sit_to_pos(tab_name)
            for machine in room_machine_datas:
                # print('machine_data', machine)      # 数据格式：('A01', 2, 4, '第二台上架设备', '8.8.8.8', '8.8.8.8')
                # print(machine)
                jigui = machine[0]  # 相当于表格的列
                u_pos = machine[1]  # 相当于表格的行
                # item = QtWidgets.QTableWidgetItem(str(machine[3]) + '\n\r' + str(machine[4]) + '\n\r' + str(machine[5]))  # 定义单元格内容
                item = QtWidgets.QTableWidgetItem('\n\r'.join(machine[3:]))  # 定义单元格内容
                item.setBackground(cell_bg_color)  # 设置单元格背景色
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # 水平居中对齐
                table.setItem(u_pos - 1, cabinet.index(jigui), item)  # 写入对应机柜数据
                if machine[2] > 1:
                    table.setSpan(u_pos - 1, cabinet.index(jigui), machine[2], 1)  # 对多U的设备进行单元格合并
                table.resizeRowsToContents()  # 自适应行高
                table.horizontalHeader().setDefaultSectionSize(120)  # 设置每列宽度
                table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置为表格不可编辑

    # 机房名与id互转
    def room_to_id(self, name=None, room_id=None):
        """
        将传入的机房名或机房id转换为对应的id或机房名
        :param name: 机房名称
        :param room_id: 机房ID
        :return: 机房名或机房id
        """
        # 生成字典与机房Id的映射
        room_id_dict = dict(map(reversed, self.room_and_id.items()))
        # print('名称-->机房ID',room_id_dict)    # {'ZB-1': 1, 'ZB-2': 2, 'ZB-3': 3, 'ZB-4': 4}
        # 如果传入机房名称为空，则返回id，如果传入的为id,则返回机房名称
        if name is None:
            return self.room_and_id[room_id]
        else:
            return room_id_dict[name]

    # 获取U位信息
    def get_u_pos(self):
        pos_model = CabPosition.select(CabPosition.num, CabPosition.position_name).execute()
        pos_data = [i.position_name for i in pos_model]
        return pos_data

    # 获取每个机房机柜数据
    def get_cabinet(self, room_id):
        cab_model = Cabinet.select(Cabinet.cab_num).where(
            (Cabinet.room_id == room_id) & (Cabinet.is_use == 1)).order_by(Cabinet.cab_num).execute()
        # print(cab_model)
        cab_data = [i.cab_num for i in cab_model]
        return cab_data

    # 将设备写入对应U位中
    def sit_to_pos(self, room):
        machine_model = MachineList.select(MachineList.cab_name, MachineList.start_position, MachineList.postion_u,
                                           Case(None, ((MachineList.machine_name.is_null(True), ''), (
                                           MachineList.machine_name.is_null(False), MachineList.machine_name))),
                                           Case(None, (
                                               (MachineList.mg_ip.is_null(True), ''),
                                               (MachineList.mg_ip.is_null(False), MachineList.mg_ip)), ),
                                           Case(None, ((MachineList.bmc_ip.is_null(True), ''),
                                                       (MachineList.bmc_ip.is_null(False), MachineList.bmc_ip)))).where(
            MachineList.room_name == room).tuples()
        # print(machine_model)
        # machine_data = [(i.cab_name, i.start_position, i.postion_u, i.machine_name, i.mg_ip, i.bmc_ip) for i in machine_model]
        machine_data = [i for i in machine_model]
        # print(machine_data)
        return machine_data


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    top_win = DisplayTop()
    top_win.show()
    sys.exit(app.exec())
