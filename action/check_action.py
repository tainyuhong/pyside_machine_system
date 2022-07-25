import sys
import paramiko
import time
from PySide6 import QtWidgets, QtCore
from ui.check import *
from ui.addhost_win import *
from db.db_handler import *
from action.connect  import SshToHost

# SQL查询语句
hosts_sql = ''' select m.machine_name,m.mg_ip from machine_list m where m.mg_ip is not Null and m.machine_sort_name= %s;'''
sort_sql = '''select s.sort_name from machine_sort s  where s.part_sort_id is not Null ;'''


# 添加主机窗口类
class AddHosts(QDialog, Ui_addhost_win):
    '''
    添加主机窗口 子窗口
    '''
    host_message = QtCore.Signal(list)  # 定义信号

    def __init__(self, parent=None):
        super(AddHosts, self).__init__(parent)
        self.setupUi(self)
        self.treeWidget.itemChanged.connect(self.select_item)  # 树形控件变动时触发复选框事件
        self.add_btn.clicked.connect(self.get_checked_item)  # 点击添加按钮

    # 复选框选择事件：选择或取消，全选或全取消
    def select_item(self, item):
        topitem = self.treeWidget.indexOfTopLevelItem(item)  # 获取顶级项索引
        # 选择项
        if item.checkState(0) == Qt.Checked:  # checkState(0)表示第0列选择状态
            if topitem >= 0:  # 返回索引大于等于0为顶级项，值为-1时，当前选择项是子项
                item_count = item.childCount()  # 获取项级项下子项个数
                # print('选择顶级项名索引：', topitem, '项名：', item.text(0))      # 显示顶级项索引及项名
                # print('选择子项个数：', item_count)
                # 显示出所有子项
                item_list = []  # 用于接收子项
                for i in range(item_count):
                    item_list.append([item.child(i).text(1), item.child(i).text(2)])  # 将子项的第二项和第三列以列表添加到子项列表中
                    item.child(i).setCheckState(0, Qt.Checked)
                # print(item_list)
            # else:
            #     print('不是父项！父项为：',item.parent().text(0))      # 查询父节点项名称
            #     print('选择子项：',item.text(1),item.text(2))

        # 取消选择
        if item.checkState(0) == Qt.Unchecked:
            if topitem >= 0:  # 返回索引大于等于0为顶级项，值为-1时，当前选择项是子项
                item_count = item.childCount()  # 获取项级项下子项个数
                # print('取消顶级项名索引：', topitem,'项名：', item.text(0))
                # print('取消子项个数：', item_count)
                # 显示出所有子项
                item_list = []  # 用于接收子项
                for i in range(item_count):
                    item_list.append([item.child(i).text(1), item.child(i).text(2)])  # 将子项的第二项和第三列以列表添加到子项列表中
                    item.child(i).setCheckState(0, Qt.Unchecked)
                # print(item_list)
            # else:
            #     print('取消不是父项！父项为：',item.parent().text(0))      # 查询父节点项名称
            #     print('取消选择子项：',item.text(1),item.text(2))

    # 获取复选框为True的项
    def get_checked_item(self):
        top_item_count = self.treeWidget.topLevelItemCount()
        select_item = []  # 已钩选列表
        for top_index in range(top_item_count):
            top_item = self.treeWidget.topLevelItem(top_index)  # 获取项级项下子项个数
            # print('顶级项：',top_item.text(0),'子项数：',top_item.childCount())
            for i in range(top_item.childCount()):
                if top_item.child(i).checkState(0) == Qt.Checked:
                    select_item.append(
                        '{}:{}'.format(top_item.child(i).text(1), top_item.child(i).text(2)))  # 将子项的第二项和第三列以列表添加到子项列表中
                    top_item.child(i).setCheckState(0, Qt.Unchecked)
                # else:
                #     pass
        # print(select_item)
        self.host_message.emit(select_item)
        self.close()


