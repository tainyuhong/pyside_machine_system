# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check_config_ui.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_check_config(object):
    def setupUi(self, check_config):
        if not check_config.objectName():
            check_config.setObjectName(u"check_config")
        check_config.resize(1024, 768)
        check_config.setStyleSheet(u"QHeaderView::section{ background-color: rgb(255,240,190)};")
        self.horizontalLayout = QHBoxLayout(check_config)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(check_config)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tabWidg_check = QTabWidget(check_config)
        self.tabWidg_check.setObjectName(u"tabWidg_check")
        font1 = QFont()
        font1.setPointSize(12)
        self.tabWidg_check.setFont(font1)
        self.tab_machine = QWidget()
        self.tab_machine.setObjectName(u"tab_machine")
        self.horizontalLayout_3 = QHBoxLayout(self.tab_machine)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_8, 6, 1, 1, 1)

        self.lb_check_status = QLabel(self.tab_machine)
        self.lb_check_status.setObjectName(u"lb_check_status")
        font2 = QFont()
        font2.setPointSize(9)
        self.lb_check_status.setFont(font2)
        self.lb_check_status.setFrameShape(QFrame.Box)
        self.lb_check_status.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.lb_check_status, 7, 0, 1, 7)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 5, 6, 1, 1)

        self.label_3 = QLabel(self.tab_machine)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(False)
        self.label_3.setFont(font3)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(698, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 5, 0, 1, 5)

        self.le_user = QLineEdit(self.tab_machine)
        self.le_user.setObjectName(u"le_user")

        self.gridLayout_2.addWidget(self.le_user, 3, 1, 1, 1)

        self.label_9 = QLabel(self.tab_machine)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"color:red")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 7)

        self.bt_add_check = QPushButton(self.tab_machine)
        self.bt_add_check.setObjectName(u"bt_add_check")
        self.bt_add_check.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_add_check, 5, 5, 1, 1)

        self.label_4 = QLabel(self.tab_machine)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 3, 4, 1, 1)

        self.tb_display = QTableWidget(self.tab_machine)
        if (self.tb_display.columnCount() < 9):
            self.tb_display.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.tb_display.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        if (self.tb_display.rowCount() < 8):
            self.tb_display.setRowCount(8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_display.setItem(0, 0, __qtablewidgetitem9)
        self.tb_display.setObjectName(u"tb_display")
        self.tb_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_display.setGridStyle(Qt.SolidLine)
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setRowCount(8)
        self.tb_display.horizontalHeader().setDefaultSectionSize(80)
        self.tb_display.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tb_display, 1, 0, 1, 7)

        self.cb_check_sort = QComboBox(self.tab_machine)
        self.cb_check_sort.addItem("")
        self.cb_check_sort.setObjectName(u"cb_check_sort")
        self.cb_check_sort.setFont(font1)

        self.gridLayout_2.addWidget(self.cb_check_sort, 3, 5, 1, 1)

        self.groupBox = QGroupBox(self.tab_machine)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font1)

        self.gridLayout.addWidget(self.machine_name, 0, 1, 1, 2)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        self.mg_ip.setFont(font1)

        self.gridLayout.addWidget(self.mg_ip, 0, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 1, 1, 1)

        self.bt_clear = QPushButton(self.groupBox)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setFont(font1)

        self.gridLayout.addWidget(self.bt_clear, 1, 2, 1, 1)

        self.lb_mgip = QLabel(self.groupBox)
        self.lb_mgip.setObjectName(u"lb_mgip")
        self.lb_mgip.setFont(font3)
        self.lb_mgip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mgip, 0, 3, 1, 1)

        self.lb_machine_name = QLabel(self.groupBox)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font3)
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 0, 0, 1, 1)

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")
        self.bt_select.setFont(font1)

        self.gridLayout.addWidget(self.bt_select, 1, 4, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)

        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 7)

        self.label_2 = QLabel(self.tab_machine)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 3, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 4, 1, 1, 1)

        self.le_passwd = QLineEdit(self.tab_machine)
        self.le_passwd.setObjectName(u"le_passwd")

        self.gridLayout_2.addWidget(self.le_passwd, 3, 3, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 8)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setRowStretch(6, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 1)

        self.horizontalLayout_3.addLayout(self.gridLayout_2)

        self.tabWidg_check.addTab(self.tab_machine, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.horizontalLayout_6 = QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 6, -1, -1)
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setStyleSheet(u"")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox_2.setFlat(False)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(15)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.query_machine_name = QLineEdit(self.groupBox_2)
        self.query_machine_name.setObjectName(u"query_machine_name")
        self.query_machine_name.setFont(font1)

        self.gridLayout_5.addWidget(self.query_machine_name, 0, 1, 1, 2)

        self.query_mg_ip = QLineEdit(self.groupBox_2)
        self.query_mg_ip.setObjectName(u"query_mg_ip")
        self.query_mg_ip.setFont(font1)

        self.gridLayout_5.addWidget(self.query_mg_ip, 0, 4, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 1, 1, 1, 1)

        self.bt_query_clear = QPushButton(self.groupBox_2)
        self.bt_query_clear.setObjectName(u"bt_query_clear")
        self.bt_query_clear.setFont(font1)

        self.gridLayout_5.addWidget(self.bt_query_clear, 1, 2, 1, 1)

        self.lb_mgip_2 = QLabel(self.groupBox_2)
        self.lb_mgip_2.setObjectName(u"lb_mgip_2")
        self.lb_mgip_2.setFont(font3)
        self.lb_mgip_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_mgip_2, 0, 3, 1, 1)

        self.lb_machine_name_2 = QLabel(self.groupBox_2)
        self.lb_machine_name_2.setObjectName(u"lb_machine_name_2")
        self.lb_machine_name_2.setFont(font3)
        self.lb_machine_name_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.lb_machine_name_2, 0, 0, 1, 1)

        self.bt_query_select = QPushButton(self.groupBox_2)
        self.bt_query_select.setObjectName(u"bt_query_select")
        self.bt_query_select.setFont(font1)

        self.gridLayout_5.addWidget(self.bt_query_select, 1, 4, 1, 1)

        self.bt_query_del = QPushButton(self.groupBox_2)
        self.bt_query_del.setObjectName(u"bt_query_del")
        self.bt_query_del.setFont(font1)

        self.gridLayout_5.addWidget(self.bt_query_del, 1, 3, 1, 1)

        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 2)
        self.gridLayout_5.setColumnStretch(2, 1)
        self.gridLayout_5.setColumnStretch(3, 1)
        self.gridLayout_5.setColumnStretch(4, 2)

        self.horizontalLayout_5.addLayout(self.gridLayout_5)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"color:red")

        self.verticalLayout_2.addWidget(self.label_8)

        self.tb_query_display = QTableWidget(self.tab)
        if (self.tb_query_display.columnCount() < 8):
            self.tb_query_display.setColumnCount(8)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.tb_query_display.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        if (self.tb_query_display.rowCount() < 8):
            self.tb_query_display.setRowCount(8)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_query_display.setItem(0, 1, __qtablewidgetitem18)
        self.tb_query_display.setObjectName(u"tb_query_display")
        self.tb_query_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_query_display.setAlternatingRowColors(True)
        self.tb_query_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_query_display.setGridStyle(Qt.SolidLine)
        self.tb_query_display.setSortingEnabled(False)
        self.tb_query_display.setRowCount(8)
        self.tb_query_display.horizontalHeader().setDefaultSectionSize(80)
        self.tb_query_display.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.tb_query_display)

        self.lb_query_check_status = QLabel(self.tab)
        self.lb_query_check_status.setObjectName(u"lb_query_check_status")
        self.lb_query_check_status.setFont(font2)
        self.lb_query_check_status.setFrameShape(QFrame.Box)
        self.lb_query_check_status.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.lb_query_check_status)


        self.horizontalLayout_6.addLayout(self.verticalLayout_2)

        self.tabWidg_check.addTab(self.tab, "")
        self.tab_shell_config = QWidget()
        self.tab_shell_config.setObjectName(u"tab_shell_config")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_shell_config)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(10)
        self.verticalSpacer_2 = QSpacerItem(20, 98, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 3, 2, 1)

        self.lb_shell_status = QLabel(self.tab_shell_config)
        self.lb_shell_status.setObjectName(u"lb_shell_status")
        self.lb_shell_status.setFont(font2)
        self.lb_shell_status.setFrameShape(QFrame.Box)
        self.lb_shell_status.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.lb_shell_status, 10, 0, 1, 5)

        self.bt_modify_shell = QPushButton(self.tab_shell_config)
        self.bt_modify_shell.setObjectName(u"bt_modify_shell")
        self.bt_modify_shell.setFont(font1)

        self.gridLayout_3.addWidget(self.bt_modify_shell, 4, 3, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 6, 3, 1, 1)

        self.text_shell = QPlainTextEdit(self.tab_shell_config)
        self.text_shell.setObjectName(u"text_shell")

        self.gridLayout_3.addWidget(self.text_shell, 2, 1, 5, 1)

        self.bt_add_shell = QPushButton(self.tab_shell_config)
        self.bt_add_shell.setObjectName(u"bt_add_shell")
        self.bt_add_shell.setFont(font1)

        self.gridLayout_3.addWidget(self.bt_add_shell, 3, 3, 1, 1)

        self.bt_del_shell = QPushButton(self.tab_shell_config)
        self.bt_del_shell.setObjectName(u"bt_del_shell")
        self.bt_del_shell.setFont(font1)

        self.gridLayout_3.addWidget(self.bt_del_shell, 5, 3, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 9, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 5, 2, 2, 1)

        self.tb_display_shell = QTableWidget(self.tab_shell_config)
        if (self.tb_display_shell.columnCount() < 3):
            self.tb_display_shell.setColumnCount(3)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.tb_display_shell.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.tb_display_shell.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.tb_display_shell.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        if (self.tb_display_shell.rowCount() < 8):
            self.tb_display_shell.setRowCount(8)
        self.tb_display_shell.setObjectName(u"tb_display_shell")
        self.tb_display_shell.setLineWidth(1)
        self.tb_display_shell.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display_shell.setAlternatingRowColors(True)
        self.tb_display_shell.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_display_shell.setRowCount(8)
        self.tb_display_shell.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_display_shell.horizontalHeader().setDefaultSectionSize(120)
        self.tb_display_shell.horizontalHeader().setStretchLastSection(True)
        self.tb_display_shell.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_3.addWidget(self.tb_display_shell, 8, 0, 1, 5)

        self.le_shell_name = QLineEdit(self.tab_shell_config)
        self.le_shell_name.setObjectName(u"le_shell_name")

        self.gridLayout_3.addWidget(self.le_shell_name, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 5, 4, 1, 1)

        self.label_5 = QLabel(self.tab_shell_config)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 0, 1, 1, 1)

        self.label_6 = QLabel(self.tab_shell_config)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_6, 4, 0, 1, 1)

        self.label_7 = QLabel(self.tab_shell_config)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"color:red")

        self.gridLayout_3.addWidget(self.label_7, 7, 1, 1, 3)

        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setRowStretch(4, 1)
        self.gridLayout_3.setRowStretch(5, 1)
        self.gridLayout_3.setRowStretch(6, 1)
        self.gridLayout_3.setRowStretch(7, 1)
        self.gridLayout_3.setRowStretch(8, 9)
        self.gridLayout_3.setRowStretch(9, 1)
        self.gridLayout_3.setColumnStretch(0, 2)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.gridLayout_3.setColumnStretch(3, 2)

        self.horizontalLayout_4.addLayout(self.gridLayout_3)

        self.tabWidg_check.addTab(self.tab_shell_config, "")

        self.verticalLayout.addWidget(self.tabWidg_check)


        self.horizontalLayout.addLayout(self.verticalLayout)

        QWidget.setTabOrder(self.tabWidg_check, self.machine_name)
        QWidget.setTabOrder(self.machine_name, self.mg_ip)
        QWidget.setTabOrder(self.mg_ip, self.bt_clear)
        QWidget.setTabOrder(self.bt_clear, self.bt_select)
        QWidget.setTabOrder(self.bt_select, self.tb_display)
        QWidget.setTabOrder(self.tb_display, self.le_user)
        QWidget.setTabOrder(self.le_user, self.le_passwd)
        QWidget.setTabOrder(self.le_passwd, self.cb_check_sort)
        QWidget.setTabOrder(self.cb_check_sort, self.bt_add_check)
        QWidget.setTabOrder(self.bt_add_check, self.query_machine_name)
        QWidget.setTabOrder(self.query_machine_name, self.query_mg_ip)
        QWidget.setTabOrder(self.query_mg_ip, self.bt_query_clear)
        QWidget.setTabOrder(self.bt_query_clear, self.bt_query_del)
        QWidget.setTabOrder(self.bt_query_del, self.bt_query_select)
        QWidget.setTabOrder(self.bt_query_select, self.tb_query_display)
        QWidget.setTabOrder(self.tb_query_display, self.le_shell_name)
        QWidget.setTabOrder(self.le_shell_name, self.text_shell)
        QWidget.setTabOrder(self.text_shell, self.bt_add_shell)
        QWidget.setTabOrder(self.bt_add_shell, self.bt_modify_shell)
        QWidget.setTabOrder(self.bt_modify_shell, self.bt_del_shell)
        QWidget.setTabOrder(self.bt_del_shell, self.tb_display_shell)

        self.retranslateUi(check_config)

        self.tabWidg_check.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(check_config)
    # setupUi

    def retranslateUi(self, check_config):
        check_config.setWindowTitle(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u4fe1\u606f\u7ef4\u62a4", None))
        self.label.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u4fe1\u606f\u7ef4\u62a4", None))
        self.lb_check_status.setText(QCoreApplication.translate("check_config", u"\u72b6\u6001\u680f", None))
        self.label_3.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u7528\u6237", None))
        self.label_9.setText(QCoreApplication.translate("check_config", u"\u67e5\u8be2\uff1a\u4e0d\u8f93\u5165\u6761\u4ef6\uff0c\u9ed8\u8ba4\u67e5\u8be2\u6240\u6709   \u6dfb\u52a0\uff1a\u5148\u9009\u62e9\u76f8\u5e94\u7684\u8bbe\u5907\uff08\u53ef\u4ee5\u591a\u9009\uff09\u8f93\u5165\u7528\u6237\u3001\u5bc6\u7801\u3001\u5de1\u68c0\u7c7b\u578b  ", None))
        self.bt_add_check.setText(QCoreApplication.translate("check_config", u"\u6dfb    \u52a0", None))
        self.label_4.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u7c7b\u578b", None))
        ___qtablewidgetitem = self.tb_display.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem1 = self.tb_display.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("check_config", u"\u673a\u623f", None));
        ___qtablewidgetitem2 = self.tb_display.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("check_config", u"\u673a\u67dc", None));
        ___qtablewidgetitem3 = self.tb_display.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("check_config", u"U\u4f4d", None));
        ___qtablewidgetitem4 = self.tb_display.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("check_config", u"U\u6570", None));
        ___qtablewidgetitem5 = self.tb_display.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tb_display.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("check_config", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem7 = self.tb_display.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907\u5382\u5546", None));
        ___qtablewidgetitem8 = self.tb_display.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907\u578b\u53f7", None));

        __sortingEnabled = self.tb_display.isSortingEnabled()
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setSortingEnabled(__sortingEnabled)

        self.cb_check_sort.setItemText(0, QCoreApplication.translate("check_config", u"\u65e0", None))

        self.groupBox.setTitle(QCoreApplication.translate("check_config", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.mg_ip.setText("")
        self.bt_clear.setText(QCoreApplication.translate("check_config", u"\u6e05\u7a7a", None))
        self.lb_mgip.setText(QCoreApplication.translate("check_config", u"\u7ba1\u7406 IP", None))
        self.lb_machine_name.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_select.setText(QCoreApplication.translate("check_config", u"\u67e5\u8be2", None))
        self.label_2.setText(QCoreApplication.translate("check_config", u"\u5bc6\u7801", None))
        self.tabWidg_check.setTabText(self.tabWidg_check.indexOf(self.tab_machine), QCoreApplication.translate("check_config", u"\u5de1\u68c0\u8bbe\u5907\u914d\u7f6e", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("check_config", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.query_mg_ip.setText("")
        self.bt_query_clear.setText(QCoreApplication.translate("check_config", u"\u6e05\u7a7a", None))
        self.lb_mgip_2.setText(QCoreApplication.translate("check_config", u"\u7ba1\u7406 IP", None))
        self.lb_machine_name_2.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_query_select.setText(QCoreApplication.translate("check_config", u"\u67e5\u8be2", None))
        self.bt_query_del.setText(QCoreApplication.translate("check_config", u"\u5220\u9664", None))
        self.label_8.setText(QCoreApplication.translate("check_config", u"\u5220\u9664\uff1a\u5728\u4e0b\u8868\u4e2d\u9009\u62e9\u76f8\u5e94\u7684\u884c\u518d\u70b9\u51fb\u5220\u9664\u6309\u94ae    \u67e5\u8be2\uff1a\u4e0d\u8f93\u5165\u6761\u4ef6\uff0c\u9ed8\u8ba4\u67e5\u8be2\u6240\u6709", None))
        ___qtablewidgetitem9 = self.tb_query_display.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("check_config", u"ID", None));
        ___qtablewidgetitem10 = self.tb_query_display.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem11 = self.tb_query_display.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("check_config", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem12 = self.tb_query_display.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("check_config", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem13 = self.tb_query_display.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u7528\u6237", None));
        ___qtablewidgetitem14 = self.tb_query_display.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("check_config", u"\u5bc6\u7801", None));
        ___qtablewidgetitem15 = self.tb_query_display.horizontalHeaderItem(6)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u5206\u7c7b", None));
        ___qtablewidgetitem16 = self.tb_query_display.horizontalHeaderItem(7)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0\u547d\u4ee4", None));

        __sortingEnabled1 = self.tb_query_display.isSortingEnabled()
        self.tb_query_display.setSortingEnabled(False)
        self.tb_query_display.setSortingEnabled(__sortingEnabled1)

        self.lb_query_check_status.setText(QCoreApplication.translate("check_config", u"\u72b6\u6001\u680f", None))
        self.tabWidg_check.setTabText(self.tabWidg_check.indexOf(self.tab), QCoreApplication.translate("check_config", u"\u5de1\u68c0\u8bbe\u5907\u67e5\u8be2/\u5220\u9664", None))
        self.lb_shell_status.setText(QCoreApplication.translate("check_config", u"\u72b6\u6001\u680f", None))
        self.bt_modify_shell.setText(QCoreApplication.translate("check_config", u"\u4fee  \u6539", None))
        self.bt_add_shell.setText(QCoreApplication.translate("check_config", u"\u6dfb  \u52a0", None))
        self.bt_del_shell.setText(QCoreApplication.translate("check_config", u"\u5220  \u9664", None))
        ___qtablewidgetitem17 = self.tb_display_shell.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("check_config", u"ID", None));
        ___qtablewidgetitem18 = self.tb_display_shell.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0shell\u540d\u79f0", None));
        ___qtablewidgetitem19 = self.tb_display_shell.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("check_config", u"Shell\u5185\u5bb9", None));
        self.label_5.setText(QCoreApplication.translate("check_config", u"\u5de1\u68c0shell\u540d\u79f0", None))
        self.label_6.setText(QCoreApplication.translate("check_config", u"Shell\u5185\u5bb9", None))
        self.label_7.setText(QCoreApplication.translate("check_config", u"\u5220\u9664\uff1a\u9009\u62e9\u4e0b\u9762\u8868\u683c\u4e2d\u76f8\u5e94\u7684\u884c\u518d\u70b9\u51fb\u76f8\u5e94\u6309\u94ae   \u4fee\u6539\uff1a\u53cc\u51fb\u9700\u8981\u4fee\u6539\u7684\u884c\uff0c\u4fee\u6539\u540e\u518d\u70b9\u51fb\u4fee\u6539\u6309\u94ae\uff0c\u6309ESC\u952e\u9000\u51fa\u4fee\u6539\u6a21\u5f0f", None))
        self.tabWidg_check.setTabText(self.tabWidg_check.indexOf(self.tab_shell_config), QCoreApplication.translate("check_config", u"\u5de1\u68c0\u547d\u4ee4\u914d\u7f6e", None))
    # retranslateUi

