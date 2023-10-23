import sys
from ui.machine_switch import *
from PySide6 import QtWidgets
from db.db_orm import *
from action.pub_infos import PubSwitch


class UiSwitch(Ui_MachineSwitch, QtWidgets.QWidget):
    # 表格事件是否触发标记位
    # flag = False

    def __init__(self, parent=None):
        super(UiSwitch, self).__init__(parent)
        self.pub_infos = PubSwitch()
        self.setupUi(self)
        self.gbox_switch.hide()  # 默认进入页面隐藏位置调整窗口

        self.display_room()  # 显示机房下拉菜单内容
        self.cb_room.currentIndexChanged.connect(
            lambda: self.display_cabinet(self.cb_room, self.cb_cabinet))  # 定义机房下拉菜单触发事件
        self.display_state()  # 显示设备状态下拉菜单

        # 表格选择事件
        self.tb_display.currentCellChanged.connect(self.select_table_event)

        # 定义按钮功能
        self.bt_select.clicked.connect(self.display)  # 查询按钮功能
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容
        self.bt_switch.clicked.connect(self.switch)  # 设置位置调整按钮功能
        self.bt_sw_commit.clicked.connect(self.select_machine)  # 设置位置调整提交功能

    # 获取机房机柜信息并显示在下拉菜单中
    def display_room(self):
        room = self.pub_infos.get_room().values()
        self.cb_room.addItems(room)

    # 获取并显示机柜信息至下拉菜单中
    def display_cabinet(self, room, bt):
        cabinet = self.pub_infos.get_cabinet_infos(room.currentText())
        bt.clear()
        bt.addItem('所有')
        bt.addItems(cabinet)

    # 设置运行状态下拉菜单
    def display_state(self):
        state_items = ['所有', '运行', '断网', '关机', '下架', '未加电']
        self.cb_state.addItems(state_items)  # 查询条件的状态下拉菜单

    # 查询按钮功能，显示查询结果至页面
    def display(self):
        self.tb_display.clearContents()  # 清空表格中内容
        room = self.cb_room.currentText()  # 机房
        cabinet = self.cb_cabinet.currentText()  # 机柜
        machine_name = self.machine_name.text().strip()  # 设备名称
        sn = self.le_sn.text().strip()  # SN
        mg_ip = self.mg_ip.text().strip()  # mg_ip
        state = self.cb_state.currentText()  # 设备状态

        # # 断开表格选择事件
        # if self.flag:
        #     self.tb_display.currentCellChanged.disconnect(self.select_table_event)

        # 查询结果数据处理
        sel_values = []  # 用于保存获取的查询条件列表
        sql = """select ml.machine_id, ml.room_name,ml.cab_name, ml.start_position, ml.start_position + ml.postion_u - 1, 
        case when isnull(ml.machine_name) then '' else ml.machine_name end as machine_name,
         ml.machine_sort_name, ml.machine_factory, ml.model, 
         case when isnull(ml.machine_sn) then '' else ml.machine_sn end as machine_sn, 
         case when isnull(ml.machine_admin) then '' else ml.machine_admin end as machine_admin, 
         case when isnull(ml.mg_ip) then '' else ml.mg_ip end as mg_ip, 
         case when isnull(ml.bmc_ip) then '' else ml.bmc_ip end as bmc_ip, 
         case when isnull(ml.comments) then '' else ml.comments end as comments from machine_list ml  where 1=1 """

        # 判断查询条件
        # 判断机房是否选择
        if room != '所有':
            sql = sql + ' and room_name= %s'
            sel_values.append(room)
        # 判断机柜是否选择
        if cabinet != '所有':
            sql = sql + ' and room_name= %s and cab_name= %s '
            sel_values.append(room)
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
        # 判断运行状态是否选择
        if state != '所有':
            sql = sql + ' and run_state = %s '
            sel_values.append(state)

        # 获取按条件查询的sql语句
        select_sql = sql

        # 判断是否有输入查询条件
        if not sel_values:
            data = db.execute_sql(select_sql).fetchall()  # 按查询查询记录
        else:
            data = db.execute_sql(select_sql, sel_values).fetchall()  # 按查询查询记录
        # print(data)

        # 将查询结果显示在页面上
        data_count = len(data)
        self.lb_status.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_status.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                # 当为第一列时添加复选框按钮
                if col == 0:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
                    # self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)  # 添加复选框
                else:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        self.tb_display.resizeColumnsToContents()  # 自适应列宽

        # 隐藏变更信息区域内容
        self.select_table_event()

    # 位置调整按钮功能设置
    def switch(self):
        # 获取选择的行信息
        select_row = self.tb_display.currentRow()
        # 位置调整窗口显示的情况下功能设置
        if self.gbox_switch.isHidden() and select_row >= 0:  # 当前已选定行，并且变更信息区域隐藏
            self.gbox_switch.show()  # 显示位置调整窗口
        else:
            QtWidgets.QMessageBox.warning(self, '选择的变更设备的信息', '请选择需要调整位置的设备！')
        room = self.pub_infos.get_room().values()
        self.cb_sw_room.addItems(room)  # 显示机房信息
        # 定义机房下拉菜单触发事件
        self.cb_sw_room.currentIndexChanged.connect(
            lambda: self.display_cabinet(self.cb_sw_room, self.cb_sw_cabinet))

        # 设置上下U位下拉菜单信息
        u_info = [str(u) for u in range(1, 42)]  # 生成1-42u U位信息
        self.cb_sw_down_pos.addItems(u_info)  # 将U位信息添加到U位下拉菜单中
        self.cb_sw_up_pos.addItems(u_info)  # 将U位信息添加到U位下拉菜单中

        # 选择的行的信息
        if select_row >= 0:
            self.cb_sw_room.setCurrentText(self.tb_display.item(select_row, 1).text())  # 机房信息
            self.cb_sw_cabinet.setCurrentText(self.tb_display.item(select_row, 2).text())  # 机柜信息
            self.cb_sw_down_pos.setCurrentText(self.tb_display.item(select_row, 3).text())  # 下U位
            self.cb_sw_up_pos.setCurrentText(self.tb_display.item(select_row, 4).text())  # 上U位
            self.le_sw_machine_name.setText(self.tb_display.item(select_row, 5).text())  # 设备名称
            self.le_sw_mg_ip.setText(self.tb_display.item(select_row, 11).text())  # 管理IP
            self.le_sw_bmc_ip.setText(self.tb_display.item(select_row, 12).text())  # 带外IP
            self.te_sw_remark.setText(self.tb_display.item(select_row, 13).text())  # 备注
        else:
            pass

    # 页面表格选定时事件功能
    def select_table_event(self):
        self.gbox_switch.hide()  # 隐藏位置调整窗口

    # 调整位置提交按钮功能
    def select_machine(self):
        # 获取选择的行信息
        select_row = self.tb_display.currentRow()  # 获取表格中总行数
        # 选择的行的信息
        before_machine_id = self.tb_display.item(select_row, 0).text()  # 设备id
        before_room = self.tb_display.item(select_row, 1).text()  # 机房信息
        before_cabinet = self.tb_display.item(select_row, 2).text()  # 机柜信息
        before_pos_down = self.tb_display.item(select_row, 3).text()  # 下U位
        before_pos_up = self.tb_display.item(select_row, 4).text()  # 上U位
        before_machine_name = self.tb_display.item(select_row, 5).text()  # 设备名称
        before_mg_ip = self.tb_display.item(select_row, 11).text()  # 管理IP
        before_bmc_ip = self.tb_display.item(select_row, 12).text()  # 带外IP
        before_remark = self.tb_display.item(select_row, 13).text()  # 备注

        # 修改前原位置信息
        before_info = [self.pub_infos.room_swap_id(name=before_room), before_cabinet, before_pos_down, before_pos_up,
                       before_machine_name, before_mg_ip,
                       before_bmc_ip, before_remark]

        # 修改后位置信息
        after_info = [self.pub_infos.room_swap_id(name=self.cb_sw_room.currentText()), self.cb_sw_cabinet.currentText(),
                      self.cb_sw_down_pos.currentText(),
                      self.cb_sw_up_pos.currentText(), self.le_sw_machine_name.text().strip(),
                      self.le_sw_mg_ip.text().strip(),
                      self.le_sw_bmc_ip.text().strip(), self.te_sw_remark.toPlainText().strip()]
        # print('修改前：',before_info,'\n修改后：',after_info)

        # 数字库中字段名称
        field = ('machine_roomid', 'cabinet_name', 'start_position', 'end_position', 'machine_name', 'mg_ip',
                 'bmc_ip', 'comments')

        # 获取并判断提交数据是否修改
        if before_info == after_info:
            QtWidgets.QMessageBox.warning(self, '位置调整的设备信息', '设备信息没有改变！')
        else:
            if QtWidgets.QMessageBox.question(self, '位置调整的设备信息',
                                              '是否确定要调整该设备的位置？') == QtWidgets.QMessageBox.Yes:
                # print('开始修改！')
                try:
                    MachineInfos.update(dict(zip(field, after_info))).where(
                        MachineInfos.machine_id == before_machine_id).execute()  # 更新设备位置信息
                except Exception as e:
                    logging.critical('位置调整信息出错：'.format(e))
                else:
                    QtWidgets.QMessageBox.information(self, '位置调整的设备信息', '设备位置调整成功！')
                    self.tb_display.clearContents()  # 清空表格插件内容
                    self.gbox_switch.hide()  # 隐藏位置调整窗口

    def clear(self):
        """
        清除条件框中内容
        :return:
        """
        self.machine_name.clear()
        self.mg_ip.clear()
        self.le_sn.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    down_win = UiSwitch()
    down_win.show()
    sys.exit(app.exec())
