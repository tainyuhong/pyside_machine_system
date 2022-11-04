# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'upshelf.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_up_shelf(object):
    def setupUi(self, up_shelf):
        if not up_shelf.objectName():
            up_shelf.setObjectName(u"up_shelf")
        up_shelf.resize(1024, 768)
        self.verticalLayout = QVBoxLayout(up_shelf)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(15, 10, 15, 20)
        self.lb_app_ip = QLabel(up_shelf)
        self.lb_app_ip.setObjectName(u"lb_app_ip")
        font = QFont()
        font.setPointSize(12)
        self.lb_app_ip.setFont(font)
        self.lb_app_ip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_app_ip, 5, 4, 1, 1)

        self.lb_sn = QLabel(up_shelf)
        self.lb_sn.setObjectName(u"lb_sn")
        self.lb_sn.setFont(font)
        self.lb_sn.setStyleSheet(u"")
        self.lb_sn.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_sn, 4, 0, 1, 1)

        self.install_date = QDateEdit(up_shelf)
        self.install_date.setObjectName(u"install_date")
        font1 = QFont()
        font1.setFamilies([u"\u5b8b\u4f53"])
        font1.setPointSize(12)
        self.install_date.setFont(font1)
        self.install_date.setCalendarPopup(True)
        self.install_date.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.install_date, 6, 5, 1, 1)

        self.cabinet = QComboBox(up_shelf)
        self.cabinet.setObjectName(u"cabinet")
        self.cabinet.setFont(font1)

        self.gridLayout.addWidget(self.cabinet, 2, 3, 1, 1)

        self.lb_install_date = QLabel(up_shelf)
        self.lb_install_date.setObjectName(u"lb_install_date")
        self.lb_install_date.setFont(font)
        self.lb_install_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_install_date, 6, 4, 1, 1)

        self.bt_save = QPushButton(up_shelf)
        self.bt_save.setObjectName(u"bt_save")
        self.bt_save.setFont(font)

        self.gridLayout.addWidget(self.bt_save, 10, 2, 1, 1)

        self.single_power = QCheckBox(up_shelf)
        self.single_power.setObjectName(u"single_power")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.single_power.setFont(font2)
        self.single_power.setStyleSheet(u"color:blue")

        self.gridLayout.addWidget(self.single_power, 7, 3, 1, 1)

        self.lb_room = QLabel(up_shelf)
        self.lb_room.setObjectName(u"lb_room")
        self.lb_room.setFont(font)
        self.lb_room.setStyleSheet(u"color:red")
        self.lb_room.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_room, 2, 0, 1, 1)

        self.comments = QTextEdit(up_shelf)
        self.comments.setObjectName(u"comments")
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setKerning(True)
        self.comments.setFont(font3)

        self.gridLayout.addWidget(self.comments, 9, 0, 1, 6)

        self.work_are = QComboBox(up_shelf)
        self.work_are.addItem("")
        self.work_are.addItem("")
        self.work_are.addItem("")
        self.work_are.addItem("")
        self.work_are.setObjectName(u"work_are")
        self.work_are.setFont(font1)

        self.gridLayout.addWidget(self.work_are, 4, 5, 1, 1)

        self.lb_admin = QLabel(up_shelf)
        self.lb_admin.setObjectName(u"lb_admin")
        self.lb_admin.setFont(font)
        self.lb_admin.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_admin, 5, 2, 1, 1)

        self.label = QLabel(up_shelf)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setUnderline(False)
        self.label.setFont(font4)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)

        self.admin = QLineEdit(up_shelf)
        self.admin.setObjectName(u"admin")
        self.admin.setFont(font1)

        self.gridLayout.addWidget(self.admin, 5, 3, 1, 1)

        self.lb_sort = QLabel(up_shelf)
        self.lb_sort.setObjectName(u"lb_sort")
        self.lb_sort.setFont(font)
        self.lb_sort.setStyleSheet(u"color:red")
        self.lb_sort.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_sort, 1, 4, 1, 1)

        self.lb_fa_date = QLabel(up_shelf)
        self.lb_fa_date.setObjectName(u"lb_fa_date")
        self.lb_fa_date.setFont(font)
        self.lb_fa_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_fa_date, 6, 0, 1, 1)

        self.lb_last_date = QLabel(up_shelf)
        self.lb_last_date.setObjectName(u"lb_last_date")
        self.lb_last_date.setFont(font)
        self.lb_last_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_last_date, 6, 2, 1, 1)

        self.app_ip = QLineEdit(up_shelf)
        self.app_ip.setObjectName(u"app_ip")
        self.app_ip.setFont(font1)

        self.gridLayout.addWidget(self.app_ip, 5, 5, 1, 1)

        self.model = QLineEdit(up_shelf)
        self.model.setObjectName(u"model")
        self.model.setFont(font1)

        self.gridLayout.addWidget(self.model, 3, 3, 1, 1)

        self.down_position = QComboBox(up_shelf)
        self.down_position.setObjectName(u"down_position")
        self.down_position.setFont(font1)

        self.gridLayout.addWidget(self.down_position, 2, 5, 1, 1)

        self.lb_mg_ip_2 = QLabel(up_shelf)
        self.lb_mg_ip_2.setObjectName(u"lb_mg_ip_2")
        self.lb_mg_ip_2.setFont(font)
        self.lb_mg_ip_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mg_ip_2, 7, 0, 1, 1)

        self.bmc_ip = QLineEdit(up_shelf)
        self.bmc_ip.setObjectName(u"bmc_ip")
        self.bmc_ip.setFont(font1)

        self.gridLayout.addWidget(self.bmc_ip, 7, 1, 1, 1)

        self.lb_mode = QLabel(up_shelf)
        self.lb_mode.setObjectName(u"lb_mode")
        self.lb_mode.setFont(font)
        self.lb_mode.setStyleSheet(u"color:red")
        self.lb_mode.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mode, 3, 2, 1, 1)

        self.lb_down = QLabel(up_shelf)
        self.lb_down.setObjectName(u"lb_down")
        self.lb_down.setFont(font)
        self.lb_down.setStyleSheet(u"color:red")
        self.lb_down.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_down, 2, 4, 1, 1)

        self.room = QComboBox(up_shelf)
        self.room.setObjectName(u"room")
        self.room.setFont(font1)
        self.room.setDuplicatesEnabled(False)

        self.gridLayout.addWidget(self.room, 2, 1, 1, 1)

        self.lb_cabinet = QLabel(up_shelf)
        self.lb_cabinet.setObjectName(u"lb_cabinet")
        self.lb_cabinet.setFont(font)
        self.lb_cabinet.setStyleSheet(u"color:red")
        self.lb_cabinet.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_cabinet, 2, 2, 1, 1)

        self.bt_clear = QPushButton(up_shelf)
        self.bt_clear.setObjectName(u"bt_clear")
        self.bt_clear.setFont(font)

        self.gridLayout.addWidget(self.bt_clear, 10, 4, 1, 1)

        self.end_ma_date = QDateEdit(up_shelf)
        self.end_ma_date.setObjectName(u"end_ma_date")
        self.end_ma_date.setFont(font1)
        self.end_ma_date.setCalendarPopup(True)
        self.end_ma_date.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.end_ma_date, 6, 3, 1, 1)

        self.lb_mg_ip = QLabel(up_shelf)
        self.lb_mg_ip.setObjectName(u"lb_mg_ip")
        self.lb_mg_ip.setFont(font)
        self.lb_mg_ip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mg_ip, 4, 2, 1, 1)

        self.lb_factory = QLabel(up_shelf)
        self.lb_factory.setObjectName(u"lb_factory")
        self.lb_factory.setFont(font)
        self.lb_factory.setStyleSheet(u"color:red")
        self.lb_factory.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_factory, 3, 0, 1, 1)

        self.lb_comments = QLabel(up_shelf)
        self.lb_comments.setObjectName(u"lb_comments")
        self.lb_comments.setFont(font2)
        self.lb_comments.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_comments, 8, 0, 1, 1)

        self.sort_name = QComboBox(up_shelf)
        self.sort_name.setObjectName(u"sort_name")
        self.sort_name.setFont(font1)

        self.gridLayout.addWidget(self.sort_name, 1, 5, 1, 1)

        self.factory_date = QDateEdit(up_shelf)
        self.factory_date.setObjectName(u"factory_date")
        self.factory_date.setFont(font1)
        self.factory_date.setCalendarPopup(True)
        self.factory_date.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.factory_date, 6, 1, 1, 1)

        self.lb_up = QLabel(up_shelf)
        self.lb_up.setObjectName(u"lb_up")
        self.lb_up.setFont(font)
        self.lb_up.setStyleSheet(u"color:red")
        self.lb_up.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_up, 3, 4, 1, 1)

        self.lmg_ip = QLineEdit(up_shelf)
        self.lmg_ip.setObjectName(u"lmg_ip")
        self.lmg_ip.setFont(font1)

        self.gridLayout.addWidget(self.lmg_ip, 4, 3, 1, 1)

        self.lb_machine_name = QLabel(up_shelf)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font)
        self.lb_machine_name.setStyleSheet(u"color:red")
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 1, 0, 1, 1)

        self.machine_sn = QLineEdit(up_shelf)
        self.machine_sn.setObjectName(u"machine_sn")
        self.machine_sn.setFont(font1)

        self.gridLayout.addWidget(self.machine_sn, 4, 1, 1, 1)

        self.lb_machine_admin = QLabel(up_shelf)
        self.lb_machine_admin.setObjectName(u"lb_machine_admin")
        self.lb_machine_admin.setFont(font)
        self.lb_machine_admin.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_admin, 5, 0, 1, 1)

        self.lb_work = QLabel(up_shelf)
        self.lb_work.setObjectName(u"lb_work")
        self.lb_work.setFont(font)
        self.lb_work.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_work, 4, 4, 1, 1)

        self.machine_admin = QLineEdit(up_shelf)
        self.machine_admin.setObjectName(u"machine_admin")
        self.machine_admin.setFont(font1)

        self.gridLayout.addWidget(self.machine_admin, 5, 1, 1, 1)

        self.machine_factory = QComboBox(up_shelf)
        self.machine_factory.setObjectName(u"machine_factory")
        self.machine_factory.setFont(font1)

        self.gridLayout.addWidget(self.machine_factory, 3, 1, 1, 1)

        self.up_position = QComboBox(up_shelf)
        self.up_position.setObjectName(u"up_position")
        self.up_position.setFont(font1)

        self.gridLayout.addWidget(self.up_position, 3, 5, 1, 1)

        self.machine_name = QLineEdit(up_shelf)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font1)

        self.gridLayout.addWidget(self.machine_name, 1, 1, 1, 3)

        self.label_2 = QLabel(up_shelf)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:red")

        self.gridLayout.addWidget(self.label_2, 11, 1, 1, 3)

        self.label_3 = QLabel(up_shelf)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 7, 4, 1, 1)

        self.le_operator = QLineEdit(up_shelf)
        self.le_operator.setObjectName(u"le_operator")
        self.le_operator.setFont(font)

        self.gridLayout.addWidget(self.le_operator, 7, 5, 1, 1)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setRowStretch(7, 1)
        self.gridLayout.setRowStretch(8, 1)
        self.gridLayout.setRowStretch(9, 4)
        self.gridLayout.setRowStretch(10, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        QWidget.setTabOrder(self.machine_name, self.sort_name)
        QWidget.setTabOrder(self.sort_name, self.room)
        QWidget.setTabOrder(self.room, self.cabinet)
        QWidget.setTabOrder(self.cabinet, self.down_position)
        QWidget.setTabOrder(self.down_position, self.machine_factory)
        QWidget.setTabOrder(self.machine_factory, self.model)
        QWidget.setTabOrder(self.model, self.up_position)
        QWidget.setTabOrder(self.up_position, self.machine_sn)
        QWidget.setTabOrder(self.machine_sn, self.lmg_ip)
        QWidget.setTabOrder(self.lmg_ip, self.work_are)
        QWidget.setTabOrder(self.work_are, self.machine_admin)
        QWidget.setTabOrder(self.machine_admin, self.admin)
        QWidget.setTabOrder(self.admin, self.app_ip)
        QWidget.setTabOrder(self.app_ip, self.factory_date)
        QWidget.setTabOrder(self.factory_date, self.end_ma_date)
        QWidget.setTabOrder(self.end_ma_date, self.install_date)
        QWidget.setTabOrder(self.install_date, self.bmc_ip)
        QWidget.setTabOrder(self.bmc_ip, self.single_power)
        QWidget.setTabOrder(self.single_power, self.le_operator)
        QWidget.setTabOrder(self.le_operator, self.comments)
        QWidget.setTabOrder(self.comments, self.bt_save)
        QWidget.setTabOrder(self.bt_save, self.bt_clear)

        self.retranslateUi(up_shelf)

        self.work_are.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(up_shelf)
    # setupUi

    def retranslateUi(self, up_shelf):
        up_shelf.setWindowTitle(QCoreApplication.translate("up_shelf", u"\u65b0\u8bbe\u5907\u4e0a\u67b6\u5b89\u88c5", None))
        self.lb_app_ip.setText(QCoreApplication.translate("up_shelf", u"\u4e1a\u52a1 IP", None))
        self.lb_sn.setText(QCoreApplication.translate("up_shelf", u"\u8bbe \u5907 SN", None))
        self.cabinet.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9\u673a\u67dc", None))
        self.lb_install_date.setText(QCoreApplication.translate("up_shelf", u"\u4e0a\u67b6\u65e5\u671f", None))
        self.bt_save.setText(QCoreApplication.translate("up_shelf", u"\u4fdd    \u5b58", None))
        self.single_power.setText(QCoreApplication.translate("up_shelf", u"\u5355\u7535\u6e90", None))
        self.lb_room.setText(QCoreApplication.translate("up_shelf", u"\u673a      \u623f", None))
        self.work_are.setItemText(0, QCoreApplication.translate("up_shelf", u"1\u751f\u4ea7", None))
        self.work_are.setItemText(1, QCoreApplication.translate("up_shelf", u"2\u7535\u6e20", None))
        self.work_are.setItemText(2, QCoreApplication.translate("up_shelf", u"3\u707e\u5907", None))
        self.work_are.setItemText(3, QCoreApplication.translate("up_shelf", u"4\u5f00\u53d1", None))

        self.work_are.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9\u4e1a\u52a1\u7c7b\u578b", None))
        self.lb_admin.setText(QCoreApplication.translate("up_shelf", u"\u7ba1 \u7406 \u5458", None))
        self.label.setText(QCoreApplication.translate("up_shelf", u"\u65b0\u8bbe\u5907\u4e0a\u67b6", None))
        self.lb_sort.setText(QCoreApplication.translate("up_shelf", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.lb_fa_date.setText(QCoreApplication.translate("up_shelf", u"\u51fa\u5382\u65e5\u671f", None))
        self.lb_last_date.setText(QCoreApplication.translate("up_shelf", u"\u5230\u4fdd\u65e5\u671f", None))
        self.down_position.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9U\u4f4d", None))
        self.lb_mg_ip_2.setText(QCoreApplication.translate("up_shelf", u"BMC IP", None))
        self.lb_mode.setText(QCoreApplication.translate("up_shelf", u"\u578b     \u53f7", None))
        self.lb_down.setText(QCoreApplication.translate("up_shelf", u"\u4e0b  U \u4f4d", None))
        self.room.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9\u673a\u623f", None))
        self.lb_cabinet.setText(QCoreApplication.translate("up_shelf", u"\u673a     \u67dc", None))
        self.bt_clear.setText(QCoreApplication.translate("up_shelf", u"\u6e05    \u7a7a", None))
        self.lb_mg_ip.setText(QCoreApplication.translate("up_shelf", u"\u7ba1 \u7406 IP", None))
        self.lb_factory.setText(QCoreApplication.translate("up_shelf", u"\u8bbe\u5907\u54c1\u724c", None))
        self.lb_comments.setText(QCoreApplication.translate("up_shelf", u"\u5907      \u6ce8", None))
        self.sort_name.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9\u7c7b\u578b", None))
        self.lb_up.setText(QCoreApplication.translate("up_shelf", u"\u4e0a  U \u4f4d", None))
        self.lb_machine_name.setText(QCoreApplication.translate("up_shelf", u"\u8bbe\u5907\u540d\u79f0", None))
        self.lb_machine_admin.setText(QCoreApplication.translate("up_shelf", u"\u8d1f \u8d23 \u4eba", None))
        self.lb_work.setText(QCoreApplication.translate("up_shelf", u"\u4e1a\u52a1\u7c7b\u578b", None))
        self.machine_factory.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9\u54c1\u724c", None))
        self.up_position.setPlaceholderText(QCoreApplication.translate("up_shelf", u"\u70b9\u51fb\u9009\u62e9U\u4f4d", None))
        self.label_2.setText(QCoreApplication.translate("up_shelf", u"* \u65b0\u8bbe\u5907\u4e0a\u67b6\uff0c\u5f55\u5165", None))
        self.label_3.setText(QCoreApplication.translate("up_shelf", u"\u5b89\u88c5\u4eba\u5458", None))
    # retranslateUi

