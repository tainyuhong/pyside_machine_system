import sys
import xlwings as xw
from PySide6 import QtWidgets
from db.db_orm import *
from ui.create_label import *
from action.pub_infos import PubSwitch


class CreateLabel(QtWidgets.QWidget, Ui_form_create):
    def __init__(self, parent=None):
        super(CreateLabel, self).__init__(parent)
        self.setupUi(self)
        self.room = PubSwitch()  # 创建机房对象

        # 显示机房下拉菜单
        self.get_room()
        # 显示机房内机柜
        self.cb_room.activated.connect(lambda: self.get_cabinet(self.cb_room.currentText()))
        # 设置查询按钮事件
        self.bt_select.clicked.connect(self.select_machine)
        # 设置全选按钮事件
        self.bt_add_all.clicked.connect(self.select_all)
        # 设置生成标签模板事件
        self.bt_create.clicked.connect(self.create_label_to_excel)

    # 获取机房名称并显示到下拉菜单
    def get_room(self):
        room = self.room.get_room()
        # print(room.values())
        self.cb_room.addItems(room.values())

    # 获取每个机房的机柜信息
    def get_cabinet(self, room):
        cabinet = self.room.get_cabinet_infos(room)  # 获取每个机房的机柜
        # print(cabinet)
        self.cb_cabinet.clear()
        self.cb_cabinet.addItem('所有')
        self.cb_cabinet.addItems(cabinet)

    # 获取输入条件并进行查询
    def select_machine(self):
        room_name = self.cb_room.currentText()  # 选择的机房
        cabinet = self.cb_cabinet.currentText()  # 选择的机柜
        machine_name = self.machine_name.text().strip()  # 输入的设备名称
        mg_ip = self.mg_ip.text().strip()  # 输入的IP
        # print('选择的机房：{}设备名称：{}  IP: {}'.format(room_name, machine_name, mg_ip))

        # 不带条件的查询
        query = MachineList.select(MachineList.machine_id, MachineList.machine_name, MachineList.room_name,
                                   MachineList.cab_name,
                                   MachineList.start_position, MachineList.postion_u, MachineList.machine_sort_name,
                                   MachineList.machine_factory, MachineList.model, MachineList.machine_sn,
                                   MachineList.machine_admin, MachineList.mg_ip, MachineList.bmc_ip)

        cond_cabinet = MachineList.cab_name == cabinet
        cond_machine_name = MachineList.machine_name.contains(machine_name)

        # 根据选择的带外IP还是带内IP选择相应的查询条件
        if self.rd_mg_ip.isChecked():
            cond_ip = MachineList.mg_ip.contains(mg_ip)  # 带内IP
        else:
            cond_ip = MachineList.bmc_ip.contains(mg_ip)  # 带外IP

        # 根据选择条件进行查询
        # 选择机房为所有
        if room_name == '所有':
            # print('未选机房')
            if machine_name != '' and mg_ip == '':
                query_condition = cond_machine_name
            elif machine_name != '' and mg_ip != '':
                query_condition = cond_machine_name & cond_ip
            elif machine_name == '' and mg_ip != '':
                query_condition = cond_ip
            elif machine_name == '' and mg_ip == '':
                query_condition = None
        # 选择机房对应机房，机柜为所有
        elif room_name != '所有' and cabinet == '所有':
            # print('选择了机房--')
            cond_room = MachineList.room_name == room_name
            if machine_name != '' and mg_ip == '':
                query_condition = cond_room & cond_machine_name
            elif machine_name != '' and mg_ip != '':
                query_condition = cond_room & cond_machine_name & cond_ip
            elif machine_name == '' and mg_ip != '':
                query_condition = cond_room & cond_ip
            elif machine_name == '' and mg_ip == '':
                query_condition = cond_room
        # 选择机房对应机房，机柜为对应机柜
        else:
            # print('选择了机房--，，，，，机柜')
            cond_room = MachineList.room_name == room_name
            if machine_name != '' and mg_ip == '':
                query_condition = cond_room & cond_cabinet & cond_machine_name
            elif machine_name != '' and mg_ip != '':
                query_condition = cond_room & cond_cabinet & cond_machine_name & cond_ip
            elif machine_name == '' and mg_ip != '':
                query_condition = cond_room & cond_cabinet & cond_ip
            elif machine_name == '' and mg_ip == '':
                query_condition = cond_room & cond_cabinet

        # 进行查询
        # print('查询SQL:', query.where(query_condition).sql())
        # 查询并获取结果
        result = [i for i in query.where(query_condition).tuples()]
        # print('查询结果：', result)
        data_count = len(result)
        self.lb_stat.setText('----> 共查询到 {} 条记录'.format(data_count))
        self.lb_stat.setStyleSheet('color:blue')
        self.tb_display.setRowCount(data_count)  # 根据内容设置行数
        self.tb_display.clearContents()
        # 将查询结果显示在表格控件中
        for row, d1 in enumerate(result):
            # print('每一行数据：',d1)
            for col, d2 in enumerate(d1):
                if col == 0:
                    self.tb_display.setItem(row, col, QTableWidgetItem(str(result[row][col])))
                    self.tb_display.item(row, 0).setCheckState(Qt.Unchecked)  # 第一列添加复选框按钮
                else:
                    if d2 is None:
                        self.tb_display.setItem(row, col, QTableWidgetItem(''))
                    else:
                        self.tb_display.setItem(row, col, QTableWidgetItem(str(result[row][col])))
        self.tb_display.resizeColumnsToContents()  # 自适应列宽

    # 设置全选按钮槽函数
    def select_all(self):
        row_count = self.tb_display.rowCount()
        # print(self.tb_display.item(0, 0).checkState())
        # 当已经全选时，再次点击将取消全选
        if row_count > 0:
            if self.tb_display.item(0, 0).checkState() is Qt.Checked:
                for i in range(row_count):
                    self.tb_display.item(i, 0).setCheckState(Qt.Unchecked)  # 取消钩选所有框
            else:
                for i in range(row_count):
                    self.tb_display.item(i, 0).setCheckState(Qt.Checked)  # 钩选所有框
        else:
            pass

    # 生成标签模板并导出EXCEL
    def create_label_to_excel(self):
        # 先获取选择的设备
        row_count = self.tb_display.rowCount()
        checked_machineid = []
        # 当已经全选时，再次点击将取消全选
        if row_count > 0:
            for i in range(row_count):
                if self.tb_display.item(i, 0).checkState() == Qt.Checked:  # 判断是否钩选框
                    machine_id = self.tb_display.item(i, 0).text()
                    machine_name = self.tb_display.item(i, 1).text()
                    machine_room = self.tb_display.item(i, 2).text()
                    machine_cabinet = self.tb_display.item(i, 3).text()
                    machine_u = self.tb_display.item(i, 4).text()
                    machine_mg_ip = self.tb_display.item(i, 11).text()
                    machine_bmc_ip = self.tb_display.item(i, 12).text()
                    machine_sn = self.tb_display.item(i, 9).text()
                    machine_admin = self.tb_display.item(i, 10).text()
                    checked_machineid.append(
                        [machine_id, '{}_{}_{}'.format(machine_room, machine_cabinet, machine_u), machine_name,
                         '带内:{}\r\n带外:{}'.format(machine_mg_ip, machine_bmc_ip), machine_sn,machine_admin])
            # print('选择的设备ID', checked_machineid)
            if len(checked_machineid) > 0:
                # 创建表格实例
                with xw.App(visible=False,add_book=False) as exl_app:
                    wb = exl_app.books.add()
                    ws = wb.sheets.active
                    ws.name='设备标签打印模板'
                    ws.range('a1').value=['设备id','位置','设备名称','IP地址','序列号','负责人']      # 向表中写入标题栏
                    ws.range('e1',(len(checked_machineid),5)).api.NumberFormat='@'  # 设置需要写入数据的单元格为文本格式
                    ws.range('a2').value=checked_machineid      # 向表格中写入数据
                    ws.range('a1').expand('table').columns.autofit()    # 设置自适应列宽
                    ws.range('d1').column_width='25'    # 设置IP地址列宽
                    # 设置边框线
                    for i in range(7,13):
                        ws.range('a1').expand('table').api.Borders(i).Weight=2
                    # 弹出文件保存目录
                    filepath, filetype = QtWidgets.QFileDialog.getSaveFileUrl(self,'导出设备标签模板',filter='.xlsx')
                    if filepath != '':
                        if Path(filepath.toLocalFile()).suffix == '.xlsx':
                            # 将文件保存到指定目录
                            try:
                                wb.save(filepath.toLocalFile())
                            except Exception as e:
                                QtWidgets.QMessageBox.critical(self, '保存文件', '保存文件错误！{}'.format(e))
                            else:
                                wb.close()
                                QtWidgets.QMessageBox.information(self, '保存文件', '保存文件成功！！')
                        else:
                            # 如果用户没有在文件名后加后缀名，则系统自动加上
                            save_file = filepath.toLocalFile() + '.xlsx'
                            # 将文件从系统下载到指定目录
                            try:
                                wb.save(save_file)
                            except Exception as e:
                                QtWidgets.QMessageBox.critical(self, '保存文件', '保存文件错误！{}'.format(e))
                            else:
                                wb.close()
                                QtWidgets.QMessageBox.information(self, '保存文件', '保存文件成功！！')
                    else:
                        print('取消')
            else:
                QtWidgets.QMessageBox.warning(self, '未选择设备', '请选择要生成标签的设备!')
        else:
            QtWidgets.QMessageBox.warning(self, '未选择设备', '请选择要生成标签的设备!')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    show_label = CreateLabel()
    show_label.show()
    sys.exit(app.exec())
