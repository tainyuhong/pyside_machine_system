# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_machine.ui'
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

class Ui_add_machine_form(object):
    def setupUi(self, add_machine_form):
        if not add_machine_form.objectName():
            add_machine_form.setObjectName(u"add_machine_form")
        add_machine_form.setWindowModality(Qt.ApplicationModal)
        add_machine_form.resize(800, 650)
        self.verticalLayout = QVBoxLayout(add_machine_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setContentsMargins(15, 10, 15, 20)
        self.down_position = QComboBox(add_machine_form)
        self.down_position.setObjectName(u"down_position")
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(12)
        self.down_position.setFont(font)

        self.gridLayout.addWidget(self.down_position, 2, 5, 1, 1)

        self.lb_machine_admin = QLabel(add_machine_form)
        self.lb_machine_admin.setObjectName(u"lb_machine_admin")
        font1 = QFont()
        font1.setPointSize(12)
        self.lb_machine_admin.setFont(font1)
        self.lb_machine_admin.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_admin, 5, 0, 1, 1)

        self.admin = QLineEdit(add_machine_form)
        self.admin.setObjectName(u"admin")
        self.admin.setFont(font)

        self.gridLayout.addWidget(self.admin, 5, 3, 1, 1)

        self.install_date = QDateEdit(add_machine_form)
        self.install_date.setObjectName(u"install_date")
        self.install_date.setFont(font)
        self.install_date.setCalendarPopup(True)
        self.install_date.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.install_date, 6, 5, 1, 1)

        self.lb_mg_ip_2 = QLabel(add_machine_form)
        self.lb_mg_ip_2.setObjectName(u"lb_mg_ip_2")
        self.lb_mg_ip_2.setFont(font1)
        self.lb_mg_ip_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mg_ip_2, 7, 0, 1, 1)

        self.up_position = QComboBox(add_machine_form)
        self.up_position.setObjectName(u"up_position")
        self.up_position.setFont(font)

        self.gridLayout.addWidget(self.up_position, 3, 5, 1, 1)

        self.cabinet = QComboBox(add_machine_form)
        self.cabinet.setObjectName(u"cabinet")
        self.cabinet.setFont(font)

        self.gridLayout.addWidget(self.cabinet, 2, 3, 1, 1)

        self.model = QLineEdit(add_machine_form)
        self.model.setObjectName(u"model")
        self.model.setFont(font)

        self.gridLayout.addWidget(self.model, 3, 3, 1, 1)

        self.lb_last_date = QLabel(add_machine_form)
        self.lb_last_date.setObjectName(u"lb_last_date")
        self.lb_last_date.setFont(font1)
        self.lb_last_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_last_date, 6, 2, 1, 1)

        self.lb_install_date = QLabel(add_machine_form)
        self.lb_install_date.setObjectName(u"lb_install_date")
        self.lb_install_date.setFont(font1)
        self.lb_install_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_install_date, 6, 4, 1, 1)

        self.lb_admin = QLabel(add_machine_form)
        self.lb_admin.setObjectName(u"lb_admin")
        self.lb_admin.setFont(font1)
        self.lb_admin.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_admin, 5, 2, 1, 1)

        self.single_power = QCheckBox(add_machine_form)
        self.single_power.setObjectName(u"single_power")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        self.single_power.setFont(font2)
        self.single_power.setStyleSheet(u"color:blue")

        self.gridLayout.addWidget(self.single_power, 7, 3, 1, 1)

        self.room = QComboBox(add_machine_form)
        self.room.setObjectName(u"room")
        self.room.setFont(font)
        self.room.setDuplicatesEnabled(False)

        self.gridLayout.addWidget(self.room, 2, 1, 1, 1)

        self.lb_sn = QLabel(add_machine_form)
        self.lb_sn.setObjectName(u"lb_sn")
        self.lb_sn.setFont(font1)
        self.lb_sn.setStyleSheet(u"")
        self.lb_sn.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_sn, 4, 0, 1, 1)

        self.lb_fa_date = QLabel(add_machine_form)
        self.lb_fa_date.setObjectName(u"lb_fa_date")
        self.lb_fa_date.setFont(font1)
        self.lb_fa_date.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_fa_date, 6, 0, 1, 1)

        self.save = QPushButton(add_machine_form)
        self.save.setObjectName(u"save")
        self.save.setFont(font1)

        self.gridLayout.addWidget(self.save, 10, 2, 1, 1)

        self.machine_sn = QLineEdit(add_machine_form)
        self.machine_sn.setObjectName(u"machine_sn")
        self.machine_sn.setFont(font)

        self.gridLayout.addWidget(self.machine_sn, 4, 1, 1, 1)

        self.lb_down = QLabel(add_machine_form)
        self.lb_down.setObjectName(u"lb_down")
        self.lb_down.setFont(font1)
        self.lb_down.setStyleSheet(u"color:red")
        self.lb_down.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_down, 2, 4, 1, 1)

        self.lb_comments = QLabel(add_machine_form)
        self.lb_comments.setObjectName(u"lb_comments")
        self.lb_comments.setFont(font2)
        self.lb_comments.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_comments, 8, 0, 1, 1)

        self.lb_up = QLabel(add_machine_form)
        self.lb_up.setObjectName(u"lb_up")
        self.lb_up.setFont(font1)
        self.lb_up.setStyleSheet(u"color:red")
        self.lb_up.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_up, 3, 4, 1, 1)

        self.machine_admin = QLineEdit(add_machine_form)
        self.machine_admin.setObjectName(u"machine_admin")
        self.machine_admin.setFont(font)

        self.gridLayout.addWidget(self.machine_admin, 5, 1, 1, 1)

        self.lb_app_ip = QLabel(add_machine_form)
        self.lb_app_ip.setObjectName(u"lb_app_ip")
        self.lb_app_ip.setFont(font1)
        self.lb_app_ip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_app_ip, 5, 4, 1, 1)

        self.lb_machine_name = QLabel(add_machine_form)
        self.lb_machine_name.setObjectName(u"lb_machine_name")
        self.lb_machine_name.setFont(font1)
        self.lb_machine_name.setStyleSheet(u"color:red")
        self.lb_machine_name.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_machine_name, 1, 0, 1, 1)

        self.factory_date = QDateEdit(add_machine_form)
        self.factory_date.setObjectName(u"factory_date")
        self.factory_date.setFont(font)
        self.factory_date.setCalendarPopup(True)
        self.factory_date.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.factory_date, 6, 1, 1, 1)

        self.lb_cabinet = QLabel(add_machine_form)
        self.lb_cabinet.setObjectName(u"lb_cabinet")
        self.lb_cabinet.setFont(font1)
        self.lb_cabinet.setStyleSheet(u"color:red")
        self.lb_cabinet.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_cabinet, 2, 2, 1, 1)

        self.work_are = QComboBox(add_machine_form)
        self.work_are.addItem("")
        self.work_are.addItem("")
        self.work_are.addItem("")
        self.work_are.addItem("")
        self.work_are.setObjectName(u"work_are")
        self.work_are.setFont(font)

        self.gridLayout.addWidget(self.work_are, 4, 5, 1, 1)

        self.comments = QTextEdit(add_machine_form)
        self.comments.setObjectName(u"comments")
        font3 = QFont()
        font3.setFamilies([u"\u5b8b\u4f53"])
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setKerning(True)
        self.comments.setFont(font3)

        self.gridLayout.addWidget(self.comments, 9, 0, 1, 6)

        self.lb_mg_ip = QLabel(add_machine_form)
        self.lb_mg_ip.setObjectName(u"lb_mg_ip")
        self.lb_mg_ip.setFont(font1)
        self.lb_mg_ip.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mg_ip, 4, 2, 1, 1)

        self.lb_factory = QLabel(add_machine_form)
        self.lb_factory.setObjectName(u"lb_factory")
        self.lb_factory.setFont(font1)
        self.lb_factory.setStyleSheet(u"color:red")
        self.lb_factory.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_factory, 3, 0, 1, 1)

        self.lb_sort = QLabel(add_machine_form)
        self.lb_sort.setObjectName(u"lb_sort")
        self.lb_sort.setFont(font1)
        self.lb_sort.setStyleSheet(u"color:red")
        self.lb_sort.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_sort, 1, 4, 1, 1)

        self.lb_mode = QLabel(add_machine_form)
        self.lb_mode.setObjectName(u"lb_mode")
        self.lb_mode.setFont(font1)
        self.lb_mode.setStyleSheet(u"color:red")
        self.lb_mode.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_mode, 3, 2, 1, 1)

        self.lmg_ip = QLineEdit(add_machine_form)
        self.lmg_ip.setObjectName(u"lmg_ip")
        self.lmg_ip.setFont(font)

        self.gridLayout.addWidget(self.lmg_ip, 4, 3, 1, 1)

        self.lb_work = QLabel(add_machine_form)
        self.lb_work.setObjectName(u"lb_work")
        self.lb_work.setFont(font1)
        self.lb_work.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_work, 4, 4, 1, 1)

        self.machine_factory = QComboBox(add_machine_form)
        self.machine_factory.setObjectName(u"machine_factory")
        self.machine_factory.setFont(font)

        self.gridLayout.addWidget(self.machine_factory, 3, 1, 1, 1)

        self.end_ma_date = QDateEdit(add_machine_form)
        self.end_ma_date.setObjectName(u"end_ma_date")
        self.end_ma_date.setFont(font)
        self.end_ma_date.setCalendarPopup(True)
        self.end_ma_date.setDate(QDate(2000, 1, 1))

        self.gridLayout.addWidget(self.end_ma_date, 6, 3, 1, 1)

        self.clear = QPushButton(add_machine_form)
        self.clear.setObjectName(u"clear")
        self.clear.setFont(font1)

        self.gridLayout.addWidget(self.clear, 10, 4, 1, 1)

        self.machine_name = QLineEdit(add_machine_form)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font)

        self.gridLayout.addWidget(self.machine_name, 1, 1, 1, 3)

        self.label = QLabel(add_machine_form)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"\u5b8b\u4f53"])
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setUnderline(True)
        self.label.setFont(font4)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 2, 1, 2)

        self.sort_name = QComboBox(add_machine_form)
        self.sort_name.setObjectName(u"sort_name")
        self.sort_name.setFont(font)

        self.gridLayout.addWidget(self.sort_name, 1, 5, 1, 1)

        self.lb_room = QLabel(add_machine_form)
        self.lb_room.setObjectName(u"lb_room")
        self.lb_room.setFont(font1)
        self.lb_room.setStyleSheet(u"color:red")
        self.lb_room.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lb_room, 2, 0, 1, 1)

        self.app_ip = QLineEdit(add_machine_form)
        self.app_ip.setObjectName(u"app_ip")
        self.app_ip.setFont(font)

        self.gridLayout.addWidget(self.app_ip, 5, 5, 1, 1)

        self.bmc_ip = QLineEdit(add_machine_form)
        self.bmc_ip.setObjectName(u"bmc_ip")
        self.bmc_ip.setFont(font)

        self.gridLayout.addWidget(self.bmc_ip, 7, 1, 1, 1)

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

        self.label_2 = QLabel(add_machine_form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color:red")

        self.verticalLayout.addWidget(self.label_2)

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
        QWidget.setTabOrder(self.install_date, self.comments)
        QWidget.setTabOrder(self.comments, self.save)
        QWidget.setTabOrder(self.save, self.clear)

        self.retranslateUi(add_machine_form)

        self.work_are.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(add_machine_form)
    # setupUi

    def retranslateUi(self, add_machine_form):
        add_machine_form.setWindowTitle(QCoreApplication.translate("add_machine_form", u"\u6dfb\u52a0\u8bbe\u5907", None))
        self.down_position.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9U\u4f4d", None))
        self.lb_machine_admin.setText(QCoreApplication.translate("add_machine_form", u"\u8d1f \u8d23 \u4eba", None))
        self.lb_mg_ip_2.setText(QCoreApplication.translate("add_machine_form", u"BMC IP", None))
        self.up_position.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9U\u4f4d", None))
        self.cabinet.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9\u673a\u67dc", None))
        self.lb_last_date.setText(QCoreApplication.translate("add_machine_form", u"\u5230\u4fdd\u65e5\u671f", None))
        self.lb_install_date.setText(QCoreApplication.translate("add_machine_form", u"\u4e0a\u67b6\u65e5\u671f", None))
        self.lb_admin.setText(QCoreApplication.translate("add_machine_form", u"\u7ba1 \u7406 \u5458", None))
        self.single_power.setText(QCoreApplication.translate("add_machine_form", u"\u5355\u7535\u6e90", None))
        self.room.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9\u673a\u623f", None))
        self.lb_sn.setText(QCoreApplication.translate("add_machine_form", u"\u8bbe \u5907 SN", None))
        self.lb_fa_date.setText(QCoreApplication.translate("add_machine_form", u"\u51fa\u5382\u65e5\u671f", None))
        self.save.setText(QCoreApplication.translate("add_machine_form", u"\u4fdd    \u5b58", None))
        self.lb_down.setText(QCoreApplication.translate("add_machine_form", u"\u4e0b  U \u4f4d", None))
        self.lb_comments.setText(QCoreApplication.translate("add_machine_form", u"\u5907      \u6ce8", None))
        self.lb_up.setText(QCoreApplication.translate("add_machine_form", u"\u4e0a  U \u4f4d", None))
        self.lb_app_ip.setText(QCoreApplication.translate("add_machine_form", u"\u4e1a\u52a1 IP", None))
        self.lb_machine_name.setText(QCoreApplication.translate("add_machine_form", u"\u8bbe\u5907\u540d\u79f0", None))
        self.lb_cabinet.setText(QCoreApplication.translate("add_machine_form", u"\u673a     \u67dc", None))
        self.work_are.setItemText(0, QCoreApplication.translate("add_machine_form", u"1\u751f\u4ea7", None))
        self.work_are.setItemText(1, QCoreApplication.translate("add_machine_form", u"2\u7535\u6e20", None))
        self.work_are.setItemText(2, QCoreApplication.translate("add_machine_form", u"3\u707e\u5907", None))
        self.work_are.setItemText(3, QCoreApplication.translate("add_machine_form", u"4\u5f00\u53d1", None))

        self.work_are.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9\u4e1a\u52a1\u7c7b\u578b", None))
        self.lb_mg_ip.setText(QCoreApplication.translate("add_machine_form", u"\u7ba1 \u7406 IP", None))
        self.lb_factory.setText(QCoreApplication.translate("add_machine_form", u"\u8bbe\u5907\u54c1\u724c", None))
        self.lb_sort.setText(QCoreApplication.translate("add_machine_form", u"\u8bbe\u5907\u7c7b\u578b", None))
        self.lb_mode.setText(QCoreApplication.translate("add_machine_form", u"\u578b     \u53f7", None))
        self.lb_work.setText(QCoreApplication.translate("add_machine_form", u"\u4e1a\u52a1\u7c7b\u578b", None))
        self.machine_factory.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9\u54c1\u724c", None))
        self.clear.setText(QCoreApplication.translate("add_machine_form", u"\u6e05    \u7a7a", None))
        self.label.setText(QCoreApplication.translate("add_machine_form", u"\u6dfb\u52a0\u8bbe\u5907", None))
        self.sort_name.setPlaceholderText(QCoreApplication.translate("add_machine_form", u"\u70b9\u51fb\u9009\u62e9\u7c7b\u578b", None))
        self.lb_room.setText(QCoreApplication.translate("add_machine_form", u"\u673a      \u623f", None))
        self.label_2.setText(QCoreApplication.translate("add_machine_form", u"\u8be5\u6a21\u5757\u4e3b\u8981\u7528\u4e8e\u8865\u5f55\u5df2\u4e0a\u67b6\uff0c\u4f46\u4e0d\u9700\u8981\u4e0a\u67b6\u5355\u7684\u8bbe\u5907\u3002", None))
    # retranslateUi

