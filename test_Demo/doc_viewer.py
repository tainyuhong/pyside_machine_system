# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'doc_viewer.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QListWidget,
    QListWidgetItem, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSplitter, QStatusBar,
    QTextBrowser, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionopen = QAction(MainWindow)
        self.actionopen.setObjectName(u"actionopen")
        self.action_title1 = QAction(MainWindow)
        self.action_title1.setObjectName(u"action_title1")
        self.action_hide = QAction(MainWindow)
        self.action_hide.setObjectName(u"action_hide")
        self.action_display = QAction(MainWindow)
        self.action_display.setObjectName(u"action_display")
        self.action_full = QAction(MainWindow)
        self.action_full.setObjectName(u"action_full")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setFrameShape(QFrame.StyledPanel)
        self.splitter.setFrameShadow(QFrame.Sunken)
        self.splitter.setLineWidth(1)
        self.splitter.setMidLineWidth(3)
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(2)
        self.splitter.setChildrenCollapsible(True)
        self.file_list = QListWidget(self.splitter)
        self.file_list.setObjectName(u"file_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.file_list.sizePolicy().hasHeightForWidth())
        self.file_list.setSizePolicy(sizePolicy1)
        self.file_list.setFrameShadow(QFrame.Raised)
        self.splitter.addWidget(self.file_list)
        self.input_text = QTextEdit(self.splitter)
        self.input_text.setObjectName(u"input_text")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(4)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy2)
        self.input_text.setFrameShape(QFrame.WinPanel)
        self.input_text.setFrameShadow(QFrame.Sunken)
        self.input_text.setOverwriteMode(False)
        self.splitter.addWidget(self.input_text)
        self.display_text = QTextBrowser(self.splitter)
        self.display_text.setObjectName(u"display_text")
        sizePolicy2.setHeightForWidth(self.display_text.sizePolicy().hasHeightForWidth())
        self.display_text.setSizePolicy(sizePolicy2)
        self.splitter.addWidget(self.display_text)

        self.verticalLayout.addWidget(self.splitter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout.addWidget(self.pushButton)

        self.html_btn = QPushButton(self.centralwidget)
        self.html_btn.setObjectName(u"html_btn")

        self.horizontalLayout.addWidget(self.html_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 22))
        self.menu_file = QMenu(self.menubar)
        self.menu_file.setObjectName(u"menu_file")
        self.menu_format = QMenu(self.menubar)
        self.menu_format.setObjectName(u"menu_format")
        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName(u"menu_help")
        self.menu_edit = QMenu(self.menubar)
        self.menu_edit.setObjectName(u"menu_edit")
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_format.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.actionnew)
        self.menu_file.addAction(self.actionopen)
        self.menu_format.addAction(self.action_title1)
        self.menu_edit.addAction(self.actionnew)
        self.menu.addAction(self.action_hide)
        self.menu.addAction(self.action_display)
        self.menu.addAction(self.action_full)
        self.toolBar.addAction(self.actionnew)
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addAction(self.action_title1)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa", None))
        self.actionopen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_title1.setText(QCoreApplication.translate("MainWindow", u"\u6807\u98981", None))
        self.action_hide.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf\u5217\u8868", None))
        self.action_display.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5217\u8868", None))
        self.action_full.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f\u9884\u89c8", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"markdown", None))
        self.html_btn.setText(QCoreApplication.translate("MainWindow", u"\u9690\u85cf", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_format.setTitle(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

