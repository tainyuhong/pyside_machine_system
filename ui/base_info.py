# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base_info.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_BaseInfo(object):
    def setupUi(self, BaseInfo):
        if not BaseInfo.objectName():
            BaseInfo.setObjectName(u"BaseInfo")
        BaseInfo.resize(782, 685)
        self.verticalLayout = QVBoxLayout(BaseInfo)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(BaseInfo)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_room = QWidget()
        self.tab_room.setObjectName(u"tab_room")
        self.verticalLayout_3 = QVBoxLayout(self.tab_room)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, -1, -1)
        self.label = QLabel(self.tab_room)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(5, 5, 6, -1)
        self.tb_room = QTableWidget(self.tab_room)
        if (self.tb_room.columnCount() < 3):
            self.tb_room.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_room.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_room.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_room.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tb_room.rowCount() < 8):
            self.tb_room.setRowCount(8)
        self.tb_room.setObjectName(u"tb_room")
        font1 = QFont()
        font1.setPointSize(12)
        self.tb_room.setFont(font1)
        self.tb_room.setAlternatingRowColors(True)
        self.tb_room.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_room.setRowCount(8)
        self.tb_room.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_room.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_room.horizontalHeader().setStretchLastSection(True)
        self.tb_room.verticalHeader().setVisible(False)
        self.tb_room.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tb_room, 0, 0, 6, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 0, 2, 1, 1)

        self.room_name = QLabel(self.tab_room)
        self.room_name.setObjectName(u"room_name")
        self.room_name.setFont(font1)
        self.room_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.room_name, 1, 1, 1, 1)

        self.le_room_name = QLineEdit(self.tab_room)
        self.le_room_name.setObjectName(u"le_room_name")
        self.le_room_name.setFont(font1)

        self.gridLayout.addWidget(self.le_room_name, 1, 2, 1, 2)

        self.room_name_alias = QLabel(self.tab_room)
        self.room_name_alias.setObjectName(u"room_name_alias")
        self.room_name_alias.setFont(font1)
        self.room_name_alias.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.room_name_alias, 2, 1, 1, 1)

        self.le_room_alias = QLineEdit(self.tab_room)
        self.le_room_alias.setObjectName(u"le_room_alias")
        self.le_room_alias.setFont(font1)

        self.gridLayout.addWidget(self.le_room_alias, 2, 2, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.bt_add_room = QPushButton(self.tab_room)
        self.bt_add_room.setObjectName(u"bt_add_room")
        self.bt_add_room.setFont(font1)

        self.gridLayout.addWidget(self.bt_add_room, 3, 2, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 1, 1, 1)

        self.bt_del_room = QPushButton(self.tab_room)
        self.bt_del_room.setObjectName(u"bt_del_room")
        self.bt_del_room.setFont(font1)

        self.gridLayout.addWidget(self.bt_del_room, 4, 2, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 5, 2, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 2)
        self.gridLayout.setColumnStretch(0, 5)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)

        self.verticalLayout_2.addLayout(self.gridLayout)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.tabWidget.addTab(self.tab_room, "")
        self.tab_cabinet = QWidget()
        self.tab_cabinet.setObjectName(u"tab_cabinet")
        self.verticalLayout_5 = QVBoxLayout(self.tab_cabinet)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, -1, -1, -1)
        self.label_4 = QLabel(self.tab_cabinet)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setContentsMargins(5, 6, 5, -1)
        self.tb_cabinet = QTableWidget(self.tab_cabinet)
        if (self.tb_cabinet.columnCount() < 6):
            self.tb_cabinet.setColumnCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_cabinet.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_cabinet.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_cabinet.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_cabinet.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_cabinet.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_cabinet.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        if (self.tb_cabinet.rowCount() < 15):
            self.tb_cabinet.setRowCount(15)
        self.tb_cabinet.setObjectName(u"tb_cabinet")
        self.tb_cabinet.setFont(font1)
        self.tb_cabinet.setAlternatingRowColors(True)
        self.tb_cabinet.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_cabinet.setRowCount(15)
        self.tb_cabinet.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_cabinet.horizontalHeader().setMinimumSectionSize(15)
        self.tb_cabinet.horizontalHeader().setDefaultSectionSize(80)
        self.tb_cabinet.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_cabinet.horizontalHeader().setStretchLastSection(True)
        self.tb_cabinet.verticalHeader().setVisible(False)
        self.tb_cabinet.verticalHeader().setDefaultSectionSize(28)
        self.tb_cabinet.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.tb_cabinet, 0, 0, 8, 1)

        self.lb_room_name = QLabel(self.tab_cabinet)
        self.lb_room_name.setObjectName(u"lb_room_name")
        self.lb_room_name.setFont(font1)
        self.lb_room_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_room_name, 1, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 5, 3, 1, 1)

        self.lb_cabinet_alias = QLabel(self.tab_cabinet)
        self.lb_cabinet_alias.setObjectName(u"lb_cabinet_alias")
        self.lb_cabinet_alias.setFont(font1)
        self.lb_cabinet_alias.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_cabinet_alias, 3, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 7, 2, 1, 1)

        self.bt_add_cabinet = QPushButton(self.tab_cabinet)
        self.bt_add_cabinet.setObjectName(u"bt_add_cabinet")
        self.bt_add_cabinet.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_add_cabinet, 5, 2, 1, 1)

        self.lb_cabinet_name = QLabel(self.tab_cabinet)
        self.lb_cabinet_name.setObjectName(u"lb_cabinet_name")
        self.lb_cabinet_name.setFont(font1)
        self.lb_cabinet_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_cabinet_name, 2, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 6, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 5, 1, 1, 1)

        self.bt_del_cabinet = QPushButton(self.tab_cabinet)
        self.bt_del_cabinet.setObjectName(u"bt_del_cabinet")
        self.bt_del_cabinet.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_del_cabinet, 6, 2, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_8, 6, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 2, 1, 1)

        self.cb_room = QComboBox(self.tab_cabinet)
        self.cb_room.setObjectName(u"cb_room")

        self.gridLayout_2.addWidget(self.cb_room, 1, 2, 1, 1)

        self.le_cab_name = QLineEdit(self.tab_cabinet)
        self.le_cab_name.setObjectName(u"le_cab_name")
        self.le_cab_name.setFont(font1)

        self.gridLayout_2.addWidget(self.le_cab_name, 2, 2, 1, 1)

        self.le_cabinet_alias = QLineEdit(self.tab_cabinet)
        self.le_cabinet_alias.setObjectName(u"le_cabinet_alias")
        self.le_cabinet_alias.setFont(font1)

        self.gridLayout_2.addWidget(self.le_cabinet_alias, 3, 2, 1, 1)

        self.ckb_is_used = QCheckBox(self.tab_cabinet)
        self.ckb_is_used.setObjectName(u"ckb_is_used")
        self.ckb_is_used.setFont(font1)

        self.gridLayout_2.addWidget(self.ckb_is_used, 4, 3, 1, 1)

        self.lb_count = QLabel(self.tab_cabinet)
        self.lb_count.setObjectName(u"lb_count")
        self.lb_count.setFont(font1)
        self.lb_count.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_count, 4, 1, 1, 1)

        self.le_U_count = QLineEdit(self.tab_cabinet)
        self.le_U_count.setObjectName(u"le_U_count")
        self.le_U_count.setFont(font1)

        self.gridLayout_2.addWidget(self.le_U_count, 4, 2, 1, 1)

        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setRowStretch(6, 1)
        self.gridLayout_2.setRowStretch(7, 2)
        self.gridLayout_2.setColumnStretch(0, 6)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 2)
        self.gridLayout_2.setColumnStretch(3, 1)

        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab_cabinet, "")
        self.tab_U = QWidget()
        self.tab_U.setObjectName(u"tab_U")
        self.verticalLayout_10 = QVBoxLayout(self.tab_U)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, -1, -1, -1)
        self.label_9 = QLabel(self.tab_U)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_9)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(15)
        self.gridLayout_3.setContentsMargins(5, 6, 5, -1)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_11, 3, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_9, 3, 3, 1, 1)

        self.le_u_name = QLineEdit(self.tab_U)
        self.le_u_name.setObjectName(u"le_u_name")
        self.le_u_name.setFont(font1)

        self.gridLayout_3.addWidget(self.le_u_name, 1, 2, 1, 1)

        self.bt_add_u = QPushButton(self.tab_U)
        self.bt_add_u.setObjectName(u"bt_add_u")
        self.bt_add_u.setFont(font1)

        self.gridLayout_3.addWidget(self.bt_add_u, 3, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_12, 4, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 0, 2, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_10, 4, 1, 1, 1)

        self.le_u_name_alias = QLineEdit(self.tab_U)
        self.le_u_name_alias.setObjectName(u"le_u_name_alias")
        self.le_u_name_alias.setFont(font1)

        self.gridLayout_3.addWidget(self.le_u_name_alias, 2, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 5, 2, 1, 1)

        self.tb_u = QTableWidget(self.tab_U)
        if (self.tb_u.columnCount() < 3):
            self.tb_u.setColumnCount(3)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_u.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_u.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_u.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        if (self.tb_u.rowCount() < 15):
            self.tb_u.setRowCount(15)
        self.tb_u.setObjectName(u"tb_u")
        self.tb_u.setFont(font1)
        self.tb_u.setAlternatingRowColors(True)
        self.tb_u.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_u.setRowCount(15)
        self.tb_u.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_u.horizontalHeader().setMinimumSectionSize(15)
        self.tb_u.horizontalHeader().setDefaultSectionSize(80)
        self.tb_u.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_u.horizontalHeader().setStretchLastSection(True)
        self.tb_u.verticalHeader().setVisible(False)
        self.tb_u.verticalHeader().setDefaultSectionSize(28)
        self.tb_u.verticalHeader().setStretchLastSection(False)

        self.gridLayout_3.addWidget(self.tb_u, 0, 0, 6, 1)

        self.bt_del_u = QPushButton(self.tab_U)
        self.bt_del_u.setObjectName(u"bt_del_u")
        self.bt_del_u.setFont(font1)

        self.gridLayout_3.addWidget(self.bt_del_u, 4, 2, 1, 1)

        self.lb_u_name_alias = QLabel(self.tab_U)
        self.lb_u_name_alias.setObjectName(u"lb_u_name_alias")
        self.lb_u_name_alias.setFont(font1)
        self.lb_u_name_alias.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_u_name_alias, 2, 1, 1, 1)

        self.lb_u_name = QLabel(self.tab_U)
        self.lb_u_name.setObjectName(u"lb_u_name")
        self.lb_u_name.setFont(font1)
        self.lb_u_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_u_name, 1, 1, 1, 1)

        self.gridLayout_3.setRowStretch(0, 2)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setRowStretch(5, 2)
        self.gridLayout_3.setColumnStretch(0, 4)
        self.gridLayout_3.setColumnStretch(1, 1)
        self.gridLayout_3.setColumnStretch(2, 2)
        self.gridLayout_3.setColumnStretch(3, 1)

        self.verticalLayout_6.addLayout(self.gridLayout_3)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 3)

        self.verticalLayout_10.addLayout(self.verticalLayout_6)

        self.tabWidget.addTab(self.tab_U, "")
        self.tab_sort = QWidget()
        self.tab_sort.setObjectName(u"tab_sort")
        self.verticalLayout_9 = QVBoxLayout(self.tab_sort)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, -1, -1, -1)
        self.label_14 = QLabel(self.tab_sort)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_14)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(5, 6, -1, -1)
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_15, 4, 1, 1, 1)

        self.tree_sort = QTreeWidget(self.tab_sort)
        self.tree_sort.setObjectName(u"tree_sort")
        self.tree_sort.header().setStretchLastSection(True)

        self.gridLayout_4.addWidget(self.tree_sort, 0, 0, 7, 1)

        self.cb_prarent_sort = QComboBox(self.tab_sort)
        self.cb_prarent_sort.addItem("")
        self.cb_prarent_sort.setObjectName(u"cb_prarent_sort")
        self.cb_prarent_sort.setFont(font1)

        self.gridLayout_4.addWidget(self.cb_prarent_sort, 1, 2, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_16, 5, 3, 1, 1)

        self.lb_parent_sort = QLabel(self.tab_sort)
        self.lb_parent_sort.setObjectName(u"lb_parent_sort")
        self.lb_parent_sort.setFont(font1)
        self.lb_parent_sort.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_parent_sort, 1, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 0, 2, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_13, 4, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 6, 2, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_14, 5, 1, 1, 1)

        self.bt_add_sort = QPushButton(self.tab_sort)
        self.bt_add_sort.setObjectName(u"bt_add_sort")
        self.bt_add_sort.setFont(font1)

        self.gridLayout_4.addWidget(self.bt_add_sort, 4, 2, 1, 1)

        self.bt_del_sort = QPushButton(self.tab_sort)
        self.bt_del_sort.setObjectName(u"bt_del_sort")
        self.bt_del_sort.setFont(font1)

        self.gridLayout_4.addWidget(self.bt_del_sort, 5, 2, 1, 1)

        self.le_sort_name = QLineEdit(self.tab_sort)
        self.le_sort_name.setObjectName(u"le_sort_name")
        self.le_sort_name.setFont(font1)

        self.gridLayout_4.addWidget(self.le_sort_name, 3, 2, 1, 1)

        self.le_sort_id = QLineEdit(self.tab_sort)
        self.le_sort_id.setObjectName(u"le_sort_id")
        self.le_sort_id.setFont(font1)

        self.gridLayout_4.addWidget(self.le_sort_id, 2, 2, 1, 1)

        self.lb_sort_name = QLabel(self.tab_sort)
        self.lb_sort_name.setObjectName(u"lb_sort_name")
        self.lb_sort_name.setFont(font1)
        self.lb_sort_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_sort_name, 3, 1, 1, 1)

        self.lb_sort_id = QLabel(self.tab_sort)
        self.lb_sort_id.setObjectName(u"lb_sort_id")
        self.lb_sort_id.setFont(font1)
        self.lb_sort_id.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.lb_sort_id, 2, 1, 1, 1)

        self.gridLayout_4.setColumnStretch(0, 5)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setColumnStretch(3, 1)
        self.gridLayout_4.setColumnMinimumWidth(0, 2)
        self.gridLayout_4.setColumnMinimumWidth(1, 1)
        self.gridLayout_4.setColumnMinimumWidth(2, 1)
        self.gridLayout_4.setColumnMinimumWidth(3, 2)

        self.verticalLayout_7.addLayout(self.gridLayout_4)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 3)

        self.verticalLayout_9.addLayout(self.verticalLayout_7)

        self.tabWidget.addTab(self.tab_sort, "")
        self.tab_manufacturer = QWidget()
        self.tab_manufacturer.setObjectName(u"tab_manufacturer")
        self.verticalLayout_11 = QVBoxLayout(self.tab_manufacturer)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 5, -1, -1)
        self.label_19 = QLabel(self.tab_manufacturer)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_19)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(10)
        self.gridLayout_5.setVerticalSpacing(20)
        self.gridLayout_5.setContentsMargins(5, 6, 5, -1)
        self.bt_del_manufacturer = QPushButton(self.tab_manufacturer)
        self.bt_del_manufacturer.setObjectName(u"bt_del_manufacturer")
        self.bt_del_manufacturer.setFont(font1)

        self.gridLayout_5.addWidget(self.bt_del_manufacturer, 3, 2, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_17, 2, 3, 1, 1)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_18, 3, 1, 1, 1)

        self.bt_add_manufacturer = QPushButton(self.tab_manufacturer)
        self.bt_add_manufacturer.setObjectName(u"bt_add_manufacturer")
        self.bt_add_manufacturer.setFont(font1)

        self.gridLayout_5.addWidget(self.bt_add_manufacturer, 2, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_9, 4, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_10, 0, 2, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_20, 3, 3, 1, 1)

        self.tb_manfacturer = QTableWidget(self.tab_manufacturer)
        if (self.tb_manfacturer.columnCount() < 2):
            self.tb_manfacturer.setColumnCount(2)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_manfacturer.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_manfacturer.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        if (self.tb_manfacturer.rowCount() < 15):
            self.tb_manfacturer.setRowCount(15)
        self.tb_manfacturer.setObjectName(u"tb_manfacturer")
        self.tb_manfacturer.setFont(font1)
        self.tb_manfacturer.setAlternatingRowColors(True)
        self.tb_manfacturer.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_manfacturer.setRowCount(15)
        self.tb_manfacturer.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_manfacturer.horizontalHeader().setMinimumSectionSize(15)
        self.tb_manfacturer.horizontalHeader().setDefaultSectionSize(80)
        self.tb_manfacturer.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_manfacturer.horizontalHeader().setStretchLastSection(True)
        self.tb_manfacturer.verticalHeader().setVisible(False)
        self.tb_manfacturer.verticalHeader().setDefaultSectionSize(28)
        self.tb_manfacturer.verticalHeader().setStretchLastSection(False)

        self.gridLayout_5.addWidget(self.tb_manfacturer, 0, 0, 5, 1)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_19, 2, 1, 1, 1)

        self.le__manufacturer_name = QLineEdit(self.tab_manufacturer)
        self.le__manufacturer_name.setObjectName(u"le__manufacturer_name")
        self.le__manufacturer_name.setFont(font1)

        self.gridLayout_5.addWidget(self.le__manufacturer_name, 1, 2, 1, 1)

        self.lb_name = QLabel(self.tab_manufacturer)
        self.lb_name.setObjectName(u"lb_name")
        self.lb_name.setFont(font1)
        self.lb_name.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_name, 1, 1, 1, 1)

        self.gridLayout_5.setRowStretch(0, 2)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setRowStretch(2, 1)
        self.gridLayout_5.setRowStretch(3, 1)
        self.gridLayout_5.setRowStretch(4, 2)
        self.gridLayout_5.setColumnStretch(0, 5)

        self.verticalLayout_8.addLayout(self.gridLayout_5)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 3)

        self.verticalLayout_11.addLayout(self.verticalLayout_8)

        self.tabWidget.addTab(self.tab_manufacturer, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(BaseInfo)

        self.tabWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(BaseInfo)
    # setupUi

    def retranslateUi(self, BaseInfo):
        BaseInfo.setWindowTitle(QCoreApplication.translate("BaseInfo", u"\u57fa\u7840\u4fe1\u606f\u7ef4\u62a4", None))
        self.label.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u623f\u4fe1\u606f\u7ba1\u7406", None))
        ___qtablewidgetitem = self.tb_room.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BaseInfo", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tb_room.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u623f\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tb_room.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BaseInfo", u"\u522b\u540d", None));
        self.room_name.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u623f\u540d\u79f0", None))
        self.room_name_alias.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u623f\u522b\u540d", None))
        self.bt_add_room.setText(QCoreApplication.translate("BaseInfo", u"\u6dfb\u52a0", None))
        self.bt_del_room.setText(QCoreApplication.translate("BaseInfo", u"\u5220\u9664", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_room), QCoreApplication.translate("BaseInfo", u"\u673a\u623f\u7ba1\u7406", None))
        self.label_4.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u67dc\u4fe1\u606f\u7ba1\u7406", None))
        ___qtablewidgetitem3 = self.tb_cabinet.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BaseInfo", u"\u7f16\u53f7", None));
        ___qtablewidgetitem4 = self.tb_cabinet.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u623f", None));
        ___qtablewidgetitem5 = self.tb_cabinet.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u67dc\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tb_cabinet.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u67dc\u522b\u540d", None));
        ___qtablewidgetitem7 = self.tb_cabinet.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("BaseInfo", u"\u603bU\u6570", None));
        ___qtablewidgetitem8 = self.tb_cabinet.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("BaseInfo", u"\u662f\u5426\u4f7f\u7528", None));
        self.lb_room_name.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u623f\u540d\u79f0", None))
        self.lb_cabinet_alias.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u67dc\u522b\u540d", None))
        self.bt_add_cabinet.setText(QCoreApplication.translate("BaseInfo", u"\u6dfb\u52a0", None))
        self.lb_cabinet_name.setText(QCoreApplication.translate("BaseInfo", u"\u673a\u67dc\u540d\u79f0", None))
        self.bt_del_cabinet.setText(QCoreApplication.translate("BaseInfo", u"\u5220\u9664", None))
        self.ckb_is_used.setText(QCoreApplication.translate("BaseInfo", u"\u662f\u5426\u4f7f\u7528", None))
        self.lb_count.setText(QCoreApplication.translate("BaseInfo", u"\u603bU\u6570", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_cabinet), QCoreApplication.translate("BaseInfo", u"\u673a\u67dc\u7ba1\u7406", None))
        self.label_9.setText(QCoreApplication.translate("BaseInfo", u"U\u4f4d\u4fe1\u606f\u7ba1\u7406", None))
        self.bt_add_u.setText(QCoreApplication.translate("BaseInfo", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem9 = self.tb_u.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("BaseInfo", u"\u7f16\u53f7", None));
        ___qtablewidgetitem10 = self.tb_u.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("BaseInfo", u"U\u4f4d\u540d\u79f0", None));
        ___qtablewidgetitem11 = self.tb_u.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("BaseInfo", u"U\u4f4d\u522b\u540d", None));
        self.bt_del_u.setText(QCoreApplication.translate("BaseInfo", u"\u5220\u9664", None))
        self.lb_u_name_alias.setText(QCoreApplication.translate("BaseInfo", u"U\u4f4d\u522b\u540d", None))
        self.lb_u_name.setText(QCoreApplication.translate("BaseInfo", u"U\u4f4d\u540d\u79f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_U), QCoreApplication.translate("BaseInfo", u"U\u4f4d\u7ba1\u7406", None))
        self.label_14.setText(QCoreApplication.translate("BaseInfo", u"\u8bbe\u5907\u5206\u7c7b\u4fe1\u606f\u7ba1\u7406", None))
        ___qtreewidgetitem = self.tree_sort.headerItem()
        ___qtreewidgetitem.setText(3, QCoreApplication.translate("BaseInfo", u"\u4e0a\u7ea7\u5206\u7c7b\u540d\u79f0", None));
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("BaseInfo", u"\u4e0a\u7ea7\u5206\u7c7bID", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("BaseInfo", u"\u5206\u7c7b\u540d\u79f0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("BaseInfo", u"ID", None));
        self.cb_prarent_sort.setItemText(0, QCoreApplication.translate("BaseInfo", u"\u65e0", None))

        self.lb_parent_sort.setText(QCoreApplication.translate("BaseInfo", u"\u4e0a\u7ea7\u5206\u7c7b", None))
        self.bt_add_sort.setText(QCoreApplication.translate("BaseInfo", u"\u6dfb\u52a0", None))
        self.bt_del_sort.setText(QCoreApplication.translate("BaseInfo", u"\u5220\u9664", None))
        self.lb_sort_name.setText(QCoreApplication.translate("BaseInfo", u"\u5206\u7c7b\u540d\u79f0", None))
        self.lb_sort_id.setText(QCoreApplication.translate("BaseInfo", u"\u5206\u7c7bID", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sort), QCoreApplication.translate("BaseInfo", u"\u8bbe\u5907\u5206\u7c7b", None))
        self.label_19.setText(QCoreApplication.translate("BaseInfo", u"\u8bbe\u5907\u54c1\u724c\u4fe1\u606f", None))
        self.bt_del_manufacturer.setText(QCoreApplication.translate("BaseInfo", u"\u5220\u9664", None))
        self.bt_add_manufacturer.setText(QCoreApplication.translate("BaseInfo", u"\u6dfb\u52a0", None))
        ___qtablewidgetitem12 = self.tb_manfacturer.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("BaseInfo", u"\u7f16\u53f7", None));
        ___qtablewidgetitem13 = self.tb_manfacturer.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("BaseInfo", u"\u54c1\u724c\u540d\u79f0", None));
        self.lb_name.setText(QCoreApplication.translate("BaseInfo", u"\u54c1\u724c\u540d\u79f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_manufacturer), QCoreApplication.translate("BaseInfo", u"\u8bbe\u5907\u54c1\u724c", None))
    # retranslateUi

