# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_label.ui'
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
    QWidget)

class Ui_form_create(object):
    def setupUi(self, form_create):
        if not form_create.objectName():
            form_create.setObjectName(u"form_create")
        form_create.resize(1024, 768)
        self.horizontalLayout_2 = QHBoxLayout(form_create)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 13, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.groupBox = QGroupBox(form_create)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.bt_select.sizePolicy().hasHeightForWidth())
        self.bt_select.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.bt_select, 1, 6, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.cb_room = QComboBox(self.groupBox)
        self.cb_room.addItem("")
        self.cb_room.setObjectName(u"cb_room")

        self.gridLayout.addWidget(self.cb_room, 0, 1, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mg_ip.sizePolicy().hasHeightForWidth())
        self.mg_ip.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.mg_ip, 1, 2, 1, 2)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.gridLayout.addWidget(self.radioButton_2, 1, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.cb_cabinet = QComboBox(self.groupBox)
        self.cb_cabinet.addItem("")
        self.cb_cabinet.setObjectName(u"cb_cabinet")

        self.gridLayout.addWidget(self.cb_cabinet, 0, 3, 1, 1)

        self.rd_mg_ip = QRadioButton(self.groupBox)
        self.rd_mg_ip.setObjectName(u"rd_mg_ip")
        self.rd_mg_ip.setChecked(True)

        self.gridLayout.addWidget(self.rd_mg_ip, 1, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_4, 1, 5, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        sizePolicy3.setHeightForWidth(self.machine_name.sizePolicy().hasHeightForWidth())
        self.machine_name.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.machine_name, 0, 5, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)

        self.horizontalLayout.addLayout(self.gridLayout)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 5)

        self.tb_display = QTableWidget(form_create)
        if (self.tb_display.columnCount() < 13):
            self.tb_display.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tb_display.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tb_display.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tb_display.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tb_display.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tb_display.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tb_display.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tb_display.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tb_display.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tb_display.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.tb_display.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.tb_display.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.tb_display.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.tb_display.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        if (self.tb_display.rowCount() < 10):
            self.tb_display.setRowCount(10)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_display.setItem(0, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_display.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_display.setItem(2, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_display.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_display.setItem(4, 0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_display.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_display.setItem(6, 0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_display.setItem(7, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_display.setItem(8, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_display.setItem(9, 0, __qtablewidgetitem22)
        self.tb_display.setObjectName(u"tb_display")
        font1 = QFont()
        font1.setPointSize(9)
        self.tb_display.setFont(font1)
        self.tb_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tb_display.setRowCount(10)
        self.tb_display.setColumnCount(13)
        self.tb_display.horizontalHeader().setVisible(True)
        self.tb_display.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_display.horizontalHeader().setHighlightSections(True)
        self.tb_display.verticalHeader().setVisible(False)
        self.tb_display.verticalHeader().setCascadingSectionResizes(False)

        self.gridLayout_2.addWidget(self.tb_display, 3, 0, 1, 5)

        self.verticalSpacer = QSpacerItem(538, 17, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 0, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.bt_add_all = QPushButton(form_create)
        self.bt_add_all.setObjectName(u"bt_add_all")
        self.bt_add_all.setFont(font)

        self.gridLayout_2.addWidget(self.bt_add_all, 5, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 5, 2, 1, 1)

        self.bt_create = QPushButton(form_create)
        self.bt_create.setObjectName(u"bt_create")
        self.bt_create.setFont(font)

        self.gridLayout_2.addWidget(self.bt_create, 5, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 5, 4, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 0, 1, 1)

        self.label = QLabel(form_create)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(26)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 5)

        self.lb_stat = QLabel(form_create)
        self.lb_stat.setObjectName(u"lb_stat")
        self.lb_stat.setFrameShape(QFrame.Box)
        self.lb_stat.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lb_stat, 7, 0, 1, 5)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 10)
        self.gridLayout_2.setRowStretch(5, 1)
        self.gridLayout_2.setColumnStretch(0, 2)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 2)

        self.horizontalLayout_2.addLayout(self.gridLayout_2)


        self.retranslateUi(form_create)

        QMetaObject.connectSlotsByName(form_create)
    # setupUi

    def retranslateUi(self, form_create):
        form_create.setWindowTitle(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u6807\u7b7e\u6a21\u677f\u751f\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("form_create", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_select.setText(QCoreApplication.translate("form_create", u"\u67e5    \u8be2", None))
        self.label_2.setText(QCoreApplication.translate("form_create", u"\u673a      \u623f", None))
        self.cb_room.setItemText(0, QCoreApplication.translate("form_create", u"\u6240\u6709", None))

        self.radioButton_2.setText(QCoreApplication.translate("form_create", u"\u5e26\u5916IP", None))
        self.label_7.setText(QCoreApplication.translate("form_create", u"\u673a\u67dc", None))
        self.cb_cabinet.setItemText(0, QCoreApplication.translate("form_create", u"\u6240\u6709", None))

        self.rd_mg_ip.setText(QCoreApplication.translate("form_create", u"\u5e26\u5185IP", None))
        ___qtablewidgetitem = self.tb_display.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907ID", None));
        ___qtablewidgetitem1 = self.tb_display.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tb_display.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("form_create", u"\u673a\u623f", None));
        ___qtablewidgetitem3 = self.tb_display.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("form_create", u"\u673a\u67dc", None));
        ___qtablewidgetitem4 = self.tb_display.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("form_create", u"\u5f00\u59cbU", None));
        ___qtablewidgetitem5 = self.tb_display.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("form_create", u"U\u6570", None));
        ___qtablewidgetitem6 = self.tb_display.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u5206\u7c7b", None));
        ___qtablewidgetitem7 = self.tb_display.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u54c1\u724c", None));
        ___qtablewidgetitem8 = self.tb_display.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("form_create", u"\u578b\u53f7", None));
        ___qtablewidgetitem9 = self.tb_display.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907SN", None));
        ___qtablewidgetitem10 = self.tb_display.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u7ba1\u7406\u5458", None));
        ___qtablewidgetitem11 = self.tb_display.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u5e26\u5185IP", None));
        ___qtablewidgetitem12 = self.tb_display.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u5e26\u5916IP", None));

        __sortingEnabled = self.tb_display.isSortingEnabled()
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setSortingEnabled(__sortingEnabled)

        self.bt_add_all.setText(QCoreApplication.translate("form_create", u"\u5168\u9009", None))
        self.bt_create.setText(QCoreApplication.translate("form_create", u"\u751f\u6210\u6807\u7b7e\u6a21\u677f", None))
        self.label.setText(QCoreApplication.translate("form_create", u"\u8bbe\u5907\u6807\u7b7e\u6a21\u677f\u751f\u6210", None))
        self.lb_stat.setText(QCoreApplication.translate("form_create", u"\u5c31\u7eea", None))
    # retranslateUi

