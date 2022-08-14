# 测试多线程moveToThread
import sys
import time
from PySide6.QtCore import  *
from db.db_orm import *
from PySide6.QtWidgets import *


class MyObject(QObject):
    update_signal = Signal(str)
    def __init__(self):
        super(MyObject, self).__init__(parent=None)

    def worker(self):
        while True:
            time.sleep(2)
            self.update_signal.emit('发送定时任务消息')

class DbStat(QObject):
    update_signal = Signal(str)     # 数据库状态信号传递

    def __init__(self,parent=None):
        super(DbStat, self).__init__(parent)

    def check_db_stat(self):
        while True:
            self.db_status()
            time.sleep(3)

    def db_status(self):
        try:
            database.connect(True)
        except Exception as e:
            # print('数据库连接失败')
            self.update_signal.emit('False')
            # QtWidgets.QMessageBox.critical(self,'数据库连接错误', '无法连接到数据库，请检查数据库配置信息是否正确！')
            # print(False)
        else:
            # print('数据库连接成功')
            self.update_signal.emit('True')
            # print(True)

class MainForm(QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setWindowTitle('多线程测试-定时发送消息')
        self.resize(500, 300)
        layout = QVBoxLayout()
        self.start_btu = QPushButton('开始')
        layout.addWidget(self.start_btu)
        self.text = QTextEdit(self)
        layout.addWidget(self.text)
        self.setLayout(layout)
        self.start_btu.clicked.connect(self.do_worker)

    def do_worker(self):
        self.text.clear()
        self.obj = DbStat()
        self.obj.update_signal.connect(self.update_text)
        self.mythread = QThread()
        self.obj.moveToThread(self.mythread)
        self.mythread.started.connect(self.obj.check_db_stat)
        self.mythread.start()

    # 更新文本框显示内容
    def update_text(self,text):
        print('接收的内容：',text)
        self.text.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())