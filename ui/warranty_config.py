# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warranty_config.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QComboBox,
    QDateEdit, QDateTimeEdit, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_WarrantyConfig(object):
    def setupUi(self, WarrantyConfig):
        if not WarrantyConfig.objectName():
            WarrantyConfig.setObjectName(u"WarrantyConfig")
        WarrantyConfig.resize(1024, 768)
        self.horizontalLayout = QHBoxLayout(WarrantyConfig)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lb_title = QLabel(WarrantyConfig)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setPointSize(30)
        font.setUnderline(False)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lb_title)

        self.groupBox = QGroupBox(WarrantyConfig)
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
        self.lb_machine_name = QLabel(self.groupBox)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        font1 = QFont()
        font1.setPointSize(12)
        self.lb_machine_name.setFont(font1)
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 0, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 5, 1, 1)

        self.le_machine_name = QLineEdit(self.groupBox)
        self.le_machine_name.setObjectName(u"le_machine_name")
        self.le_machine_name.setFont(font1)

        self.gridLayout.addWidget(self.le_machine_name, 0, 3, 1, 2)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 8, 1, 1)

        self.cb_sort = QComboBox(self.groupBox)
        self.cb_sort.setObjectName(u"cb_sort")
        self.cb_sort.setFont(font1)

        self.gridLayout.addWidget(self.cb_sort, 0, 6, 1, 2)

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")
        self.bt_select.setFont(font1)

        self.gridLayout.addWidget(self.bt_select, 0, 10, 1, 1)

        self.cb_room = QComboBox(self.groupBox)
        self.cb_room.addItem("")
        self.cb_room.setObjectName(u"cb_room")
        self.cb_room.setFont(font1)

        self.gridLayout.addWidget(self.cb_room, 0, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.cb_cabinet = QComboBox(self.groupBox)
        self.cb_cabinet.addItem("")
        self.cb_cabinet.setObjectName(u"cb_cabinet")
        self.cb_cabinet.setFont(font1)

        self.gridLayout.addWidget(self.cb_cabinet, 1, 1, 1, 1)

        self.rd_bmc_ip = QRadioButton(self.groupBox)
        self.rd_bmc_ip.setObjectName(u"rd_bmc_ip")
        self.rd_bmc_ip.setFont(font1)

        self.gridLayout.addWidget(self.rd_bmc_ip, 1, 3, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 1)

        self.bt_flush = QPushButton(self.groupBox)
        self.bt_flush.setObjectName(u"bt_flush")
        self.bt_flush.setFont(font1)
        self.bt_flush.setStyleSheet(u"color:rgb(255, 85, 0)")

        self.gridLayout.addWidget(self.bt_flush, 1, 10, 1, 1)

        self.le_sn = QLineEdit(self.groupBox)
        self.le_sn.setObjectName(u"le_sn")
        self.le_sn.setFont(font1)

        self.gridLayout.addWidget(self.le_sn, 1, 6, 1, 2)

        self.rd_mg_ip = QRadioButton(self.groupBox)
        self.rd_mg_ip.setObjectName(u"rd_mg_ip")
        self.rd_mg_ip.setFont(font1)
        self.rd_mg_ip.setChecked(True)

        self.gridLayout.addWidget(self.rd_mg_ip, 1, 2, 1, 1)

        self.le_ip = QLineEdit(self.groupBox)
        self.le_ip.setObjectName(u"le_ip")
        self.le_ip.setFont(font1)

        self.gridLayout.addWidget(self.le_ip, 1, 4, 1, 1)

        self.cb_manfactur = QComboBox(self.groupBox)
        self.cb_manfactur.setObjectName(u"cb_manfactur")
        self.cb_manfactur.setFont(font1)

        self.gridLayout.addWidget(self.cb_manfactur, 0, 9, 1, 1)

        self.cb_is_under = QComboBox(self.groupBox)
        self.cb_is_under.setObjectName(u"cb_is_under")
        self.cb_is_under.setFont(font1)

        self.gridLayout.addWidget(self.cb_is_under, 1, 9, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout.addWidget(self.label_2, 1, 8, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.gridLayout.setColumnStretch(7, 1)
        self.gridLayout.setColumnStretch(8, 1)
        self.gridLayout.setColumnStretch(9, 1)
        self.gridLayout.setColumnStretch(10, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.tb_display = QTableWidget(WarrantyConfig)
        if (self.tb_display.columnCount() < 16):
            self.tb_display.setColumnCount(16)
        if (self.tb_display.rowCount() < 8):
            self.tb_display.setRowCount(8)
        self.tb_display.setObjectName(u"tb_display")
        self.tb_display.setStyleSheet(u"selection-background-color: rgb(255, 170, 0);")
        self.tb_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_display.setGridStyle(Qt.SolidLine)
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setRowCount(8)
        self.tb_display.setColumnCount(16)
        self.tb_display.horizontalHeader().setDefaultSectionSize(80)
        self.tb_display.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.tb_display)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(WarrantyConfig)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_3 = QLabel(WarrantyConfig)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.lb_operator = QLabel(WarrantyConfig)
        self.lb_operator.setObjectName(u"lb_operator")
        self.lb_operator.setFont(font1)
        self.lb_operator.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_operator, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 4, 1, 1)

        self.bt_commit = QPushButton(WarrantyConfig)
        self.bt_commit.setObjectName(u"bt_commit")
        self.bt_commit.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_commit, 3, 4, 1, 1)

        self.cb_org = QComboBox(WarrantyConfig)
        self.cb_org.setObjectName(u"cb_org")
        self.cb_org.setFont(font1)

        self.gridLayout_2.addWidget(self.cb_org, 0, 1, 1, 1)

        self.dt_end = QDateEdit(WarrantyConfig)
        self.dt_end.setObjectName(u"dt_end")
        self.dt_end.setFont(font1)
        self.dt_end.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dt_end.setAcceptDrops(False)
        self.dt_end.setWrapping(False)
        self.dt_end.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dt_end.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.dt_end.setCurrentSection(QDateTimeEdit.YearSection)
        self.dt_end.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.dt_end, 1, 4, 1, 1)

        self.dt_start = QDateEdit(WarrantyConfig)
        self.dt_start.setObjectName(u"dt_start")
        self.dt_start.setFont(font1)
        self.dt_start.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.dt_start.setAcceptDrops(False)
        self.dt_start.setWrapping(False)
        self.dt_start.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dt_start.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.dt_start.setCurrentSection(QDateTimeEdit.YearSection)
        self.dt_start.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.dt_start, 1, 1, 1, 1)

        self.bt_select_all = QPushButton(WarrantyConfig)
        self.bt_select_all.setObjectName(u"bt_select_all")
        self.bt_select_all.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_select_all, 0, 3, 1, 1)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)

        self.verticalLayout.addLayout(self.gridLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lb_status = QLabel(WarrantyConfig)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setFrameShape(QFrame.Box)
        self.lb_status.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.lb_status)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 5)
        self.verticalLayout.setStretch(4, 2)

        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(WarrantyConfig)

        QMetaObject.connectSlotsByName(WarrantyConfig)
    # setupUi

    def retranslateUi(self, WarrantyConfig):
        WarrantyConfig.setWindowTitle(QCoreApplication.translate("WarrantyConfig", u"\u7ef4\u4fdd\u4fe1\u606f\u914d\u7f6e", None))
        self.lb_title.setText(QCoreApplication.translate("WarrantyConfig", u"\u7ef4\u4fdd\u4fe1\u606f\u914d\u7f6e", None))
        self.groupBox.setTitle(QCoreApplication.translate("WarrantyConfig", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.lb_machine_name.setText(QCoreApplication.translate("WarrantyConfig", u"\u8bbe\u5907\u540d\u79f0", None))
        self.label_7.setText(QCoreApplication.translate("WarrantyConfig", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.label.setText(QCoreApplication.translate("WarrantyConfig", u"\u8bbe\u5907\u54c1\u724c", None))
        self.bt_select.setText(QCoreApplication.translate("WarrantyConfig", u"\u67e5\u8be2", None))
        self.cb_room.setItemText(0, QCoreApplication.translate("WarrantyConfig", u"\u6240\u6709", None))

        self.label_5.setText(QCoreApplication.translate("WarrantyConfig", u"\u673a\u623f", None))
        self.cb_cabinet.setItemText(0, QCoreApplication.translate("WarrantyConfig", u"\u6240\u6709", None))

        self.rd_bmc_ip.setText(QCoreApplication.translate("WarrantyConfig", u"\u5e26\u5916IP", None))
        self.label_4.setText(QCoreApplication.translate("WarrantyConfig", u"\u673a\u67dc", None))
        self.label_6.setText(QCoreApplication.translate("WarrantyConfig", u"\u5e8f\u5217\u53f7", None))
#if QT_CONFIG(tooltip)
        self.bt_flush.setToolTip(QCoreApplication.translate("WarrantyConfig", u"\u5237\u65b0\u65b0\u4e0a\u67b6\u8bbe\u5907\u7ef4\u4fdd\u4fe1\u606f", None))
#endif // QT_CONFIG(tooltip)
        self.bt_flush.setText(QCoreApplication.translate("WarrantyConfig", u"\u5237\u65b0\u7ef4\u4fdd\u72b6\u6001", None))
        self.rd_mg_ip.setText(QCoreApplication.translate("WarrantyConfig", u"\u7ba1\u7406IP", None))
        self.le_ip.setText("")
        self.label_2.setText(QCoreApplication.translate("WarrantyConfig", u"\u7ef4\u4fdd\u72b6\u6001", None))
#if QT_CONFIG(tooltip)
        self.tb_display.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("WarrantyConfig", u"\u7ef4\u4fdd\u5355\u4f4d", None))
        self.label_3.setText(QCoreApplication.translate("WarrantyConfig", u"\u5f00\u59cb\u65f6\u95f4", None))
        self.lb_operator.setText(QCoreApplication.translate("WarrantyConfig", u"\u7ed3\u675f\u65f6\u95f4", None))
        self.bt_commit.setText(QCoreApplication.translate("WarrantyConfig", u"\u63d0  \u4ea4", None))
        self.bt_select_all.setText(QCoreApplication.translate("WarrantyConfig", u"\u5168\u9009", None))
        self.lb_status.setText(QCoreApplication.translate("WarrantyConfig", u"\u72b6\u6001\u680f", None))
    # retranslateUi

