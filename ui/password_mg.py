# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'password_mg.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_password_form(object):
    def setupUi(self, password_form):
        if not password_form.objectName():
            password_form.setObjectName(u"password_form")
        password_form.resize(1017, 768)
        self.horizontalLayout_2 = QHBoxLayout(password_form)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(password_form)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.tabWidget = QTabWidget(password_form)
        self.tabWidget.setObjectName(u"tabWidget")
        font1 = QFont()
        font1.setPointSize(12)
        self.tabWidget.setFont(font1)
        self.tabWidget.setAutoFillBackground(True)
        self.tab_display = QWidget()
        self.tab_display.setObjectName(u"tab_display")
        self.tab_display.setAutoFillBackground(True)
        self.horizontalLayout_3 = QHBoxLayout(self.tab_display)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 10, 10, 5)
        self.groupBox = QGroupBox(self.tab_display)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.le_display_ip = QLineEdit(self.groupBox)
        self.le_display_ip.setObjectName(u"le_display_ip")

        self.horizontalLayout.addWidget(self.le_display_ip)

        self.horizontalSpacer = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_select = QPushButton(self.groupBox)
        self.btn_select.setObjectName(u"btn_select")

        self.horizontalLayout.addWidget(self.btn_select)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.btn_show_pass = QPushButton(self.groupBox)
        self.btn_show_pass.setObjectName(u"btn_show_pass")

        self.horizontalLayout.addWidget(self.btn_show_pass)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addWidget(self.groupBox)

        self.tb_select = QTableWidget(self.tab_display)
        if (self.tb_select.columnCount() < 10):
            self.tb_select.setColumnCount(10)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_select.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        if (self.tb_select.rowCount() < 8):
            self.tb_select.setRowCount(8)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_select.setItem(0, 0, __qtablewidgetitem10)
        self.tb_select.setObjectName(u"tb_select")
        self.tb_select.setStyleSheet(u"QTableWidget QHeaderView::section{ background-color: rgb(255,228,181)};")
        self.tb_select.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_select.setAlternatingRowColors(True)
        self.tb_select.setRowCount(8)
        self.tb_select.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_select.horizontalHeader().setStretchLastSection(True)
        self.tb_select.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.tb_select)

        self.lb_status = QLabel(self.tab_display)
        self.lb_status.setObjectName(u"lb_status")
        font2 = QFont()
        font2.setPointSize(9)
        self.lb_status.setFont(font2)

        self.verticalLayout.addWidget(self.lb_status)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 5)

        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.tabWidget.addTab(self.tab_display, "")
        self.tab_config = QWidget()
        self.tab_config.setObjectName(u"tab_config")
        self.tab_config.setAutoFillBackground(True)
        self.verticalLayout_3 = QVBoxLayout(self.tab_config)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.grp_is_vm = QGroupBox(self.tab_config)
        self.grp_is_vm.setObjectName(u"grp_is_vm")
        self.grp_is_vm.setEnabled(True)
        self.grp_is_vm.setStyleSheet(u"QGroupBox:title {color: blue;}")
        self.grp_is_vm.setFlat(False)
        self.grp_is_vm.setCheckable(True)
        self.gridLayout_3 = QGridLayout(self.grp_is_vm)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.label_8 = QLabel(self.grp_is_vm)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.le_ip = QLineEdit(self.grp_is_vm)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setFont(font1)

        self.gridLayout_2.addWidget(self.le_ip, 0, 1, 1, 1)

        self.bt_select_mg = QPushButton(self.grp_is_vm)
        self.bt_select_mg.setObjectName(u"bt_select_mg")
        self.bt_select_mg.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_select_mg, 0, 2, 1, 1)

        self.tb_query_ma = QTableWidget(self.grp_is_vm)
        if (self.tb_query_ma.columnCount() < 6):
            self.tb_query_ma.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        if (self.tb_query_ma.rowCount() < 1):
            self.tb_query_ma.setRowCount(1)
        self.tb_query_ma.setObjectName(u"tb_query_ma")
        self.tb_query_ma.setStyleSheet(u"QTableWidget QHeaderView::section{ background-color: rgb(255,228,181)};")
        self.tb_query_ma.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_query_ma.setAlternatingRowColors(True)
        self.tb_query_ma.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_query_ma.setRowCount(1)
        self.tb_query_ma.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tb_query_ma, 1, 0, 1, 3)

        self.btn_current = QPushButton(self.grp_is_vm)
        self.btn_current.setObjectName(u"btn_current")
        self.btn_current.setFont(font1)

        self.gridLayout_2.addWidget(self.btn_current, 2, 2, 1, 1)

        self.lb_ma_conut = QLabel(self.grp_is_vm)
        self.lb_ma_conut.setObjectName(u"lb_ma_conut")
        self.lb_ma_conut.setStyleSheet(u"color:blue")

        self.gridLayout_2.addWidget(self.lb_ma_conut, 2, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 5)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 3)
        self.gridLayout_2.setColumnStretch(2, 2)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 5)

        self.verticalLayout_3.addWidget(self.grp_is_vm)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.le_password = QLineEdit(self.tab_config)
        self.le_password.setObjectName(u"le_password")
        self.le_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.le_password.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.le_password, 0, 3, 1, 1)

        self.label_6 = QLabel(self.tab_config)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)

        self.btn_add = QPushButton(self.tab_config)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout.addWidget(self.btn_add, 3, 2, 1, 2)

        self.label_5 = QLabel(self.tab_config)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.te_remark = QTextEdit(self.tab_config)
        self.te_remark.setObjectName(u"te_remark")

        self.gridLayout.addWidget(self.te_remark, 2, 1, 1, 5)

        self.label_3 = QLabel(self.tab_config)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.le_current_ip = QLineEdit(self.tab_config)
        self.le_current_ip.setObjectName(u"le_current_ip")
        self.le_current_ip.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.le_current_ip, 0, 5, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 2, 1, 1)

        self.le_user = QLineEdit(self.tab_config)
        self.le_user.setObjectName(u"le_user")
        self.le_user.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.le_user, 0, 1, 1, 1)

        self.label_4 = QLabel(self.tab_config)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tab_config)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)

        self.le_machine_name = QLineEdit(self.tab_config)
        self.le_machine_name.setObjectName(u"le_machine_name")
        self.le_machine_name.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.le_machine_name, 1, 1, 1, 1)

        self.label_9 = QLabel(self.tab_config)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)

        self.cb_room = QComboBox(self.tab_config)
        self.cb_room.setObjectName(u"cb_room")

        self.gridLayout.addWidget(self.cb_room, 1, 3, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 2)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 3)

        self.verticalLayout_3.addLayout(self.gridLayout)

        self.verticalLayout_3.setStretch(0, 4)
        self.verticalLayout_3.setStretch(1, 3)
        self.tabWidget.addTab(self.tab_config, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 10, 10, 5)
        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.groupBox_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.le_modify_display_ip = QLineEdit(self.groupBox_2)
        self.le_modify_display_ip.setObjectName(u"le_modify_display_ip")

        self.horizontalLayout_4.addWidget(self.le_modify_display_ip)

        self.horizontalSpacer_3 = QSpacerItem(152, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.btn_modify_select = QPushButton(self.groupBox_2)
        self.btn_modify_select.setObjectName(u"btn_modify_select")

        self.horizontalLayout_4.addWidget(self.btn_modify_select)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(2, 1)
        self.horizontalLayout_4.setStretch(3, 1)

        self.verticalLayout_4.addWidget(self.groupBox_2)

        self.tb_modify_select = QTableWidget(self.tab)
        if (self.tb_modify_select.columnCount() < 10):
            self.tb_modify_select.setColumnCount(10)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(7, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(8, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_modify_select.setHorizontalHeaderItem(9, __qtablewidgetitem26)
        if (self.tb_modify_select.rowCount() < 4):
            self.tb_modify_select.setRowCount(4)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_modify_select.setItem(0, 0, __qtablewidgetitem27)
        self.tb_modify_select.setObjectName(u"tb_modify_select")
        self.tb_modify_select.setStyleSheet(u"QTableWidget QHeaderView::section{ background-color: rgb(255,228,181)};")
        self.tb_modify_select.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_modify_select.setAlternatingRowColors(True)
        self.tb_modify_select.setRowCount(4)
        self.tb_modify_select.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_modify_select.horizontalHeader().setStretchLastSection(True)
        self.tb_modify_select.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.tb_modify_select)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(10)
        self.gridLayout_4.setContentsMargins(6, 6, 6, 6)
        self.le_modify_password = QLineEdit(self.tab)
        self.le_modify_password.setObjectName(u"le_modify_password")
        self.le_modify_password.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.le_modify_password.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.le_modify_password, 0, 3, 1, 1)

        self.label_11 = QLabel(self.tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)

        self.btn_modify = QPushButton(self.tab)
        self.btn_modify.setObjectName(u"btn_modify")

        self.gridLayout_4.addWidget(self.btn_modify, 3, 2, 1, 2)

        self.label_12 = QLabel(self.tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_12, 0, 2, 1, 1)

        self.te_modify_remark = QTextEdit(self.tab)
        self.te_modify_remark.setObjectName(u"te_modify_remark")

        self.gridLayout_4.addWidget(self.te_modify_remark, 2, 1, 1, 5)

        self.label_13 = QLabel(self.tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_13, 0, 4, 1, 1)

        self.le_modify_ip = QLineEdit(self.tab)
        self.le_modify_ip.setObjectName(u"le_modify_ip")
        self.le_modify_ip.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.le_modify_ip, 0, 5, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 4, 2, 1, 1)

        self.le_modify_user = QLineEdit(self.tab)
        self.le_modify_user.setObjectName(u"le_modify_user")
        self.le_modify_user.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.le_modify_user, 0, 1, 1, 1)

        self.label_14 = QLabel(self.tab)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_15 = QLabel(self.tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_15, 1, 0, 1, 1)

        self.le_modify_machine_name = QLineEdit(self.tab)
        self.le_modify_machine_name.setObjectName(u"le_modify_machine_name")
        self.le_modify_machine_name.setClearButtonEnabled(False)

        self.gridLayout_4.addWidget(self.le_modify_machine_name, 1, 1, 1, 1)

        self.label_16 = QLabel(self.tab)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_16, 1, 2, 1, 1)

        self.btn_del_pass = QPushButton(self.tab)
        self.btn_del_pass.setObjectName(u"btn_del_pass")

        self.gridLayout_4.addWidget(self.btn_del_pass, 3, 5, 1, 1)

        self.cb_modify_room = QComboBox(self.tab)
        self.cb_modify_room.setObjectName(u"cb_modify_room")

        self.gridLayout_4.addWidget(self.cb_modify_room, 1, 3, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setRowStretch(2, 1)
        self.gridLayout_4.setRowStretch(3, 1)
        self.gridLayout_4.setRowStretch(4, 1)
        self.gridLayout_4.setColumnStretch(0, 2)
        self.gridLayout_4.setColumnStretch(1, 2)
        self.gridLayout_4.setColumnStretch(2, 2)
        self.gridLayout_4.setColumnStretch(3, 2)
        self.gridLayout_4.setColumnStretch(4, 1)
        self.gridLayout_4.setColumnStretch(5, 3)

        self.verticalLayout_4.addLayout(self.gridLayout_4)

        self.lb_status_2 = QLabel(self.tab)
        self.lb_status_2.setObjectName(u"lb_status_2")
        self.lb_status_2.setFont(font2)

        self.verticalLayout_4.addWidget(self.lb_status_2)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 3)
        self.verticalLayout_4.setStretch(2, 5)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        QWidget.setTabOrder(self.tabWidget, self.le_display_ip)
        QWidget.setTabOrder(self.le_display_ip, self.btn_select)
        QWidget.setTabOrder(self.btn_select, self.btn_show_pass)
        QWidget.setTabOrder(self.btn_show_pass, self.tb_select)
        QWidget.setTabOrder(self.tb_select, self.grp_is_vm)
        QWidget.setTabOrder(self.grp_is_vm, self.le_ip)
        QWidget.setTabOrder(self.le_ip, self.bt_select_mg)
        QWidget.setTabOrder(self.bt_select_mg, self.tb_query_ma)
        QWidget.setTabOrder(self.tb_query_ma, self.btn_current)
        QWidget.setTabOrder(self.btn_current, self.le_user)
        QWidget.setTabOrder(self.le_user, self.le_password)
        QWidget.setTabOrder(self.le_password, self.le_current_ip)
        QWidget.setTabOrder(self.le_current_ip, self.le_machine_name)
        QWidget.setTabOrder(self.le_machine_name, self.te_remark)
        QWidget.setTabOrder(self.te_remark, self.btn_add)
        QWidget.setTabOrder(self.btn_add, self.le_modify_display_ip)
        QWidget.setTabOrder(self.le_modify_display_ip, self.btn_modify_select)
        QWidget.setTabOrder(self.btn_modify_select, self.tb_modify_select)
        QWidget.setTabOrder(self.tb_modify_select, self.le_modify_user)
        QWidget.setTabOrder(self.le_modify_user, self.le_modify_password)
        QWidget.setTabOrder(self.le_modify_password, self.le_modify_ip)
        QWidget.setTabOrder(self.le_modify_ip, self.le_modify_machine_name)
        QWidget.setTabOrder(self.le_modify_machine_name, self.te_modify_remark)
        QWidget.setTabOrder(self.te_modify_remark, self.btn_modify)
        QWidget.setTabOrder(self.btn_modify, self.btn_del_pass)

        self.retranslateUi(password_form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(password_form)
    # setupUi

    def retranslateUi(self, password_form):
        password_form.setWindowTitle(QCoreApplication.translate("password_form", u"\u5bc6\u7801\u7ba1\u7406\u6a21\u5757", None))
        self.label.setText(QCoreApplication.translate("password_form", u"\u5bc6\u7801\u7ba1\u7406", None))
        self.groupBox.setTitle(QCoreApplication.translate("password_form", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("password_form", u"I P", None))
#if QT_CONFIG(accessibility)
        self.le_display_ip.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_select.setToolTip(QCoreApplication.translate("password_form", u"\u9ed8\u8ba4\u67e5\u8be2\u6240\u6709", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_select.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_select.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_select.setText(QCoreApplication.translate("password_form", u"\u67e5  \u8be2", None))
        self.btn_show_pass.setText(QCoreApplication.translate("password_form", u"\u663e\u793a\u5bc6\u7801", None))
        ___qtablewidgetitem = self.tb_select.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("password_form", u"ID", None));
        ___qtablewidgetitem1 = self.tb_select.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tb_select.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("password_form", u"IP", None));
        ___qtablewidgetitem3 = self.tb_select.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("password_form", u"\u673a\u623f\u540d\u79f0", None));
        ___qtablewidgetitem4 = self.tb_select.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("password_form", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem5 = self.tb_select.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("password_form", u"\u5bc6\u7801", None));
        ___qtablewidgetitem6 = self.tb_select.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("password_form", u"SN", None));
        ___qtablewidgetitem7 = self.tb_select.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u7c7b\u578b", None));
        ___qtablewidgetitem8 = self.tb_select.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem9 = self.tb_select.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("password_form", u"\u5907\u6ce8", None));

        __sortingEnabled = self.tb_select.isSortingEnabled()
        self.tb_select.setSortingEnabled(False)
        self.tb_select.setSortingEnabled(__sortingEnabled)

        self.lb_status.setText(QCoreApplication.translate("password_form", u"\u5c31\u7eea", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_display), QCoreApplication.translate("password_form", u"\u67e5\u770b\u5bc6\u7801", None))
        self.grp_is_vm.setTitle(QCoreApplication.translate("password_form", u"\u7269\u7406\u673a", None))
        self.label_8.setText(QCoreApplication.translate("password_form", u"I P", None))
        self.le_ip.setPlaceholderText(QCoreApplication.translate("password_form", u"\u8f93\u5165\u5e26\u5185\u6216\u5e26\u5916IP\u8fdb\u884c\u67e5\u8be2", None))
        self.bt_select_mg.setText(QCoreApplication.translate("password_form", u"\u67e5 \u8be2", None))
        ___qtablewidgetitem10 = self.tb_query_ma.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem11 = self.tb_query_ma.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem12 = self.tb_query_ma.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("password_form", u"\u673a\u623f", None));
        ___qtablewidgetitem13 = self.tb_query_ma.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("password_form", u"SN", None));
        ___qtablewidgetitem14 = self.tb_query_ma.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("password_form", u"\u5e26\u5185IP", None));
        ___qtablewidgetitem15 = self.tb_query_ma.horizontalHeaderItem(5)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("password_form", u"\u5e26\u5916IP", None));
