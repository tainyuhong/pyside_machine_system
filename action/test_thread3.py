# 测试多线程moveToThread  静态参数
import sys
import time
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import paramiko

class MyObject(QObject):
    update_signal = Signal(str)
    end_signal = Signal(str)

    def __init__(self,parent=None):
        super(MyObject, self).__init__(parent)

    # 执行巡检
    def ssh_to_host(self):
        try:
            self.trans = paramiko.Transport(('192.168.1.70', 22))  # 使用Transport方式连接
            self.trans.start_client(timeout=0.5)
            # paramiko.util.log_to_file('paramiko-log.log')  # 记录执行日志
            # 用户名密码方式
            self.trans.auth_timeout = 5
            self.trans.auth_password(username='root', password='123456', fallback=True)
        # except paramiko.ssh_exception.AuthenticationException as pass_err:
        #     # logging.error('{}:{} {}'.format(hostname, ip, pass_err))
        #     print('{}:{} 用户名或密码错误，跳过巡检'.format(hostname, ip))
        #     # continue
        except Exception as e:
            print('连接错误：', e)
        else:
            print('连接主机:{}:{}   ---> 正常'.format('host-70', '192.168.1.70'))
            # 打开一个通道
            self.channel = self.trans.open_session()
            self.channel.settimeout(100)
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
                    self.update_signal.emit(display_result)   # 发送命令返回结果
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
            self.end_signal.emit('断开SSH连接')  # 发送命令返回结果


class MainForm(QWidget):

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

        self.my_thread = QThread()
        self.start_btu.clicked.connect(self.do_worker)

    def do_worker(self):
        print('开始运行程序。。')
        print('当前线程：', QThread.currentThread(), self.my_thread.isRunning())
        self.text.clear()
        self.obj = MyObject()
        self.obj.update_signal.connect(self.update_text)
        self.obj.end_signal.connect(self.stop)
        self.obj.moveToThread(self.my_thread)
        # self.mythread.started.connect(self.obj.worker)
        self.my_thread.started.connect(self.obj.ssh_to_host)

        print('启动新线程')
        self.my_thread.start()
        print('新线程self.mythread：', self.my_thread.currentThread(), self.my_thread.isRunning())



    # 更新文本框显示内容
    def update_text(self,text):
        # self.text.append(text)
        cursor = self.text.textCursor()
        self.text.moveCursor(cursor.End)  # 将光标移动到最后
        self.text.insertPlainText(text)

    # 关闭线程
    def stop(self):
        print('关闭当前线程')
        self.my_thread.quit()
        self.my_thread.wait()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())
