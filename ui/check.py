# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'check.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QPushButton, QRadioButton, QSizePolicy,
    QSplitter, QTextEdit, QWidget)

class Ui_check_form(object):
    def setupUi(self, check_form):
        if not check_form.objectName():
            check_form.setObjectName(u"check_form")
        check_form.resize(1000, 720)
        check_form.setMinimumSize(QSize(1000, 720))
        check_form.setMaximumSize(QSize(1000, 720))
        self.v_splitter = QSplitter(check_form)
        self.v_splitter.setObjectName(u"v_splitter")
        self.v_splitter.setGeometry(QRect(0, 0, 1000, 700))
        self.v_splitter.setFrameShape(QFrame.StyledPanel)
        self.v_splitter.setFrameShadow(QFrame.Raised)
        self.v_splitter.setLineWidth(0)
        self.v_splitter.setOrientation(Qt.Vertical)
        self.v_splitter.setHandleWidth(0)
        self.top_frame = QFrame(self.v_splitter)
        self.top_frame.setObjectName(u"top_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.top_frame.sizePolicy().hasHeightForWidth())
        self.top_frame.setSizePolicy(sizePolicy)
        self.top_frame.setMinimumSize(QSize(1000, 100))
        self.top_frame.setMaximumSize(QSize(1000, 100))
        self.top_frame.setLayoutDirection(Qt.RightToLeft)
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 20, 311, 51))
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:blue")
        self.label.setFrameShape(QFrame.NoFrame)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setAlignment(Qt.AlignCenter)
        self.v_splitter.addWidget(self.top_frame)
        self.h_splitter = QSplitter(self.v_splitter)
        self.h_splitter.setObjectName(u"h_splitter")
        sizePolicy.setHeightForWidth(self.h_splitter.sizePolicy().hasHeightForWidth())
        self.h_splitter.setSizePolicy(sizePolicy)
        self.h_splitter.setFrameShape(QFrame.StyledPanel)
        self.h_splitter.setFrameShadow(QFrame.Raised)
        self.h_splitter.setLineWidth(0)
        self.h_splitter.setMidLineWidth(0)
        self.h_splitter.setOrientation(Qt.Horizontal)
        self.h_splitter.setOpaqueResize(True)
        self.h_splitter.setHandleWidth(0)
        self.h_splitter.setChildrenCollapsible(True)
        self.l_frame = QFrame(self.h_splitter)
        self.l_frame.setObjectName(u"l_frame")
        self.l_frame.setMinimumSize(QSize(0, 0))
        self.l_frame.setMaximumSize(QSize(200, 16777215))
        self.l_frame.setFrameShape(QFrame.WinPanel)
        self.l_frame.setFrameShadow(QFrame.Raised)
        self.l_frame.setLineWidth(0)
        self.layoutWidget = QWidget(self.l_frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 181, 571))
        self.l_gridLayout = QGridLayout(self.layoutWidget)
        self.l_gridLayout.setObjectName(u"l_gridLayout")
        self.l_gridLayout.setContentsMargins(0, 0, 0, 0)
        self.check_cb = QCheckBox(self.layoutWidget)
        self.check_cb.setObjectName(u"check_cb")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.check_cb.setFont(font1)

        self.l_gridLayout.addWidget(self.check_cb, 0, 1, 1, 1)

        self.hosts_lb = QLabel(self.layoutWidget)
        self.hosts_lb.setObjectName(u"hosts_lb")
        self.hosts_lb.setFont(font1)

        self.l_gridLayout.addWidget(self.hosts_lb, 0, 0, 1, 1)

        self.hostlist_te = QTextEdit(self.layoutWidget)
        self.hostlist_te.setObjectName(u"hostlist_te")
        self.hostlist_te.setReadOnly(True)

        self.l_gridLayout.addWidget(self.hostlist_te, 1, 0, 1, 2)

        self.h_splitter.addWidget(self.l_frame)
        self.r_frame = QFrame(self.h_splitter)
        self.r_frame.setObjectName(u"r_frame")
        sizePolicy.setHeightForWidth(self.r_frame.sizePolicy().hasHeightForWidth())
        self.r_frame.setSizePolicy(sizePolicy)
        self.r_frame.setMinimumSize(QSize(0, 0))
        self.r_frame.setFrameShape(QFrame.WinPanel)
        self.r_frame.setFrameShadow(QFrame.Raised)
        self.r_frame.setLineWidth(0)
        self.r_frame.setMidLineWidth(0)
        self.layoutWidget1 = QWidget(self.r_frame)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(3, 10, 791, 571))
        self.r_gridLayout = QGridLayout(self.layoutWidget1)
        self.r_gridLayout.setSpacing(6)
        self.r_gridLayout.setObjectName(u"r_gridLayout")
        self.r_gridLayout.setContentsMargins(5, 0, 10, 0)
        self.stat_radio = QRadioButton(self.layoutWidget1)
        self.stat_radio.setObjectName(u"stat_radio")
        self.stat_radio.setFont(font1)

        self.r_gridLayout.addWidget(self.stat_radio, 0, 2, 1, 1)

        self.exec_btn = QPushButton(self.layoutWidget1)
        self.exec_btn.setObjectName(u"exec_btn")
        self.exec_btn.setFont(font1)
        self.exec_btn.setAutoDefault(False)
        self.exec_btn.setFlat(False)

        self.r_gridLayout.addWidget(self.exec_btn, 0, 3, 1, 1)

        self.ping_radio = QRadioButton(self.layoutWidget1)
        self.ping_radio.setObjectName(u"ping_radio")
        self.ping_radio.setFont(font1)

        self.r_gridLayout.addWidget(self.ping_radio, 0, 1, 1, 1)

        self.label_3 = QLabel(self.layoutWidget1)
        self.label_3.setObjectName(u"label_3")

        self.r_gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.dispaly_te = QTextEdit(self.layoutWidget1)
        self.dispaly_te.setObjectName(u"dispaly_te")
        self.dispaly_te.setLineWidth(0)
        self.dispaly_te.setReadOnly(True)

        self.r_gridLayout.addWidget(self.dispaly_te, 1, 0, 1, 4)

        self.r_gridLayout.setColumnStretch(0, 2)
        self.r_gridLayout.setColumnStretch(1, 3)
        self.r_gridLayout.setColumnStretch(2, 3)
        self.r_gridLayout.setColumnStretch(3, 2)
        self.h_splitter.addWidget(self.r_frame)
        self.v_splitter.addWidget(self.h_splitter)
        self.stat_lb = QLabel(check_form)
        self.stat_lb.setObjectName(u"stat_lb")
        self.stat_lb.setGeometry(QRect(5, 700, 995, 18))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stat_lb.sizePolicy().hasHeightForWidth())
        self.stat_lb.setSizePolicy(sizePolicy1)
        self.stat_lb.setStyleSheet(u"color:blue")
        self.stat_lb.setFrameShape(QFrame.Box)
        self.stat_lb.setFrameShadow(QFrame.Raised)

        self.retranslateUi(check_form)

        self.exec_btn.setDefault(False)


        QMetaObject.connectSlotsByName(check_form)
    # setupUi

    def retranslateUi(self, check_form):
        check_form.setWindowTitle(QCoreApplication.translate("check_form", u"Form", None))
        self.label.setText(QCoreApplication.translate("check_form", u"\u8bbe \u5907 \u5de1 \u68c0", None))
        self.check_cb.setText(QCoreApplication.translate("check_form", u"\u5168\u9009", None))
        self.hosts_lb.setText(QCoreApplication.translate("check_form", u"\u4e3b\u673a\u5217\u8868", None))
        self.stat_radio.setText(QCoreApplication.translate("check_form", u"\u5065\u5eb7\u72b6\u6001\u68c0\u67e5", None))
        self.exec_btn.setText(QCoreApplication.translate("check_form", u"\u6267\u884c", None))
        self.ping_radio.setText(QCoreApplication.translate("check_form", u"ping", None))
        self.label_3.setText("")
        self.stat_lb.setText(QCoreApplication.translate("check_form", u"\u5c31\u7eea", None))
    # retranslateUi

