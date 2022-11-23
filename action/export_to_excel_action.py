import sys
from PySide6 import QtWidgets, QtCore
from db.db_orm import *
from peewee import fn
from ui.export_excel import Ui_export_form


class ExportExcel(Ui_export_form, QtWidgets.QWidget):
    # 定义字段名字典
    field_dict = {'machine_id': 'ID', 'machine_name': '设备名称', 'machine_sort_name': '分类名称',
                  'machine_sn': '序列号', 'machine_factory': '设备厂商', 'model': '型号',
                  'machine_roomid': '机房ID', 'cabinet_name': '机柜编号', 'start_position': '开始U位',
                  'end_position': '结束U位', 'factory_date': '出产日期', 'end_ma_date': '到保日期',
                  'work_are': '业务类型 ', 'run_state': '运行状态 ', 'machine_admin': '管理员',
                  'app_admin': '应用管理员',
                  'mg_ip': '管理IP地址', 'app_ip1': '业务IP', 'bmc_ip': 'BMC IP',
                  'install_date': '上架安装时间',
                  'uninstall_date': '下架时间', 'single_power': '单电源', 'asset_id': '资产编号',
                  'comments': '备注'}

    def __init__(self, parent=None):
        super(ExportExcel, self).__init__(parent)
        self.setupUi(self)  # 展示报告窗口页
        self.get_field()  # 显示数据库中字段
        self.btn_export.clicked.connect(self.export_exl)  # 导出按钮事件

    # 获取要导出的字段
    def get_field(self):
        # a = ['ID', '设备名称', '分类名称', '序列号', '设备厂商', '机房ID', '机柜编号', '开始U位', '结束U位', '出产日期',
        #      '到保日期', '业务类型 ', '运行状态 ', '管理员', '应用管理员', '管理IP地址', '业务IP1', 'bmc IP',
        #      '上架安装时间', '下架时间', '单电源', '备注', '资产编号',
        #      ]

        for i in self.field_dict.values():
            box = QtWidgets.QCheckBox(i)  # 实例化一个QCheckBox，把文字传进去
            item = QtWidgets.QListWidgetItem()  # 实例化一个Item，QListWidget，不能直接加入QCheckBox
            self.listWidget.addItem(item)  # 把QListWidgetItem加入QListWidget
            self.listWidget.setItemWidget(item, box)  # 再把QCheckBox加入QListWidgetItem

    # 导出按钮事件
    def export_exl(self):
        print('导出至excel')
        new_data = dict(zip(self.field_dict.values(), self.field_dict.keys()))  # 将字典key/value进行反转
        count = self.listWidget.count()
        chooses_list = []  # 选择的字段内容
        choose_name = []  # 选择
        for i in range(count):
            # print('列表项：',self.listWidget.item(i))
            chk_item = self.listWidget.itemWidget(self.listWidget.item(i))  # 获取复选框对象
            # print('列表项：',chk_item.isChecked())
            # 判断复选框是否选择
            if chk_item.isChecked():
                chooses_list.append(chk_item.text())
                # print('数据库字段名：',new_data[chk_item.text()])
                choose_name.append(new_data[chk_item.text()])
        print('选择的字段值内容：', chooses_list)
        print('数据库字段名：', choose_name)

        # 查询数据
        export_data_model = MachineInfos.select(choose_name).tuples()
        print('查询到的数据：',export_data_model)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    report_win = ExportExcel()
    report_win.show()
    sys.exit(app.exec())
