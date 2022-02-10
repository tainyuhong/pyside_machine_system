# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machine_import.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(486, 320)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 20, 331, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 300, 451, 20))
        self.label_2.setStyleSheet(u"color:red")
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 110, 471, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.path_le = QLineEdit(self.layoutWidget)
        self.path_le.setObjectName(u"path_le")
        self.path_le.setReadOnly(False)

        self.horizontalLayout.addWidget(self.path_le)

        self.select_btn = QPushButton(self.layoutWidget)
        self.select_btn.setObjectName(u"select_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.select_btn)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 2)
        self.import_btn = QPushButton(Dialog)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setGeometry(QRect(170, 210, 75, 24))
        self.template_lb = QLabel(Dialog)
        self.template_lb.setObjectName(u"template_lb")
        self.template_lb.setGeometry(QRect(410, 270, 54, 16))
        self.template_lb.setStyleSheet(u"color:blue")
        self.template_lb.setOpenExternalLinks(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6279\u91cf\u5bfc\u5165\u8bbe\u5907\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6279\u91cf\u5bfc\u5165\u8bbe\u5907\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u7528\u4e8e\u5927\u91cf\u6570\u636e\u5bfc\u5165\u65f6\u7528", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u8def\u5f84\uff1a", None))
#if QT_CONFIG(tooltip)
        self.path_le.setToolTip(QCoreApplication.translate("Dialog", u"\u8bf7\u9009\u62e9\u9700\u8981\u5bfc\u5165\u7684\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.path_le.setText("")
        self.path_le.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u9009\u62e9\u9700\u8981\u5bfc\u5165\u7684\u6587\u4ef6", None))
        self.select_btn.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9", None))
        self.import_btn.setText(QCoreApplication.translate("Dialog", u"\u5bfc\u5165", None))
        self.template_lb.setText(QCoreApplication.translate("Dialog", u"\u6a21\u677f\u4e0b\u8f7d", None))
    # retranslateUi

