import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QAbstractBarSeries
from db.db_orm import *
from action.pub_infos import PubSwitch
from ui.report import Ui_report_form


# 展示页面
class MachineReport(Ui_report_form, QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(MachineReport, self).__init__(parent)
        self.setupUi(self)  # 展示报告窗口页
        self.pub_infos = PubSwitch()
        self.create_room_chart()  # 展示机房图表
        self.create_cabinet_chart()  # 展示机柜图表
        self.display_ma_count()  # 显示机柜内设备数量
        self.general()  # 显示概览信息

    # 创建机房信息图表
    def create_room_chart(self):
        self.chart_room = QChart()
        self.chart_room.setTitle('机房图表信息')
        self.graph_room.setChart(self.chart_room)

        # 创建条状单元
        room_barset = QBarSet('总量')
        use_room_barset = QBarSet('使用量')
        # 设置条状单元数据
        room_barset.append([self.get_room_info()[0]])  # 机房总数量
        use_room_barset.append([self.get_room_info()[1]])  # 使用的机房总数量

        # 创建条状图
        barseries = QBarSeries()
        # 将条状单元加入到条状图中
        barseries.append(room_barset)
        barseries.append(use_room_barset)

        # 将柱状图添加到图表展示窗口中
        self.chart_room.addSeries(barseries)
        self.chart_room.setAnimationOptions(QChart.SeriesAnimations)  # 设置成动画显示，默认无动画功能

        # 设置X轴  名称
        axis_x = QBarCategoryAxis()
        axis_x.append(['机房'])
        self.chart_room.addAxis(axis_x, QtCore.Qt.AlignBottom)
        barseries.attachAxis(axis_x)
        # 设置Y轴 数值
        axis_y = QValueAxis()
        axis_y.setLabelFormat('%d')  # 以整型显示刻度
        axis_y.setRange(0, self.get_room_info()[0] + 1)
        self.chart_room.addAxis(axis_y, QtCore.Qt.AlignLeft)
        barseries.attachAxis(axis_y)

        # self.chart_room.legend().setVisible(True)       # 显示图例，默认为显示
        self.chart_room.legend().setAlignment(QtCore.Qt.AlignRight)  # 在右部显示图例信息
        # 设置在柱状图中显示数值
        barseries.setLabelsVisible(True)
        barseries.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)
        room_barset.setLabelColor('blue')
        use_room_barset.setLabelColor('blue')

    # 创建机柜图表
    def create_cabinet_chart(self):
        cabinet_chart = QChart()
        cabinet_chart.setTitle('机柜图表信息')
        self.graph_cabinet.setChart(cabinet_chart)

        # room_name = []  # 机房名
        cabinet_data = []  # 机房机柜总量
        use_cabinet_data = []  # 机房机柜使用量

        # 按照机房的序列格式化生成机柜总量数据及有设备的机柜数据，对没有设备的机柜数据写0
        room_name = self.pub_infos.get_room().values()
        for i in self.pub_infos.get_room().values():
            # print('cabinet_count_list',cabinet_count_list)
            # 格式化生成机房机柜量数据
            cabinet_data.append(len(self.pub_infos.get_cabinet_infos(i)))
            # 格式化生成机房使用机柜量数据
            for u in self.get_room_info()[2]:
                if i in dict(self.get_room_info()[2]).keys() and i == u[0]:
                    use_cabinet_data.append(u[1])
                elif i not in dict(self.get_room_info()[2]).keys():
                    use_cabinet_data.append(0)  # 如果机房中没有设备则设置数据为0
                    break
        # print(room_name, cabinet_data, use_cabinet_data)
        # print(cabinet_data)
        # 创建条状图
        barseries = QBarSeries()
        # 将柱状图添加到图表展示窗口中
        cabinet_chart.addSeries(barseries)

        # 创建条状单元
        cabinet_barset = QBarSet('总量')
        use_cabinet_barset = QBarSet('使用量')

        # 将条状单元加入到条状图中
        barseries.append(cabinet_barset)
        barseries.append(use_cabinet_barset)

        # 设置X轴  名称
        axis_x = QBarCategoryAxis()
        axis_x.append(room_name)
        cabinet_chart.addAxis(axis_x, QtCore.Qt.AlignBottom)
        barseries.attachAxis(axis_x)
        # 设置Y轴 数值
        axis_y = QValueAxis()
        axis_y.setLabelFormat('%d')  # 以整型显示刻度
        axis_y.setRange(0, 56)
        cabinet_chart.addAxis(axis_y, QtCore.Qt.AlignLeft)
        barseries.attachAxis(axis_y)

        cabinet_chart.legend().setVisible(True)  # 显示图例，默认为显示
        cabinet_chart.legend().setAlignment(QtCore.Qt.AlignRight)  # 在底部显示图例信息
        cabinet_chart.setAnimationOptions(QChart.SeriesAnimations)  # 设置成动画显示，默认无动画功能
        # cabinet_chart.legend().setLabelColor('#1E90FF')     # 设置图例字体颜色

        # 设置在柱状图中显示数值
        barseries.setLabelsVisible(True)
        barseries.setLabelsPosition(QAbstractBarSeries.LabelsOutsideEnd)
        cabinet_barset.setLabelColor('blue')
        use_cabinet_barset.setLabelColor('blue')

        # 设置条状单元数据
        cabinet_barset.append(cabinet_data)
        use_cabinet_barset.append(use_cabinet_data)

    # 显示机柜内设备数据
    def display_ma_count(self):
        # 树形方式显示
        self.treeWidget.setColumnCount(3)  # 设置列数
        self.treeWidget.setHeaderLabels(['机房名称', '机柜名称', '设备数量'])
        self.treeWidget.setAlternatingRowColors(True)  # 每行颜色交叉显示
        # 根节点，机房名称做为根节点
        for room in self.get_room_info()[2]:
            # print(room.room_name)
            root = QtWidgets.QTreeWidgetItem()
            root.setText(0, room[0])  # 设置第一列文本
            root.setText(1, str(room[1]) + '个机柜')  # 设置第三列文本
            self.treeWidget.addTopLevelItem(root)  # 设置为根节点
            # 根据每个机房名--》查询机柜内设备数量
            machine_count = MachineList.select(MachineList.cab_name,
                                               fn.count(MachineList.cab_name)).where(
                MachineList.room_name == room[0]).group_by(MachineList.room_name,
                                                           MachineList.cab_name).order_by(
                MachineList.room_id, MachineList.cab_name).tuples()
            # 每个机柜内设备的数量
            machine_count_list = [i for i in machine_count]
            # print('每个机柜内设备的数量：', machine_count_list)
            # 子节点
            for cabinet in machine_count_list:
                child_item = QtWidgets.QTreeWidgetItem(root)
                # print(cabinet)
                child_item.setText(1, cabinet[0])  # 设置第二列文本：机柜名称
                child_item.setText(2, str(cabinet[1]))  # 设置第三列文本：设备数量

    # 机房信息获取
    def get_room_info(self):
        # 机房总数量
        room = MachineRoom.select().count()
        # 有设备的机房总数量
        use_room = MachineList.select(fn.Count(MachineList.room_name.distinct())).scalar()

        # 每个机房内有设备的机柜数量
        use_cabinet_count = MachineList.select(MachineList.room_name,
                                               fn.count(MachineList.cab_name.distinct())).group_by(
            MachineList.room_name).order_by(MachineList.room_name.desc()).order_by(
            MachineList.room_id).tuples().execute()
        # 有设备的机柜列表
        use_cabinet_count_list = [i for i in use_cabinet_count]
        return room, use_room, use_cabinet_count_list

    # 概览窗口显示内容
    def general(self):
        # 设备总数
        machine_count = MachineList.select().count()
        # 机柜总数量
        cab_count = Cabinet.select().where(Cabinet.is_use == 1).count()
        # 按设备分类查询每个分类的设备数量
        sort_num_model = MachineList.select(MachineList.machine_sort_name, fn.count(MachineList.machine_id)).group_by(
            MachineList.machine_sort_name).tuples()
        sort_num = []
        for i in sort_num_model:
            sort_num.append('\t{}：{}\r'.format(i[0], i[1]))
        # print(sort_num)
        text = '      总机房{} 个，在用机房{}个，在用机柜{}个，设备共{}台，各分类情况如下：\r{}'.format(
            self.get_room_info()[0], self.get_room_info()[1], cab_count, machine_count, ''.join(sort_num))
        self.textB_general.setFontPointSize(12)
        self.textB_general.setText(text)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    report_win = MachineReport()
    report_win.show()
    sys.exit(app.exec())
