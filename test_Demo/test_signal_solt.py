# 测试多窗口signal信号传递
import sys

from PySide6.QtCore import *
from PySide6.QtWidgets import *

# 主窗口
class MainUi(QWidget):
    def __init__(self,parent=None):
        super(MainUi, self).__init__(parent)
        self.setWindowTitle('第一个窗口')
        self.resize(500,300)
        self.open_btn = QPushButton('打开')
        self.username = QLabel('默认文本')
        self.box = QHBoxLayout()
        self.box.addWidget(self.open_btn)
        self.box.addWidget(self.username)
        self.setLayout(self.box)
        self.open_btn.clicked.connect(self.get_data)

    # 实例化子窗口并获取子窗口返回数据
    def get_data(self):
        child_win = ChildWin()
        child_win.name_signal.connect(self.set_to_text)
        child_win.exec()

    # 传入用户名和密码并设置到显示框中
    def set_to_text(self,name,passwd):
        self.username.setText('用户名：{}，密码：{}'.format(name,passwd))


# 子窗口
class ChildWin(QDialog):
    name_signal = Signal(str,str)       # 子窗信号，用于传递用户名
    def __init__(self,parent=None):
        super(ChildWin, self).__init__(parent)
        self.setWindowTitle('子窗口')
        self.resize(400,200)
        layout = QHBoxLayout()
        name = QLabel('用户名：')
        passwd = QLabel('密码：')
        self.namele = QLineEdit()
        self.passwdle = QLineEdit()
        self.commit_btn = QPushButton('提交')
        layout.addWidget(name)
        layout.addWidget(self.namele)
        layout.addWidget(passwd)
        layout.addWidget(self.passwdle)
        layout.addWidget(self.commit_btn)
        self.setLayout(layout)
        self.commit_btn.clicked.connect(self.get_name)      # 关连信号发信槽函数

    # 定义槽函数，用于获取用户名并发射信号
    def get_name(self):
        user_name = self.namele.text()      # 获取输入的用户名
        password = self.passwdle.text()     # 获取密码
        self.name_signal.emit(user_name,password)        # 发射信号
        self.close()    # 发射完信号后关闭窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()
    sys.exit(app.exec())