# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'warranty.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QRadioButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Warranty(object):
    def setupUi(self, Warranty):
        if not Warranty.objectName():
            Warranty.setObjectName(u"Warranty")
        Warranty.resize(1024, 768)
        self.horizontalLayout = QHBoxLayout(Warranty)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.vbox = QGroupBox(Warranty)
        self.vbox.setObjectName(u"vbox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vbox.sizePolicy().hasHeightForWidth())
        self.vbox.setSizePolicy(sizePolicy)
        self.vbox.setBaseSize(QSize(0, 0))
        self.vbox.setAlignment(Qt.AlignCenter)
        self.verticalLayout = QVBoxLayout(self.vbox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title = QLabel(self.vbox)
        self.title.setObjectName(u"title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(28)
        self.title.setFont(font)
        self.title.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title)

        self.groupBox = QGroupBox(self.vbox)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(12)
        self.groupBox.setFont(font1)
        self.groupBox.setStyleSheet(u"")
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.cb_is_under = QComboBox(self.groupBox)
        self.cb_is_under.addItem("")
        self.cb_is_under.setObjectName(u"cb_is_under")

        self.gridLayout.addWidget(self.cb_is_under, 1, 6, 1, 1)

        self.mg_ip = QLineEdit(self.groupBox)
        self.mg_ip.setObjectName(u"mg_ip")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(3)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.mg_ip.sizePolicy().hasHeightForWidth())
        self.mg_ip.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.mg_ip, 0, 4, 1, 1)

        self.cb_type = QComboBox(self.groupBox)
        self.cb_type.addItem("")
        self.cb_type.setObjectName(u"cb_type")

        self.gridLayout.addWidget(self.cb_type, 0, 6, 1, 1)

        self.le_sn = QLineEdit(self.groupBox)
        self.le_sn.setObjectName(u"le_sn")
        sizePolicy3.setHeightForWidth(self.le_sn.sizePolicy().hasHeightForWidth())
        self.le_sn.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.le_sn, 1, 4, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(2)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy4)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 5, 1, 1)

        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 5, 1, 1)

        self.select_btn = QPushButton(self.groupBox)
        self.select_btn.setObjectName(u"select_btn")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy5)

        self.gridLayout.addWidget(self.select_btn, 0, 7, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        sizePolicy4.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy4)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.room = QComboBox(self.groupBox)
        self.room.addItem("")
        self.room.setObjectName(u"room")

        self.gridLayout.addWidget(self.room, 0, 1, 1, 1)

        self.machine_name = QLineEdit(self.groupBox)
        self.machine_name.setObjectName(u"machine_name")
        sizePolicy3.setHeightForWidth(self.machine_name.sizePolicy().hasHeightForWidth())
        self.machine_name.setSizePolicy(sizePolicy3)

        self.gridLayout.addWidget(self.machine_name, 1, 1, 1, 1)

        self.rd_bmc_ip = QRadioButton(self.groupBox)
        self.rd_bmc_ip.setObjectName(u"rd_bmc_ip")

        self.gridLayout.addWidget(self.rd_bmc_ip, 0, 3, 1, 1)

        self.rd_mg_ip = QRadioButton(self.groupBox)
        self.rd_mg_ip.setObjectName(u"rd_mg_ip")
        self.rd_mg_ip.setChecked(True)

        self.gridLayout.addWidget(self.rd_mg_ip, 0, 2, 1, 1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy4.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 2, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 2)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout.setColumnStretch(6, 1)
        self.gridLayout.setColumnStretch(7, 1)

        self.verticalLayout_3.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.groupBox)

        self.warranty_select = QTableWidget(self.vbox)
        if (self.warranty_select.columnCount() < 18):
            self.warranty_select.setColumnCount(18)
        if (self.warranty_select.rowCount() < 15):
            self.warranty_select.setRowCount(15)
        self.warranty_select.setObjectName(u"warranty_select")
        sizePolicy2.setHeightForWidth(self.warranty_select.sizePolicy().hasHeightForWidth())
        self.warranty_select.setSizePolicy(sizePolicy2)
        self.warranty_select.setMinimumSize(QSize(900, 500))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        self.warranty_select.setFont(font2)
        self.warranty_select.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.warranty_select.setDragEnabled(False)
        self.warranty_select.setAlternatingRowColors(True)
        self.warranty_select.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.warranty_select.setGridStyle(Qt.SolidLine)
        self.warranty_select.setRowCount(15)
        self.warranty_select.setColumnCount(18)
        self.warranty_select.horizontalHeader().setVisible(True)
        self.warranty_select.horizontalHeader().setCascadingSectionResizes(False)
        self.warranty_select.horizontalHeader().setHighlightSections(True)
        self.warranty_select.horizontalHeader().setProperty("showSortIndicator", False)
        self.warranty_select.verticalHeader().setVisible(False)
        self.warranty_select.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.warranty_select)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 10)

        self.verticalLayout_2.addWidget(self.vbox)

        self.page_layout = QHBoxLayout()
        self.page_layout.setSpacing(20)
        self.page_layout.setObjectName(u"page_layout")
        self.home_btn = QPushButton(Warranty)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setEnabled(False)

        self.page_layout.addWidget(self.home_btn)

        self.pre_btn = QPushButton(Warranty)
        self.pre_btn.setObjectName(u"pre_btn")
        self.pre_btn.setEnabled(False)

        self.page_layout.addWidget(self.pre_btn)

        self.next_btn = QPushButton(Warranty)
        self.next_btn.setObjectName(u"next_btn")
        self.next_btn.setEnabled(False)

        self.page_layout.addWidget(self.next_btn)

        self.last_btn = QPushButton(Warranty)
        self.last_btn.setObjectName(u"last_btn")
        self.last_btn.setEnabled(False)

        self.page_layout.addWidget(self.last_btn)

        self.go_page_lb = QLabel(Warranty)
        self.go_page_lb.setObjectName(u"go_page_lb")

        self.page_layout.addWidget(self.go_page_lb)

        self.page_input_le = QLineEdit(Warranty)
        self.page_input_le.setObjectName(u"page_input_le")

        self.page_layout.addWidget(self.page_input_le)

        self.page_lb = QLabel(Warranty)
        self.page_lb.setObjectName(u"page_lb")

        self.page_layout.addWidget(self.page_lb)

        self.go_btn = QPushButton(Warranty)
        self.go_btn.setObjectName(u"go_btn")
        self.go_btn.setEnabled(False)

        self.page_layout.addWidget(self.go_btn)

        self.total_page_lb = QLabel(Warranty)
        self.total_page_lb.setObjectName(u"total_page_lb")

        self.page_layout.addWidget(self.total_page_lb)

        self.current_page_lb = QLabel(Warranty)
        self.current_page_lb.setObjectName(u"current_page_lb")

        self.page_layout.addWidget(self.current_page_lb)

        self.page_layout.setStretch(0, 2)
        self.page_layout.setStretch(1, 2)
        self.page_layout.setStretch(2, 2)
        self.page_layout.setStretch(3, 2)
        self.page_layout.setStretch(4, 1)
        self.page_layout.setStretch(5, 1)
        self.page_layout.setStretch(6, 1)
        self.page_layout.setStretch(7, 1)
        self.page_layout.setStretch(8, 3)
        self.page_layout.setStretch(9, 3)

        self.verticalLayout_2.addLayout(self.page_layout)

        self.verticalLayout_2.setStretch(0, 12)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(Warranty)

        QMetaObject.connectSlotsByName(Warranty)
    # setupUi

    def retranslateUi(self, Warranty):
        Warranty.setWindowTitle(QCoreApplication.translate("Warranty", u"\u7ef4\u4fdd\u4fe1\u606f\u67e5\u8be2", None))
        self.title.setText(QCoreApplication.translate("Warranty", u"\u8bbe\u5907\u7ef4\u4fdd\u4fe1\u606f\u67e5\u8be2", None))
        self.groupBox.setTitle(QCoreApplication.translate("Warranty", u"\u67e5\u8be2\u6761\u4ef6", None))
        self.cb_is_under.setItemText(0, QCoreApplication.translate("Warranty", u"\u6240\u6709", None))

        self.cb_type.setItemText(0, QCoreApplication.translate("Warranty", u"\u6240\u6709", None))

        self.label.setText(QCoreApplication.translate("Warranty", u"\u673a      \u623f", None))
        self.label_5.setText(QCoreApplication.translate("Warranty", u"\u7ef4\u4fdd\u7c7b\u578b", None))
        self.label_6.setText(QCoreApplication.translate("Warranty", u"\u662f\u5426\u4fdd\u5185", None))
        self.select_btn.setText(QCoreApplication.translate("Warranty", u"\u67e5    \u8be2", None))
        self.label_3.setText(QCoreApplication.translate("Warranty", u"\u8bbe\u5907\u540d\u79f0", None))
        self.room.setItemText(0, QCoreApplication.translate("Warranty", u"\u6240\u6709", None))

        self.rd_bmc_ip.setText(QCoreApplication.translate("Warranty", u"\u5e26\u5916IP", None))
        self.rd_mg_ip.setText(QCoreApplication.translate("Warranty", u"\u5e26\u5185IP", None))
        self.label_2.setText(QCoreApplication.translate("Warranty", u"\u5e8f \u5217 \u53f7", None))
        self.home_btn.setText(QCoreApplication.translate("Warranty", u"\u9996\u9875", None))
        self.pre_btn.setText(QCoreApplication.translate("Warranty", u"\u4e0a\u4e00\u9875", None))
        self.next_btn.setText(QCoreApplication.translate("Warranty", u"\u4e0b\u4e00\u9875", None))
        self.last_btn.setText(QCoreApplication.translate("Warranty", u"\u6700\u540e\u4e00\u9875", None))
        self.go_page_lb.setText(QCoreApplication.translate("Warranty", u"\u8df3\u8f6c\u5230", None))
        self.page_lb.setText(QCoreApplication.translate("Warranty", u"\u9875", None))
        self.go_btn.setText(QCoreApplication.translate("Warranty", u"\u8f6c\u5230", None))
        self.total_page_lb.setText(QCoreApplication.translate("Warranty", u"\u603b\u9875\u6570", None))
        self.current_page_lb.setText(QCoreApplication.translate("Warranty", u"\u5f53\u524d\u9875", None))
    # retranslateUi

