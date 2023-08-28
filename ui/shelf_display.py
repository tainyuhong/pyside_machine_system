# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shelf_display.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_shelf_display(object):
    def setupUi(self, shelf_display):
        if not shelf_display.objectName():
            shelf_display.setObjectName(u"shelf_display")
        shelf_display.resize(1024, 768)
        self.horizontalLayout_3 = QHBoxLayout(shelf_display)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tabWidget = QTabWidget(shelf_display)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setStyleSheet(u"")
        self.tab_up = QWidget()
        self.tab_up.setObjectName(u"tab_up")
        self.horizontalLayout = QHBoxLayout(self.tab_up)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.label = QLabel(self.tab_up)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 5)

        self.bt_up_select = QPushButton(self.tab_up)
        self.bt_up_select.setObjectName(u"bt_up_select")
        font1 = QFont()
        font1.setPointSize(12)
        self.bt_up_select.setFont(font1)

        self.gridLayout.addWidget(self.bt_up_select, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.tb_up = QTableWidget(self.tab_up)
        if (self.tb_up.columnCount() < 12):
            self.tb_up.setColumnCount(12)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_up.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        if (self.tb_up.rowCount() < 8):
            self.tb_up.setRowCount(8)
        self.tb_up.setObjectName(u"tb_up")
        self.tb_up.setAutoFillBackground(False)
        self.tb_up.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_up.setAlternatingRowColors(True)
        self.tb_up.setRowCount(8)
        self.tb_up.horizontalHeader().setDefaultSectionSize(80)

        self.gridLayout.addWidget(self.tb_up, 2, 0, 1, 5)

        self.lb_state_up = QLabel(self.tab_up)
        self.lb_state_up.setObjectName(u"lb_state_up")
        self.lb_state_up.setStyleSheet(u"color:blue")

        self.gridLayout.addWidget(self.lb_state_up, 3, 0, 1, 3)

        self.up_date = QDateEdit(self.tab_up)
        self.up_date.setObjectName(u"up_date")
        self.up_date.setEnabled(False)
        self.up_date.setFont(font1)
        self.up_date.setWrapping(False)
        self.up_date.setReadOnly(True)
        self.up_date.setCalendarPopup(True)

        self.gridLayout.addWidget(self.up_date, 1, 2, 1, 1)

        self.ckb_up = QCheckBox(self.tab_up)
        self.ckb_up.setObjectName(u"ckb_up")
        self.ckb_up.setFont(font1)

        self.gridLayout.addWidget(self.ckb_up, 1, 1, 1, 1)

        self.btn_export_up = QPushButton(self.tab_up)
        self.btn_export_up.setObjectName(u"btn_export_up")
        self.btn_export_up.setStyleSheet(u"color:blue")

        self.gridLayout.addWidget(self.btn_export_up, 3, 4, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 9)
        self.gridLayout.setColumnStretch(0, 3)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab_up, "")
        self.tab_down = QWidget()
        self.tab_down.setObjectName(u"tab_down")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_down)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 6, 6, 6)
        self.lb_state_down = QLabel(self.tab_down)
        self.lb_state_down.setObjectName(u"lb_state_down")
        self.lb_state_down.setStyleSheet(u"color:blue")

        self.gridLayout_2.addWidget(self.lb_state_down, 3, 0, 1, 3)

        self.label_3 = QLabel(self.tab_down)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 3, 1, 1)

        self.bt_down_select = QPushButton(self.tab_down)
        self.bt_down_select.setObjectName(u"bt_down_select")
        self.bt_down_select.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_down_select, 1, 4, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.down_date = QDateEdit(self.tab_down)
        self.down_date.setObjectName(u"down_date")
        self.down_date.setEnabled(False)
        self.down_date.setFont(font1)
        self.down_date.setWrapping(False)
        self.down_date.setReadOnly(True)
        self.down_date.setCalendarPopup(True)

        self.gridLayout_2.addWidget(self.down_date, 1, 2, 1, 1)

        self.tb_down = QTableWidget(self.tab_down)
        if (self.tb_down.columnCount() < 12):
            self.tb_down.setColumnCount(12)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(7, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(8, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(9, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(10, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_down.setHorizontalHeaderItem(11, __qtablewidgetitem23)
        if (self.tb_down.rowCount() < 8):
            self.tb_down.setRowCount(8)
        self.tb_down.setObjectName(u"tb_down")
        self.tb_down.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_down.setAlternatingRowColors(True)
        self.tb_down.setRowCount(8)
        self.tb_down.horizontalHeader().setDefaultSectionSize(80)

        self.gridLayout_2.addWidget(self.tb_down, 2, 0, 1, 5)

        self.ckb_down = QCheckBox(self.tab_down)
        self.ckb_down.setObjectName(u"ckb_down")
        self.ckb_down.setFont(font1)

        self.gridLayout_2.addWidget(self.ckb_down, 1, 1, 1, 1)

        self.btn_export_down = QPushButton(self.tab_down)
        self.btn_export_down.setObjectName(u"btn_export_down")
        self.btn_export_down.setStyleSheet(u"color:blue")

        self.gridLayout_2.addWidget(self.btn_export_down, 3, 4, 1, 1)

        self.bt_hand_over = QPushButton(self.tab_down)
        self.bt_hand_over.setObjectName(u"bt_hand_over")

        self.gridLayout_2.addWidget(self.bt_hand_over, 3, 3, 1, 1)

        self.gridLayout_2.setRowStretch(0, 2)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 9)
        self.gridLayout_2.setColumnStretch(0, 3)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tab_down, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.retranslateUi(shelf_display)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(shelf_display)
    # setupUi

    def retranslateUi(self, shelf_display):
        shelf_display.setWindowTitle(QCoreApplication.translate("shelf_display", u"\u4e0a\u4e0b\u67b6\u8bbe\u5907\u4fe1\u606f\u67e5\u8be2", None))
        self.label.setText(QCoreApplication.translate("shelf_display", u"\u4e0a\u67b6\u8bbe\u5907\u4fe1\u606f\u67e5\u8be2", None))
        self.bt_up_select.setText(QCoreApplication.translate("shelf_display", u"\u67e5  \u8be2", None))
        ___qtablewidgetitem = self.tb_up.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem1 = self.tb_up.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tb_up.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("shelf_display", u"\u4f4d\u7f6e", None));
        ___qtablewidgetitem3 = self.tb_up.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907\u54c1\u724c", None));
        ___qtablewidgetitem4 = self.tb_up.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907\u7c7b\u578b", None));
        ___qtablewidgetitem5 = self.tb_up.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("shelf_display", u"\u578b\u53f7", None));
        ___qtablewidgetitem6 = self.tb_up.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("shelf_display", u"\u5e8f\u5217\u53f7", None));
        ___qtablewidgetitem7 = self.tb_up.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("shelf_display", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem8 = self.tb_up.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("shelf_display", u"\u4e0a\u67b6\u65e5\u671f", None));
        ___qtablewidgetitem9 = self.tb_up.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("shelf_display", u"\u6267\u884c\u4eba", None));
        ___qtablewidgetitem10 = self.tb_up.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("shelf_display", u"\u7ba1\u7406\u5458", None));
        ___qtablewidgetitem11 = self.tb_up.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("shelf_display", u"\u5907\u6ce8", None));
        self.lb_state_up.setText(QCoreApplication.translate("shelf_display", u"\u5c31\u7eea", None))
        self.ckb_up.setText(QCoreApplication.translate("shelf_display", u"\u4e0a\u67b6\u65e5\u671f", None))
