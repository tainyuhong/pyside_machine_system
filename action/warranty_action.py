import sys
from PySide6 import QtWidgets
from ui.warranty import *
from db.db_orm import *
from action.pub_infos import PubSwitch


class UiWarrantySelect(QtWidgets.QWidget, Ui_Warranty):
    def __init__(self, parent=None):
        super(UiWarrantySelect, self).__init__(parent)
        self.setupUi(self)
        self.pub_infos = PubSwitch()
        self.get_room_data()  # 显示机房信息
        self.get_warranty_type()  # 显示维保类型下拉菜单
        self.get_under()  # 显示是否在保内下拉菜单
        # 设置表格相关信息
        self.warranty_select.setHorizontalHeaderLabels(
            ['维保ID', '设备ID', '机房名称', '机柜名称', 'U位', '设备名称', '带内IP', '带外IP', '序列号',
             '维保开始日', '维保结束日', '维保单位', '维保类型', '是否在保内', '备注'])

        # 初始化定义分页信息
        self.current_page = 1
        self.select_values = []  # 查询条件值
        self.select_btn.clicked.connect(self.get_input_data)  # 按条件进行查询
        # 分页查询按钮事件
        self.go_btn.clicked.connect(lambda: self.goToPage(self.data_sql, self.select_values[:-1]))  # 定义转到按钮点击事件
        self.next_btn.clicked.connect(lambda: self.nextPage(self.data_sql, self.select_values[:-1]))  # 定义下一页按钮事件
        self.pre_btn.clicked.connect(lambda: self.prePage(self.data_sql, self.select_values[:-1]))  # 定义上一页按钮事件
        self.home_btn.clicked.connect(lambda: self.firstPage(self.data_sql, self.select_values[:-1]))  # # 定义首页按钮事件
        self.last_btn.clicked.connect(lambda: self.lastPage(self.data_sql, self.select_values[:-1]))  # 定义最后一页事件

    # 获取机房名称信息
    def get_room_data(self):
        room_name = self.pub_infos.get_room().values()

        # print('机房信息：',room_name)
        self.room.addItems(room_name)

    # 获取维保类型
    def get_warranty_type(self):
        # print('维保类型')
        w_type = ['未知', '原厂保', '续保']
        self.cb_type.addItems(w_type)

    # 获取是否在保内分类
    def get_under(self):
        # print('维保类型')
        under = ['未知', '在保内', '已过保']
        self.cb_is_under.addItems(under)

    # 根据查询进行查询获取数据
    def get_input_data(self):
        # 在未进行查询时，翻页按钮不可用
        self.pre_btn.setDisabled(False)  # 上一页按钮可用
        self.next_btn.setDisabled(False)  # 下一页按钮可用
        self.home_btn.setDisabled(False)  # 首页按钮可用
        self.last_btn.setDisabled(False)  # 最后一页按钮可用
        self.go_btn.setDisabled(False)  # 转到指定页可用

        # 根据条件查询设备
        sel_values = []  # 用于保存获取的查询条件列表
        sql = '''SELECT w_id, machine_id, room_name, cabinet_name, start_position, machine_name, mg_ip, bmc_ip, 
                machine_sn,start_date, end_date, organ, w_type, is_under, comment
                     FROM view_warranty  WHERE 1=1 
              '''

        # 判断并组合查询SQL
        if self.room.currentIndex() > 0:
            sql = sql + ' and room_name= %s'
            sel_values.append(self.room.currentText())
        if self.rd_mg_ip.isChecked() and self.mg_ip.text() != '':
            sql = sql + ' and mg_ip like "%%"%s"%%"'
            sel_values.append(self.mg_ip.text())
        if self.rd_bmc_ip.isChecked() and self.mg_ip.text() != '':
            sql = sql + ' and bmc_ip like "%%"%s"%%"'
            sel_values.append(self.mg_ip.text())
        if self.machine_name.text() != '':
            sql = sql + ' and machine_name like "%%"%s"%%"'
            sel_values.append(self.machine_name.text())
        if self.le_sn.text() != '':
            sql = sql + ' and machine_sn like "%%"%s"%%"'
            sel_values.append(self.le_sn.text())

        # 维保类型
        if self.cb_type.currentText() == '未知':
            sql = sql + ' and w_type= %s'
            sel_values.append('未知')
        if self.cb_type.currentText() == '原厂保':
            sql = sql + ' and w_type= %s'
            sel_values.append('原厂保')
        if self.cb_type.currentText() == '续保':
            sql = sql + ' and w_type= %s'
            sel_values.append('续保')
        # if self.cb_type.currentText() == '所有':
        #     sql = sql
        # sel_values.append(self.cb_type.currentText())
        # 是否在保内
        if self.cb_is_under.currentText() == '未知':
            sql = sql + ' and is_under= %s'
            sel_values.append('未知')
        if self.cb_is_under.currentText() == '在保内':
            sql = sql + ' and is_under= %s'
            sel_values.append('在保内')
        if self.cb_is_under.currentText() == '已过保':
            sql = sql + ' and is_under= %s'
            sel_values.append('已过保')
        # if self.cb_is_under.currentText() == '所有':
        #     sql = sql
        # sel_values.append(self.cb_type.currentText())
        self.data_sql = sql  # 获取按条件查询的sql语句
        self.select_values = sel_values  # 获取查询条件值
        # print('查询条件',self.select_values)
        # print('查询SQL',self.data_sql)
        if not self.select_values:
            self.recordQuery(self.data_sql, [0])
        else:
            self.recordQuery(self.data_sql, 0, self.select_values)  # 按查询查询记录
        # print('总页数', self.totalPage)
        self.current_page = 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数

    # 获取要查询的总页数
    def page_record(self, sql, values):
        # 连接数据库并显示数据至页面
        # print('总页数条件：', values)
        # print('总页数SQL：', sql)
        data = db.execute_sql(sql, values).fetchall()  # 获取查询的数据，返回格式为一个内嵌的2元组，格式：（总记录数，数据内容）
        # data = self.db.query_single(sql, values)  # 获取查询的数据，返回格式为一个内嵌的2元组，格式：（总记录数，数据内容）
        # print('数据条数：',len(data))
        total_record = len(data)  # 查询到的数据总记录条数
        if total_record % 15 == 0:
            self.totalPage = (total_record // 15)
            self.total_page_lb.setText('总页数：{}页 共 {} 条记录'.format(self.totalPage, total_record))  # 分页显示数据
        else:
            self.totalPage = (total_record // 15) + 1
            self.total_page_lb.setText('总页数：{}页 共 {} 条记录'.format(self.totalPage, total_record))  # 分页显示数据
        # print('总页数',self.totalPage)
        return self.totalPage

    # 定义查询记录并显示数据
    def recordQuery(self, sql, limiIndex, sql_args=None):
        """
        定义查询记录并显示数据
        :param sql:     不带分页功能的查询语句
        :param limiIndex:   sql索引记录开始点
        :param sql_args:    传入sql的参数
        :return:
        """
        sql_page = sql + ' limit %s,15 '  # 定义分页查询SQL
        # print('sql_page：：',sql_page)
        # print('limiIndex',limiIndex)

        if sql_args is None:
            page_data = db.execute_sql(sql_page, limiIndex).fetchall()  # 每页数据内容
            # print('查询页数据：',page_data)
            # page_data = self.db.query_single(sql_page, limiIndex)  # 每页数据内容
        else:
            sql_args.append(limiIndex)  # 将索引记录放入SQL传入的参数列表中
            # print('有参数sql_args:',sql_args)
            page_data = db.execute_sql(sql_page, sql_args).fetchall()  # 每页数据内容
            # print('查询页数据：', page_data)
            # page_data = self.db.query_single(sql_page, sql_args)  # 每页数据内容
        self.warranty_select.clearContents()  # 清除所有内容
        for i in range(len(page_data)):
            for _ in range(self.warranty_select.columnCount()):  # 表格的列数
                if page_data[i][_] is None:
                    self.warranty_select.setItem(i, _, QTableWidgetItem(''))  # 显示单元格数据
                else:
                    self.warranty_select.setItem(i, _, QTableWidgetItem(str(page_data[i][_])))  # 显示单元格数据
        # self.warranty_select.resizeColumnsToContents()  # 自适应列宽
        self.warranty_select.setColumnWidth(5, 200)  # 设备名称列宽
        self.warranty_select.setColumnWidth(6, 150)  # 带内IP列宽
        self.warranty_select.setColumnWidth(7, 150)  # bmc_ip列宽
        self.warranty_select.setColumnWidth(8, 200)  # 序列号列宽
        self.warranty_select.setColumnWidth(9, 100)  # 设备开始日期列宽
        self.warranty_select.setColumnWidth(10, 100)  # 设备结束日期列宽
        # print('self.select_values',self.select_values)
        self.page_record(self.data_sql, self.select_values[:-1])  # 显示总页数 self.select_values最除索引记录的所有参数
        self.warranty_select.resizeRowsToContents()  # 对于单元格内容过长自动换行


    # 转到指定页事件
    def goToPage(self, sql, sql_args):
        if self.page_input_le.text() != '' and int(self.page_input_le.text()) <= self.totalPage and int(
                self.page_input_le.text()) > 0:
            self.current_page = int(self.page_input_le.text())  # 获取输入的查询页数
            limiIndex = (int(self.page_input_le.text()) - 1) * 15  # 定位查询开始记录索引点
            sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
            self.recordQuery(sql, sql_args)  # 查询数据并进行显示
            self.page_input_le.setText('')
            self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
            if self.current_page == self.totalPage:
                self.pre_btn.setDisabled(False)  # 当为第一页时，按钮可用
                self.next_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
                self.home_btn.setDisabled(False)  # 当为最后一页时，按钮可用
                self.last_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
            elif self.current_page == 1:  # 当索引小于0时，设置默认当前页为第一页
                self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
                self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
                self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
                self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用
            else:
                self.pre_btn.setDisabled(False)  # 上一页按钮可用
                self.next_btn.setDisabled(False)  # 下一页按钮可用
                self.home_btn.setDisabled(False)  # 首页按钮可用
                self.last_btn.setDisabled(False)  # 最后一页按钮可用

        else:
            QtWidgets.QMessageBox.information(self, '提示', '请输入正确的跳转页数')

    # 下一页查询事件
    def nextPage(self, sql, sql_args):
        # print('self.currentPage',self.current_page)
        # print('self.totalPage',self.totalPage)
        if self.current_page < self.totalPage:
            limiIndex = self.current_page * 15  # 获取当前索引号
            sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
            # print('下一页按钮中sql_args：',sql_args)
            self.recordQuery(sql, sql_args)  # 传入值进行查询
            # print('当前页：',self.current_page)
            self.pre_btn.setDisabled(False)  # 上一页按钮可用
            self.next_btn.setDisabled(False)  # 下一页按钮可用
            self.home_btn.setDisabled(False)  # 首页按钮可用
            self.last_btn.setDisabled(False)  # 最后一页按钮可用
            # print('向后--当前页', self.currentPage)
        else:
            # print('已是最后一页')
            self.pre_btn.setDisabled(False)  # 当为第一页时，按钮可用
            self.next_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
            self.home_btn.setDisabled(False)  # 当为最后一页时，按钮可用
            self.last_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
            return
        self.current_page += 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        # print('当前页：', self.current_page)

    # 上一页查询事件
    def prePage(self, sql, sql_args):
        limiIndex = (self.current_page - 2) * 15  # 获取当前索引号
        self.current_page -= 1
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        if limiIndex >= 0:
            sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
            self.recordQuery(sql, sql_args)
            # print('向前--当前页', self.current_page)
            # print('limiIndex:',limiIndex)
            self.pre_btn.setDisabled(False)
            self.next_btn.setDisabled(False)
            self.home_btn.setDisabled(False)
            self.last_btn.setDisabled(False)
        else:
            # print('已是第一页了')
            self.current_page = 1  # 当索引小于0时，设置默认当前页为第一页
            # print('向前--当前页', self.current_page)
            self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
            self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
            self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
            self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用
            return

    # 首页查询事件
    def firstPage(self, sql, sql_args):
        limiIndex = 0  # 获取当前索引号
        sql_args.append(limiIndex)  # 将sql分页索引开始记录值添加到sql参数列表中
        self.recordQuery(sql, sql_args)
        self.current_page = 1  # 当索引小于0时，设置默认当前页为第一页
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        self.pre_btn.setDisabled(True)  # 当为第一页时，上一页按钮不可用
        self.next_btn.setDisabled(False)  # 当为第一页时，下一页按钮可用
        self.home_btn.setDisabled(True)  # 当为第一页时，首页按钮不可用
        self.last_btn.setDisabled(False)  # 当为第一页时，最后一页按钮不可用

    # 最后一页查询事件
    def lastPage(self, sql, sql_args):
        # print('最后一页',self.totalPage)
        limiindex = (self.totalPage - 1) * 15  # 获取当前索引号
        sql_args.append(limiindex)  # 将sql分页索引开始记录值添加到sql参数列表中
        self.recordQuery(sql, sql_args)
        self.current_page = self.totalPage
        self.current_page_lb.setText('当前第 {} 页'.format(self.current_page))  # 显示当前页数
        self.pre_btn.setDisabled(False)  # 当为第一页时，按钮可用
        self.next_btn.setDisabled(True)  # 当为最后一页时，按钮不可用
        self.home_btn.setDisabled(False)  # 当为最后一页时，按钮可用
        self.last_btn.setDisabled(True)  # 当为最后一页时，按钮不可用


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = UiWarrantySelect()
    mainWindow.show()
    sys.exit(app.exec())
