import sys

import peewee

from ui.base_info import *
from PySide6 import QtWidgets, QtGui
# import logging
from db.db_orm import *
#
# logger = logging.getLogger('peewee')
# logger.addHandler(logging.StreamHandler())
# logger.setLevel(logging.DEBUG)


class UiBaseInfo(Ui_BaseInfo, QtWidgets.QWidget):
    modify_cabinet_id = None  # 定义要修改的机柜id
    room_and_id = None  # 定义一个机房ID与机房名称的映射，后用于字典
    old_sort_data = None  # 选定的要修改的item的ID ,为上级分类时，2个元素，子分类4个元素
    modify_item = None  # 选定的要修改的ITEM

    def __init__(self, parent=None):
        super(UiBaseInfo, self).__init__(parent)
        self.setupUi(self)
        # 机房界面
        self.display_room()  # 机房信息窗口
        self.bt_add_room.clicked.connect(self.add_room)  # 添加机房信息
        self.bt_del_room.clicked.connect(self.del_room)  # 删除机房信息

        # 机柜信息界面
        self.display_cabinet()  # 机柜信息窗口
        self.get_room()  # 显示机房信息列表
        self.bt_add_cabinet.clicked.connect(self.add_cabinet)  # 添加机柜信息
        self.bt_del_cabinet.clicked.connect(self.del_cabinet)  # 删除机柜信息
        self.tb_cabinet.doubleClicked.connect(self.cabinet_doubleclick)  # 删除机柜信息
        self.bt_cab_modify.clicked.connect(self.modify_cabinet)  # 删除机柜信息

        # U位信息界面
        self.display_u()  # U位信息窗口
        self.bt_add_u.clicked.connect(self.add_u)  # 添加U位
        self.bt_del_u.clicked.connect(self.del_u)  # 删除U位

        # 品牌信息界面
        self.display_manfacturer()  # 品牌信息窗口
        self.bt_add_manufacturer.clicked.connect(self.add_manfacturer)  # 添加U位
        self.bt_del_manufacturer.clicked.connect(self.del_manfacturer)  # 删除U位

        # 分类信息界面
        # 设置分类id输入条件
        self.le_sort_id.setValidator(QtGui.QIntValidator())  # 设置只请允许整数
        self.display_sort()  # 显示设备分类信息树结构
        self.bt_add_sort.clicked.connect(self.add_sort)  # 添加分类
        self.bt_del_sort.clicked.connect(self.del_sort)  # 删除分类
        self.tree_sort.doubleClicked.connect(self.double_click_sort)  # 双击事件，进入修改模式获取数据
        self.bt_sort_modify.clicked.connect(self.modify_sort)  # 修改分类信息
        # self.tab_sort.keyReleaseEvent                     # ESC退出修改模式

    # 机房窗口
    # 显示机房信息
    def display_room(self):
        # 定义查询机房数据
        room_model = MachineRoom.select(MachineRoom.room_id, MachineRoom.room_name, MachineRoom.room_alias)
        # 输出查询内容
        data = [(i.room_id, i.room_name, i.room_alias) for i in room_model]
        # 将机房信息取出作为公共变量
        self.room_and_id = {}  # 定义一个机房ID与机房名称的映射字典
        # 生成机房ID与机房名称的映射字典
        for i in room_model:
            self.room_and_id[i.room_id] = i.room_name
        # print('机房信息字典',self.room_and_id)

        self.tb_room.setRowCount(len(data))  # 设置表格的行数
        # print('查询数据：',data)
        # 显示机房内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_room.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 机房名与id互转
    def room_to_id(self, name=None, room_id=None):
        """
        将传入的机房名或机房id转换为对应的id或机房名
        :param name: 机房名称
        :param room_id: 机房ID
        :return: 机房名或机房id
        """
        # 生成字典与机房Id的映射
        room_id_dict = dict(map(reversed, self.room_and_id.items()))
        # print('名称-->机房ID',room_id_dict)    # {'ZB-1': 1, 'ZB-2': 2, 'ZB-3': 3, 'ZB-4': 4}
        # 如果传入机房名称为空，则返回id，如果传入的为id,则返回机房名称
        if name is None:
            return self.room_and_id[room_id]
        else:
            return room_id_dict[name]

    # 添加机房
    def add_room(self):
        room_name = self.le_room_name.text().strip()
        room_alias = self.le_room_alias.text().strip()
        # print(room_name, room_alias)
        # 查询room_name是否在数据库中存在
        if MachineRoom.get_or_none(MachineRoom.room_name == room_name) is None and room_name != '':
            if QtWidgets.QMessageBox.question(self, '添加机房', '是否需要添加该机房信息！') == QtWidgets.QMessageBox.Yes:
                try:
                    data = [room_name, room_alias]  # 定义获取到的机房信息
                    # 保存到数据库
                    result = MachineRoom.insert_many([data],
                                                     fields=[MachineRoom.room_name, MachineRoom.room_alias]).execute()
                except Exception as e:
                    print(e)
                else:
                    self.room_and_id[result] = room_name  # 更新全局机房与id字典的信息
                    # print('添加机房后的字典变量：',self.room_and_id)
                    # print('返回ID:', result)  # 返回主键id
                    index = self.tb_room.rowCount()  # 定义索引为总行数
                    self.tb_room.insertRow(index)  # 表格中插入一行
                    data.insert(0, str(result))
                    # print('插入数据库后的数据：', data)
                    for num, _ in enumerate(data):
                        self.tb_room.setItem(index, num, QTableWidgetItem(_))  # 添加到表格中
                    QtWidgets.QMessageBox.information(self, '添加机房', '添加机房信息成功！')
                    self.le_room_name.setText('')
                    self.le_room_alias.setText('')
                    self.get_room()  # 更新机柜信息界面中机房名称下拉菜单值
            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self, '添加机房', '设备名重复！请重新输入！！')

    # 删除指定机房
    def del_room(self):
        item = self.tb_room.currentRow()  # 获取当前选择的行号的索引
        room_id = self.tb_room.item(item, 0).text()  # 获取room_id

        # 从数据库中删除
        if QtWidgets.QMessageBox.question(self, '删除机房信息', '是否确定要删除该机房信息！') == QtWidgets.QMessageBox.Yes:
            if Cabinet.get_or_none(Cabinet.room == room_id) is None:
                try:
                    MachineRoom.get_by_id(room_id).delete().where(MachineRoom.room_id == room_id).execute()
                    # print(result)  # 打印执行结果，为1时代表执行成功，0失败
                except Exception as e:
                    print('删除机房错误：', e)
                else:
                    self.tb_room.removeRow(item)  # 页面中删除一行
                    self.room_and_id.pop(int(room_id))  # 从机房变量中删除
                    QtWidgets.QMessageBox.information(self, '删除成功', '删除机房信息成功！')
                    self.get_room()  # 更新机柜信息界面中机房名称下拉菜单值
                    self.tb_room.setCurrentItem(None)  # 设置为非选择状态
                    # print('删除机房后字典值',self.room_and_id)
            else:
                QtWidgets.QMessageBox.warning(self, '删除机房信息错误', '该机房下存在机柜，请先删除机柜再删除机房！')
        else:
            pass


    # 机柜窗口
    # 显示机柜窗口
    def display_cabinet(self):
        # 定义查询机柜数据
        cabinet_model = Cabinet.select(Cabinet.cab_id, Cabinet.room, Cabinet.cab_num, Cabinet.cab_name,
                                       Cabinet.count_position, Cabinet.is_use).order_by(Cabinet.room,
                                                                                        Cabinet.cab_num).prefetch(
            MachineRoom, Cabinet)
        # 输出查询内容
        data = [(i.cab_id, self.room_to_id(room_id=i.room.room_id), i.cab_num, i.cab_name, i.count_position, i.is_use)
                for i in cabinet_model]
        self.tb_cabinet.setRowCount(len(data))  # 设置表格的行数
        # print('查询数据：',data)
        # 显示机柜内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_cabinet.setItem(row, col, QTableWidgetItem(str(data[row][col])))
        self.tb_cabinet.resizeColumnsToContents()

    # 机柜信息页面中获取机房信息
    def get_room(self):
        room_model = MachineRoom.select(MachineRoom.room_name).order_by(MachineRoom.room_id)
        # print('机房数据sql', room_model)
        room_data = [i.room_name for i in room_model]
        # print(room_data)
        self.cb_room.clear()
        self.cb_room.addItems(room_data)  # 设置机柜页面机房下拉菜单

    # 添加机柜
    def add_cabinet(self):
        room = self.cb_room.currentText()
        cab_name = self.le_cab_name.text()
        cab_alias = self.le_cabinet_alias.text()
        u_count = self.le_U_count.text()
        is_used = '1' if self.ckb_is_used.isChecked() is True else '0'

        if cab_name != '' and QtWidgets.QMessageBox.question(self, '添加机柜', '确认是否添加！') == QtWidgets.QMessageBox.Yes:
            try:
                data = [str(self.room_to_id(name=room)), cab_name, cab_alias, u_count, is_used]  # 定义机柜信息数据
                # print(data)
                # 保存到数据库,并返回表格中id给result
                result = Cabinet.insert_many([data], fields=[Cabinet.room, Cabinet.cab_num, Cabinet.cab_name,
                                                             Cabinet.count_position, Cabinet.is_use]).execute()
            except Exception as e:
                print('添加机柜错误：', e)
            else:
                index = self.tb_cabinet.rowCount()  # 定义索引为总行数
                self.tb_cabinet.insertRow(index)  # 表格中插入一行
                data.insert(0, str(result))  # 将数据库中机柜ID插入到data中
                # # print('插入数据库后的数据：', data)
                for num, _ in enumerate(data):
                    if num == 1:
                        self.tb_cabinet.setItem(index, num, QTableWidgetItem(self.room_to_id(room_id=int(_))))  # 添加到表格中
                    else:
                        self.tb_cabinet.setItem(index, num, QTableWidgetItem(_))  # 添加到表格中
                QtWidgets.QMessageBox.information(self, '添加机柜', '添加机柜信息成功！')
                self.le_cab_name.setText('')
                self.le_cabinet_alias.setText('')
                self.le_U_count.setText('')

    # 删除机柜
    def del_cabinet(self):
        item = self.tb_cabinet.currentRow()  # 获取当前选择的行号的索引
        cabinet_id = self.tb_cabinet.item(item, 0).text()  # 获取cabinet_id
        # print('cabinet_id', cabinet_id)
        # 从数据库中删除
        if QtWidgets.QMessageBox.question(self, '删除机柜信息', '是否确定要删除该机柜信息！') == QtWidgets.QMessageBox.Yes:
            try:
                # 从数据库中删除
                result = Cabinet.delete().where(Cabinet.cab_id == cabinet_id).execute()
                # print(result)  # 打印执行结果，为1时代表执行成功，0失败
                if result == 0:
                    return QtWidgets.QMessageBox.critical(self, '删除失败', '删除机柜信息失败！')
            except peewee.IntegrityError:
                QtWidgets.QMessageBox.critical(self, '删除失败', '该机柜存在设备，不能删除！')
            except Exception as e:
                print('删除机房错误：', e)
                QtWidgets.QMessageBox.critical(self, '删除失败', '删除机柜信息失败！\n {}'.format(e))
            else:
                self.tb_cabinet.removeRow(item)  # 页面中删除一行
                QtWidgets.QMessageBox.information(self, '删除成功', '删除机柜信息成功！')
                self.tb_cabinet.setCurrentItem(None)  # 设置为非选择状态
        else:
            pass

    # 机柜界面双击获取对应信息到文本框中
    def cabinet_doubleclick(self):
        item = self.tb_cabinet.currentRow()  # 获取当前选择的行号的索引
        cabinet_id = self.tb_cabinet.item(item, 0).text()  # 获取cabinet_id
        room_id = self.tb_cabinet.item(item, 1).text()  # 获取room_id
        cab_name = self.tb_cabinet.item(item, 2).text()  # 获取cab_name
        cab_alias = self.tb_cabinet.item(item, 3).text()  # 获取cab_alias
        u_count = self.tb_cabinet.item(item, 4).text()  # 获取u_count
        is_used = self.tb_cabinet.item(item, 5).text()  # 获取is_used
        # print(cabinet_id, room_id, cab_name, cab_alias, u_count, is_used)
        self.modify_cabinet_id = (cabinet_id, room_id, cab_name, cab_alias, u_count, is_used)  # 获取修改的信息

        # 将双击选择的行内容加载到对应文本框中
        self.cb_room.setCurrentText(room_id)  # 设置机房名
        self.le_cab_name.setText(cab_name)
        self.le_cabinet_alias.setText(cab_alias)
        self.le_U_count.setText(u_count)
        self.ckb_is_used.setChecked(True if is_used == '1' else False)  # 设置复选框的值

    # 修改机柜信息
    def modify_cabinet(self):
        if self.modify_cabinet_id is not None:
            # print('选择的需要修改的', self.modify_cabinet_id)
            room = self.cb_room.currentText()
            cab_name = self.le_cab_name.text()
            cab_alias = self.le_cabinet_alias.text()
            u_count = self.le_U_count.text()
            is_used = '1' if self.ckb_is_used.isChecked() is True else '0'
            data = (str(self.room_to_id(name=room)), cab_name, cab_alias, u_count, is_used)
            # print('修改后的数据', data)
            old_data = self.modify_cabinet_id[1:]
            # print('查询到的结果', old_data)
            if old_data != data and cab_name != '':
                # 定义要修改传入数据库的数据格式为字典
                item = {'room': self.room_to_id(name=room), 'cab_num': cab_name, 'cab_name': cab_alias,
                        'count_position': u_count, 'is_use': is_used}
                # print('要传入数据库中数据格式：', item)
                if QtWidgets.QMessageBox.question(self, '删除机柜信息', '是否确定要删除该机柜信息！') == QtWidgets.QMessageBox.Yes:
                    try:
                        result_model = Cabinet.update(item).where(Cabinet.cab_id == self.modify_cabinet_id[0]).execute()
                        # print('修改SQL', result_model)
                    except Exception as e:
                        print('删除机柜信息错误：', e)
                    else:
                        self.tb_cabinet.clearContents()  # 删除表中内容
                        self.display_cabinet()  # 调用显示表格数据函数重新查询，刷新表格数据
                        # 清除输入框信息
                        self.le_cab_name.setText('')
                        self.le_cabinet_alias.setText('')
                        self.le_U_count.setText('')
                        self.modify_cabinet_id = None
                        QtWidgets.QMessageBox.information(self, '修改机柜信息', '修改机柜信息成功！！')
                        self.tb_cabinet.setCurrentItem(None)  # 设置为非选择状态
            else:
                QtWidgets.QMessageBox.warning(self, '修改机柜信息', '没有选择需要修改的机柜！\n 双击要修改的行')
        else:
            QtWidgets.QMessageBox.warning(self, '修改机柜信息', '没有选择需要修改的机柜！\n 双击要修改的行')

    # U位信息窗口
    # 显示U位信息
    def display_u(self):
        # 定义查询U位数据
        u_model = CabPosition.select(CabPosition.id, CabPosition.num, CabPosition.position_name)
        # 输出查询内容
        data = [(i.id, i.num, i.position_name) for i in u_model]
        self.tb_u.setRowCount(len(data))  # 设置表格的行数
        # print('查询数据：',data)
        # 显示U位内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_u.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 添加U位信息
    def add_u(self):
        """
        添加U位信息
        :return:
        """
        u_name = self.le_u_name.text().strip()
        uname_alias = self.le_u_name_alias.text().strip()
        # 查询room_name是否在数据库中存在
        if CabPosition.get_or_none(CabPosition.num == u_name) is None and u_name != '':
            if QtWidgets.QMessageBox.question(self, '添加U位信息', '是否需要添加U位信息！') == QtWidgets.QMessageBox.Yes:
                try:
                    data = [u_name, uname_alias]  # 定义获取到的机房信息
                    # 保存到数据库
                    result = CabPosition.insert_many([data],
                                                     fields=[CabPosition.num, CabPosition.position_name]).execute()
                except Exception as e:
                    print(e)
                else:
                    # print('返回ID:', result)  # 返回主键id
                    index = self.tb_u.rowCount()  # 定义索引为总行数
                    self.tb_u.insertRow(index)  # 表格中插入一行
                    data.insert(0, str(result))
                    # print('插入数据库后的数据：', data)
                    for num, _ in enumerate(data):
                        self.tb_u.setItem(index, num, QTableWidgetItem(_))  # 添加到表格中
                    QtWidgets.QMessageBox.information(self, '添加U位信息', '添加U位信息成功！')
                    self.le_u_name.setText('')
                    self.le_u_name_alias.setText('')

            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self, '添加U位信息', 'U位名为空或重复！请重新输入！！')

    # 删除指定U位信息
    def del_u(self):
        item = self.tb_u.currentRow()  # 获取当前选择的行号的索引
        u_id = self.tb_u.item(item, 0).text()  # 获取u_id
        # 从数据库中删除
        if QtWidgets.QMessageBox.question(self, '删除U位信息', '是否确定要删除该U位信息！') == QtWidgets.QMessageBox.Yes:
            try:
                CabPosition.get_by_id(u_id).delete().where(CabPosition.id == u_id).execute()
                # print(result)  # 打印执行结果，为1时代表执行成功，0失败
            except Exception as e:
                print('删除U位错误：', e)
            else:
                self.tb_u.removeRow(item)  # 页面中删除一行
                QtWidgets.QMessageBox.information(self, '删除成功', '删除U位信息成功！')
                self.tb_u.setCurrentItem(None)  # 设置为非选择状态
        else:
            pass

    # 显示品牌信息
    def display_manfacturer(self):
        # 定义查询U位数据
        manfacturer_model = Manufacturer.select(Manufacturer.id, Manufacturer.manufacturer_name)
        # 输出查询内容
        data = [(i.id, i.manufacturer_name) for i in manfacturer_model]
        self.tb_manfacturer.setRowCount(len(data))  # 设置表格的行数
        # print('查询数据：',data)
        # 显示U位内容至表格
        for row, d1 in enumerate(data):
            for col, d2 in enumerate(d1):
                self.tb_manfacturer.setItem(row, col, QTableWidgetItem(str(data[row][col])))

    # 添加设备品牌信息
    def add_manfacturer(self):
        """
        添加设备品牌信息
        :return:
        """
        name = self.le__manufacturer_name.text().strip()
        # 查询room_name是否在数据库中存在
        if Manufacturer.get_or_none(Manufacturer.manufacturer_name == name) is None and name != '':
            if QtWidgets.QMessageBox.question(self, '添加设备品牌信息', '是否需要添加设备品牌信息！') == QtWidgets.QMessageBox.Yes:
                try:
                    data = [name]  # 定义获取到的设备品牌信息
                    # 保存到数据库
                    result = Manufacturer.insert_many([data], fields=[Manufacturer.manufacturer_name]).execute()
                except Exception as e:
                    print(e)
                else:
                    # print('返回ID:', result)  # 返回主键id
                    index = self.tb_manfacturer.rowCount()  # 定义索引为总行数
                    self.tb_manfacturer.insertRow(index)  # 表格中插入一行
                    data.insert(0, str(result))
                    # print('插入数据库后的数据：', data)
                    for num, _ in enumerate(data):
                        self.tb_manfacturer.setItem(index, num, QTableWidgetItem(_))  # 添加到表格中
                    QtWidgets.QMessageBox.information(self, '添加设备品牌信息', '添加设备品牌信息成功！')
                    self.le__manufacturer_name.setText('')

            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self, '添加U位信息', 'U位名为空或重复！请重新输入！！')

    # 删除设备品牌信息
    def del_manfacturer(self):
        item = self.tb_manfacturer.currentRow()  # 获取当前选择的行号的索引
        manufacturer_id = self.tb_manfacturer.item(item, 0).text()  # 获取u_id
        # 从数据库中删除
        if QtWidgets.QMessageBox.question(self, '删除设备品牌信息', '是否确定要删除该设备品牌信息！') == QtWidgets.QMessageBox.Yes:
            try:
                Manufacturer.get_by_id(manufacturer_id).delete().where(Manufacturer.id == manufacturer_id).execute()
                # print(result)  # 打印执行结果，为1时代表执行成功，0失败
            except Exception as e:
                print('删除设备品牌信息：', e)
            else:
                self.tb_manfacturer.removeRow(item)  # 页面中删除一行
                QtWidgets.QMessageBox.information(self, '删除成功', '删除设备品牌信息成功！')
                self.tb_manfacturer.setCurrentItem(None)  # 设置为非选择状态
        else:
            pass

    # 显示设备分类信息树结构
    def display_sort(self):
        sort_infos = MachineSort.select(MachineSort.sort_id, MachineSort.sort_name).where(
            MachineSort.part_sort == None)  # 分类信息
        top_sort_data = [(i.sort_id, i.sort_name) for i in sort_infos]
        # print(top_sort_data)
        top_sort_name = [(i.sort_name) for i in sort_infos]  # 获取上级分类信息
        self.cb_prarent_sort.clear()  # 清空列表
        self.cb_prarent_sort.addItem('无')
        self.cb_prarent_sort.addItems(top_sort_name)  # 添加列表信息到上级分类菜单中
        # 遍历主分类
        for sort in top_sort_data:
            RootItem = QTreeWidgetItem()  # 定义根项
            RootItem.setText(0, str(sort[0]))  # 设置根项第一列内容
            RootItem.setText(1, str(sort[1]))  # 设置根项第二列内容
            self.tree_sort.addTopLevelItem(RootItem)  # 设置为顶层项
            # 遍历子分类
            child_sort_infos = MachineSort.select(MachineSort.sort_id, MachineSort.sort_name).where(
                MachineSort.part_sort == sort[0])  # 分类信息
            child_sort_data = [(i.sort_id, i.sort_name) for i in child_sort_infos]
            # print('子分类信息',child_sort_data)
            for child_item in child_sort_data:
                Child_Item = QTreeWidgetItem(RootItem)
                Child_Item.setText(2, str(child_item[0]))  # 设置第三列
                Child_Item.setText(3, child_item[1])  # 设置第四列
        self.tree_sort.expandItem(self.tree_sort.topLevelItem(0))
        self.tree_sort.setColumnWidth(0, 70)  # 设置第一列的宽度
        self.tree_sort.setColumnWidth(2, 80)  # 设置第三列的宽度
        self.tree_sort.resizeColumnToContents(3)  # 自动设置第4列列宽

    # 添加分类信息
    def add_sort(self):
        print('状态', self.modify_item, self.old_sort_data)
        if self.modify_item is None and self.old_sort_data is None:         # 修改模式，不能进行添加操作
            # 获取输入的id/分类名信息
            sort_id = self.le_sort_id.text().strip()
            sort_name = self.le_sort_name.text().strip()  # 获取输入的分类名称
            if sort_id and sort_name != '':
                sort_id = '{:0>4}'.format(self.le_sort_id.text().strip())  # 获取输入的分类id,将分类id格式化为4位长度，不足的前面补0
                # 判断是否作为父类，索引为0时创建父类，否则为子类
                if self.cb_prarent_sort.currentIndex() != 0:  # 索引不为0创建子类：即选择下菜菜单中其它父类
                    top_sort_id = MachineSort.get_or_none(
                        MachineSort.sort_name == self.cb_prarent_sort.currentText())  # 上级分类信息

                    # 从数据库中获取分类id及名称
                    new_sort_id = MachineSort.get_or_none(
                        MachineSort.sort_id == str(top_sort_id) + sort_id)  # 新分类id str(top_sort_id)+sort_id
                    new_sort_name = MachineSort.get_or_none(MachineSort.sort_name == sort_name)  # 当前新分类名, sort_name
                    # print('新ID是否存在：', new_sort_id, '分类名', new_sort_name)
                    # 判断数据库中分类ID和分类名称与输入的是否重复
                    if new_sort_id or new_sort_name is not None:
                        QtWidgets.QMessageBox.warning(self, '添加分类信息', '分类ID或分类名称重复，请重新输入！')
                    else:
                        # 不重复：作为子类添加到列表及数据库中
                        try:
                            MachineSort.insert_many(
                                [(str(top_sort_id) + sort_id, sort_name, top_sort_id, self.cb_prarent_sort.currentText())],
                                fields=(MachineSort.sort_id, MachineSort.sort_name, MachineSort.part_sort,
                                        MachineSort.part_sort_name)).execute()

                        except Exception as e:
                            print('添加子分类错误：', e)
                        else:
                            print('上级分类id:', top_sort_id)
                            item = self.tree_sort.findItems(str(top_sort_id), Qt.MatchExactly)  # 获取父类在树中的位置,返回的为一个列表
                            # 展开当前项并添加到树中
                            self.tree_sort.expandItem(item[0])
                            child_item = QTreeWidgetItem(item[0])
                            child_item.setText(2, str(top_sort_id) + sort_id)  # 设置第三列
                            child_item.setText(3, sort_name)  # 设置第四列
                            QtWidgets.QMessageBox.information(self, '添加分类信息', '添加分类信息成功！')
                            self.tree_sort.setCurrentItem(child_item)  # 标记为当前选择项
                            # 置空输入框内容
                            self.cb_prarent_sort.setCurrentIndex(0)
                            self.le_sort_id.setText('')
                            self.le_sort_name.setText('')
                            self.tree_sort.setCurrentItem(None)         # 设置为非选择状态
                # 作为你父类创建,且sort_id必须大于1000
                else:
                    if int(sort_id) > 1000:
                        # print('没有选择上级分类')
                        # print('当前分类新id', sort_id)
                        # print('当前分类名', sort_name)
                        # 从数据库中获取分类id及名称
                        new_sort_id = MachineSort.get_or_none(
                            MachineSort.sort_id == sort_id)  # 新分类id sort_id
                        new_sort_name = MachineSort.get_or_none(MachineSort.sort_name == sort_name)  # 当前新分类名, sort_name
                        # print('新ID是否存在：', new_sort_id, '分类名', new_sort_name)
                        # 判断数据库中分类ID和分类名称与输入的是否重复
                        if new_sort_id or new_sort_name is not None:
                            QtWidgets.QMessageBox.warning(self, '添加分类信息', '分类ID或分类名称重复，请重新输入！')
                        else:
                            # 不重复：添加到列表及数据库中
                            try:
                                MachineSort.insert_many([(sort_id, sort_name)],
                                                        fields=(MachineSort.sort_id, MachineSort.sort_name)).execute()
                            except Exception as e:
                                print('添加分类错误：', e)
                            else:
                                # 添加到树中
                                top_item = QTreeWidgetItem()
                                top_item.setText(0, sort_id)  # 设置第一列
                                top_item.setText(1, sort_name)  # 设置第二列
                                self.tree_sort.addTopLevelItem(top_item)  # 设置为顶级项
                                QtWidgets.QMessageBox.information(self, '添加分类信息', '添加分类信息成功！')
                                self.tree_sort.setCurrentItem(top_item)  # 标记为当前选择项
                                self.cb_prarent_sort.addItem(sort_name)  # 添加至上级分类下拉菜单中
                                # 置空输入框内容
                                self.cb_prarent_sort.setCurrentIndex(0)
                                self.le_sort_id.setText('')
                                self.le_sort_name.setText('')
                                self.tree_sort.setCurrentItem(None)  # 设置为非选择状态
                    else:
                        QtWidgets.QMessageBox.warning(self, '添加分类信息', '主分类的ID应该大于1000！')
            else:
                print('请输入需要添加的分类ID及分类名称信息！')
        else:
            QtWidgets.QMessageBox.warning(self, '添加分类信息', '修改模式，不能进行添加操作！！')

    # 删除分类信息
    def del_sort(self):
        if self.modify_item is None and self.old_sort_data is None:   # 修改模式，不能进行删除操作
            item = self.tree_sort.currentItem()  # 获取当前选择的行项对象
            if item is not None:
                # 判断当前选择的项是否为父类
                if item.parent() is None:
                    # print('当前为父类，ID：',item.text(0))
                    # print('当前项的索引', self.tree_sort.indexOfTopLevelItem(item))
                    # print('子项数量：',item.childCount())
                    # 判断是否存在子项，存在时，不能删除当前主分类
                    if item.childCount() > 0:
                        QtWidgets.QMessageBox.warning(self, '删除分类信息', '存在子分类，不能删除！！')
                    # 没有子分类，# 从数据库中删除
                    else:
                        if QtWidgets.QMessageBox.question(self, '删除分类信息', '是否确定要删除该分类！') == QtWidgets.QMessageBox.Yes:
                            try:
                                MachineSort.delete().where(MachineSort.sort_id == item.text(0)).execute()
                                # print(result)  # 打印执行结果，为1时代表执行成功，0失败
                            except Exception as e:
                                print('删除分类错误：', e)
                            else:
                                self.tree_sort.takeTopLevelItem(self.tree_sort.indexOfTopLevelItem(item))  # 删除当前选择项
                                QtWidgets.QMessageBox.information(self, '删除成功', '删除分类成功！')
                                self.tree_sort.setCurrentItem(None)  # 设置为非选择状态
                        else:
                            pass
                else:
                    # print('当前为子分类，ID：',item.text(2))
                    # print('当前子项的索引', item.parent().indexOfChild(item))
                    # 从数据库中删除
                    if QtWidgets.QMessageBox.question(self, '删除分类信息', '是否确定要删除该分类！') == QtWidgets.QMessageBox.Yes:
                        try:
                            MachineSort.delete().where(MachineSort.sort_id == item.text(2)).execute()
                            # print(result)  # 打印执行结果，为1时代表执行成功，0失败
                        except Exception as e:
                            print('删除分类错误：', e)
                        else:
                            item.parent().takeChild(item.parent().indexOfChild(item))  # 删除当前选择项
                            QtWidgets.QMessageBox.information(self, '删除成功', '删除分类成功！')
                            self.tree_sort.setCurrentItem(None)  # 设置为非选择状态
                    else:
                        pass
            else:
                QtWidgets.QMessageBox.warning(self, '删除分类信息', '请先选择要删除的项，再点击删除按钮！！')
        else:
            QtWidgets.QMessageBox.warning(self, '删除分类信息', '修改模式，不能进行删除操作！！')

    # 双击分类进行修改模式
    def double_click_sort(self):
        """
        修改设备分类：先判断选择的是主分类还是子分类。
        主分类：判断是否有子分类，没有子分类时可以修改ID和分类名称，有子分类时则只能修改名称
        子分类：可以修改分类ID和名称
        :return:
        """
        item = self.tree_sort.currentItem()  # 获取当前选择的行项对象
        self.modify_item = item
        # 判断当前选择的项是否为父类
        if item.parent() is None:
            # 当前选择项为父类
            # print('当前为父类，ID：', item.text(0), item.text(1))
            # print('当前项的索引', self.tree_sort.indexOfTopLevelItem(item))
            # print('子项数量：', item.childCount())
            self.cb_prarent_sort.setCurrentIndex(0)  # 设置上级分类选择为无
            self.old_sort_data = (item.text(0), item.text(1))  # 定义需要修改的项
            self.cb_prarent_sort.setDisabled(True)  # 设置为不可选择
            # 判断是否存在子项，存在时，不能修改当前主分类的ID
            if item.childCount() > 0:
                # print('存在子分类，不能修改当前分类的ID,只能修改分类名称！！')
                self.le_sort_id.setDisabled(True)  # 设置为不可输入
                # 将树中获取的信息显示至输入框中
                self.le_sort_id.setText(item.text(0))  # 显示到id输入框
                self.le_sort_name.setText(item.text(1))  # 显示到分类名称输入框

            # 没有子分类，可以修改主分类ID和分类名称
            else:
                # 将树中获取的信息显示至输入框中
                self.le_sort_id.setDisabled(False)  # 设置为可输入
                self.le_sort_id.setText(item.text(0))  # 显示到id输入框
                self.le_sort_name.setText(item.text(1))  # 显示到分类名称输入框

        else:
            # 当前选择项为子类
            print('当前为子分类，ID：', item.text(2), item.text(3))
            print('当前子项的索引', item.parent().indexOfChild(item), '上级分类：', item.parent().text(1))
            self.le_sort_id.setDisabled(False)  # 设置为可输入
            # 将树中获取的信息显示至输入框中
            self.cb_prarent_sort.setCurrentText(item.parent().text(1))  # 设置上级分类为选择项的分类
            self.cb_prarent_sort.setDisabled(True)                      # 设置为不可选择
            self.le_sort_id.setText(item.text(2)[4:])  # 显示到id输入框
            self.le_sort_name.setText(item.text(3))  # 显示到分类名称输入框
            self.old_sort_data = (item.text(2), item.text(3))  # 定义需要修改的项的原ID

    # 修改分类ID
    # todo 修改后，上级分类下拉菜单名称不同时更新，待处理
    def modify_sort(self):
        # 获取输入框中值
        modify_sort_data = (self.le_sort_id.text(), self.le_sort_name.text())
        if QtWidgets.QMessageBox.question(self, '修改分类信息', '是否确定要修改该分类！') == QtWidgets.QMessageBox.Yes:
            # 判断是否为主分类
            if len(self.old_sort_data[0]) > 4:  # 为子分类
                modify_sort_data = (self.old_sort_data[0][:4] + self.le_sort_id.text(), self.le_sort_name.text())
                print('需要修改的数据信息：', modify_sort_data, '原始数据：', self.old_sort_data)
                # 判断是否与原数据一致
                if modify_sort_data != self.old_sort_data:
                    try:
                        MachineSort.update(sort_id=modify_sort_data[0],sort_name=modify_sort_data[1]).where(MachineSort.sort_id==self.old_sort_data[0]).execute()
                    except Exception as e:
                        print('执行修改分类错误：',e)
                    else:
                        self.modify_item.setText(2, modify_sort_data[0])  # 设置第三列值
                        self.modify_item.setText(3, modify_sort_data[1])  # 设置第四列值
                        QtWidgets.QMessageBox.information(self, '修改分类成功', '修改分类成功！')
                        self.cb_prarent_sort.setCurrentIndex(0)
                        self.le_sort_id.setDisabled(False)  # 设置为可编辑
                        self.cb_prarent_sort.setDisabled(False)  # 设置为可选择下拉菜单
                        self.le_sort_id.setText('')  # 设置分类ID为空
                        self.le_sort_name.setText('')  # 设置分类名称为空
                        self.modify_item = None  # 置空
                        self.old_sort_data = None  # 置空
                        self.tree_sort.setCurrentItem(None)         # 设置为非选择状态
                else:
                    QtWidgets.QMessageBox.warning(self, '修改分类信息', '分类名称或ID没有进行修改！')
            else:  # 为父类（上级分类）
                print('需要修改的数据信息：', modify_sort_data, '原始数据：', self.old_sort_data)
                # 判断是否与原数据一致
                if modify_sort_data != self.old_sort_data:
                    try:
                        MachineSort.update(sort_id=modify_sort_data[0],sort_name=modify_sort_data[1]).where(MachineSort.sort_id==self.old_sort_data[0]).execute()
                    except Exception as e:
                        print('执行修改分类错误：',e)
                    else:
                        self.modify_item.setText(0, modify_sort_data[0])  # 设置第一列值
                        self.modify_item.setText(1, modify_sort_data[1])  # 设置第二列值
                        QtWidgets.QMessageBox.information(self, '修改分类成功', '修改分类成功！')
                        self.cb_prarent_sort.setCurrentIndex(0)
                        self.le_sort_id.setDisabled(False)  # 设置为可编辑
                        self.cb_prarent_sort.setDisabled(False)  # 设置为可选择下拉菜单
                        self.le_sort_id.setText('')  # 设置分类ID为空
                        self.le_sort_name.setText('')  # 设置分类名称为空
                        self.modify_item = None  # 置空
                        self.old_sort_data = None  # 置空
                        self.tree_sort.setCurrentItem(None)  # 设置为非选择状态
                else:
                    QtWidgets.QMessageBox.warning(self, '修改分类信息', '分类名称或ID没有进行修改！')


    # 重新定义键盘esc键事件，退出修改模式
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            # 当在分类窗口时，退出修改模式
            if self.tabWidget.currentIndex() == 3:
                print('在设备分类窗口，按了ESC键')
                self.cb_prarent_sort.setCurrentIndex(0)
                self.le_sort_id.setDisabled(False)  # 设置为可编辑
                self.cb_prarent_sort.setDisabled(False)     # 设置为可选择下拉菜单
                self.le_sort_id.setText('')  # 设置分类ID为空
                self.le_sort_name.setText('')  # 设置分类名称为空
                self.modify_item = None  # 置空
                self.old_sort_data = None  # 置空
                self.tree_sort.setCurrentItem(None)  # 设置为非选择状态
            # 当在机柜管理窗口时，退出修改模式
            if self.tabWidget.currentIndex() == 1:
                print('在机柜管理窗口，按了ESC键')
                self.le_cab_name.setText('')  # 设置机柜名称为空
                self.le_cabinet_alias.setText('')  # 设置机柜别名为空
                self.le_U_count.setText('')  # 设置机柜别名为空
                self.ckb_is_used.setChecked(True)  # 设置为True
                self.modify_cabinet_id = None  # 置空
                self.tb_cabinet.setCurrentItem(None)  # 设置为非选择状态
        else:
            pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    base_win = UiBaseInfo()
    base_win.show()
    sys.exit(app.exec())