#if QT_CONFIG(tooltip)
        self.btn_export_up.setToolTip(QCoreApplication.translate("shelf_display", u"\u5bfc\u51faexcel", None))
#endif // QT_CONFIG(tooltip)
        self.btn_export_up.setText(QCoreApplication.translate("shelf_display", u"\u5bfc\u51fa\u4e0a\u67b6\u4fe1\u606f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_up), QCoreApplication.translate("shelf_display", u"\u4e0a\u67b6\u8bbe\u5907\u4fe1\u606f\u67e5\u8be2", None))
        self.lb_state_down.setText(QCoreApplication.translate("shelf_display", u"\u5c31\u7eea", None))
        self.label_3.setText(QCoreApplication.translate("shelf_display", u"\u4e0b\u67b6\u8bbe\u5907\u4fe1\u606f\u67e5\u8be2", None))
        self.bt_down_select.setText(QCoreApplication.translate("shelf_display", u"\u67e5  \u8be2", None))
        ___qtablewidgetitem12 = self.tb_down.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem13 = self.tb_down.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem14 = self.tb_down.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("shelf_display", u"\u4f4d\u7f6e", None));
        ___qtablewidgetitem15 = self.tb_down.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907\u54c1\u724c", None));
        ___qtablewidgetitem16 = self.tb_down.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("shelf_display", u"\u8bbe\u5907\u7c7b\u578b", None));
        ___qtablewidgetitem17 = self.tb_down.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("shelf_display", u"\u578b\u53f7", None));
        ___qtablewidgetitem18 = self.tb_down.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("shelf_display", u"\u5e8f\u5217\u53f7", None));
        ___qtablewidgetitem19 = self.tb_down.horizontalHeaderItem(7)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("shelf_display", u"IP", None));
        ___qtablewidgetitem20 = self.tb_down.horizontalHeaderItem(8)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("shelf_display", u"\u4e0b\u67b6\u65e5\u671f", None));
        ___qtablewidgetitem21 = self.tb_down.horizontalHeaderItem(9)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("shelf_display", u"\u6267\u884c\u4eba", None));
        ___qtablewidgetitem22 = self.tb_down.horizontalHeaderItem(10)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("shelf_display", u"\u7ba1\u7406\u5458", None));
        ___qtablewidgetitem23 = self.tb_down.horizontalHeaderItem(11)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("shelf_display", u"\u5907\u6ce8", None));
        self.ckb_down.setText(QCoreApplication.translate("shelf_display", u"\u4e0b\u67b6\u65e5\u671f", None))
#if QT_CONFIG(tooltip)
        self.btn_export_down.setToolTip(QCoreApplication.translate("shelf_display", u"\u5bfc\u51faexcel", None))
#endif // QT_CONFIG(tooltip)
        self.btn_export_down.setText(QCoreApplication.translate("shelf_display", u"\u5bfc\u51fa\u4e0b\u67b6\u4fe1\u606f", None))
        self.bt_hand_over.setText(QCoreApplication.translate("shelf_display", u"\u751f\u6210\u79fb\u4ea4\u6e05\u5355", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_down), QCoreApplication.translate("shelf_display", u"\u4e0b\u67b6\u8bbe\u5907\u4fe1\u606f\u67e5\u8be2", None))
    # retranslateUi

