# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'down_shelf.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractSpinBox, QApplication, QDateEdit,
    QDateTimeEdit, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextEdit, QWidget)

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
        self.lb_title = QLabel(down_shelf)
        self.lb_title.setObjectName(u"lb_title")
        font = QFont()
        font.setPointSize(30)
        font.setUnderline(False)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet(u"")
        self.lb_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lb_title, 0, 0, 1, 8)

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
        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        font1 = QFont()
        font1.setPointSize(12)
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
        self.lb_mgip.setFont(font1)
        self.lb_mgip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mgip, 0, 3, 1, 1)

        self.lb_machine_name = QLabel(self.groupBox)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font1)
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


        self.gridLayout_2.addWidget(self.groupBox, 1, 0, 1, 8)

        self.tb_display = QTableWidget(down_shelf)
        if (self.tb_display.columnCount() < 16):
            self.tb_display.setColumnCount(16)
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
        if (self.tb_display.rowCount() < 8):
            self.tb_display.setRowCount(8)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_display.setItem(0, 0, __qtablewidgetitem16)
        self.tb_display.setObjectName(u"tb_display")
        self.tb_display.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_display.setAlternatingRowColors(True)
        self.tb_display.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tb_display.setGridStyle(Qt.SolidLine)
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setRowCount(8)
        self.tb_display.horizontalHeader().setDefaultSectionSize(80)

        self.gridLayout_2.addWidget(self.tb_display, 2, 0, 1, 8)

        self.label_3 = QLabel(down_shelf)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_2.addWidget(self.label_3, 3, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 6, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(698, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 8, 0, 1, 6)

        self.bt_donw_shelf = QPushButton(down_shelf)
        self.bt_donw_shelf.setObjectName(u"bt_donw_shelf")
        self.bt_donw_shelf.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_donw_shelf, 8, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(58, 26, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 8, 7, 1, 1)

        self.lb_status = QLabel(down_shelf)
        self.lb_status.setObjectName(u"lb_status")
        self.lb_status.setFrameShape(QFrame.Box)
        self.lb_status.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.lb_status, 10, 0, 1, 8)

        self.comments = QTextEdit(down_shelf)
        self.comments.setObjectName(u"comments")
        self.comments.setTabChangesFocus(True)

        self.gridLayout_2.addWidget(self.comments, 4, 0, 2, 3)

        self.label = QLabel(down_shelf)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 4, 4, 1, 1)

        self.le_down_operator = QLineEdit(down_shelf)
        self.le_down_operator.setObjectName(u"le_down_operator")
        self.le_down_operator.setFont(font1)

        self.gridLayout_2.addWidget(self.le_down_operator, 4, 5, 1, 2)

        self.label_2 = QLabel(down_shelf)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 5, 4, 1, 1)

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

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 5, 3, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 6, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 9, 2, 1, 1)

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

        QWidget.setTabOrder(self.machine_name, self.mg_ip)
        QWidget.setTabOrder(self.mg_ip, self.bt_clear)
        QWidget.setTabOrder(self.bt_clear, self.bt_select)
        QWidget.setTabOrder(self.bt_select, self.tb_display)
        QWidget.setTabOrder(self.tb_display, self.comments)
        QWidget.setTabOrder(self.comments, self.le_down_operator)
        QWidget.setTabOrder(self.le_down_operator, self.down_time)
        QWidget.setTabOrder(self.down_time, self.bt_donw_shelf)

        self.retranslateUi(down_shelf)

        QMetaObject.connectSlotsByName(down_shelf)
    # setupUi

    def retranslateUi(self, down_shelf):
        down_shelf.setWindowTitle(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u4e0b\u67b6", None))
        self.lb_title.setText(QCoreApplication.translate("down_shelf", u"\u4e0b \u67b6 \u8bbe \u5907", None))
        self.groupBox.setTitle(QCoreApplication.translate("down_shelf", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.mg_ip.setText("")
        self.bt_clear.setText(QCoreApplication.translate("down_shelf", u"\u6e05\u7a7a", None))
        self.lb_mgip.setText(QCoreApplication.translate("down_shelf", u"\u7ba1\u7406 IP", None))
        self.lb_machine_name.setText(QCoreApplication.translate("down_shelf", u"\u8bbe\u5907\u540d\u79f0", None))
        self.bt_select.setText(QCoreApplication.translate("down_shelf", u"\u67e5\u8be2", None))
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
        ___qtablewidgetitem10.setText(QCoreApplication.translate("down_shelf", u"\u4e1a\u52a1\u7c7b\u578b", None));
        ___qtablewidgetitem11 = self.tb_display.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("down_shelf", u"\u8d1f\u8d23\u4eba", None));
        ___qtablewidgetitem12 = self.tb_display.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("down_shelf", u"\u5e94\u7528\u7ba1\u7406\u5458", None));
        ___qtablewidgetitem13 = self.tb_display.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("down_shelf", u"\u7ba1\u7406IP", None));
        ___qtablewidgetitem14 = self.tb_display.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("down_shelf", u"\u5e94\u7528IP", None));
        ___qtablewidgetitem15 = self.tb_display.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("down_shelf", u"\u5907\u6ce8", None));

        __sortingEnabled = self.tb_display.isSortingEnabled()
        self.tb_display.setSortingEnabled(False)
        self.tb_display.setSortingEnabled(__sortingEnabled)

        self.label_3.setText(QCoreApplication.translate("down_shelf", u"\u4e0b\u67b6\u60c5\u51b5\u8bf4\u660e", None))
        self.bt_donw_shelf.setText(QCoreApplication.translate("down_shelf", u"\u4e0b     \u67b6", None))
        self.lb_status.setText(QCoreApplication.translate("down_shelf", u"\u72b6\u6001\u680f", None))
        self.label.setText(QCoreApplication.translate("down_shelf", u"\u4e0b\u67b6\u6267\u884c\u4eba", None))
        self.label_2.setText(QCoreApplication.translate("down_shelf", u"\u4e0b\u67b6\u65f6\u95f4", None))
    # retranslateUi

