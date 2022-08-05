import sys
from PySide6 import QtWidgets,QtGui,QtCore
import pandas as pd
from db.db_orm import *

class win(QtWidgets.QWidget):
    def __init__(self,parent=None):
        super(win, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(200, 100, 800, 550)
        self.setWindowTitle('pandas与orm结合实例')
        layout = QtWidgets.QVBoxLayout()
        table = QtWidgets.QTableWidget()
        layout.addWidget(table)
        table.setRowCount(42)
        # data_model = MachineInfos.select(MachineInfos.machine_roomid,MachineInfos.machine_name,MachineInfos.mg_ip).execute()
        # data = [(i.machine_roomid.room_id,i.machine_name,i.mg_ip) for i in data_model]
        # print('数据库中数据：',data)
        # df = pd.DataFrame(data,columns=('machine_roomid','machine_name','mg_ip'))
        # print('pandas数据：',df)
        # cab_data_model = Cabinet.select(Cabinet.cab_num).execute()
        # cab_data = [i.cab_num for i in cab_data_model]
        u_data_model = CabPosition.select(CabPosition.num).execute()
        u_data = [i.num for i in u_data_model]
        table.setColumnCount(11)
        table.setHorizontalHeaderLabels(['KF01', 'KF02', 'KF03', 'KF04', 'KF05', 'KF06', 'KF07', 'KF08', 'KF09', 'KF10', 'KF11'])

        # print('机柜数据：',cab_data)
        print('U数据：',u_data)
        cab_data_model = Cabinet.select(Cabinet.cab_num).where(Cabinet.room == 4).execute()
        count = 0
        for num,c in enumerate(cab_data_model):
            print('机柜名：',c.cab_num)
            count += 1
            u_data = [i.num for i in u_data_model]
            print(u_data)
            for index, u in enumerate(u_data):
                table.setItem(index,num,QtWidgets.QTableWidgetItem(str(u)))
        # table.setHorizontalHeaderLabels(labs)
        table.setColumnCount(count)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = win()
    add_win.show()
    sys.exit(app.exec())