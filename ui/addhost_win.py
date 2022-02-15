# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addhost_win.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QColumnView, QDialog, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_addhost_win(object):
    def setupUi(self, addhost_win):
        if not addhost_win.objectName():
            addhost_win.setObjectName(u"addhost_win")
        addhost_win.resize(400, 300)
        self.label = QLabel(addhost_win)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 20, 54, 16))
        self.add_btn = QPushButton(addhost_win)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setGeometry(QRect(310, 60, 75, 24))
        self.columnView = QColumnView(addhost_win)
        self.columnView.setObjectName(u"columnView")
        self.columnView.setGeometry(QRect(20, 60, 256, 192))

        self.retranslateUi(addhost_win)

        QMetaObject.connectSlotsByName(addhost_win)
    # setupUi

    def retranslateUi(self, addhost_win):
        addhost_win.setWindowTitle(QCoreApplication.translate("addhost_win", u"\u6dfb\u52a0\u4e3b\u673a", None))
        self.label.setText(QCoreApplication.translate("addhost_win", u"\u6dfb\u52a0\u4e3b\u673a", None))
        self.add_btn.setText(QCoreApplication.translate("addhost_win", u"\u6dfb\u52a0", None))
    # retranslateUi

