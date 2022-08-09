import sys
from PySide6 import QtWidgets, QtGui, QtCore
from ui.Main_win import *
from action.machine_select_action import UiMachineSelect
from action.machine_imp_exp import UiImport
from action.check_action import UiCheck
from action.add_machine_action import UiAdd
from action.modify_machine_action import UiModifyMachine
from action.base_info_action import UiBaseInfo
from action.up_shelf_action import UiUpShelf
from action.down_shelf_action import UiDownShelf
from action.shelf_display_action import UiShelfDisplay
from action.top_action import DisplayTop


class UiMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义基础数据菜单触发事件
        self.action_base.triggered.connect(self.base_info_win)
        # 定义设备查询菜单触发事件
        self.actioncxsb.triggered.connect(self.show_select_win)
        # 定义设备落位图菜单触发事件
        self.action_top.triggered.connect(self.show_top_win)

        # 定义批量导入菜单触发事件
        self.actionpldr.triggered.connect(self.imp_machine_win)
        # 定义设备巡检菜单触发事件
        self.actionsj.triggered.connect(self.check_win)
        # 定义添加设备菜单触发事件
        self.actiontjsb.triggered.connect(self.add_machine_win)
        # 定义修改设备菜单触发事件
        self.actionxg.triggered.connect(self.modify_win)
        # 定义设备上架菜单触发事件
        self.actionsjgl.triggered.connect(self.up_shelf_win)
        # 定义设备下架菜单触发事件
        self.actionxjgl.triggered.connect(self.down_shelf_win)
        # 定义上下架信息查询菜单触发事件
        self.action_shelf_display.triggered.connect(self.shelf_display_win)

    # 定义基础数据窗口显示
    def base_info_win(self):
        self.base_info_window = UiBaseInfo()
        self.base_info_window.show()

    # 定义设备查询窗口显示
    def show_select_win(self):
        self.select_window = UiMachineSelect()
        self.select_window.show()

    # 定义设备落位图窗口显示
    def show_top_win(self):
        self.top_window = DisplayTop()
        self.top_window.show()


    # 定义批量导入窗口显示
    def imp_machine_win(self):
        imp_window = UiImport()
        imp_window.show()

    # 定义添加设备窗口显示
    def add_machine_win(self):
        self.add_window = UiAdd()
        self.add_window.show()

    # 定义修改设备窗口显示
    def modify_win(self):
        self.modify_window = UiModifyMachine()
        self.modify_window.show()

    # 定义设备上架窗口显示
    def up_shelf_win(self):
        self.up_shelf_window = UiUpShelf()
        self.up_shelf_window.show()

    # 定义设备下架窗口显示
    def down_shelf_win(self):
        self.down_shelf_window = UiDownShelf()
        self.down_shelf_window.show()

    # 定义设备下架窗口显示
    def shelf_display_win(self):
        self.shelf_window = UiShelfDisplay()
        self.shelf_window.show()

    # 定义巡检窗口显示
    def check_win(self):
        self.check_window = UiCheck()  # 需要通过self实例化为全局变量，不加self的话，一运行就被回收，也就无法显示。
        self.check_window.show()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = UiMainWindow()
    win.show()
    sys.exit(app.exec())
