import sys
from ui.warranty_config import Ui_WarrantyConfig, QTableWidgetItem
from PySide6 import QtWidgets, QtCore
from db.db_orm import Organization, MachineSort, MachineList
from action.pub_infos import PubSwitch


class WarrantyCconfig(QtWidgets.QWidget, Ui_WarrantyConfig):
    def __init__(self, parent=None):
        super(WarrantyCconfig, self).__init__(parent)
        self.setupUi(self)
        self.pub_infos = PubSwitch()

        self.sql = {}  # 用于保存获取的查询条件拼接字段 字典
        self.display_room()  # 显示机房下拉菜单内容
        self.display_sort()  # 显示分类信息
        self.cb_room.currentIndexChanged.connect(self.display_cabinet)  # 定义机房下拉菜单触发事件

        # 查询按钮事件
        self.bt_select.clicked.connect(self.display)

        # 提交按钮事件
        self.bt_commit.clicked.connect(self.commit)

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

    # 获取设备分类信息
    def display_sort(self):
        sort_model = MachineSort.select(MachineSort.sort_name).where(MachineSort.part_sort_name.is_null(False)).tuples()
        sort_data = [sort[0] for sort in sort_model]
        # print('分类信息：',sort_data)
        self.cb_sort.clear()
        self.cb_sort.addItem('所有')
        self.cb_sort.addItems(sort_data)

    # 显示查询结果至页面
    def display(self):
        self.tb_display.clearContents()  # 清空表格中内容
        room = self.cb_room.currentText()  # 机房
        cabinet = self.cb_cabinet.currentText()  # 机柜
        machine_name = self.machine_name.text().strip()  # 设备名称
        sn = self.le_sn.text().strip()  # SN
        mg_ip = self.mg_ip.text().strip()  # mg_ip
        sort = self.cb_sort.currentText()  # 设备分类

        # 判断查询条件
        self.get_room()
        self.get_cabinet()
        self.get_sort()
        print('sql:', self.sql)

        # 获取查询结果
        data_model = MachineList.select(MachineList.machine_id, MachineList.room_name, MachineList.cab_name,
                                        MachineList.start_position, MachineList.postion_u, MachineList.machine_name,
                                        MachineList.machine_sort_name, MachineList.machine_factory, MachineList.model,
                                        MachineList.machine_sn, MachineList.machine_admin, MachineList.mg_ip,
                                        MachineList.bmc_ip, MachineList.comments).where(
            *([key == value for key, value in self.sql.items()])).tuples()

        print('data_model:',data_model)

        data = data_model.tuples()
        # 将查询结果显示在页面上
        data_count = len(data)
        self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_status.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                # 当为第一列时添加复选框按钮
                if col == 0:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                    self.tb_display.item(row, 0).setCheckState(QtCore.Qt.Unchecked)  # 添加复选框
                else:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        self.tb_display.resizeColumnsToContents()  # 自适应列宽

    # 获取查询条件--机房
    def get_room(self):
        if self.cb_room.currentText() != '所有':
            self.sql[MachineList.room_name] = self.cb_room.currentText()
        else:
            if MachineList.room_name in self.sql:
                self.sql.pop(MachineList.room_name)

    # 获取查询条件--机柜
    def get_cabinet(self):
        if self.cb_cabinet.currentText() != '所有':
            self.sql[MachineList.cab_name] = self.cb_cabinet.currentText()
        else:
            if MachineList.cab_name in self.sql:
                self.sql.pop(MachineList.cab_name)  # 移除

    # 获取查询条件--设备分类
    def get_sort(self):
        if self.cb_sort.currentText() != '所有':
            self.sql[MachineList.machine_sort_name] = self.cb_sort.currentText()
        else:
            if MachineList.machine_sort_name in self.sql:
                self.sql.pop(MachineList.machine_sort_name)

    def commit(self):
        """
        提交维保信息配置
        :return:
        """
        data_model = Organization.select(Organization.org_id, Organization.org_name).tuples()
        data = [i for i in data_model]
        print('单位数据：', data)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    warranty_config_win = WarrantyCconfig()
    warranty_config_win.show()
    sys.exit(app.exec())