#if QT_CONFIG(tooltip)
        self.tb_query_ma.setToolTip(QCoreApplication.translate("password_form", u"\u8bf7\u9009\u62e9\u9700\u8981\u6dfb\u52a0\u5bc6\u7801\u7684IP\u5355\u5143\u683c", None))
#endif // QT_CONFIG(tooltip)
        self.btn_current.setText(QCoreApplication.translate("password_form", u"\u9009 \u62e9", None))
        self.lb_ma_conut.setText("")
        self.le_password.setInputMask("")
        self.label_6.setText(QCoreApplication.translate("password_form", u"\u5907\u6ce8", None))
        self.btn_add.setText(QCoreApplication.translate("password_form", u"\u6dfb  \u52a0", None))
        self.label_5.setText(QCoreApplication.translate("password_form", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("password_form", u"   I P  ", None))
        self.label_4.setText(QCoreApplication.translate("password_form", u"\u7528\u6237\u540d", None))
        self.label_7.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u540d\u79f0", None))
        self.label_9.setText(QCoreApplication.translate("password_form", u"\u673a\u623f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("password_form", u"\u6dfb\u52a0\u8bbe\u5907\u5bc6\u7801", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("password_form", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.label_10.setText(QCoreApplication.translate("password_form", u"I P", None))
#if QT_CONFIG(accessibility)
        self.le_modify_display_ip.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(tooltip)
        self.btn_modify_select.setToolTip(QCoreApplication.translate("password_form", u"\u9ed8\u8ba4\u67e5\u8be2\u6240\u6709", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_modify_select.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.btn_modify_select.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_modify_select.setText(QCoreApplication.translate("password_form", u"\u67e5  \u8be2", None))
        ___qtablewidgetitem16 = self.tb_modify_select.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("password_form", u"ID", None));
        ___qtablewidgetitem17 = self.tb_modify_select.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem18 = self.tb_modify_select.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("password_form", u"IP", None));
        ___qtablewidgetitem19 = self.tb_modify_select.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("password_form", u"\u673a\u623f\u540d\u79f0", None));
        ___qtablewidgetitem20 = self.tb_modify_select.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("password_form", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem21 = self.tb_modify_select.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("password_form", u"\u5bc6\u7801", None));
        ___qtablewidgetitem22 = self.tb_modify_select.horizontalHeaderItem(6)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("password_form", u"SN", None));
        ___qtablewidgetitem23 = self.tb_modify_select.horizontalHeaderItem(7)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u7c7b\u578b", None));
        ___qtablewidgetitem24 = self.tb_modify_select.horizontalHeaderItem(8)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem25 = self.tb_modify_select.horizontalHeaderItem(9)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("password_form", u"\u5907\u6ce8", None));

        __sortingEnabled1 = self.tb_modify_select.isSortingEnabled()
        self.tb_modify_select.setSortingEnabled(False)
        self.tb_modify_select.setSortingEnabled(__sortingEnabled1)

