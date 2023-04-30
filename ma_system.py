import sys
import time
from PySide6 import QtWidgets, QtCore
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
from action.check_config_action import UiCconfigCheck
from action.password_config_action import UiPassword
from action.report_action import MachineReport
from action.export_to_excel_action import ExportExcel       # 导出设备信息
from action.warranty_action import UiWarrantySelect        # 维保信息查询
from db.db_orm import database


class UiMainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)
        self.setupUi(self)

        # 定义基础数据菜单触发事件
        self.action_base.triggered.connect(self.base_info_win)

        # 查询管理
        # 定义设备查询菜单触发事件
        self.actioncxsb.triggered.connect(self.show_select_win)
        # 定义设备落位图菜单触发事件
        self.action_top.triggered.connect(self.show_top_win)
        # 定义设备分析报告页面
        self.action_report.triggered.connect(self.anlysis_report_win)
        # 定义维保信息查询菜单触发事件
        self.actionwb.triggered.connect(self.show_wb_select_win)

        # 定义批量导入菜单触发事件
        self.actionpldr.triggered.connect(self.imp_machine_win)
        # 定义导出设备信息菜单触发事件
        self.actionexport_exl.triggered.connect(self.export_ma_win)

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
        self.lb_status = QtWidgets.QLabel('')

        # 定义设备巡检菜单触发事件
        self.actionsj.triggered.connect(self.check_win)
        # 定义设备巡检配置菜单触发事件
        self.actionsjpz.triggered.connect(self.check_config_win)

        # 定义用户密码查看菜单触发事件
        self.actionuser_pass.triggered.connect(self.user_pass_win)

        self.statusbar.showMessage('状态栏')
        self.statusbar.addPermanentWidget(self.lb_status)

    # 定义基础数据窗口显示
    def base_info_win(self):
        self.base_info_window = UiBaseInfo()
        self.base_info_window.show()

    # 定义设备查询窗口显示
    @staticmethod
    def show_select_win():
        select_window = UiMachineSelect()   # 设备信息查询
        select_window.show()

    # 定义维保信息查询显示窗口
    @staticmethod
    def show_wb_select_win():
        select_wb_win = UiWarrantySelect()     # 维保信息查询
        select_wb_win.show()

    # 定义设备落位图窗口显示
    def show_top_win(self):
        self.top_window = DisplayTop()
        self.top_window.show()

    # 定义分析报告页面
    def anlysis_report_win(self):
        self.anlysis_report = MachineReport()
        self.anlysis_report.show()

    # 定义批量导入窗口显示
    def imp_machine_win(self):
        imp_window = UiImport()
        imp_window.show()

    # 定义导出设备信息窗口显示
    def export_ma_win(self):
        self.exp_window = ExportExcel()
        self.exp_window.show()

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

    # 定义巡检配置窗口显示
    def check_config_win(self):
        self.check_config_window = UiCconfigCheck()  # 需要通过self实例化为全局变量，不加self的话，一运行就被回收，也就无法显示。
        self.check_config_window.show()

    # 根据数据库的状态设置状态栏数据库状态颜色
    def display(self, text):
        # print(text)
        if text == 'True':
            self.lb_status.setText('数据库连接正常')
            self.lb_status.setStyleSheet(u"background-color: rgb(85, 255, 0)")
        else:
            self.lb_status.setText('数据库连接断开')
            self.lb_status.setStyleSheet(u"background-color: rgb(255, 0, 0)")

    # 定义用户密码查看窗口显示
    def user_pass_win(self):
        input_pass = QtWidgets.QInputDialog(self)
        # input_pass.show()
        input_pass.setWindowTitle('菜单密码')
        input_pass.setLabelText('请输入菜单密码')
        input_pass.setTextEchoMode(QtWidgets.QLineEdit.Password)
        input_pass.setOkButtonText('确认')
        input_pass.setCancelButtonText('取消')
        if input_pass.exec():
            # print('Value:',input_pass.textValue(),input_pass.okButtonText())
            if input_pass.okButtonText() == '确认' and input_pass.textValue().strip() == '123456':
                self.user_passwd_window = UiPassword()  # 需要通过self实例化为全局变量，不加self的话，一运行就被回收，也就无法显示。
                self.user_passwd_window.show()
            else:
                QtWidgets.QMessageBox.warning(self, '密码输入错误', '密码错误！')


# 数据库状态检测对象
class DbStat(QObject):
    db_signal = QtCore.Signal(str)  # 数据库状态信号

    def __init__(self, parent=None):
        super(DbStat, self).__init__(parent)

    # 持续检测数据库当前状态
    def check_db_stat(self):
        while True:
            self.db_status()  # 执行连接检查
            time.sleep(3)  # 等待

    # 检测数据库连接状态
    def db_status(self):
        try:
            database._connect()  # 尝试连接数据库
            # database.connect(True)
        except Exception as e:
            self.db_signal.emit('False')  # 连接异常发送False信号
            # QtWidgets.QMessageBox.critical(self,'数据库连接错误', '无法连接到数据库，请检查数据库配置信息是否正确！')
        else:
            self.db_signal.emit('True')  # 连接正常发送True信号


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = UiMainWindow()
    win.show()
    mysql_stat = DbStat()  # 创建数据库检查实例
    mysql_stat.db_signal.connect(win.display)  # 将数据库状态信号连接至页面状态栏
    new_thread = QtCore.QThread()  # 创建一个线程用于获取数据库状态
    mysql_stat.moveToThread(new_thread)  # 将数据库状态实例移到新线程上
    new_thread.started.connect(mysql_stat.check_db_stat)  # 新线程开始时执行数据库状态检测
    new_thread.start()  # 开始线程
    sys.exit(app.exec())
