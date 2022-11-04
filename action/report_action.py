import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCharts import QChart, QBarSeries, QBarSet, QBarCategoryAxis, QValueAxis, QAbstractBarSeries
from db.db_orm import *
from peewee import fn
from ui.report import Ui_report_form

# 机柜名称
room_data_model = MachineRoom.select(MachineRoom.room_name).order_by(MachineRoom.room_id).execute()
# 机房总数量
room = MachineRoom.select().count()
# 每个机房内机柜的数量，以元组方式展示
cabinet_count = Cabinet.select(Cabinet.room, fn.count(Cabinet.cab_name)).where(Cabinet.is_use == 1).group_by(
    Cabinet.room).execute()
# 机柜总数量
cabinet_count_list = [(i.room.room_name, i.cab_name) for i in cabinet_count]
# print('机柜总数量', cabinet_count_list)

# 有设备的机房总数量
use_room = MachineList.select(fn.Count(MachineList.room_name.distinct())).scalar()
# print(use_room)

# 每个机房内有设备的机柜数量
use_cabinet_count = MachineList.select(MachineList.room_name, fn.count(MachineList.cab_name.distinct())).group_by(
    MachineList.room_name).order_by(MachineList.room_name.desc()).order_by(MachineList.room_id).tuples().execute()
# 有设备的机柜列表
use_cabinet_count_list = [i for i in use_cabinet_count]


# print('有设备的机房机柜数量：', use_cabinet_count_list)

# # 每个机房有哪些机柜
# use_cabinet_name = MachineList.select(MachineList.room_name, MachineList.cab_name).group_by(MachineList.room_name,
#                                                                                             MachineList.cab_name).tuples()
# # 有设备的机柜名
# use_cabinet_name_list = [i for i in use_cabinet_name]
# print('有设备的机柜名：', use_cabinet_name_list)


# 展示页面
class MachineReport(Ui_report_form, QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MachineReport, self).__init__(parent)
        self.setupUi(self)  # 展示报告窗口页
        self.create_room_chart()  # 展示机房图表
        self.create_cabinet_chart()  # 展示机柜图表
        self.display_ma_count()  # 显示机柜内设备数量

    # 创建机房信息图表
    def create_room_chart(self):
        self.chart_room = QChart()
        self.chart_room.setTitle('机房图表信息')
        self.graph_room.setChart(self.chart_room)

        # 创建条状单元
        room_barset = QBarSet('总量')
        use_room_barset = QBarSet('使用量')
        # 设置条状单元数据
        room_barset.append([room])
        use_room_barset.append([use_room])

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
        axis_y.setRange(0, room + 1)
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

        room_name = []  # 机房名
        cabinet_data = []  # 机房机柜总量
        use_cabinet_data = []  # 机房机柜使用量

        # 按照机房的序列格式化生成机柜总量数据及有设备的机柜数据，对没有设备的机柜数据写0
        for i in room_data_model:
            room_name.append(i.room_name)
            # print('cabinet_count_list',cabinet_count_list)
            # 格式化生成机房机柜量数据
            for c in cabinet_count_list:  # cabinet_count_list [('ZB-1', 36), ('ZB-2', 22), ('ZB-3', 8), ('ZB-4', 11), ('CZ-1', 8), ('603', 22)]
                # print('机房名：',i.room_name,'CCCC',c)
                if i.room_name in dict(cabinet_count_list).keys() and c[0] == i.room_name:
                    cabinet_data.append(c[1])
                elif i.room_name not in dict(cabinet_count_list).keys():
                    cabinet_data.append(0)  # 如果机房中没有设备则设置数据为0
                    break
            # 格式化生成机房使用机柜量数据
            for u in use_cabinet_count_list:  # use_cabinet_count_list  [('ZB-4', 3), ('ZB-3', 1), ('ZB-2', 20), ('ZB-1', 32), ('CZ-1', 8), ('603', 1)]
                if i.room_name in dict(use_cabinet_count_list).keys() and i.room_name == u[0]:
                    use_cabinet_data.append(u[1])
                elif i.room_name not in dict(use_cabinet_count_list).keys():
                    use_cabinet_data.append(0)
                    break
        # print(room_name, cabinet_data, use_cabinet_data)

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
        axis_y.setRange(0, 38)
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
        for room in use_cabinet_count_list:
            # print(room.room_name)
            root = QtWidgets.QTreeWidgetItem()
            root.setText(0, room[0])  # 设置第一列文本
            root.setText(2, str(room[1]) + '个机柜')  # 设置第三列文本
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
                child_item.setText(1, cabinet[0])       # 设置第二列文本
                child_item.setText(2, str(cabinet[1]))      # 设置第三列文本


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    report_win = MachineReport()
    report_win.show()
    sys.exit(app.exec())
