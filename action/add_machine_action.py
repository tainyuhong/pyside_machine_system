import sys
from PySide6 import QtWidgets
from ui.add_machine import *
from db.db_orm import *
from action.pub_infos import PubSwitch


class UiAdd(Ui_add_machine_form, QtWidgets.QWidget):
    """
    添加设备窗口类，该模块用于补录设备信息    注意：不用于适用新设备上架
    """
    room_and_id = None  # 定义一个机房ID与机房名称的映射，后用于字典

    def __init__(self, parent=None):
        super(UiAdd, self).__init__(parent)
        self.setupUi(self)
        self.pub_infos = PubSwitch()

        # 初始化下拉菜单数据
        self.sort_name.addItems(self.get_machine_sort())  # 给设备分类下拉菜单添加项
        self.display_room()
        self.room.activated.connect(self.get_cabinet)  # 在选择机房后发送机柜信号
        self.machine_factory.addItems(self.get_manufacturer())  # 给设备厂商添加项
        self.up_position.addItems(self.get_position())  # 添加上U位下拉菜单项
        self.down_position.addItems(self.get_position())  # 添加下U位下拉菜单项

        # 设置上架安装日期为当天
        self.install_date.setDate(QDate.currentDate())  # 设置默认为系统当天

        # 定义按钮功能
        self.save.clicked.connect(self.save_infos)  # 保存提交内容
        self.clear.clicked.connect(self.clear_all)  # 清空选项内容

    # 获取机房信息
    def display_room(self):
        """
        获取数据库中机房信息显示至机房下拉菜单中
        :return: 机房列表
        """
        room = self.pub_infos.get_room().values()
        self.room.addItems(room)

    def save_infos(self):
        """
        提交设备信息至数据库中
        :return:
        """
        machine_name = self.machine_name.text().strip()  # 设备名称
        sort_name = self.sort_name.currentText()  # 设备分类
        room = self.pub_infos.room_swap_id(name=self.room.currentText())  # 机房名转换成id
        cabinet = self.cabinet.currentText()  # 机柜名
        down_position = self.down_position.currentText()  # 下U位
        up_position = self.up_position.currentText()  # 上U位
        machine_factory = self.machine_factory.currentText()  # 厂商
        model = self.model.text().strip()  # 型号
        machine_sn = self.machine_sn.text().strip()  # SN
        lmg_ip = self.lmg_ip.text().strip()  # 管理IP
        work_are = '' if self.work_are.currentIndex() + 1 == 0 else self.work_are.currentIndex() + 1  # 业务区域,值为0时置空
        machine_admin = self.machine_admin.text().strip()  # 设备管理员
        admin = self.admin.text().strip()  # 业务人员
        app_ip = self.app_ip.text().strip()  # 应用IP
        factory_date = self.factory_date.date().toString('yyyy/M/d')  # 设置默认为2000/1/1
        end_ma_date = self.end_ma_date.date().toString('yyyy/M/d')  # 设置默认为2000/1/1
        install_date = self.install_date.date().toString('yyyy/M/d')  # 设置默认为系统当天
        bmc_ip = self.bmc_ip.text().strip()  # BMC IP
        single_power = '0' if not self.single_power.isChecked() else '1'  # 是否单电源
        comments = self.comments.toPlainText().strip()  # 备注信息
        asset_id = self.le_asset_id.text().strip()      # 资产编号
        add_data = (
            machine_name, sort_name, room, cabinet, down_position, up_position, machine_factory, model, machine_sn,
            lmg_ip, work_are, machine_admin, admin, app_ip, factory_date, end_ma_date, install_date, bmc_ip,
            single_power,comments,asset_id)
        # print(add_data)
        # 检查主要填写数据是否为空
        if machine_name == '' or sort_name == '' or room == 0 or cabinet == '' or down_position == '' or \
                model == '' or up_position == '' or machine_factory == '':
            QtWidgets.QMessageBox.warning(self, '添加设备', '请输入需要添加的【设备信息】<br>--> 红色字部分内容为必填内容！')
        else:
            # 询问是否保存
            # print('添加设备数据：',add_data)
            if QtWidgets.QMessageBox.question(self, '是否保存数据', '---> 是否保存数据 ？ <---') == QtWidgets.QMessageBox.Yes:
                # 保存至数据库中
                try:
                    MachineInfos.insert_many([add_data, ], [
                        'machine_name', 'machine_sort_name', 'machine_roomid', 'cabinet_name', 'start_position',
                        'end_position',
                        'machine_factory', 'model', 'machine_sn', 'mg_ip', 'work_are', 'machine_admin', 'app_admin',
                        'app_ip1',
                        'factory_date', 'end_ma_date', 'install_date', 'bmc_ip', 'single_power', 'comments','asset_id']).execute()
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self,'保存数据错误！', ''.format(e))
                    logging.error('保存数据错误！', e)
                else:
                    if QtWidgets.QMessageBox.question(self,'数据保存','数据保存成功！是否继续添加') == QtWidgets.QMessageBox.Yes:
                        self.machine_name.clear()       # 清空设备名称
                        self.machine_sn.clear()           # 清空SN内容
                    else:
                        self.close()     # 退出窗口
            else:
                pass

    def clear_all(self):
        '''
        清空所填内容
        :return:
        '''
        self.machine_name.clear()
        self.sort_name.setCurrentIndex(-1)
        self.room.setCurrentIndex(-1)
        self.cabinet.setCurrentIndex(-1)
        self.up_position.setCurrentIndex(-1)
        self.machine_factory.setCurrentIndex(-1)
        self.model.clear()
        self.down_position.setCurrentIndex(-1)
        self.machine_sn.clear()
        self.lmg_ip.clear()
        self.work_are.setCurrentIndex(-1)
        self.machine_admin.clear()
        self.admin.clear()
        self.app_ip.clear()
        self.factory_date.setDate(QDate(2000, 1, 1))  # 设置默认为2000/1/1
        self.end_ma_date.setDate(QDate(2000, 1, 1))  # 设置默认为2000/1/1
        self.install_date.setDate(QDate.currentDate())  # 设置默认为系统当天
        self.comments.clear()
        self.lb_asset_id.clear()

    def get_machine_sort(self):
        """
        获取数据库中设备分类显示至分类下拉菜单中
        :return: 设备分类列表
        """
        sort_data = MachineSort.select().where(MachineSort.part_sort != 'null').order_by(
            MachineSort.sort_id)  # 查询父类不为空的分类
        # print(sort_data)
        sort = [i.sort_name for i in sort_data]  # 利用列表生成器生成设备分类
        return sort

    def get_cabinet(self):
        """
        获取数据库中机柜信息显示至机柜下拉菜单中，同时与机房进行关联显示
        :return: 机柜列表
        """
        cabinet = self.pub_infos.get_cabinet_infos(self.room.currentText())
        self.cabinet.clear()  # 清除所有选项
        self.cabinet.addItems(cabinet)  # # 添加新的选项

    def get_position(self):
        """
        获取数据库中机柜U位信息
        :return: U位列表
        """
        # 查询U位信息
        position_data = CabPosition.select(CabPosition.num)
        position = [str(i.num) for i in position_data]  # 利用列表生成器生成设备分类
        # print(position)
        return position

    def get_manufacturer(self):
        """
        获取数据库中设备厂商信息显示
        :return: 厂商信息
        """
        # 查询设备品牌厂商
        manufacturer_data = Manufacturer.select(Manufacturer.manufacturer_name)
        # print(manufacturer_data)
        manufacturer = [i.manufacturer_name for i in manufacturer_data]  # 利用列表生成器生成设备分类
        # print(manufacturer)
        # self.machine_factory.clear()        # 清除所有选项
        return manufacturer


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    add_win = UiAdd()
    add_win.show()
    sys.exit(app.exec())
