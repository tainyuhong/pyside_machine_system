import sys
from ui.modify import *
from PySide6 import QtWidgets
from action.pub_infos import PubSwitch  # 机房信息
from db.db_orm import *

# import logging

"""
业务判断逻辑
1、查询逻辑
    根据设备名称、MG_IP自由组合查询，包含任务一个字段就进行查询
2、修改判断逻辑
    使用了两个标志参数，save_flag、is_selected
    save_flag = True  # 判断是否有修改
    is_selected = False  # 在点击了查询按钮后设置为True，表示已经进行了查询
    + 在点击了查询按钮后，先判断查询状态，为是时，先断开信号，为否时，进入后续操作、发送单元格修改信号给槽display_changed，并将is_selected设置为True
    + 保存修改：将save_flag标志设置为True,同时将is_selected设置为未查询

"""


#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class UiModifyMachine(Ui_modify, QtWidgets.QWidget):
    is_selected = False  # 是否再次查询

    def __init__(self, parent=None):
        super(UiModifyMachine, self).__init__(parent)
        self.room = PubSwitch()  # 创建机房对象
        self.room_name = self.room.get_room()  # 获取机房名称信息
        self.setupUi(self)
        self.modify_data = []  # 暂存修改数据元素及值
        self.get_room()  # 获取机房信息并显示至下拉菜单中
        self.cb_room.currentTextChanged.connect(self.get_cabinet)  # 通过机房信息下拉菜单触发机柜信息变化

        # 定义按钮功能
        self.bt_select.clicked.connect(self.select)  # 查询内容
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容
        self.bt_modify.clicked.connect(self.open_modify)  # 进入修改状态
        self.bt_save.clicked.connect(self.submit_modify)  # 保存修改

    # 获取机房信息并显示到下拉菜单中
    def get_room(self):
        self.cb_room.addItems(self.room_name.values())

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
        # print('选择的机房：{}设备名称：{}  IP: {}'.format(room_name, machine_name, mg_ip))
        # print('是否保存的状态：', self.save_flag)
        # 判断是否进行过一次查询
        if self.is_selected:
            # print('断开信号---')
            self.tb_display.itemChanged.disconnect(self.display_changed)  # 启用单元格式信号
        else:
            # print('不断开信号')
            pass

        # 不带条件的查询
        query = MachineInfos.select(MachineInfos.machine_id, MachineInfos.machine_roomid, MachineInfos.cabinet_name,
                                    MachineInfos.start_position, MachineInfos.end_position, MachineInfos.machine_name,
                                    MachineInfos.machine_sort_name, MachineInfos.machine_factory, MachineInfos.model,
                                    MachineInfos.machine_sn, MachineInfos.factory_date, MachineInfos.end_ma_date,
                                    MachineInfos.work_are, MachineInfos.run_state,MachineInfos.machine_admin, MachineInfos.app_admin,
                                    MachineInfos.mg_ip, MachineInfos.app_ip1, MachineInfos.bmc_ip,
                                    MachineInfos.asset_id, MachineInfos.comments)

        cond_cabinet = MachineInfos.cabinet_name == cabinet
        cond_machine_name = MachineInfos.machine_name.contains(machine_name)

        # 根据选择的带外IP还是带内IP选择相应的查询条件
        if self.rd_mg_ip.isChecked():
            cond_ip = MachineInfos.mg_ip.contains(mg_ip)    # 带内IP
        else:
            cond_ip = MachineInfos.bmc_ip.contains(mg_ip)   #带外IP

        # 根据选择条件进行查询
        # 选择机房为所有
        if room_name == '所有':
            if machine_name != '' and mg_ip == '':
                query_condition = cond_machine_name
            elif machine_name != '' and mg_ip != '':
                query_condition = cond_machine_name & cond_ip
            elif machine_name == '':
                query_condition = cond_ip
        # 选择机房对应机房，机柜为所有
        elif room_name != '所有' and cabinet == '所有':
            cond_room = MachineInfos.machine_roomid == self.room.room_swap_id(name=room_name)
            if machine_name != '' and mg_ip == '':
                query_condition = cond_room & cond_machine_name
            elif machine_name != '' and mg_ip != '':
                query_condition = cond_room & cond_machine_name & cond_ip
            elif machine_name == '':
                query_condition = cond_room & cond_ip
        # 选择机房对应机房，机柜为对应机柜
        else:
            cond_room = MachineInfos.machine_roomid == self.room.room_swap_id(name=room_name)
            if machine_name != '' and mg_ip == '':
                query_condition = cond_room & cond_cabinet & cond_machine_name
            elif machine_name != '' and mg_ip != '':
                query_condition = cond_room & cond_cabinet & cond_machine_name & cond_ip
            elif machine_name == '':
                query_condition = cond_room & cond_cabinet & cond_ip

        # 进行查询
        # print('查询SQL:', query.where(condition).sql())
        # 查询并获取结果
        result = [i for i in query.where(query_condition).tuples()]
        # print('查询结果：', result)
        data_count = len(result)
        self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_status.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        self.tb_display.clearContents()
        # 将查询结果显示在表格控件中
        for row, d1 in enumerate(result):
            # print('每一行数据：',d1)
            for col, d2 in enumerate(d1):
                # # 添加机房下拉菜控件
                # cb = QComboBox()
                # cb.addItems(self.room_name.values())
                if col == 0:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(result[row][col])))
                    self.tb_display.item(row, 0).setFlags(Qt.ItemIsEnabled)  # 第一列设置为不可编辑
                if col == 1:
                    self.tb_display.setItem(row, col, QTableWidgetItem(self.room.room_swap_id(room_id=d2)))
                    # cb.setCurrentText(self.room.room_swap_id(room_id=d2))  # 将机房ID转换为机房名称并设置为当前选择项
                    # cb.setDisabled(True)    # 设置下拉菜单不可编辑
                    # self.tb_display.setCellWidget(row, 1, cb)  # 将机房下拉菜单添加到表格对应位置
                else:
                    if d2 is None:
                        self.tb_display.setItem(row, col, QTableWidgetItem(''))
                    else:
                        self.tb_display.setItem(row, col, QTableWidgetItem(str(result[row][col])))
        self.tb_display.resizeColumnsToContents()   # 自适应列宽
        self.tb_display.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tb_display.setToolTip('业务类型：1生产,2电渠,3灾备,4开发,5备份,6分行\n\r运行状态:1运行,2断网,3关机,4下架,5未加电')

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
        self.tb_display.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)     # 允许编辑
        self.tb_display.itemChanged.connect(self.display_changed)  # 启用单元格式信号
        # 机房列下拉菜单设置为可修改
        # self.tb_display.widget.connect(self.modify_room)

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
                          'model', 'machine_sn', 'factory_date', 'end_ma_date', 'work_are','run_state',
                          'machine_admin', 'app_admin', 'mg_ip', 'app_ip1', 'bmc_ip', 'asset_id', 'comments')
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
        # 判断要修改的数据是否存在
        if len(self.modify_data) > 0:
            # 获取到的修改数据的格式
            # [{'machine_id': '5556', 'end_position': '15'}, {'machine_id': '5556', 'app_admin': '吴'}]
            count = 0
            # 遍历修改内容列表，并提交至数据库中
            for item in self.modify_data:
                if 'machine_roomid' in item.keys():
                    item['machine_roomid']=self.room.room_swap_id(name=item['machine_roomid'])
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiModifyMachine()
    add_win.show()
    sys.exit(app.exec())
