import sys
from ui.down_shelf import *
from PySide6 import QtWidgets
from db.db_orm import *
from action.pub_infos import PubSwitch


class UiDownShelf(Ui_down_shelf, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(UiDownShelf, self).__init__(parent)
        self.pub_infos = PubSwitch()
        self.setupUi(self)
        # 隐藏执行人及时间控件
        self.lb_operator.hide()
        self.le_down_operator.hide()
        self.lb_datetime.hide()
        self.down_time.hide()

        self.display_room()  # 显示机房下拉菜单内容
        self.cb_room.currentIndexChanged.connect(self.display_cabinet)  # 定义机房下拉菜单触发事件
        self.display_state()  # 显示设备状态下拉菜单

        # 定义按钮功能
        self.bt_select.clicked.connect(self.display)  # 查询内容
        self.bt_clear.clicked.connect(self.clear)  # 清空条件框内容

        # 设置下架时间默认为系统当天
        self.down_time.setDate(QDate.currentDate())  # 设置默认为系统当天
        self.bt_donw_shelf.clicked.connect(self.select_machine)  # 设置为下架状态

        # 处理方式下拉菜单选择事件触发
        self.cb_operate_state.currentTextChanged.connect(self.choose_operation)

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

    # 设置运行状态下拉菜单
    def display_state(self):
        state_items = ['所有', '运行', '断网', '关机', '下架', '未加电']
        self.cb_state.addItems(state_items)  # 查询条件的状态下拉菜单
        self.cb_operate_state.addItems(state_items[1:])  # 执行方式选择下拉菜单

    # 显示查询结果至页面
    def display(self):
        self.tb_display.clearContents()  # 清空表格中内容
        room = self.cb_room.currentText()  # 机房
        cabinet = self.cb_cabinet.currentText()  # 机柜
        machine_name = self.machine_name.text().strip()  # 设备名称
        sn = self.le_sn.text().strip()  # SN
        mg_ip = self.mg_ip.text().strip()  # mg_ip
        state = self.cb_state.currentText()  # 设备状态

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
                    self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)  # 添加复选框，且不选择状态
                else:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        self.tb_display.resizeColumnsToContents()  # 自适应列宽

    # 处理方式选择事件判断
    def choose_operation(self):
        if self.cb_operate_state.currentText() == '下架':
            # 显示执行人及时间控件
            self.lb_operator.show()
            self.le_down_operator.show()
            self.lb_datetime.show()
            self.down_time.show()
        else:
            # 隐藏执行人及时间控件
            self.lb_operator.hide()
            self.le_down_operator.hide()
            self.lb_datetime.hide()
            self.down_time.hide()

    # 下架操作---钩选的要下架的设备
    def select_machine(self):
        # 获取选择的行信息
        rowcount = self.tb_display.rowCount()  # 获取表格中总行数
        select_data = []  # 定义钩选的设备列表

        # 遍历所有行的第一列，将钩选的设备ID添加到select_data设备列表中
        for i in range(rowcount):
            select_row = self.tb_display.item(i, 0)  # 每行的第一列
            if select_row is not None:
                if select_row.checkState() == Qt.Checked:  # 判断是否钩选
                    # print('设备id:', select_row.text())
                    select_data.append(select_row.text())
                else:
                    pass
            else:
                pass

        # 获取并提交数据
        if len(select_data) == 0:
            QtWidgets.QMessageBox.warning(self, '设备下线下架操作', '请选择要执行操作的设备！')
        else:
            # 判断选择的执行方式
            choose = self.cb_operate_state.currentText()

            # 获取钩选的设备是否存在于下架设备信息表中
            down_data = [down[0] for down in ViewDownshelf.select(ViewDownshelf.machine_id).where(
                ViewDownshelf.machine_id in select_data).tuples()]
            # print('下架信息表：', down_data)
            # 选择下架操作
            if choose == '下架':
                # 获取输入的下架信息
                comments = self.comments.toPlainText().strip()  # 下架情况说明
                operator = self.le_down_operator.text().strip()  # 下架执行人
                down_time = self.down_time.date().toString('yyyy/M/d')  # 下架时间
                if comments == '' or operator == '':
                    QtWidgets.QMessageBox.warning(self, '设备下架操作', '请填写下架情况说明和执行人员！')
                else:
                    # print('选择的设备：', select_data)
                    if QtWidgets.QMessageBox.question(self, '设备下架',
                                                      '是否确认要下架选择的设备？') == QtWidgets.QMessageBox.Yes:
                        # 按格式生成下架数据（machine_id,up_or_down,operator, down_time, comments）
                        for _ in select_data:
                            # 判断是否存在于已下架设备表中，如果是则更新相关信息
                            if int(_) in down_data:
                                # print('在下架设备表中。')
                                try:
                                    with db.atomic():
                                        ShelfManage.update(up_or_down=4, operator=operator, date=down_time,
                                                           comments=comments).where(
                                            ShelfManage.machine_id == _).execute()  # 插入下架设备信息到下架表中
                                        MachineInfos.update(run_state=4, uninstall_date=down_time).where(
                                            MachineInfos.machine_id == _).execute()  # 修改设备表运行状态为下架
                                except Exception as e:
                                    logging.critical('执行下架出错：'.format(e))
                                # else:
                                #     QtWidgets.QMessageBox.information(self, '设备下架成功', '成功下架设备！')
                                #     self.tb_display.clearContents()  # 清空表格插件内容
                            else:
                                # print('不在下架设备表中。')
                                data = []  # 定义下架数据
                                data.append((_, 2, operator, down_time, comments))
                                try:
                                    with db.atomic():
                                        ShelfManage.insert_many(data, fields=(
                                            'machine_id', 'up_or_down', 'operator', 'date',
                                            'comments')).execute()  # 插入下架设备信息到下架表中
                                        MachineInfos.update(run_state=4, uninstall_date=down_time).where(
                                            MachineInfos.machine_id==_).execute()  # 修改设备表运行状态为下架
                                except Exception as e:
                                    logging.critical('执行下架出错：'.format(e))
                        QtWidgets.QMessageBox.information(self, '设备下架成功', '成功下架设备！')
                        self.tb_display.clearContents()  # 清空表格插件内容
                    else:
                        pass
            # 断网、关机、运行状态处理
            else:
                comments = self.comments.toPlainText().strip()  # 下架情况说明
                if choose == '运行':
                    state = '1'
                elif choose == '断网':
                    state = '2'
                elif choose == '关机':
                    state = '3'
                else:
                    state = '5'
                # print('当前选择状态为：',state,'选择设备',select_data)
                if QtWidgets.QMessageBox.question(self, '执行操作',
                                                  '是否确认要对已选设备状态设置为【{}】？'.format(
                                                      choose)) == QtWidgets.QMessageBox.Yes:
                    try:
                        with db.atomic():
                            MachineInfos.update(run_state=state, comments=comments).where(
                                MachineInfos.machine_id.in_(select_data)).execute()  # 修改设备表运行状态为对应状态
                    except Exception as e:
                        logging.critical('执行操作失败：'.format(e))
                        # print(e)
                    else:
                        QtWidgets.QMessageBox.information(self, '操作成功', '操作执行成功！')
                        self.tb_display.clearContents()  # 清空表格插件内容
                else:
                    pass

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
    down_win = UiDownShelf()
    down_win.show()
    sys.exit(app.exec())
