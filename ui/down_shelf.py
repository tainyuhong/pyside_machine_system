# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'down_shelf.ui'
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
    QSpacerItem, QTableWidget, QTableWidgetItem, QTextEdit,
    QWidget)

class Ui_down_shelf(object):
    def setupUi(self, down_shelf):
        if not down_shelf.objectName():
            down_shelf.setObjectName(u"down_shelf")
        down_shelf.setWindowModality(Qt.WindowModal)
        down_shelf.resize(1024, 768)
        self.horizontalLayout = QHBoxLayout(down_shelf)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 6, 7, 1, 1)

        self.lb_title = QLabel(down_shelf)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setPointSize(30)
        font.setUnderline(False)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_title, 0, 0, 1, 8)

        self.lb_status = QLabel(down_shelf)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setFrameShape(QFrame.Box)
        self.lb_status.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.lb_status, 10, 0, 1, 8)

        self.lb_datetime = QLabel(down_shelf)
        self.lb_datetime.setObjectName(u"lb_datetime")
        font1 = QFont()
        font1.setPointSize(12)
        self.lb_datetime.setFont(font1)
        self.lb_datetime.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_datetime, 5, 4, 1, 1)

        self.groupBox = QGroupBox(down_shelf)
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
        self.rd_bmc_ip = QRadioButton(self.groupBox)
        self.rd_bmc_ip.setObjectName(u"rd_bmc_ip")
        self.rd_bmc_ip.setFont(font1)

        self.gridLayout.addWidget(self.rd_bmc_ip, 1, 3, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.cb_room = QComboBox(self.groupBox)
        self.cb_room.addItem("")
        self.cb_room.setObjectName(u"cb_room")
        self.cb_room.setFont(font1)

        self.gridLayout.addWidget(self.cb_room, 0, 1, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font1)

        self.gridLayout.addWidget(self.machine_name, 0, 3, 1, 2)

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")
        self.bt_select.setFont(font1)

        self.gridLayout.addWidget(self.bt_select, 0, 8, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 1, 5, 1, 1)

        self.cb_cabinet = QComboBox(self.groupBox)
        self.cb_cabinet.addItem("")
        self.cb_cabinet.setObjectName(u"cb_cabinet")
        self.cb_cabinet.setFont(font1)

        self.gridLayout.addWidget(self.cb_cabinet, 1, 1, 1, 1)

        self.rd_mg_ip = QRadioButton(self.groupBox)
        self.rd_mg_ip.setObjectName(u"rd_mg_ip")
        self.rd_mg_ip.setFont(font1)
        self.rd_mg_ip.setChecked(True)

        self.gridLayout.addWidget(self.rd_mg_ip, 1, 2, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        self.mg_ip.setFont(font1)

        self.gridLayout.addWidget(self.mg_ip, 1, 4, 1, 1)

        self.cb_state = QComboBox(self.groupBox)
        self.cb_state.setObjectName(u"cb_state")
        self.cb_state.setFont(font1)

        self.gridLayout.addWidget(self.cb_state, 1, 6, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 0, 5, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lb_machine_name = QLabel(self.groupBox)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font1)
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 0, 2, 1, 1)

        self.bt_clear = QPushButton(self.groupBox)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setFont(font1)

        self.gridLayout.addWidget(self.bt_clear, 1, 7, 1, 1)

        self.le_sn = QLineEdit(self.groupBox)
        self.le_sn.setObjectName(u"le_sn")
        self.le_sn.setFont(font1)

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


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 8)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 5, 3, 1, 1)

        self.le_down_operator = QLineEdit(down_shelf)
        self.le_down_operator.setObjectName(u"le_down_operator")
        self.le_down_operator.setFont(font1)

        self.gridLayout_2.addWidget(self.le_down_operator, 4, 5, 1, 2)

        self.horizontalSpacer = QSpacerItem(698, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 8, 0, 1, 6)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 9, 2, 1, 1)

        self.bt_donw_shelf = QPushButton(down_shelf)
        self.bt_donw_shelf.setObjectName(u"bt_donw_shelf")
        self.bt_donw_shelf.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_donw_shelf, 8, 6, 1, 1)

        self.comments = QTextEdit(down_shelf)
        self.comments.setObjectName(u"comments")
        self.comments.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.comments, 4, 1, 2, 2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 2, 1, 1)

        self.down_time = QDateEdit(down_shelf)
        self.down_time.setObjectName(u"down_time")
        self.down_time.setFont(font1)
        self.down_time.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.down_time.setAcceptDrops(False)
        self.down_time.setWrapping(False)
        self.down_time.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.down_time.setCorrectionMode(QAbstractSpinBox.CorrectToPreviousValue)
        self.down_time.setCurrentSection(QDateTimeEdit.YearSection)
        self.down_time.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.down_time, 5, 5, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(58, 26, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 8, 7, 1, 1)

        self.lb_operator = QLabel(down_shelf)
        self.lb_operator.setObjectName(u"lb_operator")
        self.lb_operator.setFont(font1)
        self.lb_operator.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_operator, 4, 4, 1, 1)

        self.tb_display = QTableWidget(down_shelf)
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
        self.tb_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tb_display.setGridStyle(Qt.SolidLine)
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setRowCount(8)
        self.tb_display.horizontalHeader().setDefaultSectionSize(80)
        self.tb_display.verticalHeader().setVisible(False)

        self.gridLayout_2.addWidget(self.tb_display, 2, 0, 1, 8)

        self.label_3 = QLabel(down_shelf)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 4, 0, 1, 1)

        self.label_8 = QLabel(down_shelf)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)

        self.cb_operate_state = QComboBox(down_shelf)
        self.cb_operate_state.setObjectName(u"cb_operate_state")
        self.cb_operate_state.setFont(font1)

        self.gridLayout_2.addWidget(self.cb_operate_state, 3, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 9)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(9, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayout_2.setColumnStretch(5, 1)
        self.gridLayout_2.setColumnStretch(6, 1)

        self.horizontalLayout.addLayout(self.gridLayout_2)

        QWidget.setTabOrder(self.machine_name, self.tb_display)
        QWidget.setTabOrder(self.tb_display, self.comments)
        QWidget.setTabOrder(self.comments, self.le_down_operator)
        QWidget.setTabOrder(self.le_down_operator, self.down_time)
        QWidget.setTabOrder(self.down_time, self.bt_donw_shelf)

        self.retranslateUi(down_shelf)

        QMetaObject.connectSlotsByName(down_shelf)
    # setupUi

    def retranslateUi(self, down_shelf):
        down_shelf.setWindowTitle(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u4e0b\u7ebf\u4e0b\u67b6\u7ba1\u7406", None))
        self.lb_title.setText(QCoreApplication.translate("down_shelf", u"\u8bbe \u5907\u4e0b \u7ebf/\u4e0b \u67b6 \u7ba1 \u7406", None))
        self.lb_status.setText(QCoreApplication.translate("down_shelf", u"\u72b6\u6001\u680f", None))
        self.lb_datetime.setText(QCoreApplication.translate("down_shelf", u"\u6267\u884c\u65f6\u95f4", None))
        self.groupBox.setTitle(QCoreApplication.translate("down_shelf", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.rd_bmc_ip.setText(QCoreApplication.translate("down_shelf", u"\u5e26\u5916IP", None))
        self.label_5.setText(QCoreApplication.translate("down_shelf", u"\u673a\u623f", None))
        self.cb_room.setItemText(0, QCoreApplication.translate("down_shelf", u"\u6240\u6709", None))

        self.bt_select.setText(QCoreApplication.translate("down_shelf", u"\u67e5\u8be2", None))
        self.label_7.setText(QCoreApplication.translate("down_shelf", u"\u8fd0\u884c\u72b6\u6001", None))
        self.cb_cabinet.setItemText(0, QCoreApplication.translate("down_shelf", u"\u6240\u6709", None))

        self.rd_mg_ip.setText(QCoreApplication.translate("down_shelf", u"\u7ba1\u7406IP", None))
        self.mg_ip.setText("")
        self.label_6.setText(QCoreApplication.translate("down_shelf", u"\u5e8f\u5217\u53f7", None))
        self.label_4.setText(QCoreApplication.translate("down_shelf", u"\u673a\u67dc", None))
        self.lb_machine_name.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_clear.setText(QCoreApplication.translate("down_shelf", u"\u6e05\u7a7a", None))
        self.bt_donw_shelf.setText(QCoreApplication.translate("down_shelf", u"\u63d0  \u4ea4", None))
        self.lb_operator.setText(QCoreApplication.translate("down_shelf", u"\u6267  \u884c  \u4eba", None))
        ___qtablewidgetitem = self.tb_display.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem1 = self.tb_display.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("down_shelf", u"\u673a\u623f", None));
        ___qtablewidgetitem2 = self.tb_display.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("down_shelf", u"\u673a\u67dc", None));
        ___qtablewidgetitem3 = self.tb_display.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("down_shelf", u"\u4e0bU\u4f4d", None));
        ___qtablewidgetitem4 = self.tb_display.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("down_shelf", u"\u4e0aU\u4f4d", None));
        ___qtablewidgetitem5 = self.tb_display.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tb_display.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u5206\u7c7b", None));
        ___qtablewidgetitem7 = self.tb_display.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u5382\u5546", None));
        ___qtablewidgetitem8 = self.tb_display.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u578b\u53f7", None));
        ___qtablewidgetitem9 = self.tb_display.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("down_shelf", u"\u5e8f\u5217\u53f7", None));
        ___qtablewidgetitem10 = self.tb_display.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("down_shelf", u"\u8d1f\u8d23\u4eba", None));
        ___qtablewidgetitem11 = self.tb_display.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("down_shelf", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem12 = self.tb_display.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("down_shelf", u"\u5e26\u5916IP", None));
        ___qtablewidgetitem13 = self.tb_display.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("down_shelf", u"\u5907\u6ce8", None));

        __sortingEnabled = self.tb_display.isSortingEnabled()
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("down_shelf", u"\u6267\u884c\u60c5\u51b5\u8bf4\u660e", None))
        self.label_8.setText(QCoreApplication.translate("down_shelf", u"\u5904\u7406\u65b9\u5f0f", None))
    # retranslateUi

