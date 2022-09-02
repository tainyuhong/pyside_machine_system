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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_password_form(object):
    def setupUi(self, password_form):
        if not password_form.objectName():
            password_form.setObjectName(u"password_form")
        password_form.resize(1024, 768)
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

        self.bt_select = QPushButton(self.groupBox)
        self.bt_select.setObjectName(u"bt_select")

        self.horizontalLayout.addWidget(self.bt_select)

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
        self.tb_select.setObjectName(u"tb_select")
        self.tb_select.setStyleSheet(u"QTableWidget QHeaderView::section{ background-color: rgb(255,228,181)};")
        self.tb_select.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_select.setAlternatingRowColors(True)
        self.tb_select.horizontalHeader().setStretchLastSection(True)

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
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_query_ma.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        self.tb_query_ma.setObjectName(u"tb_query_ma")
        self.tb_query_ma.setStyleSheet(u"QTableWidget QHeaderView::section{ background-color: rgb(255,228,181)};")
        self.tb_query_ma.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_query_ma.setAlternatingRowColors(True)
        self.tb_query_ma.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tb_query_ma.horizontalHeader().setStretchLastSection(True)

        self.gridLayout_2.addWidget(self.tb_query_ma, 1, 0, 1, 3)

        self.bt_current = QPushButton(self.grp_is_vm)
        self.bt_current.setObjectName(u"bt_current")
        self.bt_current.setFont(font1)

        self.gridLayout_2.addWidget(self.bt_current, 2, 2, 1, 1)

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
        self.label_5 = QLabel(self.tab_config)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)

        self.btn_add = QPushButton(self.tab_config)
        self.btn_add.setObjectName(u"btn_add")

        self.gridLayout.addWidget(self.btn_add, 2, 2, 1, 2)

        self.le_user = QLineEdit(self.tab_config)
        self.le_user.setObjectName(u"le_user")

        self.gridLayout.addWidget(self.le_user, 0, 1, 1, 1)

        self.le_password = QLineEdit(self.tab_config)
        self.le_password.setObjectName(u"le_password")

        self.gridLayout.addWidget(self.le_password, 0, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 3, 2, 1, 1)

        self.label_4 = QLabel(self.tab_config)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.le_current_ip = QLineEdit(self.tab_config)
        self.le_current_ip.setObjectName(u"le_current_ip")

        self.gridLayout.addWidget(self.le_current_ip, 0, 5, 1, 1)

        self.label_6 = QLabel(self.tab_config)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.te_remark = QTextEdit(self.tab_config)
        self.te_remark.setObjectName(u"te_remark")

        self.gridLayout.addWidget(self.te_remark, 1, 1, 1, 5)

        self.label_3 = QLabel(self.tab_config)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 4, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
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

        self.verticalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


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
        self.bt_select.setToolTip(QCoreApplication.translate("password_form", u"\u9ed8\u8ba4\u67e5\u8be2\u6240\u6709", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.bt_select.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.bt_select.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.bt_select.setText(QCoreApplication.translate("password_form", u"\u67e5  \u8be2", None))
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
        self.bt_current.setText(QCoreApplication.translate("password_form", u"\u9009 \u62e9", None))
        self.lb_ma_conut.setText("")
        self.label_5.setText(QCoreApplication.translate("password_form", u"\u5bc6\u7801", None))
        self.btn_add.setText(QCoreApplication.translate("password_form", u"\u6dfb \u52a0", None))
        self.label_4.setText(QCoreApplication.translate("password_form", u"\u7528\u6237\u540d", None))
        self.label_6.setText(QCoreApplication.translate("password_form", u"\u5907\u6ce8", None))
        self.label_3.setText(QCoreApplication.translate("password_form", u"   I P  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_config), QCoreApplication.translate("password_form", u"\u7ef4\u62a4\u8bbe\u5907\u5bc6\u7801", None))
    # retranslateUi

