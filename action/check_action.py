import os
import sys
import openpyxl
from PySide6 import QtWidgets, QtGui, QtCore
# from PySide6.QtWidgets import QTreeWidgetItemIterator
from ui.check import *
from ui.addhost_win import *
from db.db_handler import *
from connect import SshToHost


# SQL查询语句
hosts_sql = ''' select m.machine_name,m.mg_ip from machine_list m where m.mg_ip is not Null and m.machine_sort_name= %s;'''
sort_sql = '''select s.sort_name from machine_sort s  where s.part_sort_id is not Null ;'''

class AddHosts(QDialog,Ui_addhost_win):
    '''
    添加主机窗口 子窗口
    '''
    host_message = QtCore.Signal(list)       # 定义信号
    def __init__(self,parent=None):
        super(AddHosts, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.itemChanged.connect(self.select_item)       # 树形控件变动时触发复选框事件
        self.add_btn.clicked.connect(self.get_checked_item)            # 点击添加按钮

    # 复选框选择事件：选择或取消，全选或全取消
    def select_item(self,item):
        topitem = self.treeWidget.indexOfTopLevelItem(item)     # 获取顶级项索引
        # 选择项
        if item.checkState(0) == Qt.Checked:  # checkState(0)表示第0列选择状态
            if topitem >= 0:        # 返回索引大于等于0为顶级项，值为-1时，当前选择项是子项
                item_count = item.childCount()  # 获取项级项下子项个数
                # print('选择顶级项名索引：', topitem, '项名：', item.text(0))      # 显示顶级项索引及项名
                # print('选择子项个数：', item_count)
                # 显示出所有子项
                item_list = []      # 用于接收子项
                for i in range(item_count):
                    item_list.append([item.child(i).text(1),item.child(i).text(2)])     # 将子项的第二项和第三列以列表添加到子项列表中
                    item.child(i).setCheckState(0,Qt.Checked)
                # print(item_list)
            # else:
            #     print('不是父项！父项为：',item.parent().text(0))      # 查询父节点项名称
            #     print('选择子项：',item.text(1),item.text(2))

        # 取消选择
        if item.checkState(0) == Qt.Unchecked:
            if topitem >= 0:        # 返回索引大于等于0为顶级项，值为-1时，当前选择项是子项
                item_count = item.childCount()  # 获取项级项下子项个数
                # print('取消顶级项名索引：', topitem,'项名：', item.text(0))
                # print('取消子项个数：', item_count)
                # 显示出所有子项
                item_list = []      # 用于接收子项
                for i in range(item_count):
                    item_list.append([item.child(i).text(1),item.child(i).text(2)])     # 将子项的第二项和第三列以列表添加到子项列表中
                    item.child(i).setCheckState(0,Qt.Unchecked)
                # print(item_list)
            # else:
            #     print('取消不是父项！父项为：',item.parent().text(0))      # 查询父节点项名称
            #     print('取消选择子项：',item.text(1),item.text(2))

    # 获取复选框为True的项
    def get_checked_item(self):
        top_item_count = self.treeWidget.topLevelItemCount()
        select_item = []        # 已钩选列表
        for top_index in range(top_item_count):
            top_item = self.treeWidget.topLevelItem(top_index)  # 获取项级项下子项个数
            # print('顶级项：',top_item.text(0),'子项数：',top_item.childCount())
            for i in range(top_item.childCount()):
                if top_item.child(i).checkState(0) == Qt.Checked:
                    select_item.append('{}:{}'.format(top_item.child(i).text(1), top_item.child(i).text(2)))  # 将子项的第二项和第三列以列表添加到子项列表中
                    top_item.child(i).setCheckState(0, Qt.Unchecked)
                # else:
                #     pass
        print(select_item)
        self.host_message.emit(select_item)
        self.close()


# 多线程
class WorkThread(QtCore.QThread):
    trigger = QtCore.Signal()
    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        self.ssh.exec_cmd( )  # (i[2],1) 1:为命令类型
        self.trigger.emit()


class UiCheck(Ui_check_form,QtWidgets.QFrame):
    '''
    设备巡检窗口类
    '''
    def __init__(self,parent=None):
        super(UiCheck, self).__init__(parent)
        self.hosts_list = []    # 初始化主机列表为空列表
        self.setupUi(self)
        self.ssh = SshToHost()
        self.ping_radio.setChecked(True)        # 设置ping按钮默认为选择
        self.addhost_btn.clicked.connect(self.select_hosts)     # 查询所有设备
        # 判断是执行ping还是巡检命令
        self.exec_btn.clicked.connect(self.chose_action)         # 执行ping

        # # 设定任务栏时间
        # self.timer = QtCore.QTimer()
        # time = QDateTime().currentDateTime()    # 时间对象
        # timedisplay = time.toString('yyyy-MM-dd hh:mm:ss')
        # self.status_le.setText(timedisplay)
        # self.timer.start(0.1)


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
        host_win.host_message.connect(self.display_to_text)
        host_win.exec()

    # 将获取的主机列表显示至主机添加窗口中，hosts为列表格式
    def display_to_text(self,hosts):
        print('子窗口返回数据：',hosts)
        self.hosts_list = hosts
        self.host_listw.addItems(self.hosts_list)

    def chose_action(self):
        if self.ping_radio.isChecked():
            print('ping状态',self.ping_radio.isChecked())
            self.do_ping()       # 执行ping
        else:
            print('stat状态', self.stat_radio.isChecked())
            self.do_check()       # 执行巡检

    def do_ping(self):
        """
                    主机主机存活状态检查函数
                    :type info: tuple
                    :param info: 主机列表信息  ，传入格式：（('hostname','ip','user','passwd')，('hostname','ip','user','passwd')。。。）
                    :return:
                    """
        print('正在检测主机连通性状态，请稍候. \n\n')
        print(self.hosts_list)
        up = []     # 初始定义存活主机
        down = []       # 初始定义非存活主机
        hosts_ip = []   # 用于接收存活主机列表
        for i in self.hosts_list:
            hosts_ip.append(i.split(':'))
        print('新的主机IP表',hosts_ip)
        for host in hosts_ip:
            cursor = self.dispaly_te.textCursor()
            self.dispaly_te.moveCursor(cursor.End)      # 将光标移动到最后
            self.dispaly_te.append(self.ssh.is_alive(host,up,down))     # 将返回的结果显示至文本框 SshToHost.is_alive ping函数
            QtWidgets.QApplication.processEvents()      # 实时刷新页面，防止页面无响应

    # 执行巡检任务
    def do_check(self):
        check_sql = ''' select * from view_check_cmd c '''
        check_cmd_sql = ''' select c.cmd from view_check_cmd c where c.ip=%s and c.cmd_id=%s  '''
        db = DBMysql()
        check_hosts = db.query_single(check_sql)
        print(check_hosts)
        for i in check_hosts:
            print('巡检中主机：',i)
            self.ssh.exec_cmd(i[1:5],check_cmd_sql,(i[2],1))       # (i[2],1) 1:为命令类型



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiCheck()
    import_win.show()
    sys.exit(app.exec())
