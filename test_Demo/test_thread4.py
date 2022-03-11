# 测试多线程moveToThread 动态传递参数
import sys
import time
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import paramiko

# 任务处理类
class MyObject(QObject):
    update_signal = Signal(str)     # 发送执行命令结果给主进程用于返回显示至界面
    end_signal = Signal(str)        # 处理完任务发送信息

    def __init__(self,parent=None):
        super(MyObject, self).__init__(parent)
        self.ip = None

    # 执行巡检
    def ssh_to_host(self):
        print('执行任务中的Ip:',self.ip)
        for i in self.ip:
            try:
                # self.trans = paramiko.Transport(('192.168.1.70', 22))  # 使用Transport方式连接
                self.trans = paramiko.Transport((i, 22))  # 使用Transport方式连接
                self.trans.start_client(timeout=0.5)
                # paramiko.util.log_to_file('paramiko-log.log')  # 记录执行日志
                # 用户名密码方式
                self.trans.auth_timeout = 3
                self.trans.auth_password(username='root', password='123456', fallback=True)
            # except paramiko.ssh_exception.AuthenticationException as pass_err:
            #     # logging.error('{}:{} {}'.format(hostname, ip, pass_err))
            #     print('{}:{} 用户名或密码错误，跳过巡检'.format(hostname, ip))
            #     # continue
            except Exception as e:
                print('连接错误：', e)
                self.update_signal.emit(str(e))  # 发送错误至主窗口结果
            else:
                print('连接主机:{}:{}   ---> 正常'.format('host-70', i))
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
                cmd_file = (('date\r\nhostname\r\nuname\r\nifconfig',),)
                # print('cmd_file', cmd_file)
                if len(cmd_file) > 0:
                    # print('cmd_file',cmd_file)
                    single_cmd = cmd_file[0][0].split('\r\n')  # 提取配置文件中脚本命令
                    # print('single_cmd',single_cmd)
                    print('00000', QThread.currentThread())
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
                        self.update_signal.emit(display_result)   # 发送命令返回至主窗口结果
                    print()
                    print('\n111111', QThread.currentThread())
                    print('=' * 80)
                else:
                    print('没有配置相关命令！，请配置检查脚本命令后再操作！！')
                    return
            finally:
                self.channel.close()
                self.trans.close()
                print('\n2222')
        self.end_signal.emit('断开SSH连接')  # 发送巡检命令执行完信号

    # 接收主界面线程发送的主机IP信息
    def accpet_hostsinfo(self,ip):
        print('子进程接收到信息：',ip)
        self.ip = ip



class MainForm(QWidget):
    host_signal = Signal(list)      # 定义主机信息信号

    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setWindowTitle('多线程测试-定时发送消息')
        self.resize(800, 600)
        layout = QVBoxLayout()
        self.start_btu = QPushButton('开始')
        layout.addWidget(self.start_btu)
        self.text = QTextEdit(self)
        layout.addWidget(self.text)
        self.setLayout(layout)

        self.ip = None

        self.my_thread = QThread()      # 实例化一个子线程
        self.start_btu.clicked.connect(self.send_hosts_to_child)   # 将开始按钮的点击信号连接至发送主机信息给子线程的槽函数self.send_hosts_to_child
        self.start_btu.clicked.connect(self.do_worker)      # 将开始按钮的点击事件信号连接至执行任务的槽函数

    # 执行巡检任务命令发送
    def do_worker(self):
        print('开始运行程序。。')
        print('当前线程：', QThread.currentThread(), self.my_thread.isRunning())
        self.text.clear()
        self.obj = MyObject()   # 实例化子线程巡检
        self.host_signal.connect(self.obj.accpet_hostsinfo(self.ip))        # 主机信号连接至任务处理的子线程获取主机信息槽函数
        self.obj.update_signal.connect(self.update_text)    # 任务处理子线程显示巡检结果信号连接至主线程更新槽函数self.update_text)
        self.obj.end_signal.connect(self.stop)      # 任务子线程执行巡检结果完毕信号连接至主线程关闭子线程槽函数self.stop
        self.obj.moveToThread(self.my_thread)   # 将子线程移至子线程中处理
        self.my_thread.started.connect(self.obj.ssh_to_host)
        print('启动新线程')
        self.my_thread.start()      # 启动子线程
        print('新线程self.mythread：', self.my_thread.currentThread(), self.my_thread.isRunning())

    # 传递主机IP信息给任务处理子线程
    def send_hosts_to_child(self):
        # ip_info = ['192.168.1.70','192.168.1.61']
        self.ip = ['192.168.1.70','192.168.1.61']   #
        # for i in ip_info:
        #     self.ip = i
        self.host_signal.emit(self.ip)      # 发送主机信息self.ip
        # self.send_signal.emit(['Ip已发送'])


    # 更新文本框显示内容
    def update_text(self,text):
        cursor = self.text.textCursor()
        self.text.moveCursor(cursor.End)  # 将光标移动到最后
        self.text.insertPlainText(text)     # 插入文本

    # 关闭线程
    def stop(self):
        print('关闭当前线程')
        self.my_thread.quit()       # 退出子线程
        self.my_thread.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())
