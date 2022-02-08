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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(486, 320)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(0, 230, 471, 32))
        self.buttonBox.setLayoutDirection(Qt.LeftToRight)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
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
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.path_le = QLineEdit(self.layoutWidget)
        self.path_le.setObjectName(u"path_le")

        self.horizontalLayout.addWidget(self.path_le)

        self.import_btn = QPushButton(self.layoutWidget)
        self.import_btn.setObjectName(u"import_btn")

        self.horizontalLayout.addWidget(self.import_btn)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u6279\u91cf\u5bfc\u5165\u8bbe\u5907\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u6279\u91cf\u5bfc\u5165\u8bbe\u5907\u4fe1\u606f", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6ce8\uff1a\u7528\u4e8e\u5927\u91cf\u6570\u636e\u5bfc\u5165\u65f6\u7528", None))
        self.import_btn.setText(QCoreApplication.translate("Dialog", u"\u9009\u62e9", None))
    # retranslateUi

