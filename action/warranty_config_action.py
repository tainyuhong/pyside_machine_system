import sys
from ui.warranty_config import Ui_WarrantyConfig, QTableWidgetItem
from PySide6 import QtWidgets, QtCore,QtGui
from db.db_orm import Organization, MachineSort, MachineList, WarrantyInfos, db, log
from action.pub_infos import PubSwitch


class WarrantyConfig(QtWidgets.QWidget, Ui_WarrantyConfig):
    def __init__(self, parent=None):
        super(WarrantyConfig, self).__init__(parent)
        self.setupUi(self)
        self.pub_infos = PubSwitch()
        self.set_wide()  # 调用表格列设置宽度
        self.set_time()  # 设置默认维保信息

        self.sql_join = []
        self.sql = {}  # 用于保存获取的查询条件拼接字段 字典

        self.display_room()  # 显示机房下拉菜单内容
        self.display_sort()  # 显示分类信息
        self.cb_room.currentIndexChanged.connect(self.display_cabinet)  # 定义机房下拉菜单触发事件
        self.get_organization()  # 显示厂商信息

        # 查询按钮事件
        self.bt_select.clicked.connect(self.display)

        # 全选按钮事件
        self.bt_select_all.clicked.connect(self.select_all)

        # 提交按钮事件
        self.bt_commit.clicked.connect(self.commit)

    # 设置表格各列的宽度
    def set_wide(self):
        """
        设置表格各列的宽度
        :return:
        """
        self.tb_display.setColumnWidth(0, 70)
        self.tb_display.setColumnWidth(1, 50)
        self.tb_display.setColumnWidth(2, 50)
        self.tb_display.setColumnWidth(3, 50)
        self.tb_display.setColumnWidth(4, 50)
        self.tb_display.setColumnWidth(5, 200)
        self.tb_display.setColumnWidth(6, 70)
        self.tb_display.setColumnWidth(7, 70)
        self.tb_display.setColumnWidth(8, 100)
        self.tb_display.setColumnWidth(9, 180)
        self.tb_display.setColumnWidth(10, 80)
        self.tb_display.setColumnWidth(11, 120)
        self.tb_display.setColumnWidth(12, 120)
        self.tb_display.setColumnWidth(13, 150)

    # 获取机房机柜信息并显示在下拉菜单中
    def display_room(self):
        room = self.pub_infos.get_room().values()
        self.cb_room.addItems(room)

    # 获取并显示机柜信息至下拉菜单中
    def display_cabinet(self):
        cabinet = self.pub_infos.get_cabinet_infos(self.cb_room.currentText())
        self.cb_cabinet.clear()
        self.cb_cabinet.addItem('所有')
        self.cb_cabinet.addItems(cabinet)

    # 获取设备分类信息
    def display_sort(self):
        sort_model = MachineSort.select(MachineSort.sort_name).where(MachineSort.part_sort_name.is_null(False)).tuples()
        sort_data = [sort[0] for sort in sort_model]
        # print('分类信息：',sort_data)
        self.cb_sort.clear()
        self.cb_sort.addItem('所有')
        self.cb_sort.addItems(sort_data)

    # 获取厂商信息
    def get_organization(self):
        data_model = Organization.select(Organization.org_name).tuples()
        data = [i[0] for i in data_model]
        # print('单位数据：', data)
        self.cb_org.addItem('')
        self.cb_org.addItems(data)

    # 设置默认的维保时间范围
    def set_time(self):
        self.dt_start.setDate(QtCore.QDate.currentDate())
        # 在设置了开始时间后结束时间默认增加12个月
        self.dt_end.setDate(QtCore.QDate.currentDate().addYears(1))

    # 显示查询结果至页面
    def display(self):
        self.tb_display.clearContents()  # 清空表格中内容
        self.tb_display.scrollToTop()  # 将滚动条滚动到顶端
        self.sql_join = []  # 置空，保证每次重新获取新的查询条件

        # 判断查询条件并拼接
        self.get_room()  # 判断是否选择机房
        self.get_cabinet()  # 判断是否选择机柜
        self.get_sort()  # 判断是否选择设备分类
        self.get_machine_name()  # 判断是否选输入设备名称
        self.get_ip()  # 判断是否输入设备IP
        self.get_machine_sn()  # 判断是否输入设备序列号

        # 获取查询结果
        # 定义查询语句
        query = MachineList.select(MachineList.machine_id, MachineList.room_name, MachineList.cab_name,
                                   MachineList.start_position, MachineList.postion_u, MachineList.machine_name,
                                   MachineList.machine_sort_name, MachineList.machine_factory, MachineList.model,
                                   MachineList.machine_sn, MachineList.machine_admin, MachineList.mg_ip,
                                   MachineList.bmc_ip, MachineList.organ, MachineList.is_under, MachineList.comments)

        temp = [key == value for key, value in self.sql.items()]
        # 当拼接sql不为空时，按条件进行查询
        self.sql_join = self.sql_join + temp
        if self.sql_join:
            data_model = query.where(*self.sql_join).tuples()
            # print('data_model',data_model)
        else:
            # 当拼接sql没有输入条件时，查询所有
            data_model = query.tuples()

        data = [i for i in data_model.tuples()]  # 以元组的方式显示数据
        # print('data:',data)
        # 将查询结果显示在页面上
        data_count = len(data)
        self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_status.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                item_data = QTableWidgetItem(str(data[row][col]))
                # 当为第一列时添加复选框按钮
                if col == 0:
                    self.tb_display.setItem(row, col, item_data)
                    self.tb_display.item(row, 0).setCheckState(QtCore.Qt.CheckState.Unchecked)  # 添加复选框
                if col == 14:
                    if item_data.text() == '保内':
                        item_data.setBackground(QtGui.QColor(50, 205, 50))  # 设置单元格背景颜色
                        self.tb_display.setItem(row, col, item_data)
                    elif item_data == '过保':
                        item_data.setBackground(QtGui.QColor(255, 182, 193))  # 设置单元格背景颜色
                        self.tb_display.setItem(row, col, item_data)
                    else:
                        self.tb_display.setItem(row, col, item_data)

                else:
                    # 将查询的数据中None字段，显示为空字符''
                    # print(data[row][col])
                    if data[row][col] is None:
                        self.tb_display.setItem(row, col, QTableWidgetItem(''))
                    else:
                        self.tb_display.setItem(row, col, item_data)


        # self.tb_display.resizeColumnsToContents()  # 自适应列宽
        self.tb_display.resizeRowsToContents()  # 对于单元格内容过长自动换行

    # 获取查询条件--机房
    def get_room(self):
        """
        拼接机房SQL
        :return:
        """
        if self.cb_room.currentText() != '所有':
            self.sql[MachineList.room_name] = self.cb_room.currentText()
        else:
            if MachineList.room_name in self.sql:
                self.sql.pop(MachineList.room_name)

    # 获取查询条件--机柜
    def get_cabinet(self):
        """
        拼接机柜SQL
        :return:
        """
        if self.cb_cabinet.currentText() != '所有':
            self.sql[MachineList.cab_name] = self.cb_cabinet.currentText()
        else:
            if MachineList.cab_name in self.sql:
                self.sql.pop(MachineList.cab_name)  # 移除

    # 获取查询条件--设备分类
    def get_sort(self):
        """
        拼接设备分类 模糊查询 SQL
        :return:
        """
        if self.cb_sort.currentText() != '所有':
            self.sql[MachineList.machine_sort_name] = self.cb_sort.currentText()
        else:
            if MachineList.machine_sort_name in self.sql:
                self.sql.pop(MachineList.machine_sort_name)

    # 获取查询条件--设备名称
    def get_machine_name(self):
        """
        拼接设备名称 模糊查询SQL
        :return:
        """
        if self.le_machine_name.text().strip() != '':
            self.sql_join.append(MachineList.machine_name.contains(self.le_machine_name.text().strip()))
            # print('模糊查询后：', self.sql_join)
        else:
            pass

    # 获取查询条件--设备ip
    def get_ip(self):
        """
        拼接设备IP模糊查询  SQL
        :return:
        """
        if self.le_ip.text().strip() != '':
            if self.rd_mg_ip.isChecked():
                self.sql_join.append(MachineList.mg_ip.contains(self.le_ip.text().strip()))
                # self.sql[MachineList.mg_ip] = self.le_ip.text().strip()
            else:
                self.sql_join.append(MachineList.bmc_ip.contains(self.le_ip.text().strip()))
                # self.sql[MachineList.bmc_ip] = self.le_ip.text().strip()
        else:
            pass

    # 获取查询条件--设备序列号
    def get_machine_sn(self):
        if self.le_sn.text().strip() != '':
            self.sql_join.append(MachineList.machine_sn.contains(self.le_sn.text().strip()))
        else:
            pass

    # 全选按钮
    def select_all(self):
        row_count = self.tb_display.rowCount()  # 总行数

        for row in range(row_count):
            item = self.tb_display.item(row, 0)
            if item is not None and item.checkState() != QtCore.Qt.CheckState.Checked:
                # 全部选择
                item.setCheckState(QtCore.Qt.CheckState.Checked)
            elif item is not None and item.checkState() == QtCore.Qt.CheckState.Checked:
                # 全部取消
                item.setCheckState(QtCore.Qt.CheckState.Unchecked)
            else:
                pass

    # # 对维保情况设置颜色
    # def set_color(self):
    #     items = []  #
    #     row_count = self.tb_display.rowCount()  # 总行数
    #     for row in range(row_count):
    #         item = self.tb_display.item(row, 0)
    #         items.append(item.text())
    #     print('items', items)

    def commit(self):
        """
        提交维保信息配置
        :return:
        """
        # 判断是否选择维保单位
        if self.cb_org.currentIndex() != 0:

            # 获取选择设备
            selected_item = []  # 选择的设备
            row_count = self.tb_display.rowCount()  # 总行数
            for row in range(row_count):
                item = self.tb_display.item(row, 0)
                # 将钩选状态的设备 加到选择的selected_item列表中
                if item is not None and item.checkState() == QtCore.Qt.CheckState.Checked:
                    selected_item.append((item.text(), self.cb_org.currentText(),
                                          self.dt_start.text(),
                                          self.dt_end.text(), 2, 1))  # 2:表示续保，1：表示维保期内
                else:
                    pass

            print('selected_item', selected_item)
            log.debug('selected_item')

            # 判断是否有选择设备
            if len(selected_item) > 0:

                # 判断是否确定提交，添加到数据库中
                if QtWidgets.QMessageBox.question(self, '维保信息配置',
                                                  '确认要配置选择的设备吗？') == QtWidgets.QMessageBox.StandardButton.Yes:
                    log.debug('提交维保配置信息')
                    # 保存至数据库
                    with db.atomic():
                        try:
                            WarrantyInfos.insert_many(selected_item, fields=[WarrantyInfos.machine, WarrantyInfos.organ,
                                                                             WarrantyInfos.start_date,
                                                                             WarrantyInfos.end_date,
                                                                             WarrantyInfos.w_type,
                                                                             WarrantyInfos.is_under]).execute()
                        except Exception as e:
                            print('数据提交错误：', e)
                        else:
                            print('维保信息配置成功！')
                            QtWidgets.QMessageBox.information(self, '维保信息配置', '配置成功！')

            else:
                QtWidgets.QMessageBox.warning(self, '维保信息配置', '请钩选需要配置的设备，再提交！')

        else:
            QtWidgets.QMessageBox.warning(self, '维保信息配置', '请选择维保单位再进行提交！')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    warranty_config_win = WarrantyConfig()
    warranty_config_win.show()
    sys.exit(app.exec())
