import sys
from PySide6 import QtWidgets
from ui.upshelf import *
from db.db_orm import *
from action.pub_infos import PubSwitch


class UiUpShelf(Ui_up_shelf, QtWidgets.QWidget):
    """
    添加设备窗口类，用于新设备上架
    """
    room_and_id = None  # 定义一个机房ID与机房名称的映射，后用于字典

    def __init__(self, parent=None):
        super(UiUpShelf, self).__init__(parent)
        self.setupUi(self)
        self.pub_info = PubSwitch()  # 创建公用机房机柜信息实例

        # 初始化下拉菜单数据
        self.sort_name.addItems(self.get_machine_sort())  # 给设备分类下拉菜单添加项
        self.display_room()  # 给机房下拉菜单添加项
        self.cb_room.activated.connect(self.get_cabinet)  # 在选择机房后发送机柜信号
        self.machine_factory.addItems(self.get_manufacturer())  # 给设备厂商添加项
        self.cb_up_position.addItems(self.get_position())  # 添加上U位下拉菜单项
        self.cb_down_position.addItems(self.get_position())  # 添加下U位下拉菜单项

        # 设置上架安装日期为当天
        self.install_date.setDate(QDate.currentDate())  # 设置默认为系统当天
        # 设置出厂日期为当天
        self.factory_date.setDate(QDate(2000, 1, 1))  # 设置默认为系统当天
        # 设置原厂维保结束日期为当天
        self.end_ma_date.setDate(QDate(2000, 1, 1))  # 设置默认为系统当天

        # 定义按钮功能
        self.bt_save.clicked.connect(self.save_infos)  # 保存提交内容
        self.bt_clear.clicked.connect(self.clear_all)  # 清空选项内容

    # 获取机房信息
    def display_room(self):
        """
        获取数据库中机房信息显示至机房下拉菜单中
        :return: 机房列表
        """
        room = self.pub_info.get_room().values()
        # print(room)
        self.cb_room.addItems(room)

    def save_infos(self):
        """
        提交设备信息至数据库中
        :return:
        """
        machine_name = self.machine_name.text().strip()  # 设备名称
        sort_name = self.sort_name.currentText()  # 设备分类
        room = self.pub_info.room_swap_id(name=self.cb_room.currentText())  # 机房名转换成id
        cabinet = self.cb_cabinet.currentText()  # 机柜名
        down_position = self.cb_down_position.currentText()  # 下U位
        up_position = self.cb_up_position.currentText()  # 上U位
        machine_factory = self.machine_factory.currentText()  # 厂商
        model = self.model.text().strip()  # 型号
        machine_sn = self.machine_sn.text().strip()  # SN
        lmg_ip = self.lmg_ip.text().strip()  # 管理IP
        work_are = '' if self.cb_work_are.currentIndex() + 1 == 0 else self.cb_work_are.currentIndex() + 1  # 业务区域,值为0时置空
        machine_admin = self.machine_admin.text().strip()  # 设备管理员
        admin = self.admin.text().strip()  # 业务人员
        app_ip = self.app_ip.text().strip()  # 应用IP
        factory_date = self.factory_date.date().toString('yyyy/M/d')  # 设置默认为2000/1/1
        end_ma_date = self.end_ma_date.date().toString('yyyy/M/d')  # 设置默认为2000/1/1
        install_date = self.install_date.date().toString('yyyy/M/d')  # 设置默认为系统当天
        bmc_ip = self.bmc_ip.text().strip()  # BMC IP
        single_power = '0' if not self.single_power.isChecked() else '1'  # 是否单电源
        comments = self.comments.toPlainText().strip()  # 备注信息
        operator = self.le_operator.text().strip()  # 安装人员
        asset_id = self.le_asset_id.text().strip()  # 资产编号
        system_name = self.le_system_name.text().strip()  # 业务系统
        # 添加到设备信息库的数据信息
        add_data = (
            machine_name, sort_name, room, cabinet, down_position, up_position, machine_factory, model, machine_sn,
            lmg_ip, work_are, machine_admin, admin, app_ip, factory_date, end_ma_date, install_date, bmc_ip,
            single_power, comments, asset_id, system_name)
        # 添加到设备上架库的信息
        up_shelf_data = [1, operator, install_date, comments]
        # print(add_data)
        # 检查主要填写数据是否为空
        if machine_name == '' or sort_name == '' or room == 0 or cabinet == '' or down_position == '' or \
                model == '' or up_position == '' or machine_factory == '':
            QtWidgets.QMessageBox.warning(self, '添加设备',
                                          '请输入需要添加的【设备信息】<br>--> 红色字部分内容为必填内容！')
        else:
            # 询问是否保存
            # print('添加设备数据：',add_data)
            if QtWidgets.QMessageBox.question(self, '是否保存数据',
                                              '---> 是否保存数据 ？ <---') == QtWidgets.QMessageBox.Yes:
                #  判断设备的SN不为空，且是否在设备下架表中
                #  > 在SN在下架表中时，则获取对应设备的id,并更新设备的位置、名称相关信息，同时设置上架表中状态为重新上架 状态码为：3
                #  > 设备的SN不在下架表中时，直接添加设备至设备信息表和上架设备信息表中

                machine_id = MachineInfos.select(MachineInfos.machine_id).where(
                    MachineInfos.machine_sn == machine_sn).tuples()
                id_isnot = ShelfManage.get_or_none(ShelfManage.machine in machine_id)
                # print('设备SN:', id_isnot)
                if id_isnot and machine_sn != '':  # 判断是否在下架表中,并且不为空值
                    mid = [m_id[0] for m_id in machine_id]
                    # print('在仓库中！', mid)
                    # 保存至数据库中
                    try:
                        with (db.atomic()):
                            # 更新设备信息数据表
                            MachineInfos.update(machine_name=machine_name, machine_sort_name=sort_name,
                                                machine_roomid=room, cabinet_name=cabinet, start_position=down_position,
                                                end_position=up_position, machine_factory=machine_factory, model=model,
                                                machine_sn=machine_sn, mg_ip=lmg_ip, work_are=work_are,
                                                machine_admin=machine_admin, app_admin=admin, app_ip1=app_ip,
                                                factory_date=factory_date, end_ma_date=end_ma_date,
                                                install_date=install_date, bmc_ip=bmc_ip, single_power=single_power,
                                                comments=comments, asset_id=asset_id, system_name=system_name).where(
                                MachineInfos.machine_id == mid[0]).execute()
                            # 更新设备上架数据表状态为3,如果在设备上架表中没有，则添加一条记录，并设置状态为3
                            if ShelfManage.get_or_none(ShelfManage.machine == mid[0]):
                                ShelfManage.update(up_or_down=3).where(ShelfManage.machine == mid[0]).execute()
                            else:
                                up_shelf_data.insert(0, mid[0])  # 将设备ID添加到上架数据列表中
                                up_shelf_data[1] = 3  # 设置上架数据列表中上架字段为 重新上架：3

                                # 在数据库中插入重新上架数据
                                ShelfManage.insert_many([up_shelf_data],
                                                        fields=[ShelfManage.machine_id, ShelfManage.up_or_down,
                                                                ShelfManage.operator, ShelfManage.date,
                                                                ShelfManage.comments]).execute()
                    except Exception as e:
                        QtWidgets.QMessageBox.critical(self, '保存数据错误！', '错误：{}'.format(e))
                    else:
                        if QtWidgets.QMessageBox.question(self, '设备上架',
                                                          '数据保存成功！是否继续添加') == QtWidgets.QMessageBox.Yes:
                            self.machine_name.clear()  # 清空设备名称
                            self.machine_sn.clear()  # 清空SN内容
                        else:
                            self.close()  # 退出窗口

                else:
                    # print('新设备上架！')
                    # 保存至数据库中
                    try:
                        with db.atomic():
                            # 添加到设备信息数据表
                            result = MachineInfos.insert_many([add_data, ], [
                                'machine_name', 'machine_sort_name', 'machine_roomid', 'cabinet_name', 'start_position',
                                'end_position', 'machine_factory', 'model', 'machine_sn', 'mg_ip', 'work_are',
                                'machine_admin',
                                'app_admin', 'app_ip1', 'factory_date', 'end_ma_date', 'install_date', 'bmc_ip',
                                'single_power', 'comments', 'asset_id', 'system_name']).execute()
                            # 添加到设备上架数据表
                            up_shelf_data.insert(0, result)  # result 插入数据后返回的id值
                            # print('result:',result)
                            # print('上架设备信息：', up_shelf_data)
                            ShelfManage.insert_many([up_shelf_data],
                                                    fields=[ShelfManage.machine_id, ShelfManage.up_or_down,
                                                            ShelfManage.operator, ShelfManage.date,
                                                            ShelfManage.comments]).execute()
                            # 将设备生产日期同步写入到维保信息表中
                            WarrantyInfos.insert(machine_id=result, start_date=factory_date,
                                                 end_date=end_ma_date).execute()

                    except Exception as e:
                        QtWidgets.QMessageBox.critical(self, '保存数据错误！', '错误：{}'.format(e))
                    else:
                        if QtWidgets.QMessageBox.question(self, '设备上架',
                                                          '数据保存成功！是否继续添加') == QtWidgets.QMessageBox.Yes:
                            self.machine_name.clear()  # 清空设备名称
                            self.machine_sn.clear()  # 清空SN内容
                        else:
                            self.close()  # 退出窗口
            else:
                pass

    def clear_all(self):
        """
        清空所填内容
        :return:
        """
        self.machine_name.clear()
        self.sort_name.setCurrentIndex(-1)
        self.cb_room.setCurrentIndex(-1)
        self.cb_cabinet.setCurrentIndex(-1)
        self.cb_up_position.setCurrentIndex(-1)
        self.machine_factory.setCurrentIndex(-1)
        self.model.clear()
        self.cb_down_position.setCurrentIndex(-1)
        self.machine_sn.clear()
        self.lmg_ip.clear()
        self.cb_work_are.setCurrentIndex(-1)
        self.machine_admin.clear()
        self.admin.clear()
        self.app_ip.clear()
        self.factory_date.setDate(QDate.currentDate())  # 设置默认为2000/1/1
        self.end_ma_date.setDate(QDate.currentDate())  # 设置默认为2000/1/1
        self.install_date.setDate(QDate.currentDate())  # 设置默认为系统当天
        self.comments.clear()
        self.le_operator.clear()
        self.le_asset_id.clear()
        self.le_system_name.clear()

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
        # 当机房为ZB-1时，Cabinet.room=1，根据条件进行判断...
        cabinet_data = Cabinet.select(Cabinet.cab_num).where(
            (Cabinet.room == self.pub_info.room_swap_id(name=self.cb_room.currentText())) & (
                    Cabinet.is_use == 1)).order_by(
            Cabinet.cab_num)
        # print(cabinet_data)
        cabinet = [i.cab_num for i in cabinet_data]  # 利用列表生成器生成设备分类
        # print(cabinet)
        self.cb_cabinet.clear()  # 清除所有选项
        self.cb_cabinet.addItems(cabinet)  # # 添加新的选项

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
    up_shelf_win = UiUpShelf()
    up_shelf_win.show()
    sys.exit(app.exec())
