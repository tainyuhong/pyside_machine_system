# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'export_excel.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_export_form(object):
    def setupUi(self, export_form):
        if not export_form.objectName():
            export_form.setObjectName(u"export_form")
        export_form.resize(1024, 768)
        self.verticalLayout = QVBoxLayout(export_form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 6, 1, 1, 1)

        self.label_2 = QLabel(export_form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 2, 1, 1, 1)

        self.listWidget = QListWidget(export_form)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout.addWidget(self.listWidget, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.btn_export = QPushButton(export_form)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setFont(font)

        self.gridLayout.addWidget(self.btn_export, 5, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.label = QLabel(export_form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(35)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.label_3 = QLabel(export_form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 7, 0, 1, 3)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(2, 1)
        self.gridLayout.setRowStretch(3, 7)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 5)
        self.gridLayout.setColumnStretch(2, 1)

        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(export_form)

        QMetaObject.connectSlotsByName(export_form)
    # setupUi

    def retranslateUi(self, export_form):
        export_form.setWindowTitle(QCoreApplication.translate("export_form", u"\u5bfc\u51fa\u81f3excel", None))
        self.label_2.setText(QCoreApplication.translate("export_form", u"\u8bf7\u94a9\u9009\u9700\u8981\u5bfc\u51fa\u7684\u4fe1\u606f", None))
        self.btn_export.setText(QCoreApplication.translate("export_form", u"\u5bfc  \u51fa", None))
        self.label.setText(QCoreApplication.translate("export_form", u"\u5bfc\u51fa\u8bbe\u5907\u4fe1\u606f\u81f3EXCEL", None))
        self.label_3.setText(QCoreApplication.translate("export_form", u"\u72b6\u6001", None))
    # retranslateUi