#if QT_CONFIG(tooltip)
        self.tb_modify_select.setToolTip(QCoreApplication.translate("password_form", u"\u53cc\u51fb\u8fdb\u5165\u4fee\u6539\u6a21\u5f0f", None))
#endif // QT_CONFIG(tooltip)
        self.le_modify_password.setInputMask("")
        self.label_11.setText(QCoreApplication.translate("password_form", u"\u5907\u6ce8", None))
#if QT_CONFIG(tooltip)
        self.btn_modify.setToolTip(QCoreApplication.translate("password_form", u"\u4fdd\u5b58\u4fee\u6539", None))
#endif // QT_CONFIG(tooltip)
        self.btn_modify.setText(QCoreApplication.translate("password_form", u"\u4fee\u6539", None))
        self.label_12.setText(QCoreApplication.translate("password_form", u"\u5bc6\u7801", None))
        self.label_13.setText(QCoreApplication.translate("password_form", u"   I P  ", None))
        self.label_14.setText(QCoreApplication.translate("password_form", u"\u7528\u6237\u540d", None))
        self.label_15.setText(QCoreApplication.translate("password_form", u"\u8bbe\u5907\u540d\u79f0", None))
        self.label_16.setText(QCoreApplication.translate("password_form", u"\u673a\u623f", None))
#if QT_CONFIG(tooltip)
        self.btn_del_pass.setToolTip(QCoreApplication.translate("password_form", u"\u5148\u9009\u62e9\u9700\u8981\u5220\u9664\u7684\u884c", None))
#endif // QT_CONFIG(tooltip)
        self.btn_del_pass.setText(QCoreApplication.translate("password_form", u"\u5220\u9664", None))
        self.lb_status_2.setText(QCoreApplication.translate("password_form", u"\u5c31\u7eea", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("password_form", u"\u4fee\u6539/\u5220\u9664\u5bc6\u7801", None))
    # retranslateUi

