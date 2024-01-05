import sys
from ui.modify import *
from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtGui import QFontMetrics
from action.pub_infos import PubSwitch  # 机房信息
from db.db_orm import *

# import logging

"""
业务判断逻辑
1、查询逻辑
    根据设备名称、MG_IP自由组合查询，包含任务一个字段就进行查询
2、修改判断逻辑
    使用了一个标志参数，is_selected
    is_selected = False  # 在点击了查询按钮后设置为True，表示已经进行了查询
    + 在点击了【查询】按钮后，先判断查询状态，为是时，先断开信号，为否时，跳过，进入后续操作(序列号有输入时，只按序列号里德查询)
    + 点击修【改按】钮发送单元格修改信号给槽display_changed，在点击了修改按钮后设置为不可用，避免重复点击修改按钮，在保存完或重新查询时激活修改按钮
    + 保存修改：self.modify_data = []  # 置空暂存列表数据 ，同时将is_selected设置为未查询
"""


class UiModifyMachine(QtWidgets.QWidget, Ui_modify):
    is_selected = False  # 是否再次查询

    def __init__(self, parent=None):
        super(UiModifyMachine, self).__init__(parent)
        self.setupUi(self)  # 初始化窗口
        self.set_table_info()  # 初始化表格参数信息
        self.room = PubSwitch()  # 创建机房对象
        self.room_name = self.room.get_room()  # 获取机房名称信息

        self.modify_data = []  # 暂存修改数据元素及值
        self.get_room()  # 获取机房信息并显示至下拉菜单中
        self.get_machine_sort()  # 显示设备分类信息
        self.cb_room.currentTextChanged.connect(self.get_cabinet)  # 通过机房信息下拉菜单触发机柜信息变化

        # 定义按钮功能
        self.bt_select.clicked.connect(self.select)  # 查询内容
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容
        self.bt_modify.clicked.connect(self.open_modify)  # 进入修改状态
        self.bt_save.clicked.connect(self.submit_modify)  # 保存修改

    # 定义表格表头及各列宽度
    def set_table_info(self):
        table_info = {'设备ID': 50, '机房': 50, '机柜': 50, '下U位': 50, '上U位': 50, '设备名称': 180, '设备分类': 100,
                      '设备厂商': 100, '设备型号': 100, '序列号': 170, '管理IP': 100, 'BMC IP': 100, '应用IP': 100,
                      '业务类型': 80, '运行状态': 80, '负责人': 80, '应用管理员': 80, '出厂日期': 100, '到保日期': 100,
                      '资产编号': 100, '备注': 150}
        # 设置表格表头信息
        self.tb_display.setHorizontalHeaderLabels(table_info.keys())

        # 设置指定列的列宽
        for num, width in enumerate(table_info.values()):
            self.tb_display.setColumnWidth(num, width)  # 设置指定列的列宽

    # 获取机房信息并显示到下拉菜单中
    def get_room(self):
        self.cb_room.addItems(self.room_name.values())

    # 获取设备分类信息并添加至下拉菜单中
    def get_machine_sort(self):
        data_model = MachineSort.select(MachineSort.sort_name).where(MachineSort.part_sort.is_null(False)).order_by(
            MachineSort.sort_id)
        sort = [i.sort_name for i in data_model]
        self.cb_sort.addItem('所有')
        self.cb_sort.addItems(sort)  # 添加设备分类下拉菜单信息
        # print(sort)

    # 获取机柜信息并显示到下拉菜单中
    def get_cabinet(self):
        # 通过选择机房获取机柜相应信息
        cabinet_name = self.room.get_cabinet_infos(self.cb_room.currentText())
        # print('机房信息：',cabinet_name)
        self.cb_cabinet.clear()
        self.cb_cabinet.addItem('所有')
        self.cb_cabinet.addItems(cabinet_name)

    # 查询需要修改的内容
    def select(self):
        room_name = self.cb_room.currentText()  # 选择的机房
        cabinet = self.cb_cabinet.currentText()  # 选择的机柜
        machine_name = self.machine_name.text().strip()  # 输入的设备名称
        mg_ip = self.mg_ip.text().strip()  # 输入的IP
        sn = self.le_sn.text().strip()  # 输入的序列号
        sort_name = self.cb_sort.currentText()  # 选择的分类
        # print('选择的机房：{}设备名称：{}  IP: {} SN: {}|'.format(room_name, machine_name, mg_ip,sn))
        # print('是否保存的状态：', self.save_flag)
        # 判断是否进行过一次查询
        if self.is_selected:
            # print('断开信号---')
            self.tb_display.itemChanged.disconnect(self.display_changed)  # 启用单元格式信号
            self.is_selected = False  # 修改标记为false,未查询
        else:
            # print('不断开信号')
            pass
        # 按条件进行查询
        sel_values = []  # 用于保存获取的查询条件列表
        sql = """select `t1`.`machine_id`, `t1`.`machine_roomid`, `t1`.`cabinet_name`, `t1`.`start_position`,
                        `t1`.`end_position`, `t1`.`machine_name`, `t1`.`machine_sort_name`, `t1`.`machine_factory`,
                        `t1`.`model`, `t1`.`machine_sn`, `t1`.`mg_ip`, `t1`.`bmc_ip`, `t1`.`app_ip1`, `t1`.`work_are`,
                        `t1`.`run_state`, `t1`.`machine_admin`, `t1`.`app_admin`, `t1`.`factory_date`,
                         `t1`.`end_ma_date`, `t1`.`asset_id`, `t1`.`comments`
                        from `machine_infos` as `t1`  where 1=1 """
        # 判断机房是否选择
        if room_name != '所有':
            sql = sql + ' and machine_roomid= %s '
            sel_values.append(self.room.room_swap_id(name=room_name))
        # 判断机柜是否选择
        if cabinet != '所有':
            sql = sql + '  and cabinet_name= %s '
            # sel_values.append(self.room.room_swap_id(name=room_name))
            sel_values.append(cabinet)
        # 判断管理IP是否选择
        if self.rd_mg_ip.isChecked() and self.mg_ip.text() != '':
            sql = sql + ' and mg_ip like "%%"%s"%%"'
            sel_values.append(mg_ip)
        # 判断BMC IP是否选择
        if self.rd_bmc_ip.isChecked() and self.mg_ip.text() != '':
            sql = sql + ' and bmc_ip like "%%"%s"%%"'
            sel_values.append(mg_ip)
        # 判断设备名称是否输入
        if machine_name != '':
            sql = sql + ' and machine_name like "%%"%s"%%"'
            sel_values.append(machine_name)
        # 判断SN 是否输入
        if sn != '':
            sql = sql + ' and machine_sn like "%%"%s"%%" '
            sel_values.append(sn)
        # 判断是否选择设备分类
        if sort_name != '所有':
            sql = sql + ' and machine_sort_name =%s'
            sel_values.append(sort_name)

        # 判断是否钩选已下架
        if self.ck_is_down.isChecked():
            sql = sql + ' and run_state = 4 '
        else:
            sql = sql + ' and run_state != 4 '

        # 获取按条件查询的sql语句
        select_sql = sql + 'order by `t1`.`machine_roomid`, `t1`.`cabinet_name`, `t1`.`start_position` desc'
        # print('sql',select_sql,'sel_values',sel_values)
        # # 执行sql，获取查询结果 判断是否有输入查询条件
        if not sel_values:
            result = db.execute_sql(select_sql).fetchall()  # 按查询查询记录
        else:
            result = db.execute_sql(select_sql, sel_values).fetchall()  # 按查询查询记录

        # print('查询结果：', result)
        data_count = len(result)
        self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_status.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        self.tb_display.clearContents()
        # 将查询结果显示在表格控件中
        for row, d1 in enumerate(result):
            for col, d2 in enumerate(d1):
                # # 添加机房下拉菜控件
                if col == 1:
                    self.tb_display.setItem(row, col, QTableWidgetItem(self.room.room_swap_id(room_id=d2)))
                    # cb.setCurrentText(self.room.room_swap_id(room_id=d2))  # 将机房ID转换为机房名称并设置为当前选择项

                else:
                    if d2 is None:
                        self.tb_display.setItem(row, col, QTableWidgetItem(''))
                    else:
                        self.tb_display.setItem(row, col, QTableWidgetItem(str(result[row][col])))
        self.tb_display.resizeRowsToContents()  # 自适应行高,根据内容自动换行

        self.tb_display.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 设置表格为不可修改状态
        self.tb_display.setToolTip(
            '业务类型：1生产,2电渠,3灾备,4开发,5备份,6分行\n\r运行状态:1运行,2断网,3关机,4下架,5未加电')

        # 激活修改按钮
        self.bt_modify.setDisabled(False)
        # 置空暂存列表数据
        self.modify_data = []

    def clear(self):
        """
        清除条件框中内容
        :return:
        """
        self.cb_room.setCurrentIndex(0)
        self.cb_cabinet.setCurrentIndex(0)
        self.machine_name.clear()
        self.mg_ip.clear()
        self.rd_mg_ip.setChecked(True)

    # 进入修改状态
    def open_modify(self):
        self.is_selected = True
        self.modify_data = []  # 置空暂存列表数据
        self.tb_display.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)  # 允许编辑

        # 使用委托，设置第1-3列不可编辑,控制设备类型一列
        self.tb_display.setItemDelegate(ColumnEditDelegate(self))

        self.tb_display.itemChanged.connect(self.display_changed)  # 启用单元格式信号
        # 在点击了修改按钮后设置为不可用，避免重复点击修改按钮
        self.bt_modify.setDisabled(True)

    def display_changed(self):
        """
        获取变更的内容，并将数据保存到modify_data列表中
        :return:
        """
        changed_item = self.tb_display.currentItem()  # 获取当前修改的单元格信息
        if changed_item:
            item_row = changed_item.row()  # 所在行
            item_col = changed_item.column()  # 所在列
            item_name = changed_item.text()  # 修改后项的值
            machine_id = self.tb_display.item(item_row, 0).text()  # 修改数据所属的设备id
            # print('修改后的内容：', item_row, item_col, item_name, machine_id)
            # 表中字段列表
            table_list = ('machine_id', 'machine_roomid', 'cabinet_name', 'start_position',
                          'end_position', 'machine_name', 'machine_sort_name', 'machine_factory',
                          'model', 'machine_sn', 'mg_ip', 'bmc_ip', 'app_ip1', 'work_are', 'run_state',
                          'machine_admin', 'app_admin', 'factory_date', 'end_ma_date', 'asset_id', 'comments')
            # 将修改字段添加到修改数据列表中
            self.modify_data.append({'machine_id': machine_id, table_list[item_col]: item_name})
            # table_list[item_col]:item_name 数据库中要修改的字段名，对应修改后的值
            # print('要修改的数据集',self.modify_data)
        else:
            pass

    def submit_modify(self):
        """
        提交修改内容至数据库中
        :return:
        """
        # 激活修改按钮
        self.bt_modify.setDisabled(False)
        # 设置表格为不可修改状态
        self.tb_display.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        # print('是否有要修改的数据：', self.modify_data)
        # 判断要修改的数据是否存在
        if len(self.modify_data) > 0:
            # 获取到的修改数据的格式
            # [{'machine_id': '5556', 'end_position': '15'}, {'machine_id': '5556', 'app_admin': '吴'}]
            count = 0
            # 遍历修改内容列表，并提交至数据库中
            for item in self.modify_data:
                if 'machine_roomid' in item.keys():
                    item['machine_roomid'] = self.room.room_swap_id(name=item['machine_roomid'])
                else:
                    pass
                try:
                    result = MachineInfos.update(item).where(
                        MachineInfos.machine_id == item.get('machine_id')).execute()
                    # print(result)
                except Exception as e:
                    logging.critical('数据保存失败，错误：'.format(e))
                    QtWidgets.QMessageBox.critical(self, '数据保存失败', '错误：{}'.format(e))
                else:
                    if result == 0:
                        QtWidgets.QMessageBox.critical(self, '数据修改失败', '修改失败！')
                    else:
                        logging.info('----> 成功修改 设备编号为 {} 的信息<---'.format(item.get('machine_id')))
                        count += 1

            QtWidgets.QMessageBox.information(self, '修改设备', '成功修改【 {} 】处设备信息！'.format(count))
            self.modify_data = []  # 置空暂存列表数据
            self.is_selected = False  # 设置为未查询过
            self.tb_display.itemChanged.disconnect(self.display_changed)  # 断开信号
        else:
            QtWidgets.QMessageBox.warning(self, '修改设备', '没有数据需要保存！')


# 创建一个1-3列不可编辑的委托,创建设备类型列的委托
class ColumnEditDelegate(QtWidgets.QStyledItemDelegate):
    """
    创建一个1-3列不可编辑的委托,创建设备类型列的委托
    """

    def __init__(self, parent=None):
        super(ColumnEditDelegate, self).__init__(parent)

    def createEditor(self, parent, option, index):
        data_model = MachineSort.select(MachineSort.sort_name).where(MachineSort.part_sort.is_null(False)).order_by(
            MachineSort.sort_id)
        sort = [i.sort_name for i in data_model]
        if index.column() == 6:
            editor = QtWidgets.QComboBox(parent)
            editor.addItems(sort)
            return editor
        elif index.column() not in (0, 1, 2):
            return super(ColumnEditDelegate, self).createEditor(parent, option, index)
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiModifyMachine()
    add_win.show()
    sys.exit(app.exec())
