# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machine_switch.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MachineSwitch(object):
    def setupUi(self, MachineSwitch):
        if not MachineSwitch.objectName():
            MachineSwitch.setObjectName(u"MachineSwitch")
        MachineSwitch.resize(1024, 768)
        self.horizontalLayout_3 = QHBoxLayout(MachineSwitch)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lb_status = QLabel(MachineSwitch)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setFrameShape(QFrame.Box)
        self.lb_status.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.lb_status, 6, 0, 1, 3)

        self.gbox_switch = QGroupBox(MachineSwitch)
        self.gbox_switch.setObjectName(u"gbox_switch")
        self.horizontalLayout = QHBoxLayout(self.gbox_switch)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.te_sw_remark = QTextEdit(self.gbox_switch)
        self.te_sw_remark.setObjectName(u"te_sw_remark")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.te_sw_remark.sizePolicy().hasHeightForWidth())
        self.te_sw_remark.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.te_sw_remark.setFont(font)

        self.gridLayout_2.addWidget(self.te_sw_remark, 2, 1, 1, 5)

        self.cb_sw_room = QComboBox(self.gbox_switch)
        self.cb_sw_room.addItem("")
        self.cb_sw_room.setObjectName(u"cb_sw_room")
        self.cb_sw_room.setFont(font)

        self.gridLayout_2.addWidget(self.cb_sw_room, 0, 1, 1, 1)

        self.bt_sw_commit = QPushButton(self.gbox_switch)
        self.bt_sw_commit.setObjectName(u"bt_sw_commit")
        self.bt_sw_commit.setFont(font)

        self.gridLayout_2.addWidget(self.bt_sw_commit, 2, 7, 1, 1)

        self.cb_sw_up_pos = QComboBox(self.gbox_switch)
        self.cb_sw_up_pos.setObjectName(u"cb_sw_up_pos")
        self.cb_sw_up_pos.setFont(font)

        self.gridLayout_2.addWidget(self.cb_sw_up_pos, 1, 3, 1, 1)

        self.cb_sw_cabinet = QComboBox(self.gbox_switch)
        self.cb_sw_cabinet.setObjectName(u"cb_sw_cabinet")
        self.cb_sw_cabinet.setFont(font)

        self.gridLayout_2.addWidget(self.cb_sw_cabinet, 0, 3, 1, 1)

        self.label_3 = QLabel(self.gbox_switch)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_9 = QLabel(self.gbox_switch)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)

        self.label = QLabel(self.gbox_switch)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.gbox_switch)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 1, 2, 1, 1)

        self.cb_sw_down_pos = QComboBox(self.gbox_switch)
        self.cb_sw_down_pos.setObjectName(u"cb_sw_down_pos")
        self.cb_sw_down_pos.setFont(font)

        self.gridLayout_2.addWidget(self.cb_sw_down_pos, 1, 1, 1, 1)

        self.label_8 = QLabel(self.gbox_switch)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 2, 1, 1)

        self.label_11 = QLabel(self.gbox_switch)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 4, 1, 1)

        self.le_sw_bmc_ip = QLineEdit(self.gbox_switch)
        self.le_sw_bmc_ip.setObjectName(u"le_sw_bmc_ip")
        self.le_sw_bmc_ip.setFont(font)

        self.gridLayout_2.addWidget(self.le_sw_bmc_ip, 1, 5, 1, 1)

        self.le_sw_mg_ip = QLineEdit(self.gbox_switch)
        self.le_sw_mg_ip.setObjectName(u"le_sw_mg_ip")
        self.le_sw_mg_ip.setFont(font)

        self.gridLayout_2.addWidget(self.le_sw_mg_ip, 0, 7, 1, 1)

        self.label_10 = QLabel(self.gbox_switch)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 6, 1, 1)

        self.label_13 = QLabel(self.gbox_switch)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_13, 0, 4, 1, 1)

        self.le_sw_machine_name = QLineEdit(self.gbox_switch)
        self.le_sw_machine_name.setObjectName(u"le_sw_machine_name")
        self.le_sw_machine_name.setFont(font)

        self.gridLayout_2.addWidget(self.le_sw_machine_name, 0, 5, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 2)
        self.gridLayout_2.setColumnStretch(6, 1)
        self.gridLayout_2.setColumnStretch(7, 2)

        self.horizontalLayout.addLayout(self.gridLayout_2)


        self.gridLayout_3.addWidget(self.gbox_switch, 4, 0, 1, 3)

        self.bt_switch = QPushButton(MachineSwitch)
        self.bt_switch.setObjectName(u"bt_switch")
        self.bt_switch.setFont(font)

        self.gridLayout_3.addWidget(self.bt_switch, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(308, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 3, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(288, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 2, 1, 1)

        self.tb_display = QTableWidget(MachineSwitch)
        if (self.tb_display.columnCount() < 14):
            self.tb_display.setColumnCount(14)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        if (self.tb_display.rowCount() < 8):
            self.tb_display.setRowCount(8)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_display.setItem(0, 0, __qtablewidgetitem14)
        self.tb_display.setObjectName(u"tb_display")
        self.tb_display.setStyleSheet(u"selection-background-color: rgb(255, 170, 0);")
        self.tb_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_display.setGridStyle(Qt.SolidLine)
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setRowCount(8)
        self.tb_display.horizontalHeader().setVisible(True)
        self.tb_display.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_display.horizontalHeader().setDefaultSectionSize(80)
        self.tb_display.verticalHeader().setVisible(False)
        self.tb_display.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_3.addWidget(self.tb_display, 2, 0, 1, 3)

        self.groupBox = QGroupBox(MachineSwitch)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rd_bmc_ip = QRadioButton(self.groupBox)
        self.rd_bmc_ip.setObjectName(u"rd_bmc_ip")
        self.rd_bmc_ip.setFont(font)

        self.gridLayout.addWidget(self.rd_bmc_ip, 1, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.cb_room = QComboBox(self.groupBox)
        self.cb_room.addItem("")
        self.cb_room.setObjectName(u"cb_room")
        self.cb_room.setFont(font)

        self.gridLayout.addWidget(self.cb_room, 0, 1, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font)

        self.gridLayout.addWidget(self.machine_name, 0, 3, 1, 2)

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")
        self.bt_select.setFont(font)

        self.gridLayout.addWidget(self.bt_select, 0, 8, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)

        self.cb_cabinet = QComboBox(self.groupBox)
        self.cb_cabinet.addItem("")
        self.cb_cabinet.setObjectName(u"cb_cabinet")
        self.cb_cabinet.setFont(font)

        self.gridLayout.addWidget(self.cb_cabinet, 1, 1, 1, 1)

        self.rd_mg_ip = QRadioButton(self.groupBox)
        self.rd_mg_ip.setObjectName(u"rd_mg_ip")
        self.rd_mg_ip.setFont(font)
        self.rd_mg_ip.setChecked(True)

        self.gridLayout.addWidget(self.rd_mg_ip, 1, 2, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        self.mg_ip.setFont(font)

        self.gridLayout.addWidget(self.mg_ip, 1, 4, 1, 1)

        self.cb_state = QComboBox(self.groupBox)
        self.cb_state.setObjectName(u"cb_state")
        self.cb_state.setFont(font)

        self.gridLayout.addWidget(self.cb_state, 1, 6, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lb_machine_name = QLabel(self.groupBox)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font)
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 0, 2, 1, 1)

        self.bt_clear = QPushButton(self.groupBox)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setFont(font)

        self.gridLayout.addWidget(self.bt_clear, 1, 7, 1, 1)

        self.le_sn = QLineEdit(self.groupBox)
        self.le_sn.setObjectName(u"le_sn")
        self.le_sn.setFont(font)

        self.gridLayout.addWidget(self.le_sn, 0, 6, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.gridLayout.setColumnStretch(7, 1)
        self.gridLayout.setColumnStretch(8, 2)

        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 3)

        self.lb_title = QLabel(MachineSwitch)
        self.lb_title.setObjectName(u"lb_title")
        font1 = QFont()
        font1.setPointSize(30)
        font1.setUnderline(False)
        self.lb_title.setFont(font1)
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lb_title, 0, 0, 1, 3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 2)
        self.gridLayout_3.setRowStretch(2, 6)
        self.gridLayout_3.setRowStretch(3, 1)
        self.gridLayout_3.setRowStretch(4, 2)
        self.gridLayout_3.setRowStretch(5, 1)

        self.horizontalLayout_3.addLayout(self.gridLayout_3)


        self.retranslateUi(MachineSwitch)

        QMetaObject.connectSlotsByName(MachineSwitch)
    # setupUi

    def retranslateUi(self, MachineSwitch):
        MachineSwitch.setWindowTitle(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u4f4d\u7f6e\u8c03\u6574", None))
        self.lb_status.setText(QCoreApplication.translate("MachineSwitch", u"\u72b6\u6001\u680f", None))
        self.gbox_switch.setTitle(QCoreApplication.translate("MachineSwitch", u"\u53d8\u66f4\u4fe1\u606f", None))
        self.cb_sw_room.setItemText(0, QCoreApplication.translate("MachineSwitch", u"\u6240\u6709", None))

        self.bt_sw_commit.setText(QCoreApplication.translate("MachineSwitch", u"\u63d0  \u4ea4", None))
        self.label_3.setText(QCoreApplication.translate("MachineSwitch", u"\u5907\u6ce8", None))
        self.label_9.setText(QCoreApplication.translate("MachineSwitch", u"\u673a  \u623f", None))
        self.label.setText(QCoreApplication.translate("MachineSwitch", u"\u4e0bU\u4f4d", None))
        self.label_2.setText(QCoreApplication.translate("MachineSwitch", u"\u4e0aU\u4f4d", None))
        self.label_8.setText(QCoreApplication.translate("MachineSwitch", u"\u673a  \u67dc", None))
        self.label_11.setText(QCoreApplication.translate("MachineSwitch", u"BMC IP", None))
        self.label_10.setText(QCoreApplication.translate("MachineSwitch", u"\u5e26\u5185IP", None))
        self.label_13.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_switch.setText(QCoreApplication.translate("MachineSwitch", u"\u8c03\u6574\u4f4d\u7f6e", None))
        ___qtablewidgetitem = self.tb_display.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem1 = self.tb_display.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MachineSwitch", u"\u673a\u623f", None));
        ___qtablewidgetitem2 = self.tb_display.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MachineSwitch", u"\u673a\u67dc", None));
        ___qtablewidgetitem3 = self.tb_display.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MachineSwitch", u"\u4e0bU\u4f4d", None));
        ___qtablewidgetitem4 = self.tb_display.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MachineSwitch", u"\u4e0aU\u4f4d", None));
        ___qtablewidgetitem5 = self.tb_display.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tb_display.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u5206\u7c7b", None));
        ___qtablewidgetitem7 = self.tb_display.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u5382\u5546", None));
        ___qtablewidgetitem8 = self.tb_display.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u578b\u53f7", None));
        ___qtablewidgetitem9 = self.tb_display.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MachineSwitch", u"\u5e8f\u5217\u53f7", None));
        ___qtablewidgetitem10 = self.tb_display.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MachineSwitch", u"\u8d1f\u8d23\u4eba", None));
        ___qtablewidgetitem11 = self.tb_display.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MachineSwitch", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem12 = self.tb_display.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MachineSwitch", u"\u5e26\u5916IP", None));
        ___qtablewidgetitem13 = self.tb_display.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MachineSwitch", u"\u5907\u6ce8", None));

        __sortingEnabled = self.tb_display.isSortingEnabled()
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setSortingEnabled(__sortingEnabled)

        self.groupBox.setTitle(QCoreApplication.translate("MachineSwitch", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.rd_bmc_ip.setText(QCoreApplication.translate("MachineSwitch", u"\u5e26\u5916IP", None))
        self.label_5.setText(QCoreApplication.translate("MachineSwitch", u"\u673a\u623f", None))
        self.cb_room.setItemText(0, QCoreApplication.translate("MachineSwitch", u"\u6240\u6709", None))

        self.bt_select.setText(QCoreApplication.translate("MachineSwitch", u"\u67e5\u8be2", None))
        self.label_7.setText(QCoreApplication.translate("MachineSwitch", u"\u8fd0\u884c\u72b6\u6001", None))
        self.cb_cabinet.setItemText(0, QCoreApplication.translate("MachineSwitch", u"\u6240\u6709", None))

        self.rd_mg_ip.setText(QCoreApplication.translate("MachineSwitch", u"\u7ba1\u7406IP", None))
        self.mg_ip.setText("")
        self.label_6.setText(QCoreApplication.translate("MachineSwitch", u"\u5e8f\u5217\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("MachineSwitch", u"\u673a\u67dc", None))
        self.lb_machine_name.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_clear.setText(QCoreApplication.translate("MachineSwitch", u"\u6e05\u7a7a", None))
        self.lb_title.setText(QCoreApplication.translate("MachineSwitch", u"\u8bbe\u5907\u4f4d\u7f6e\u8c03\u6574", None))
    # retranslateUi

