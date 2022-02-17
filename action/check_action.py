import os
import sys
import openpyxl
from PySide6 import QtWidgets, QtGui, QtCore
from PySide6.QtWidgets import QTreeWidgetItemIterator
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
        self.treeWidget.itemChanged.connect(self.select_item)       # 树形控件变动时触发复选框事件

    # 复选框事件
    def select_item(self,item):
        topitem = self.treeWidget.indexOfTopLevelItem(item)     # 获取顶级项索引
        if item.checkState(0) == Qt.Checked:  # checkState(0)表示第0列选择状态
            print('被选择', item.text(0))
            if topitem >= 0:        # 返回索引大于等于0，不为顶级项时，为-1
                item_count = item.childCount()  # 获取项级项下子项个数
                print('顶级项名：', topitem)
                print('子项个数：', item_count)

                # 显示出所有子项
                item_list = []      # 用于接收子项
                for i in range(item_count):
                    item_list.append([item.child(i).text(1),item.child(i).text(2)])     # 将子项的第二项和第三列以列表添加到子项列表中
                    item.child(i).setCheckState(0,Qt.Checked)
                print(item_list)
            else:
                print('不是父项！父项为：',item.parent().text(0))      # 查询父节点项名称
                print('子项索引',item)
        # if item.checkState(col) == Qt.Unchecked:
        #     print('取消被选择', item.text(0))
        #
        #     if topitem >= 0 :
        #         print('顶级项名：', topitem)
        #         item_count=item.childCount()
        #         print('子项个数：', item_count)
        #         # 显示出所有子项
        #         item_list = []      # 用于接收子项
        #         for i in range(item_count):
        #             item_list.append([item.child(i).text(1),item.child(i).text(2)])     # 将子项的第二项和第三列以列表添加到子项列表中
        #             item.child(i).setCheckState(0,Qt.Unchecked)






class UiCheck(Ui_check_form,QtWidgets.QFrame):
    '''
    设备巡检窗口类
    '''
    def __init__(self,parent=None):
        super(UiCheck, self).__init__(parent)
        self.setupUi(self)
        self.addhost_btn.clicked.connect(self.select_hosts)     # 查询所有设备


    def select_hosts(self):

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
                Child_Item.setText(1, child_item[0])        # 显示第二列
                Child_Item.setText(2, child_item[1])        # 显示第三列
                Child_Item.setCheckState(0,Qt.Unchecked)       # 添加复选框

        host_win.exec()




if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiCheck()
    import_win.show()
    sys.exit(app.exec())
