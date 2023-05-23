import sys
from ui.top import Ui_top
from PySide6 import QtWidgets, QtGui, QtCore
import xlwings as xw
from db.db_orm import *
from action.pub_infos import PubSwitch

"""
设备位图

"""


class DisplayTop(QtWidgets.QWidget, Ui_top):
    load_win = set()
    def __init__(self, parent=None):
        super(DisplayTop, self).__init__(parent)
        self.setupUi(self)
        self.pub_infos = PubSwitch()
        self.rooms = self.pub_infos.get_room().values()
        self.setWindowState(QtCore.Qt.WindowMaximized)  # 最大化打开窗口
        self.create_room_win()  # 创建机房窗口视图

        self.tabWidget.currentChanged.connect(self.display_machine)  # 页面切换时触发设备查询事件

        self.bt_exp.clicked.connect(self.exp_to_excel)  # 导出按钮事件

    # 生成每个机房的页面窗口视图
    def create_room_win(self):
        # 获取机房数据
        for tab_name in self.rooms:
            tab = QtWidgets.QWidget()
            tab.setObjectName(tab_name)
            # if self.tabWidget.currentIndex() == num:
            self.tabWidget.addTab(tab, tab_name)  # 添加到tab控件中
            vertlayout = QtWidgets.QVBoxLayout(tab)  # 在tab页面上创建垂直布局层
            table = QtWidgets.QTableWidget()  # 定义表格控件
            vertlayout.addWidget(table)  # 将表格添加到垂直布局中

        ind = self.tabWidget.currentIndex()     # 当前页面索引号
        # print('当前索引：',ind)
        if ind == 0:
            self.display_machine()

    # # 将设备放入机柜对应位置上
    def display_machine(self):
        tab_name = self.tabWidget.tabText(self.tabWidget.currentIndex())
        if tab_name in self.load_win:
            return
        else:
            cell_bg_color = QtGui.QBrush(QtGui.QColor(250, 250, 210))  # 定义表格单元格画刷颜色
            # 获取机房设备信息

            room_machine_datas = self.get_machine_info(tab_name)
            # 查找页面中表格控件，并赋值给table
            table = self.tabWidget.currentWidget().findChild(QtWidgets.QTableWidget)
            # 对每个机房机房数据进行处理,生成空机柜模型
            cabinet = self.get_cabinet(self.pub_infos.room_swap_id(name=tab_name))  # 机柜数据
            u_pos_data = self.get_u_pos()  # U位信息
            table.setRowCount(len(u_pos_data))  # U数
            table.setVerticalHeaderLabels(u_pos_data)
            table.setColumnCount(len(cabinet))  # 每页列数
            table.setAlternatingRowColors(True)  # 每行颜色交叉显示
            table.setHorizontalHeaderLabels(cabinet)  # 将机柜名设置为每列的列名
            # 将设备数据写入到表格的对应位置中
            for machine in room_machine_datas:
                # print('machine_data', machine)      # 数据格式：('A01', 2, 4, '第二台上架设备', '8.8.8.8', '8.8.8.8')
                # print(machine)
                jigui = machine[0]  # 相当于表格的列
                u_postion = machine[1]  # 相当于表格的行
                item = QtWidgets.QTableWidgetItem('\n\r'.join(machine[3:]))  # 定义单元格内容
                item.setBackground(cell_bg_color)  # 设置单元格背景色
                item.setTextAlignment(QtCore.Qt.AlignCenter)  # 水平居中对齐

                # 机柜数据 格式：setItem(row,col,item)
                table.setItem(u_postion - 1, cabinet.index(jigui), item)  # 写入对应机柜数据
                # 如果设备U数大于2U,对多U的设备进行单元格合并
                if machine[2] > 1:
                    table.setSpan(u_postion - 1, cabinet.index(jigui), machine[2], 1)
                table.resizeRowsToContents()  # 自适应行高
                table.horizontalHeader().setDefaultSectionSize(120)  # 设置每列宽度
                table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置为表格不可编辑

                # 为避免重复打开页面需要重新加载，将页面索引加入
                self.load_win.add(tab_name)# 为避免重复打开页面需要重新加载，将页面索引加入
            self.load_win.add(tab_name)

    # 获取U位信息
    @staticmethod
    def get_u_pos():
        pos_model = CabPosition.select(CabPosition.num, CabPosition.position_name).execute()
        pos_data = [i.position_name for i in pos_model]
        return pos_data

    # 获取每个机房所有机柜数据
    @staticmethod
    def get_cabinet(room_id):
        cab_model = Cabinet.select(Cabinet.cab_num).where(
            (Cabinet.room_id == room_id) & (Cabinet.is_use == 1)).order_by(Cabinet.cab_num).execute()
        # print(cab_model)
        cab_data = [i.cab_num for i in cab_model]
        # print(cab_data)
        return cab_data

    # 查询设备待下一步写入对应U位中
    @staticmethod
    def get_machine_info(room):
        machine_model = MachineList.select(MachineList.cab_name, MachineList.start_position, MachineList.postion_u,
                                           Case(None, ((MachineList.machine_name.is_null(True), ''), (
                                               MachineList.machine_name.is_null(False), MachineList.machine_name))),
                                           Case(None, (
                                               (MachineList.mg_ip.is_null(True), ''),
                                               (MachineList.mg_ip.is_null(False), MachineList.mg_ip)), ),
                                           Case(None, ((MachineList.bmc_ip.is_null(True), ''),
                                                       (MachineList.bmc_ip.is_null(False), MachineList.bmc_ip)))).where(
            MachineList.room_name == room).tuples()
        # print(machine_model)
        machine_data = [i for i in machine_model]
        # print(machine_data)
        # 数据格式 [('A01', 37, 1, '10G带外管理接入3', '', ''), ('A01', 34, 1, '10G业务管理交换机1', '', '')]
        return machine_data

    # 导入机柜top示意图
    def exp_to_excel(self):
        filepath, filetype = QtWidgets.QFileDialog.getSaveFileUrl(self, '导出机柜落位图', filter='.xlsx')
        # print('保存文件路径：',filepath,filepath.toLocalFile())
        if filepath != '':
            # 如果用户没有在文件名后加后缀名，则系统自动加上
            save_file = filepath.toLocalFile() + '.xlsx'
            # 将文件从系统下载到指定目录
            try:
                # 创建工作簿
                exl_app = xw.App(visible=False, add_book=False)
                wb = exl_app.books.add()
                a = 'Sheet1'  # 给定默认工作表名
                # 按机房名创建工作表
                for i in self.rooms:
                    wb.sheets.add(i, after=wb.sheets[a])  # 增加工作表，在上一个表后
                    a = i
                wb.sheets['Sheet1'].delete()  # 删除默认添加的sheet页
                # print(wb.sheets.count)      # 工作表总数
                for ind in range(wb.sheets.count):
                    ws_name = wb.sheets(ind + 1).name
                    # print(ws_name)
                    # 获取机柜名称，写入表格第一行
                    cabinet_name = self.get_cabinet(self.pub_infos.room_swap_id(name=ws_name))
                    # 获取U位信息
                    u = self.get_u_pos()
                    # print(u)
                    u.sort(reverse=True)  # 进行反向排序
                    sh1 = wb.sheets[ws_name]  # 写入数据
                    sh1.api.activate
                    sh1.range('A2').options(transpose=True).value = u
                    sh1.range('B1').value = cabinet_name  # 机柜名称：从第一行第二列开始写入

                    # 获取设备数据
                    machine_data = self.get_machine_info(ws_name)

                    # 写入表格中
                    for data in machine_data:  # data 数据格式 ：('A01', 37, 1, '10G带外管理接入3', '', '')
                        # print(data)
                        row = 42 - data[1] + 2  # 42u-所在U索引号+1+标题栏
                        col = cabinet_name.index(data[0]) + 2  # 在机柜列表中查询机柜当前的索引号+2
                        sh1.cells(row, col).value = '\n\r'.join(data[3:])  # 给指定单元格赋值

                        # 合并单元格处理
                        rng = sh1.range((row, col), (row - data[2] + 1, col))  # 设备单元格区域
                        rng.merge()  # 合并单元格
                        rng.color = (255, 228, 181)  # 设置颜色

                    # 整个工作表格式化
                    sh1.range('B1').expand('right').column_width = 27
                    sh1.autofit('r')  # 自适应行高
                    # 增加边框线
                    for i in range(7, 13):
                        sh1.range('A1').expand().api.Borders(i).Weight = 2
                    # 设置第一行第一列的颜色
                    sh1.range('B1').expand('right').color = (100, 149, 237)
                    sh1.range('A2').expand('down').color = (255, 165, 0)
                    wb.save(save_file)
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, '保存文件', '保存文件错误！{}'.format(e))
            else:
                wb.close()
                exl_app.quit()
                QtWidgets.QMessageBox.information(self, '保存文件', '保存文件成功！！')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    top_win = DisplayTop()
    top_win.show()
    sys.exit(app.exec())
