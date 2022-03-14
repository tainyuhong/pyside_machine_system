import sys
from PySide6 import QtWidgets, QtGui, QtCore
from ui.Main_win import *
from action.MachineSelect_action import *
from action.machine_imp_exp import *
from action.check_action import *



class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义设备查询菜单触发事件
        self.actioncxsb.triggered.connect(self.show_select_win)
        # 定义批量导入菜单触发事件
        self.actionpldr.triggered.connect(self.imp_machine_win)
        # 定义设备巡检菜单触发事件
        self.actionsj.triggered.connect(self.check_win)


    # 定义设备查询窗口显示
    def show_select_win(self):
        select_window = Ui_MachineSelect()
        select_window.show()

    # 定义批量导入窗口显示
    def imp_machine_win(self):
        imp_window = UiImport()
        imp_window.show()

    # 定义巡检窗口显示
    def check_win(self):
        self.check_window = UiCheck()       # 需要通过self实例化为全局变量，不加self的话，一运行就被回收，也就无法显示。
        self.check_window.show()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Ui_MainWindow()
    win.show()
    sys.exit(app.exec())

