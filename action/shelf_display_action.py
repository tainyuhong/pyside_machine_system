import sys
from ui.shelf_display import *
from PySide6 import QtWidgets
from db.db_orm import *
from openpyxl import Workbook
# import logging
#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)
"""
设备上下架信息查看
"""

class UiShelfDisplay(Ui_shelf_display, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiShelfDisplay, self).__init__(parent)
        self.setupUi(self)
        # 上架信息窗口
        # self.display_up_data()  # 默认页面查询
        self.bt_up_select.clicked.connect(lambda : self.select(self.ckb_up, self.up_date, self.display_up_data))      # 定义查询按钮事件
        self.ckb_up.stateChanged.connect(lambda:self.checkbox_state(self.ckb_up,self.up_date))
        self.btn_export_up.clicked.connect(lambda:self.export_up_to_xls(self.tb_up))       # 导出上架信息

        # 下架信息窗口
        # if self.tabWidget.currentIndex() == 1:
        self.display_down_data()  # 默认页面查询
        self.bt_down_select.clicked.connect(lambda: self.select(self.ckb_down, self.down_date,
                                                                self.display_down_data))  # 定义查询按钮事件
        self.ckb_down.stateChanged.connect(lambda: self.checkbox_state(self.ckb_down, self.down_date))
        self.btn_export_down.clicked.connect(lambda: self.export_up_to_xls(self.tb_down))  # 导出下架信息
    # 上架信息查询
    def display_up_data(self,up_date=None):
        self.tb_up.clearContents()                  # 清空表格中内容
        if up_date is not None:
            updata_model = ViewUpshelf.select().where(ViewUpshelf.date==up_date)  # 定义数据查询模型
            updata = [
                (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model, i.machine_sn,
                 i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in updata_model]  # 定义显示数据内容
        else:
            updata_model = ViewUpshelf.select()  # 定义数据查询模型
            updata = [(i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model, i.machine_sn,
                      i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in updata_model]  # 定义显示数据内容
        # print('上架数据：',updata,len(updata))
        if len(updata) != 0:
            # 显示到页面中
            self.tb_up.setRowCount(len(updata))         # 定义表格显示内容行数
            for row, d1 in enumerate(updata):
                for col, d2 in enumerate(d1):
                    self.tb_up.setItem(row, col, QTableWidgetItem(str(updata[row][col])))
            self.tb_up.resizeColumnsToContents()        # 根据内容自定义列宽
            self.lb_state_up.setText('------> 查询到 {} 条记录 <------'.format(len(updata)))
            self.btn_export_up.setDisabled(True)  # 启用导出按钮
        else:
            self.tb_up.clearContents()  # 清空表格中内容
            self.tb_up.horizontalHeader().setDefaultSectionSize(80)         # 设置默认宽度为80
            QtWidgets.QMessageBox.warning(self, '上架信息查询', '未查询到任何上架信息！')
            self.btn_export_up.setDisabled(True)    # 禁用导出按钮

    # 导出上架信息至excel
    def export_up_to_xls(self,table):
        """
        导出上架信息至excel
        :param table: 页面窗口表格显示控件
        :return:
        """
        # # 写入测试数据
        # for row,i in enumerate(range(8)):
        #     for col,num in enumerate(range(12)):
        #         self.tb_up.setItem(row,col,QTableWidgetItem('{}-{}'.format(i,num)))

        wb = Workbook()     # 定义工作表
        sh = wb.active      # 激活页
        # print('表格名称',sh.title)

        # 导出至表格
        table_title = []    # 获取表头信息
        for i in range(12):
            table_title.append(table.horizontalHeaderItem(i).text())    # 插入表格标题一行
        # print(table_title)
        # 判断是否保存文件
        filesave,ok = QtWidgets.QFileDialog.getSaveFileName(self,'保存到excel','','*.xlsx')
        if ok:
            # print('filesave:',filesave)
            sh.append(table_title)
            row_count = table.rowCount()
            col_count = table.columnCount()
            for cell_row in range(row_count):
                for cell_col in range(col_count):
                    sh.cell(row=cell_row+2,column=cell_col+1,value=table.item(cell_row,cell_col).text())
            # print('导出完成')
            wb.save(filesave)       # 保存excel
            QtWidgets.QMessageBox.information(self, '导出完成', '导出完成！')

    # 下架信息查询
    def display_down_data(self, down_date=None):
        self.tb_down.clearContents()  # 清空表格中内容
        if down_date is not None:
            data_model = ViewDownshelf.select().where(ViewDownshelf.date == down_date)  # 定义数据查询模型
            data = [
                (i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model, i.machine_sn,
                 i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in data_model]  # 定义显示数据内容
        else:
            data_model = ViewDownshelf.select()  # 定义数据查询模型
            data = [(i.machine_id, i.machine_name, i.postion, i.machine_factory, i.machine_sort_name, i.model, i.machine_sn,
                     i.mg_ip, i.date, i.operator, i.machine_admin, i.comments) for i in data_model]  # 定义显示数据内容
        # print('上架数据：', data)
        if len(data) != 0:
            # 显示到页面中
            self.tb_down.setRowCount(len(data))  # 定义表格显示内容行数
            for row, d1 in enumerate(data):
                for col, d2 in enumerate(d1):
                    self.tb_down.setItem(row, col, QTableWidgetItem(str(data[row][col])))
            self.tb_down.resizeColumnsToContents()        # 根据内容自定义列宽
            self.lb_state_down.setText('------> 查询到 {} 条记录 <------'.format(len(data)))
        else:
            self.tb_down.clearContents()  # 清空表格中内容
            self.tb_down.horizontalHeader().setDefaultSectionSize(80)         # 设置默认宽度为80
            QtWidgets.QMessageBox.warning(self, '上架信息查询', '未查询到任何上架信息！')

    # 查询按钮
    def select(self,ckb,dt,fuc):
        """
        两个TAB窗口根据是否钩选日期来进行判断查询
        :param ckb: 复选框
        :param dt: 时间控件
        :param fuc: 查询函数
        :return:
        """
        if ckb.checkState()==Qt.Checked:
            date = dt.text()
            # print('选择日间：',date)
            fuc(date)
        else:
            fuc()

    # 定义是否启用时间选择控件
    def checkbox_state(self,ckbox,dt):
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