# 主机巡检窗口类
class UiCheck(Ui_check_form, QtWidgets.QDialog, QObject):
    '''
    设备巡检窗口类
    '''
    host_signal = QtCore.Signal(list)  # 定义主机信息信号

    def __init__(self, parent=None):
        super(UiCheck, self).__init__(parent)
        self.hosts_list = []  # 初始化主机列表为空列表
        self.setupUi(self)
        self.ssh = SshToHost()
        self.db = DBMysql()
        self.check_thread = None
        self.ping_radio.setChecked(True)  # 设置ping按钮默认为选择
        self.addhost_btn.clicked.connect(self.select_hosts)  # 查询所有设备
        # 判断是执行ping还是巡检命令
        self.exec_btn.clicked.connect(self.chose_action)  # 执行ping

    def select_hosts(self):

        host_win = AddHosts()
        sort_infos = self.db.query_single(sort_sql)  # 分类信息

        # 遍历分类，显示设备信息
        for sort in sort_infos:
            hosts_infos = self.db.query_single(hosts_sql, sort)  # 从数据库读取主机信息
            RootItem = QTreeWidgetItem()  # 定义根项
            RootItem.setText(0, sort[0])  # 设置根项内容
            RootItem.setCheckState(0, Qt.Unchecked)  # 添加复选框
            host_win.treeWidget.addTopLevelItem(RootItem)  # 设置为顶层项
            # 遍历主机信息显示并添加到列表中
            for child_item in hosts_infos:
                Child_Item = QTreeWidgetItem(RootItem)
                Child_Item.setText(1, child_item[0])  # 显示第二列
                Child_Item.setText(2, child_item[1])  # 显示第三列
                Child_Item.setCheckState(0, Qt.Unchecked)  # 添加复选框
        host_win.host_message.connect(self.display_to_text)
        host_win.exec()

    # 将获取的主机列表显示至主机添加窗口中，hosts为列表格式
    def display_to_text(self, hosts):
        # print('子窗口返回数据：', hosts)
        self.hosts_list = hosts
        self.host_listw.addItems(self.hosts_list)

    def chose_action(self):
        if self.ping_radio.isChecked():
            # 执行ping检查
            # print('ping状态', self.ping_radio.isChecked())
            if len(self.hosts_list) >0:
                self.do_ping()  # 执行ping
            else:
                QtWidgets.QMessageBox.warning(self,'选择主机','请先添加要巡检的主机！')
        else:
            hosts_ip = []  # 用于接收存活主机列表
            if len(self.hosts_list) > 0:

                for i in self.hosts_list:
                    hosts_ip.append(i.split(':'))
                # print('新的主机IP表', hosts_ip)

                # print('巡检中选择IP',self.hosts_list)    # ['k8s-node1:192.168.1.61', 'K8S-node2:192.168.1.62', 'K8S-NODE3:192.168.1.63']
                ip_list = []
                for _ in hosts_ip:
                    ip_list.append(_[1])
                # print('ip集合',tuple(ip_list))
                check_cmd_sql = ''' select * from view_check_cmd c where c.cmd_id='1' and c.ip in {}  '''.format(tuple(ip_list))  # 查询指定设备SQL
                self.check_hosts = self.db.query_single(check_cmd_sql)
                # print(self.check_hosts= ((1, 'k8s-master', '192.168.1.70', 'root', '123456', 1, 'date\r\nhostname\r\nuname', '日期', 5741),
                # (2, 'k8s-node1', '192.168.1.61', 'root', '123456', 2, 'hostname', '主机名', 5742))
                self.exec_btn.setDisabled(True)
                self.check_thread = QtCore.QThread()
                self.check = Actin_Thread()     # 实例化子线程巡检
                self.host_signal.connect(self.check.accpet_hostsinfo(self.check_hosts))     # 主机信号连接至任务处理的子线程获取主机信息槽函数
                self.check.update_signal.connect(self.update_text)      # 任务处理子线程显示巡检结果信号连接至主线程更新槽函数self.update_text)
                self.check_thread.started.connect(self.check.do_check)  # 将多线程连接到执行巡检任务的槽函数
                self.check.end_signal.connect(self.stop)  # 任务子线程执行巡检结果完毕信号连接至主线程关闭子线程槽函数self.stop
                self.check.moveToThread(self.check_thread)      # # 将子线程移至子线程中处理
                self.check_thread.start()       # 启动子线程
            else:
                QtWidgets.QMessageBox.warning(self,'选择主机','请先添加要巡检的主机！')


    def do_ping(self):
        """
        主机主机存活状态检查函数
        :type info: tuple
        :param info: 主机列表信息  ，传入格式：（('hostname','ip','user','passwd')，('hostname','ip','user','passwd')。。。）
        :return:
        """
        print('正在检测主机连通性状态，请稍候. \n\n')
        # print(self.hosts_list)
        up = []  # 初始定义存活主机
        down = []  # 初始定义非存活主机
        hosts_ip = []  # 用于接收存活主机列表
        for i in self.hosts_list:
            hosts_ip.append(i.split(':'))
        # print('新的主机IP表', hosts_ip)
        for host in hosts_ip:
            cursor = self.dispaly_te.textCursor()
            self.dispaly_te.moveCursor(cursor.End)  # 将光标移动到最后
            self.dispaly_te.append(self.ssh.is_alive(host, up, down))  # 将返回的结果显示至文本框 SshToHost.is_alive ping函数
            QtWidgets.QApplication.processEvents()  # 实时刷新页面，防止页面无响应

    # 更新文本框显示内容
    def update_text(self, text):
        # self.dispaly_te.setTextColor(QColor('#0000FF'))
        cursor = self.dispaly_te.textCursor()
        self.dispaly_te.moveCursor(cursor.End)  # 将光标移动到最后
        self.dispaly_te.insertPlainText(text)  # 插入文本


    # 关闭线程
    def stop(self):
        self.check_thread.quit()  # 退出子线程
        # self.check_thread.wait()
        self.exec_btn.setEnabled(True)      # 在任务执行完在激活执行按钮


