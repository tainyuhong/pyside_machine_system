import sys
from pathlib import Path
from time import time
from ui.shelf_display import *
from PySide6 import QtWidgets
from db.db_orm import *
import xlwings as xw

"""
设备上下架信息查看
"""


class UiShelfDisplay(Ui_shelf_display, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiShelfDisplay, self).__init__(parent)
        self.setupUi(self)

        self.sql = []   # 用于接收拼接SQL
        self.down_sql = []      # 用于接收拼接下架SQL

        # self.tabWidget.currentChanged.connect(self.print_win_index)
        # 上架信息窗口
        # self.display_up_data()  # 默认页面查询
        self.bt_up_select.clicked.connect(
            lambda: self.select(self.ckb_up, self.up_date, self.display_up_data))  # 定义查询按钮事件

        # 设置上架日期复选框事件
        self.ckb_up.stateChanged.connect(lambda: self.checkbox_state(self.ckb_up, self.up_date,self.end_up_time))
        self.btn_export_up.clicked.connect(lambda: self.export_up_to_xls(self.tb_up))  # 导出上架信息

        # 下架信息窗口
        if self.tabWidget.currentIndex() == 1:
            self.display_down_data()  # 默认页面查询
        else:
            pass
        self.bt_down_select.clicked.connect(lambda: self.select(self.ckb_down, self.down_date,
                                                                self.display_down_data))  # 定义查询按钮事件
        # 设置下架日期复选框事件
        self.ckb_down.stateChanged.connect(lambda: self.checkbox_state(self.ckb_down, self.down_date,self.end_down_time))
        # self.btn_export_down.clicked.connect(lambda: self.export_up_to_xls(self.tb_down))  # 导出下架信息
        self.btn_export_down.clicked.connect(self.exp_down_list)  # 导出下架信息
        self.bt_hand_over.clicked.connect(self.create_hand_over_list)  # 生成移交清单

    # 上架信息查询
    def display_up_data(self, up_date=None):
        self.tb_up.clearContents()  # 清空表格中内容
        self.sql = []
        # 拼接SQL
        self.choose_reup()          # 判断是否钩上架
        self.choose_date()          # 判断日期

        sql = ViewUpshelf.select(ViewUpshelf.machine_id,ViewUpshelf.machine_name,ViewUpshelf.postion,
                                          ViewUpshelf.machine_factory,ViewUpshelf.machine_sort_name, ViewUpshelf.model,ViewUpshelf.machine_sn,
                                          ViewUpshelf.mg_ip,ViewUpshelf.date, ViewUpshelf.operator,
                                          ViewUpshelf.machine_admin,ViewUpshelf.comments)
        if len(self.sql) > 0:
            updata_model = sql.where(* self.sql).tuples()  # 定义数据查询模型
        else:
            updata_model = sql.tuples()
        updata = [v for v in updata_model]
        # print('up sql',updata_model.sql())

        # 判断查询到的数据是否为0
        if len(updata) != 0:
            # 显示到页面中
            self.tb_up.setRowCount(len(updata))  # 定义表格显示内容行数
            for row, d1 in enumerate(updata):
                for col, d2 in enumerate(d1):
                    self.tb_up.setItem(row, col, QTableWidgetItem(str(updata[row][col])))
            self.tb_up.resizeColumnsToContents()  # 根据内容自定义列宽
            self.lb_state_up.setText('------> 查询到 {} 条记录 <------'.format(len(updata)))
            self.btn_export_up.setDisabled(False)  # 启用导出按钮
        else:
            self.tb_up.clearContents()  # 清空表格中内容
            self.tb_up.horizontalHeader().setDefaultSectionSize(80)  # 设置默认宽度为80
            QtWidgets.QMessageBox.warning(self, '上架信息查询', '未查询到任何上架信息！')
            self.btn_export_up.setDisabled(True)  # 禁用导出按钮

    # 判断是否钩选重复上架
    def choose_reup(self):
        if self.ckb_reupshelf.isChecked():
            self.sql.append(ViewUpshelf.up_or_down == 3)
        else:
            self.sql.append(ViewUpshelf.up_or_down == 1)

    # 判断是否钩选上架日期
    def choose_date(self):
        # print('日期',self.up_date.text())
        if self.ckb_up.isChecked():
            self.sql.append(ViewUpshelf.date.between(self.up_date.text(),self.end_up_time.text()) )
        else:
            pass

    # 判断是否钩选下架日期
    def choose_down_date(self):
        if self.ckb_down.isChecked():
            self.down_sql.append(ViewDownshelf.date.between(self.down_date.text(),self.end_down_time.text()))
        else:
            self.down_sql.append(ViewDownshelf.up_or_down == 2)

    # 导出上架信息至excel
    def export_up_to_xls(self, table):
        """
        导出上架信息至excel
        :param table: 页面窗口表格显示控件
        :return:
        """
        # 判断第一行第一列是否有数据，如果没有则没有需要导出的数据
        if table.item(0, 0):
            with xw.App(visible=False, add_book=False) as xl_app:
                wb = xl_app.books.add()  # 定义工作表
                sh = wb.sheets.active

                # 导出至excel表格中
                table_title = []  # 获取表头信息
                for i in range(12):
                    table_title.append(table.horizontalHeaderItem(i).text())  # 插入表格标题一行
                # print(table_title)
                # 判断是否保存文件
                filesave, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存到excel', '', '*.xlsx')
                if ok:
                    # print('filesave:',filesave)
                    sh.range('A1').value = table_title  # 写入标题栏
                    row_count = table.rowCount()
                    col_count = table.columnCount()
                    # excel中进行文本格式化后再写入内容
                    sh.range((2, 2), (row_count + 1, col_count + 1)).options(expand='table').api.NumberFormat = '@'
                    # 从页面表格中获取数据写入到EXCEL中
                    data = []       # 表单数据内容
                    for cell_row in range(row_count):
                        data_row = []       # 接收每一行数据内容
                        for cell_col in range(col_count):
                            data_row.append(table.item(cell_row, cell_col).text())
                        data.append(data_row)

                    # 向表格中一次性写入所有数据
                    sh.range(2, 1).options(expand='table').value=data
                    # 自适应列宽
                    sh.autofit('c')
                    # 添加边框线
                    for i in range(7, 13):
                        sh.range('A1').expand('table').api.Borders(i).Weight = 2
                    wb.save(filesave)  # 保存excel
                    wb.close()
                    QtWidgets.QMessageBox.information(self, '导出完成', '导出完成！')
        else:
            QtWidgets.QMessageBox.critical(self, '导出错误', '未找到要导出的数据！')

    # 导出下架设备信息
    def exp_down_list(self):
        # 判断第一行第一列是否有数据，如果没有则没有需要导出的数据
        if self.tb_down.item(0, 0):
            with xw.App(visible=False, add_book=False) as xl_app:
                filesave, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存到excel', '', '*.xlsx')
                if ok:
                    # 打开模板表
                    wb = xl_app.books.open(Path(__file__).parents[1] / 'machine_template' / 'down_audit_tmp.xlsx')
                    sh = wb.sheets[0]

                    # 下架设备数据写入到EXCEL中
                    row_count = self.tb_down.rowCount()  # 行数
                    # 如果行数大于13则复制格式到多余的行上
                    if row_count > 13:
                        for _ in range(row_count - 13):
                            sh.range('A15', 'J15').copy(sh.range((16 + _, 1), (16 + _, 10)))

                    num = 1  # 初始化序号
                    data = []       # 接收查到的到表格数据
                    for cell_row in range(row_count):
                        # 接收查到的到表格的行数据
                        row_data = [num, self.tb_down.item(cell_row, 1).text(), self.tb_down.item(cell_row, 2).text(),
                                    self.tb_down.item(cell_row, 3).text(), self.tb_down.item(cell_row, 4).text(),
                                    self.tb_down.item(cell_row, 5).text(), self.tb_down.item(cell_row, 6).text(),
                                    self.tb_down.item(cell_row, 7).text(), self.tb_down.item(cell_row, 8).text(),
                                    self.tb_down.item(cell_row, 11).text()]
                        num += 1  # 每添加一行增加1

                        # 将每一行数据提交到总表中
                        data.append(row_data)

                    # 将获取到的页面数据插入到表格中
                    # print('data',data)
                    sh.range(3, 1).options(expand='table').value = data
                    wb.save(filesave)  # 保存excel
                    wb.close()
                    QtWidgets.QMessageBox.information(self, '导出完成', '导出完成！')

        else:
            QtWidgets.QMessageBox.critical(self, '导出错误', '未找到要导出的数据！')

    # 生成移交清单
    def create_hand_over_list(self):
        # 判断第一行第一列是否有数据，如果没有则没有需要导出的数据
        if self.tb_down.item(0, 0):
            with xw.App(visible=False, add_book=False) as xl_app:
                # 打开模板表
                wb = xl_app.books.open(Path(__file__).parents[1] / 'machine_template' / 'hand_over_list_tmp.xlsx')
                sh = wb.sheets[0]
                sh.cells(2, 2).value = self.tb_down.item(0, 8).text()  # 时间
                sh.cells(3, 2).value = self.tb_down.item(0, 11).text()  # 事项
                # 设备清单数据写入到EXCEL中
                row_count = self.tb_down.rowCount()  # 行数
                # col_count = self.tb_down.columnCount()  # 列数
                # 定义存放从页面获取的表格数据内容
                data = []
                for cell_row in range(row_count):
                    # 获取每行的数据   设备型号,数量,序列号
                    row_data = [self.tb_down.item(cell_row, 3).text() + self.tb_down.item(
                        cell_row, 5).text(),1,self.tb_down.item(cell_row, 6).text()]
                    # 将行数据加入到data列表中
                    data.append(row_data)

                # 所获取的所有数据写入到表格中
                sh.range(6,2).options(expand='table').value=data

                # todo 对于超过10的数据还需要对格式进行调整优化否则没有序列及字体或格式有问题
                # print('data',data)

                filesave, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存到excel', '', '*.xlsx')
                if ok:
                    wb.save(filesave)  # 保存excel
                    wb.close()
                    QtWidgets.QMessageBox.information(self, '导出完成', '导出完成！')

        else:
            QtWidgets.QMessageBox.critical(self, '导出错误', '未找到要导出的数据！')

    # 下架信息查询
    def display_down_data(self, down_date=None):
        self.tb_down.clearContents()  # 清空表格中内容

        self.down_sql = []
        self.choose_down_date()     # 判断是否钩下架时间

        sql = ViewDownshelf.select(ViewDownshelf.machine_id,ViewDownshelf.machine_name,ViewDownshelf.postion,
                                          ViewDownshelf.machine_factory,ViewDownshelf.machine_sort_name,ViewDownshelf.model,
                                          ViewDownshelf.machine_sn,ViewDownshelf.mg_ip,ViewDownshelf.date,ViewDownshelf.operator,
                                          ViewDownshelf.machine_admin,ViewDownshelf.comments)
        if len(self.down_sql) > 0:
            data_model = sql.where(* self.down_sql).tuples().order_by(ViewDownshelf.date.desc())
        else:
            data_model = sql.tuples().order_by(ViewDownshelf.date.desc())
        # print('down sql', data_model.sql())
        data = [d for d in data_model]

        # 获取重复下架的设备信息
        redown_data_model = ViewDownshelf.select(ViewDownshelf.machine_id).where(
            ViewDownshelf.up_or_down == 4).tuples()
        redown_data = [red[0] for red in redown_data_model]

        # 处理并显示查询数据
        if len(data) != 0:
            # 显示到页面中
            self.tb_down.setRowCount(len(data))  # 定义表格显示内容行数
            for row, d1 in enumerate(data):
                for col, d2 in enumerate(d1):
                    item = QTableWidgetItem(str(d2))  # 定义单元格内容

                    # 判断第一列的设备id是否为重复上架信息中设备
                    if col == 0 and d2 in redown_data:
                        # print('值', d2, '行号：', row)
                        item.setBackground(QBrush(QColor(255, 165, 0)))  # 设置单元格背景颜色
                    else:
                        pass
                    self.tb_down.setItem(row, col, item)  # 在表格对应位置填充相应内容
            self.tb_down.resizeColumnsToContents()  # 根据内容自定义列宽

            self.lb_state_down.setText('设备ID黄色标记的为重复下架设备         ------> 查询到 {} 条记录 <------'.format(len(data)))
        else:
            self.tb_down.clearContents()  # 清空表格中内容
            self.tb_down.horizontalHeader().setDefaultSectionSize(80)  # 设置默认宽度为80
            QtWidgets.QMessageBox.warning(self, '上架信息查询', '未查询到任何上架信息！')

    # 查询按钮
    def select(self, ckb, dt, fuc):
        """
        两个TAB窗口根据是否钩选日期来进行判断查询
        :param ckb: 复选框
        :param dt: 时间控件
        :param fuc: 查询函数
        :return:
        """
        if ckb.checkState() == Qt.Checked:
            date = dt.text()
            # print('选择日间：',date)
            fuc(date)
        else:
            fuc()

    # 定义是否启用时间选择控件
    def checkbox_state(self, ckbox, dt,dt_end):
        if ckbox.checkState() == Qt.Checked:
            # 开始时间
            dt.setDate(QDate.currentDate())         # 设置日期为当前日期
            dt.setEnabled(True)
            dt.setReadOnly(False)
            dt.setCalendarPopup(True)
            # 结束时间
            dt_end.setDate(QDate.currentDate())  # 设置默认结束时间为当前时期
            dt_end.setEnabled(True)
            dt_end.setReadOnly(False)
            dt_end.setCalendarPopup(True)
        else:
            dt.setEnabled(False)
            dt_end.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    shelf_win = UiShelfDisplay()
    shelf_win.show()
    sys.exit(app.exec())
