# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify.ui'
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
    QLabel, QLineEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_modify(object):
    def setupUi(self, modify):
        if not modify.objectName():
            modify.setObjectName(u"modify")
        modify.setWindowModality(Qt.WindowModal)
        modify.resize(1024, 768)
        self.horizontalLayout_2 = QHBoxLayout(modify)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_title = QLabel(modify)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setPointSize(30)
        font.setUnderline(False)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lb_title)

        self.groupBox = QGroupBox(modify)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_room = QComboBox(self.groupBox)
        self.cb_room.addItem("")
        self.cb_room.setObjectName(u"cb_room")
        font1 = QFont()
        font1.setPointSize(12)
        self.cb_room.setFont(font1)

        self.gridLayout.addWidget(self.cb_room, 0, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.bt_clear = QPushButton(self.groupBox)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setFont(font1)

        self.gridLayout.addWidget(self.bt_clear, 1, 7, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")
        self.bt_select.setFont(font1)

        self.gridLayout.addWidget(self.bt_select, 0, 7, 1, 1)

        self.cb_cabinet = QComboBox(self.groupBox)
        self.cb_cabinet.addItem("")
        self.cb_cabinet.setObjectName(u"cb_cabinet")
        self.cb_cabinet.setFont(font1)

        self.gridLayout.addWidget(self.cb_cabinet, 1, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.cb_sort = QComboBox(self.groupBox)
        self.cb_sort.setObjectName(u"cb_sort")
        self.cb_sort.setFont(font1)

        self.gridLayout.addWidget(self.cb_sort, 0, 3, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font1)

        self.gridLayout.addWidget(self.machine_name, 0, 6, 1, 1)

        self.rd_bmc_ip = QRadioButton(self.groupBox)
        self.rd_bmc_ip.setObjectName(u"rd_bmc_ip")
        self.rd_bmc_ip.setFont(font1)

        self.gridLayout.addWidget(self.rd_bmc_ip, 1, 5, 1, 1)

        self.le_sn = QLineEdit(self.groupBox)
        self.le_sn.setObjectName(u"le_sn")
        self.le_sn.setFont(font1)

        self.gridLayout.addWidget(self.le_sn, 1, 3, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        self.mg_ip.setFont(font1)

        self.gridLayout.addWidget(self.mg_ip, 1, 6, 1, 1)

        self.rd_mg_ip = QRadioButton(self.groupBox)
        self.rd_mg_ip.setObjectName(u"rd_mg_ip")
        self.rd_mg_ip.setFont(font1)
        self.rd_mg_ip.setChecked(True)

        self.gridLayout.addWidget(self.rd_mg_ip, 1, 4, 1, 1)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)

        self.lb_machine_name = QLabel(self.groupBox)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font1)
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 0, 4, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(6, 2)
        self.gridLayout.setColumnStretch(7, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.tb_display = QTableWidget(modify)
        if (self.tb_display.columnCount() < 21):
            self.tb_display.setColumnCount(21)
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
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_display.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        if (self.tb_display.rowCount() < 15):
            self.tb_display.setRowCount(15)
        self.tb_display.setObjectName(u"tb_display")
        self.tb_display.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setGridStyle(Qt.SolidLine)
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setRowCount(15)
        self.tb_display.setColumnCount(21)

        self.verticalLayout_2.addWidget(self.tb_display)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 10, -1, 15)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_modify = QPushButton(modify)
        self.bt_modify.setObjectName(u"bt_modify")
        self.bt_modify.setFont(font1)

        self.horizontalLayout.addWidget(self.bt_modify)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.bt_save = QPushButton(modify)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setFont(font1)

        self.horizontalLayout.addWidget(self.bt_save)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.lb_status = QLabel(modify)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setFrameShape(QFrame.Box)
        self.lb_status.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.lb_status)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 9)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.retranslateUi(modify)

        QMetaObject.connectSlotsByName(modify)
    # setupUi

    def retranslateUi(self, modify):
        modify.setWindowTitle(QCoreApplication.translate("modify", u"\u4fee\u6539\u8bbe\u5907\u4fe1\u606f", None))
        self.lb_title.setText(QCoreApplication.translate("modify", u"\u4fee\u6539\u8bbe\u5907\u4fe1\u606f", None))
        self.groupBox.setTitle(QCoreApplication.translate("modify", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.cb_room.setItemText(0, QCoreApplication.translate("modify", u"\u6240\u6709", None))

        self.label.setText(QCoreApplication.translate("modify", u"\u673a\u623f", None))
        self.bt_clear.setText(QCoreApplication.translate("modify", u"\u6e05\u7a7a", None))
        self.label_2.setText(QCoreApplication.translate("modify", u"\u673a\u67dc", None))
        self.bt_select.setText(QCoreApplication.translate("modify", u"\u67e5\u8be2", None))
        self.cb_cabinet.setItemText(0, QCoreApplication.translate("modify", u"\u6240\u6709", None))

        self.label_3.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907\u5206\u7c7b", None))
        self.rd_bmc_ip.setText(QCoreApplication.translate("modify", u"\u5e26\u5916IP", None))
        self.mg_ip.setText("")
        self.rd_mg_ip.setText(QCoreApplication.translate("modify", u"\u5e26\u5185IP", None))
        self.label_4.setText(QCoreApplication.translate("modify", u"\u5e8f\u5217\u53f7", None))
        self.lb_machine_name.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907\u540d\u79f0", None))
        ___qtablewidgetitem = self.tb_display.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem1 = self.tb_display.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("modify", u"\u673a\u623f", None));
        ___qtablewidgetitem2 = self.tb_display.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("modify", u"\u673a\u67dc", None));
        ___qtablewidgetitem3 = self.tb_display.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("modify", u"\u4e0bU\u4f4d", None));
        ___qtablewidgetitem4 = self.tb_display.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("modify", u"\u4e0aU\u4f4d", None));
        ___qtablewidgetitem5 = self.tb_display.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem6 = self.tb_display.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907\u5206\u7c7b", None));
        ___qtablewidgetitem7 = self.tb_display.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907\u5382\u5546", None));
        ___qtablewidgetitem8 = self.tb_display.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("modify", u"\u8bbe\u5907\u578b\u53f7", None));
        ___qtablewidgetitem9 = self.tb_display.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("modify", u"\u5e8f\u5217\u53f7", None));
        ___qtablewidgetitem10 = self.tb_display.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("modify", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem11 = self.tb_display.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("modify", u"BMC IP", None));
        ___qtablewidgetitem12 = self.tb_display.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("modify", u"\u5e94\u7528IP", None));
        ___qtablewidgetitem13 = self.tb_display.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("modify", u"\u4e1a\u52a1\u7c7b\u578b", None));
        ___qtablewidgetitem14 = self.tb_display.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("modify", u"\u8fd0\u884c\u72b6\u6001", None));
        ___qtablewidgetitem15 = self.tb_display.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("modify", u"\u8d1f\u8d23\u4eba", None));
        ___qtablewidgetitem16 = self.tb_display.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("modify", u"\u5e94\u7528\u7ba1\u7406\u5458", None));
        ___qtablewidgetitem17 = self.tb_display.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("modify", u"\u51fa\u5382\u65e5\u671f", None));
        ___qtablewidgetitem18 = self.tb_display.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("modify", u"\u5230\u4fdd\u65e5\u671f", None));
        ___qtablewidgetitem19 = self.tb_display.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("modify", u"\u8d44\u4ea7\u7f16\u53f7", None));
        ___qtablewidgetitem20 = self.tb_display.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("modify", u"\u5907\u6ce8", None));
        self.bt_modify.setText(QCoreApplication.translate("modify", u"\u4fee    \u6539", None))
        self.bt_save.setText(QCoreApplication.translate("modify", u"\u4fdd\u5b58", None))
        self.lb_status.setText(QCoreApplication.translate("modify", u"\u72b6\u6001\u680f", None))
    # retranslateUi

