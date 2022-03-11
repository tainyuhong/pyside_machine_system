# 测试多线程moveToThread
import sys
import time
from PySide6.QtCore import  *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class MyObject(QObject):
    update_signal = Signal(str)
    def __init__(self):
        super(MyObject, self).__init__(parent=None)

    def worker(self):
        while True:
            time.sleep(2)
            self.update_signal.emit('发送定时任务消息')


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
        self.obj = MyObject()
        self.obj.update_signal.connect(self.update_text)
        self.mythread = QThread()
        self.obj.moveToThread(self.mythread)
        self.mythread.started.connect(self.obj.worker)
        self.mythread.start()

    # 更新文本框显示内容
    def update_text(self,text):
        self.text.append(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec())