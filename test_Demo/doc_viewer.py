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
from PySide6.QtWidgets import (QApplication, QFrame, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QSplitter,
    QStatusBar, QTabWidget, QTextBrowser, QTextEdit,
    QToolBar, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 750)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_bold = QAction(MainWindow)
        self.action_bold.setObjectName(u"action_bold")
        self.action_displaylist = QAction(MainWindow)
        self.action_displaylist.setObjectName(u"action_displaylist")
        self.action_displaylist.setCheckable(True)
        self.action_displaylist.setChecked(True)
        self.action_full = QAction(MainWindow)
        self.action_full.setObjectName(u"action_full")
        self.action_to_md = QAction(MainWindow)
        self.action_to_md.setObjectName(u"action_to_md")
        self.action_to_md.setCheckable(True)
        self.action_save = QAction(MainWindow)
        self.action_save.setObjectName(u"action_save")
        self.action_exit = QAction(MainWindow)
        self.action_exit.setObjectName(u"action_exit")
        self.actioncut = QAction(MainWindow)
        self.actioncut.setObjectName(u"actioncut")
        self.actionpate = QAction(MainWindow)
        self.actionpate.setObjectName(u"actionpate")
        self.actionselectall = QAction(MainWindow)
        self.actionselectall.setObjectName(u"actionselectall")
        self.action_find = QAction(MainWindow)
        self.action_find.setObjectName(u"action_find")
        self.action_replace = QAction(MainWindow)
        self.action_replace.setObjectName(u"action_replace")
        self.action_copy = QAction(MainWindow)
        self.action_copy.setObjectName(u"action_copy")
        self.action_italic = QAction(MainWindow)
        self.action_italic.setObjectName(u"action_italic")
        self.action_underline = QAction(MainWindow)
        self.action_underline.setObjectName(u"action_underline")
        self.action_annotate = QAction(MainWindow)
        self.action_annotate.setObjectName(u"action_annotate")
        self.action_deleteline = QAction(MainWindow)
        self.action_deleteline.setObjectName(u"action_deleteline")
        self.action_removestyle = QAction(MainWindow)
        self.action_removestyle.setObjectName(u"action_removestyle")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_markdown = QAction(MainWindow)
        self.action_markdown.setObjectName(u"action_markdown")
        self.action_web = QAction(MainWindow)
        self.action_web.setObjectName(u"action_web")
        self.action_clip = QAction(MainWindow)
        self.action_clip.setObjectName(u"action_clip")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.tabWidget = QTabWidget(self.splitter)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet(u"background-color:rgb(240,255,255)")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab_file = QWidget()
        self.tab_file.setObjectName(u"tab_file")
        self.verticalLayout_2 = QVBoxLayout(self.tab_file)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.tree_file = QTreeWidget(self.tab_file)
        self.tree_file.setObjectName(u"tree_file")
        self.tree_file.setStyleSheet(u"background-color:rgb(225,255,255)")

        self.verticalLayout_2.addWidget(self.tree_file)

        self.tabWidget.addTab(self.tab_file, "")
        self.tab_profile = QWidget()
        self.tab_profile.setObjectName(u"tab_profile")
        self.verticalLayout_3 = QVBoxLayout(self.tab_profile)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tree_profile = QTreeWidget(self.tab_profile)
        self.tree_profile.headerItem().setText(0, "")
        self.tree_profile.setObjectName(u"tree_profile")

        self.verticalLayout_3.addWidget(self.tree_profile)

        self.tabWidget.addTab(self.tab_profile, "")
        self.splitter.addWidget(self.tabWidget)
        self.input_text = QTextEdit(self.splitter)
        self.input_text.setObjectName(u"input_text")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(4)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.input_text.sizePolicy().hasHeightForWidth())
        self.input_text.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(12)
        self.input_text.setFont(font)
        self.input_text.setAutoFillBackground(False)
        self.input_text.setStyleSheet(u"background-color:rgb(253,245,230)")
        self.input_text.setFrameShape(QFrame.WinPanel)
        self.input_text.setFrameShadow(QFrame.Sunken)
        self.input_text.setOverwriteMode(False)
        self.splitter.addWidget(self.input_text)
        self.display_text = QTextBrowser(self.splitter)
        self.display_text.setObjectName(u"display_text")
        sizePolicy1.setHeightForWidth(self.display_text.sizePolicy().hasHeightForWidth())
        self.display_text.setSizePolicy(sizePolicy1)
        self.display_text.setStyleSheet(u"background-color:rgb(240,255,240)")
        self.splitter.addWidget(self.display_text)

        self.verticalLayout.addWidget(self.splitter)

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
        self.menufindandreplace = QMenu(self.menu_edit)
        self.menufindandreplace.setObjectName(u"menufindandreplace")
        self.menu_view = QMenu(self.menubar)
        self.menu_view.setObjectName(u"menu_view")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_quick = QToolBar(MainWindow)
        self.toolBar_quick.setObjectName(u"toolBar_quick")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_quick)

        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_edit.menuAction())
        self.menubar.addAction(self.menu_format.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_format.addAction(self.action_bold)
        self.menu_format.addAction(self.action_italic)
        self.menu_format.addAction(self.action_underline)
        self.menu_format.addSeparator()
        self.menu_format.addAction(self.action_annotate)
        self.menu_format.addAction(self.action_deleteline)
        self.menu_format.addSeparator()
        self.menu_format.addAction(self.action_removestyle)
        self.menu_format.addSeparator()
        self.menu_format.addAction(self.action_markdown)
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_web)
        self.menu_edit.addAction(self.action_copy)
        self.menu_edit.addAction(self.actioncut)
        self.menu_edit.addAction(self.actionpate)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.actionselectall)
        self.menu_edit.addSeparator()
        self.menu_edit.addAction(self.menufindandreplace.menuAction())
        self.menufindandreplace.addAction(self.action_find)
        self.menufindandreplace.addAction(self.action_replace)
        self.menu_view.addAction(self.action_displaylist)
        self.menu_view.addAction(self.action_full)
        self.toolBar.addAction(self.action_open)
        self.toolBar.addAction(self.action_save)
        self.toolBar.addAction(self.action_exit)
        self.toolBar_quick.addAction(self.action_to_md)
        self.toolBar_quick.addAction(self.action_displaylist)
        self.toolBar_quick.addSeparator()
        self.toolBar_quick.addAction(self.action_clip)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Base\u7b14\u8bb0", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.action_bold.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u7c97", None))
        self.action_displaylist.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a/\u9690\u85cf\u5217\u8868", None))
        self.action_full.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c4f\u9884\u89c8", None))
        self.action_to_md.setText(QCoreApplication.translate("MainWindow", u"\u6e90\u7801/\u9884\u89c8", None))
#if QT_CONFIG(tooltip)
        self.action_to_md.setToolTip(QCoreApplication.translate("MainWindow", u"\u6e90\u7801/\u9884\u89c8", None))
#endif // QT_CONFIG(tooltip)
        self.action_save.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.action_exit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actioncut.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207", None))
        self.actionpate.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34", None))
        self.actionselectall.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009", None))
        self.action_find.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e", None))
        self.action_replace.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362", None))
        self.action_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.action_italic.setText(QCoreApplication.translate("MainWindow", u"\u659c\u4f53", None))
        self.action_underline.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u5212\u7ebf", None))
        self.action_annotate.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u91ca", None))
        self.action_deleteline.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664\u7ebf", None))
        self.action_removestyle.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u9664\u6837\u5f0f", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.action_markdown.setText(QCoreApplication.translate("MainWindow", u"markdown\u9884\u89c8", None))
        self.action_web.setText(QCoreApplication.translate("MainWindow", u"\u7f51\u7ad9", None))
        self.action_clip.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u7c98\u8d34\u677f\u5185\u5bb9", None))
        ___qtreewidgetitem = self.tree_file.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u6211\u7684", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_profile), QCoreApplication.translate("MainWindow", u"\u5927\u7eb2", None))
        self.menu_file.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_format.setTitle(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f", None))
        self.menu_help.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9", None))
        self.menu_edit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None))
        self.menufindandreplace.setTitle(QCoreApplication.translate("MainWindow", u"\u67e5\u627e\u66ff\u6362", None))
        self.menu_view.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_quick.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
    # retranslateUi

