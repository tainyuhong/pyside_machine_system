# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'report.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QSizePolicy, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_report_form(object):
    def setupUi(self, report_form):
        if not report_form.objectName():
            report_form.setObjectName(u"report_form")
        report_form.resize(1024, 768)
        self.horizontalLayout = QHBoxLayout(report_form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.graph_room = QChartView(report_form)
        self.graph_room.setObjectName(u"graph_room")

        self.gridLayout.addWidget(self.graph_room, 2, 0, 1, 1)

        self.graph_cabinet = QChartView(report_form)
        self.graph_cabinet.setObjectName(u"graph_cabinet")

        self.gridLayout.addWidget(self.graph_cabinet, 2, 1, 1, 1)

        self.label_2 = QLabel(report_form)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.label = QLabel(report_form)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(45)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_4 = QLabel(report_form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(report_form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)

        self.treeWidget = QTreeWidget(report_form)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.gridLayout.addWidget(self.treeWidget, 4, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 2)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 6)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 7)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 3)

        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(report_form)

        QMetaObject.connectSlotsByName(report_form)
    # setupUi

    def retranslateUi(self, report_form):
        report_form.setWindowTitle(QCoreApplication.translate("report_form", u"\u5206\u6790\u62a5\u544a", None))
        self.label_2.setText(QCoreApplication.translate("report_form", u"\u4e00\u3001\u673a\u623f\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("report_form", u"\u7edf\u8ba1\u5206\u6790", None))
        self.label_4.setText(QCoreApplication.translate("report_form", u"\u4e09\u3001\u8bbe\u5907\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("report_form", u"\u4e8c\u3001\u673a\u67dc\u4fe1\u606f", None))
    # retranslateUi

