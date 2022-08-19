# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addhost_win.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_addhost_win(object):
    def setupUi(self, addhost_win):
        if not addhost_win.objectName():
            addhost_win.setObjectName(u"addhost_win")
        addhost_win.setWindowModality(Qt.NonModal)
        addhost_win.resize(850, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(addhost_win.sizePolicy().hasHeightForWidth())
        addhost_win.setSizePolicy(sizePolicy)
        addhost_win.setModal(True)
        self.horizontalLayout = QHBoxLayout(addhost_win)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(addhost_win)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.treeWidget = QTreeWidget(addhost_win)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setColumnCount(3)
        self.treeWidget.header().setDefaultSectionSize(120)

        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.add_btn = QPushButton(addhost_win)
        self.add_btn.setObjectName(u"add_btn")

        self.gridLayout.addWidget(self.add_btn, 1, 2, 1, 1)

        self.label_2 = QLabel(addhost_win)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 9)
        self.gridLayout.setColumnStretch(0, 7)
        self.gridLayout.setColumnStretch(2, 2)

        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(addhost_win)

        QMetaObject.connectSlotsByName(addhost_win)
    # setupUi

    def retranslateUi(self, addhost_win):
        addhost_win.setWindowTitle(QCoreApplication.translate("addhost_win", u"\u6dfb\u52a0\u4e3b\u673a", None))
        self.label.setText(QCoreApplication.translate("addhost_win", u"\u6dfb\u52a0\u4e3b\u673a", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("addhost_win", u"\u7ba1\u7406IP", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("addhost_win", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("addhost_win", u"\u8bbe\u5907\u5206\u7c7b", None));
        self.add_btn.setText(QCoreApplication.translate("addhost_win", u"\u6dfb\u52a0", None))
        self.label_2.setText("")
    # retranslateUi

