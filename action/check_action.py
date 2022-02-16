import os
import sys
import openpyxl
from PySide6 import QtWidgets, QtGui, QtCore
from ui.check import *
from ui.addhost_win import *
from db.db_handler import *


# SQL查询语句
hosts_sql = ''' select m.machine_name,m.mg_ip from machine_list m where m.mg_ip is not Null and m.machine_sort_name= %s;'''
sort_sql = '''select s.sort_name from machine_sort s  where s.part_sort_id is not Null ;'''

class AddHosts(QDialog,Ui_addhost_win):
    '''
    添加主机窗口类
    '''
    def __init__(self,parent=None):
        super(AddHosts, self).__init__(parent)
        self.setupUi(self)


class UiCheck(Ui_check_form,QtWidgets.QFrame):
    '''
    设备巡检窗口类
    '''
    def __init__(self,parent=None):
        super(UiCheck, self).__init__(parent)
        self.setupUi(self)

        self.addhost_btn.clicked.connect(self.select_hosts)     # 查询所有设备

    def select_hosts(self):

        def select_item():
            print()

        db = DBMysql()
        host_win = AddHosts()
        sort_infos = db.query_single(sort_sql)          # 分类信息

        # 遍历分类，显示设备信息
        for sort in sort_infos:
            hosts_infos = db.query_single(hosts_sql, sort)        # 从数据库读取主机信息
            RootItem = QTreeWidgetItem()                            # 定义根项
            RootItem.setText(0, sort[0])                            # 设置根项内容
            RootItem.setCheckState(0, Qt.Unchecked)                 # 添加复选框
            host_win.treeWidget.addTopLevelItem(RootItem)           # 设置为顶层项
            # 遍历主机信息显示并添加到列表中
            for child_item in hosts_infos:
                Child_Item = QTreeWidgetItem(RootItem)
                print('子项',child_item)
                Child_Item.setText(1, child_item[0])        # 显示第二列
                Child_Item.setText(2, child_item[1])        # 显示第三列
                Child_Item.setCheckState(0,Qt.Unchecked)       # 添加复选框
        host_win.exec()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiCheck()
    import_win.show()
    sys.exit(app.exec())
