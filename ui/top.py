# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'top.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_top(object):
    def setupUi(self, top):
        if not top.objectName():
            top.setObjectName(u"top")
        top.resize(1024, 768)
        self.horizontalLayout = QHBoxLayout(top)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(top)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.tabWidget = QTabWidget(top)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.South)
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabWidget.setElideMode(Qt.ElideNone)

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(top)

        QMetaObject.connectSlotsByName(top)
    # setupUi

    def retranslateUi(self, top):
        top.setWindowTitle(QCoreApplication.translate("top", u"\u8bbe\u5907\u4f4d\u7f6e\u793a\u610f\u56fe", None))
        self.label.setText(QCoreApplication.translate("top", u"\u673a\u67dc\u8bbe\u5907\u4f4d\u7f6e\u793a\u610f\u56fe", None))
    # retranslateUi

