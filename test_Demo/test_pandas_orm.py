import sys
from PySide6 import QtWidgets, QtGui, QtCore
# import pandas as pd
from db.db_orm import *


class win(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(win, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 100, 800, 550)
        self.setWindowTitle('pandas与orm结合实例')
        layout = QtWidgets.QVBoxLayout()
        table = QtWidgets.QTableWidget()
        self.setLayout(layout)
        layout.addWidget(table)
        table.setRowCount(42)
        table.setAlternatingRowColors(True)
        data_model = MachineList.select(MachineList.room_name, MachineList.cab_name, MachineList.start_position,
                                        MachineList.postion_u, MachineList.machine_name, MachineList.mg_ip).where(
            MachineList.room_name == 'ZB-1').execute()
        data = [(i.room_name, i.cab_name, i.start_position, i.postion_u, i.machine_name, i.mg_ip) for i in data_model]
        # print('数据库中数据：', data)
        # df = pd.DataFrame(data,columns=('machine_roomid','machine_name','mg_ip'))
        # print('pandas数据：',df)
        # cab_data_model = Cabinet.select(Cabinet.cab_num).execute()
        # cab_data = [i.cab_num for i in cab_data_model]

        # 获取表格的U位信息
        u_data_model = CabPosition.select(CabPosition.num).execute()
        u_data = [str(i.num) + 'U' for i in u_data_model]
        # print('机柜数据：',cab_data)
        # print('U数据：', u_data)

        table.setVerticalHeaderLabels(u_data)
        # 获取机柜数据
        cab_data_model = Cabinet.select(Cabinet.cab_num).where(Cabinet.room == 1).execute()
        cab_data = [c.cab_num for num, c in enumerate(cab_data_model)]

        table.setColumnCount(len(cab_data))  # 设置表格列数
        table.setHorizontalHeaderLabels(cab_data)  # 设置表的列名
        # print('列名：', cab_data)

        # 初始化表格
        for row, u in enumerate(u_data):
            for col, c in enumerate(cab_data):
                table.setItem(row, col, QtWidgets.QTableWidgetItem(''))

        # 将数据写入对应机柜表格数据中
        for machine_data in data:
            # print('machine_data', machine_data)
            jigui = machine_data[1]  # 相当于表格的列
            u_pos = machine_data[2]  # 相当于表格的行
            table.setItem(u_pos - 1, cab_data.index(jigui),
                          QtWidgets.QTableWidgetItem(str(machine_data[4]) +'\n\r'+ str(machine_data[5])))      # 写入对应机柜数据
            if machine_data[3] > 1:
                table.setSpan(u_pos-1, cab_data.index(jigui), machine_data[3], 1)           # 对多U的设备进行单元格合并
            table.resizeRowsToContents()  # 自适应行高




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = win()
    add_win.show()
    sys.exit(app.exec())
