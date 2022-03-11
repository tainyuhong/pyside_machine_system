# 测试多线程QTread
import sys
import time
from PySide6.QtCore import  *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# 多线程
class WorkThread(QThread):
    trigger = Signal()
    def __init__(self):
        super(WorkThread, self).__init__()

    def run(self):
        for i in range(10000000):
            print(i)
        self.trigger.emit()
# 界面
class MainUi(QWidget):
    def __init__(self,parent=None):
        super(MainUi, self).__init__(parent)
        self.setWindowTitle('多线程测试-电子显示')
        self.resize(500, 300)
        layout = QVBoxLayout()
        self.lcdNumber=QLCDNumber()
        layout.addWidget(self.lcdNumber)
        self.start_btu = QPushButton('开始')
        layout.addWidget(self.start_btu)
        self.setLayout(layout)

        self.timer = QTimer()
        self.workthread = WorkThread()

        self.timer.timeout.connect(self.set_time)
        self.start_btu.clicked.connect(self.worker)
        self.sec = 0

    def worker(self):
        self.timer.start(1000)
        self.workthread.start()
        self.workthread.trigger.connect(self.time_stop)
        # for i in range(1000000000):
        #     pass
        # self.timer.stop()

    def time_stop(self):
        self.timer.stop()
        print('运行结束用时：',self.lcdNumber.value())
        self.sec=0

    def set_time(self):
        # time.sleep(1)
        self.sec += 1
        self.lcdNumber.display(self.sec)
            # QApplication.processEvents()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()

    sys.exit(app.exec())