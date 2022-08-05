# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_win.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1100, 700)
        self.actionjfgl = QAction(MainWindow)
        self.actionjfgl.setObjectName(u"actionjfgl")
        self.actionjg = QAction(MainWindow)
        self.actionjg.setObjectName(u"actionjg")
        self.actionu = QAction(MainWindow)
        self.actionu.setObjectName(u"actionu")
        self.actiontjsb = QAction(MainWindow)
        self.actiontjsb.setObjectName(u"actiontjsb")
        self.actionxg = QAction(MainWindow)
        self.actionxg.setObjectName(u"actionxg")
        self.actionsjgl = QAction(MainWindow)
        self.actionsjgl.setObjectName(u"actionsjgl")
        self.actionxjgl = QAction(MainWindow)
        self.actionxjgl.setObjectName(u"actionxjgl")
        self.actionsjpz = QAction(MainWindow)
        self.actionsjpz.setObjectName(u"actionsjpz")
        self.actionsj = QAction(MainWindow)
        self.actionsj.setObjectName(u"actionsj")
        self.actioncxsb = QAction(MainWindow)
        self.actioncxsb.setObjectName(u"actioncxsb")
        self.actionpldr = QAction(MainWindow)
        self.actionpldr.setObjectName(u"actionpldr")
        self.action_base = QAction(MainWindow)
        self.action_base.setObjectName(u"action_base")
        self.action_shelf_display = QAction(MainWindow)
        self.action_shelf_display.setObjectName(u"action_shelf_display")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1100, 22))
        self.mu_baseinfo = QMenu(self.menubar)
        self.mu_baseinfo.setObjectName(u"mu_baseinfo")
        self.mu_machine = QMenu(self.menubar)
        self.mu_machine.setObjectName(u"mu_machine")
        self.mu_select = QMenu(self.menubar)
        self.mu_select.setObjectName(u"mu_select")
        self.mu_shelf = QMenu(self.menubar)
        self.mu_shelf.setObjectName(u"mu_shelf")
        self.mu_poll = QMenu(self.menubar)
        self.mu_poll.setObjectName(u"mu_poll")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.mu_baseinfo.menuAction())
        self.menubar.addAction(self.mu_machine.menuAction())
        self.menubar.addAction(self.mu_select.menuAction())
        self.menubar.addAction(self.mu_shelf.menuAction())
        self.menubar.addAction(self.mu_poll.menuAction())
        self.mu_baseinfo.addAction(self.action_base)
        self.mu_machine.addAction(self.actiontjsb)
        self.mu_machine.addAction(self.actionxg)
        self.mu_machine.addAction(self.actionpldr)
        self.mu_select.addAction(self.actioncxsb)
        self.mu_shelf.addAction(self.actionsjgl)
        self.mu_shelf.addAction(self.actionxjgl)
        self.mu_shelf.addSeparator()
        self.mu_shelf.addAction(self.action_shelf_display)
        self.mu_poll.addAction(self.actionsjpz)
        self.mu_poll.addAction(self.actionsj)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u673a\u623f\u8bbe\u5907\u7ba1\u7406\u7cfb\u7edfpyside6-V1.0", None))
        self.actionjfgl.setText(QCoreApplication.translate("MainWindow", u"\u673a\u623f\u7ba1\u7406", None))
        self.actionjg.setText(QCoreApplication.translate("MainWindow", u"\u673a\u67dc\u7ba1\u7406", None))
        self.actionu.setText(QCoreApplication.translate("MainWindow", u"U\u4f4d\u7ba1\u7406", None))
        self.actiontjsb.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u8bbe\u5907", None))
        self.actionxg.setText(QCoreApplication.translate("MainWindow", u"\u4fee\u6539\u8bbe\u5907\u4fe1\u606f", None))
        self.actionsjgl.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u67b6\u7ba1\u7406", None))
        self.actionxjgl.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u67b6\u7ba1\u7406", None))
        self.actionsjpz.setText(QCoreApplication.translate("MainWindow", u"\u5de1\u68c0\u914d\u7f6e", None))
        self.actionsj.setText(QCoreApplication.translate("MainWindow", u"\u5de1\u68c0\u64cd\u4f5c", None))
        self.actioncxsb.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8bbe\u5907", None))
        self.actionpldr.setText(QCoreApplication.translate("MainWindow", u"\u6279\u91cf\u5bfc\u5165\u8bbe\u5907", None))
        self.action_base.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u4fe1\u606f\u7ba1\u7406", None))
        self.action_shelf_display.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e0b\u67b6\u4fe1\u606f\u67e5\u8be2", None))
        self.mu_baseinfo.setTitle(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u4fe1\u606f", None))
        self.mu_machine.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7ba1\u7406", None))
        self.mu_select.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u7ba1\u7406", None))
        self.mu_shelf.setTitle(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e0b\u67b6\u7ba1\u7406", None))
        self.mu_poll.setTitle(QCoreApplication.translate("MainWindow", u"\u5de1\u68c0\u7ba1\u7406", None))
    # retranslateUi

