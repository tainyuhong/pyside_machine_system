import sys
from ui.base_info import *
from PySide6 import QtWidgets, QtGui, QtCore
from db.db_orm import *


class UiBaseInfo(Ui_BaseInfo,QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(UiBaseInfo, self).__init__(parent)
        self.setupUi(self)
        self.display_room()             # 机房信息窗口
        self.display_cabinet()          # 机柜信息窗口
        self.display_U()                # U位信息窗口
        self.display_manfacturer()      # 品牌信息窗口
        self.display_sort()             # 分类信息窗口

    # 显示机房
    def display_room(self):
        # 定义查询机房数据
        room_model = MachineRoom.select(MachineRoom.room_id,MachineRoom.room_name,MachineRoom.room_alias).execute()
        # 输出查询内容
        data = [(i.room_id,i.room_name,i.room_alias) for i in room_model]
        # print('查询数据：',data)
        # 显示机房内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_room.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 显示机柜
    def display_cabinet(self):
        # 定义查询机柜数据
        cabinet_model = Cabinet.select(Cabinet.cab_id,Cabinet.room,Cabinet.cab_num,Cabinet.cab_name,Cabinet.count_position,Cabinet.is_use).execute()
        # 输出查询内容
        data = [(i.cab_id,i.room,i.cab_num,i.cab_name,i.count_position,i.is_use) for i in cabinet_model]
        # print('查询数据：',data)
        # 显示机柜内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_cabinet.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 显示U位信息
    def display_U(self):
        # 定义查询U位数据
        u_model = CabPosition.select(CabPosition.id,CabPosition.num,CabPosition.position_name).execute()
        # 输出查询内容
        data = [(i.id,i.num,i.position_name) for i in u_model]
        # print('查询数据：',data)
        # 显示U位内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_u.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 显示品牌信息
    def display_manfacturer(self):
        # 定义查询U位数据
        manfacturer_model = Manufacturer.select(Manufacturer.id,Manufacturer.manufacturer_name).execute()
        # 输出查询内容
        data = [(i.id,i.manufacturer_name) for i in manfacturer_model]
        # print('查询数据：',data)
        # 显示U位内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_manfacturer.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 显示设备分类
    def display_sort(self):
        sort_infos = MachineSort.select(MachineSort.sort_id,MachineSort.sort_name).where(MachineSort.part_sort==None)  # 分类信息
        data = [(i.sort_id, i.sort_name) for i in sort_infos]
        print(data)
        # 遍历分类，显示设备信息
        # for sort in sort_infos:
        #     hosts_infos = self.db.query_single(hosts_sql, sort)  # 从数据库读取主机信息
        #     RootItem = QTreeWidgetItem()  # 定义根项
        #     RootItem.setText(0, sort[0])  # 设置根项内容
        #     RootItem.setCheckState(0, Qt.Unchecked)  # 添加复选框
        #     host_win.treeWidget.addTopLevelItem(RootItem)  # 设置为顶层项
        #     # 遍历主机信息显示并添加到列表中
        #     for child_item in hosts_infos:
        #         Child_Item = QTreeWidgetItem(RootItem)
        #         Child_Item.setText(1, child_item[0])  # 显示第二列
        #         Child_Item.setText(2, child_item[1])  # 显示第三列
        #         Child_Item.setCheckState(0, Qt.Unchecked)  # 添加复选框

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    base_win = UiBaseInfo()
    base_win.show()
    sys.exit(app.exec())