# 巡检任务类
class Actin_Thread(QObject):
    update_signal = QtCore.Signal(str)  # 发送执行命令结果给主进程用于返回显示至界面
    end_signal = QtCore.Signal(str)  # 处理完任务发送信息

    def __init__(self):
        super(Actin_Thread, self).__init__()
        self.ssh = SshToHost()
        self.check_hosts = None

    # 执行巡检任务
    def do_check(self):
        # print('执行任务中的Ip:', self.check_hosts)
        for i in self.check_hosts:
            try:
                self.trans = paramiko.Transport((i[2], 22))  # 使用Transport方式连接
                self.trans.start_client(timeout=0.5)
                # paramiko.util.log_to_file('paramiko-log.log')  # 记录执行日志
                # 用户名密码方式
                self.trans.auth_timeout = 3
                self.trans.auth_password(username=i[3], password=i[4], fallback=True)
            # except paramiko.ssh_exception.AuthenticationException as pass_err:
            #     # logging.error('{}:{} {}'.format(hostname, ip, pass_err))
            #     print('{}:{} 用户名或密码错误，跳过巡检'.format(hostname, ip))
            #     # continue
            except Exception as e:
                print('连接错误：', e)
                self.update_signal.emit(str(e))  # 发送错误至主窗口结果
            else:
                print('连接主机:{}:{}   ---> 正常'.format('host-70', i[2]))
                # 打开一个通道
                self.channel = self.trans.open_session()
                self.channel.settimeout(10)
                # 获取一个终端
                self.channel.get_pty()
                # 激活器
                self.channel.invoke_shell()
                # 根据配置文件定义command项执行脚本
                # 获取脚本命令内容
                # print('cmd_sql', cmd_sql)
                # print('args', args)
                # cmd_file = db.query_single(cmd_sql, args)  # 查看有几个可执行的脚本配置文件
                cmd_file = i[6]
                # print('cmd_file', cmd_file)  # 'date\r\nhostname\r\nuname'
                self.update_signal.emit('\n\n当前巡检主机：{} ....\n\n'.format(i[2]))  # 在发送日志前先显示巡检主机
                if len(cmd_file) > 0:
                    # print('cmd_file',cmd_file)
                    single_cmd = cmd_file.split('\r\n')  # 提取配置文件中脚本命令
                    # print('single_cmd',single_cmd)
                    # print('00000', QtCore.QThread.currentThread())
                    for c in single_cmd:  # 遍历每个命令
                        # print('命令c：', c,type(c))
                        # 发送要执行的命令
                        time.sleep(1)
                        # logging.info('执行命令：【{}】'.format(c))  # 记录需要执行的命令到日志
                        self.channel.send(c + '\n')  # 在每一个命令后加上换行
                        # self.channel.send(c)  # 在每一个命令后加上换行
                        end_symbol = ('# ', '$ ', '$', '> ', '>')  # 设置我们定义的结束符
                        # 将命令执行结果保存到display_result
                        display_result = ''
                        # # 回显很长的命令可能执行较久，通过循环分批次取回回显
                        time.sleep(0.1)
                        while True:
                            result = self.channel.recv(256)
                            try:
                                result = result.decode('utf-8')
                                # logging.warning('使用UTF-8编码！')
                            except:
                                result = result.decode('gb18030')
                                # logging.warning('使用gb18030编码！')
                            display_result += result  # 输出到日志显示窗口
                            if result.endswith(end_symbol):
                                break

                        self.update_signal.emit(display_result)  # 发送命令返回至主窗口结果
                    print()
                    # print('\n111111', QtCore.QThread.currentThread())
                    print('=' * 80)
                else:
                    print('没有配置相关命令！，请配置检查脚本命令后再操作！！')
                    return
            finally:
                self.channel.close()
                self.trans.close()
                # print('\n2222')
        self.end_signal.emit('断开SSH连接')  # 发送巡检命令执行完信号

    # 接收主界面线程发送的主机IP信息
    def accpet_hostsinfo(self, host_info):
        # print('子进程接收到信息：', host_info)
        self.check_hosts = host_info


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiCheck()
    import_win.show()
    sys.exit(app.exec())
