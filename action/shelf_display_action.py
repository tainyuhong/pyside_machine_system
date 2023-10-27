import sys
from pathlib import Path
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
        # self.tabWidget.currentChanged.connect(self.print_win_index)
        # 上架信息窗口
        # self.display_up_data()  # 默认页面查询
        self.bt_up_select.clicked.connect(
            lambda: self.select(self.ckb_up, self.up_date, self.display_up_data))  # 定义查询按钮事件
        self.ckb_up.stateChanged.connect(lambda: self.checkbox_state(self.ckb_up, self.up_date))
        self.btn_export_up.clicked.connect(lambda: self.export_up_to_xls(self.tb_up))  # 导出上架信息

        # 下架信息窗口
        if self.tabWidget.currentIndex() == 1:
            self.display_down_data()  # 默认页面查询
        else:
            pass
        self.bt_down_select.clicked.connect(lambda: self.select(self.ckb_down, self.down_date,
                                                                self.display_down_data))  # 定义查询按钮事件
        self.ckb_down.stateChanged.connect(lambda: self.checkbox_state(self.ckb_down, self.down_date))
        # self.btn_export_down.clicked.connect(lambda: self.export_up_to_xls(self.tb_down))  # 导出下架信息
        self.btn_export_down.clicked.connect(self.exp_down_list)  # 导出下架信息
        self.bt_hand_over.clicked.connect(self.create_hand_over_list)  # 生成移交清单

    # 上架信息查询
    def display_up_data(self, up_date=None):
        self.tb_up.clearContents()  # 清空表格中内容

        # 判断是否钩选重新上架
        if self.ckb_reupshelf.isChecked():
            print('重新上架的')
            if up_date is not None:
                updata_model = ViewUpshelf.select().where(
                    ViewUpshelf.date == up_date & ViewUpshelf.up_or_down == 3)  # 定义数据查询模型
                updata = [
                    (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model,
                     i.machine_sn,
                     i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in updata_model]  # 定义显示数据内容
            else:
                updata_model = ViewUpshelf.select().where(ViewUpshelf.up_or_down == 3)  # 定义数据查询模型
                updata = [
                    (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model,
                     i.machine_sn,
                     i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in updata_model]  # 定义显示数据内容
            # print('上架数据：',updata,len(updata))
        else:
            if up_date is not None:
                updata_model = ViewUpshelf.select().where(
                    ViewUpshelf.date == up_date & ViewUpshelf.up_or_down == 1)  # 定义数据查询模型
                updata = [
                    (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model,
                     i.machine_sn,
                     i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in updata_model]  # 定义显示数据内容
            else:
                updata_model = ViewUpshelf.select().where(ViewUpshelf.up_or_down == 1)  # 定义数据查询模型
                updata = [
                    (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model,
                     i.machine_sn,
                     i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in updata_model]  # 定义显示数据内容
            # print('上架数据：',updata,len(updata))

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
                    for cell_row in range(row_count):
                        for cell_col in range(col_count):
                            sh.cells(cell_row + 2, cell_col + 1).value = table.item(cell_row, cell_col).text()
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
                for cell_row in range(row_count):
                    # 序号
                    sh.cells(cell_row + 3, 1).value = num
                    # 设备名称
                    sh.cells(cell_row + 3, 2).value = self.tb_down.item(cell_row, 1).text()
                    # 位置
                    sh.cells(cell_row + 3, 3).value = self.tb_down.item(cell_row, 2).text()
                    # 品牌
                    sh.cells(cell_row + 3, 4).value = self.tb_down.item(cell_row, 3).text()
                    # 类型
                    sh.cells(cell_row + 3, 5).value = self.tb_down.item(cell_row, 4).text()
                    # 型号
                    sh.cells(cell_row + 3, 6).value = self.tb_down.item(cell_row, 5).text()
                    # 序列号
                    sh.cells(cell_row + 3, 7).value = self.tb_down.item(cell_row, 6).text()
                    # 管理IP
                    sh.cells(cell_row + 3, 8).value = self.tb_down.item(cell_row, 7).text()
                    # 下架日期
                    sh.cells(cell_row + 3, 9).value = self.tb_down.item(cell_row, 8).text()
                    # 备注
                    sh.cells(cell_row + 3, 10).value = self.tb_down.item(cell_row, 11).text()
                    num += 1  # 每添加一行增加1

                filesave, ok = QtWidgets.QFileDialog.getSaveFileName(self, '保存到excel', '', '*.xlsx')
                if ok:
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
                for cell_row in range(row_count):
                    # 设备型号
                    sh.cells(cell_row + 6, 2).value = self.tb_down.item(cell_row, 3).text() + self.tb_down.item(
                        cell_row, 5).text()
                    # 数量
                    sh.cells(cell_row + 6, 3).value = 1
                    # 序列号
                    sh.cells(cell_row + 6, 4).value = self.tb_down.item(cell_row, 6).text()

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
        if down_date is not None:
            data_model = ViewDownshelf.select().where(ViewDownshelf.date == down_date)  # 定义数据查询模型
            data = [
                (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model, i.machine_sn,
                 i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in data_model]  # 定义显示数据内容

            # 获取重复下架的设备信息
            redown_data_model = ViewDownshelf.select(ViewDownshelf.date == down_date & ViewDownshelf.machine_id).where(
                ViewDownshelf.up_or_down == 4).tuples()
            redown_data = [red[0] for red in redown_data_model]
            # print('重复上架设备：', redown_data)
        else:
            data_model = ViewDownshelf.select()  # 定义数据查询模型
            data = [
                (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model, i.machine_sn,
                 i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in data_model]  # 定义显示数据内容

            # 获取重复下架的设备信息
            redown_data_model = ViewDownshelf.select(ViewDownshelf.machine_id).where(
                ViewDownshelf.up_or_down == 4).tuples()
            redown_data = [red[0] for red in redown_data_model]
            # print('重复上架设备：', redown_data)

        # print('上架数据：', data)
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
    def checkbox_state(self, ckbox, dt):
        if ckbox.checkState() == Qt.Checked:
            dt.setDate(QDate.currentDate())  # 设置日期为当前日期
            dt.setEnabled(True)
            dt.setReadOnly(False)
            dt.setCalendarPopup(True)
        else:
            dt.setEnabled(False)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    shelf_win = UiShelfDisplay()
    shelf_win.show()
    sys.exit(app.exec())
