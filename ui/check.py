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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QListWidget, QListWidgetItem,
    QPushButton, QRadioButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_check_form(object):
    def setupUi(self, check_form):
        if not check_form.objectName():
            check_form.setObjectName(u"check_form")
        check_form.resize(1006, 734)
        check_form.setMinimumSize(QSize(1006, 734))
        check_form.setMaximumSize(QSize(1006, 734))
        self.layoutWidget = QWidget(check_form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 1002, 731))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.top_frame = QFrame(self.layoutWidget)
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

        self.verticalLayout_2.addWidget(self.top_frame)

        self.conteck_ly = QHBoxLayout()
        self.conteck_ly.setSpacing(0)
        self.conteck_ly.setObjectName(u"conteck_ly")
        self.conteck_ly.setSizeConstraint(QLayout.SetMinimumSize)
        self.l_frame = QFrame(self.layoutWidget)
        self.l_frame.setObjectName(u"l_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.l_frame.sizePolicy().hasHeightForWidth())
        self.l_frame.setSizePolicy(sizePolicy1)
        self.l_frame.setMinimumSize(QSize(0, 0))
        self.l_frame.setMaximumSize(QSize(16777215, 16777215))
        self.l_frame.setFrameShape(QFrame.WinPanel)
        self.l_frame.setFrameShadow(QFrame.Raised)
        self.l_frame.setLineWidth(0)
        self.layoutWidget_2 = QWidget(self.l_frame)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(11, 10, 281, 581))
        self.lgdLayout = QGridLayout(self.layoutWidget_2)
        self.lgdLayout.setObjectName(u"lgdLayout")
        self.lgdLayout.setContentsMargins(0, 0, 0, 0)
        self.addhost_btn = QPushButton(self.layoutWidget_2)
        self.addhost_btn.setObjectName(u"addhost_btn")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.addhost_btn.setFont(font1)

        self.lgdLayout.addWidget(self.addhost_btn, 0, 1, 1, 1)

        self.hosts_lb = QLabel(self.layoutWidget_2)
        self.hosts_lb.setObjectName(u"hosts_lb")
        self.hosts_lb.setFont(font1)
        self.hosts_lb.setAlignment(Qt.AlignCenter)

        self.lgdLayout.addWidget(self.hosts_lb, 0, 0, 1, 1)

        self.host_listw = QListWidget(self.layoutWidget_2)
        self.host_listw.setObjectName(u"host_listw")
        self.host_listw.setMinimumSize(QSize(0, 0))
        self.host_listw.setMaximumSize(QSize(16777215, 16777215))

        self.lgdLayout.addWidget(self.host_listw, 1, 0, 1, 2)


        self.conteck_ly.addWidget(self.l_frame)

        self.r_frame = QFrame(self.layoutWidget)
        self.r_frame.setObjectName(u"r_frame")
        sizePolicy1.setHeightForWidth(self.r_frame.sizePolicy().hasHeightForWidth())
        self.r_frame.setSizePolicy(sizePolicy1)
        self.r_frame.setMinimumSize(QSize(0, 0))
        self.r_frame.setLayoutDirection(Qt.LeftToRight)
        self.r_frame.setFrameShape(QFrame.WinPanel)
        self.r_frame.setFrameShadow(QFrame.Raised)
        self.r_frame.setLineWidth(0)
        self.r_frame.setMidLineWidth(0)
        self.layoutWidget_3 = QWidget(self.r_frame)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(13, 11, 681, 581))
        self.verticalLayout = QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ping_radio = QRadioButton(self.layoutWidget_3)
        self.ping_radio.setObjectName(u"ping_radio")
        self.ping_radio.setFont(font1)

        self.horizontalLayout_2.addWidget(self.ping_radio)

        self.stat_radio = QRadioButton(self.layoutWidget_3)
        self.stat_radio.setObjectName(u"stat_radio")
        self.stat_radio.setFont(font1)

        self.horizontalLayout_2.addWidget(self.stat_radio)

        self.exec_btn = QPushButton(self.layoutWidget_3)
        self.exec_btn.setObjectName(u"exec_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.exec_btn.sizePolicy().hasHeightForWidth())
        self.exec_btn.setSizePolicy(sizePolicy2)
        self.exec_btn.setFont(font1)
        self.exec_btn.setAutoDefault(False)
        self.exec_btn.setFlat(False)

        self.horizontalLayout_2.addWidget(self.exec_btn)

        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.dispaly_te = QTextEdit(self.layoutWidget_3)
        self.dispaly_te.setObjectName(u"dispaly_te")
        self.dispaly_te.setLineWidth(0)
        self.dispaly_te.setReadOnly(True)

        self.verticalLayout.addWidget(self.dispaly_te)


        self.conteck_ly.addWidget(self.r_frame)

        self.conteck_ly.setStretch(0, 3)
        self.conteck_ly.setStretch(1, 7)

        self.verticalLayout_2.addLayout(self.conteck_ly)

        self.status_le = QLabel(self.layoutWidget)
        self.status_le.setObjectName(u"status_le")
        self.status_le.setStyleSheet(u"color:blue")

        self.verticalLayout_2.addWidget(self.status_le)

        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 18)

        self.retranslateUi(check_form)

        self.exec_btn.setDefault(False)


        QMetaObject.connectSlotsByName(check_form)
    # setupUi

    def retranslateUi(self, check_form):
        check_form.setWindowTitle(QCoreApplication.translate("check_form", u"Form", None))
        self.label.setText(QCoreApplication.translate("check_form", u"\u8bbe \u5907 \u5de1 \u68c0", None))
        self.addhost_btn.setText(QCoreApplication.translate("check_form", u"\u6dfb\u52a0", None))
        self.hosts_lb.setText(QCoreApplication.translate("check_form", u"\u4e3b\u673a\u5217\u8868", None))
        self.ping_radio.setText(QCoreApplication.translate("check_form", u"ping", None))
        self.stat_radio.setText(QCoreApplication.translate("check_form", u"\u5065\u5eb7\u72b6\u6001\u68c0\u67e5", None))
        self.exec_btn.setText(QCoreApplication.translate("check_form", u"\u6267\u884c", None))
        self.status_le.setText(QCoreApplication.translate("check_form", u"\u5c31\u7eea", None))
    # retranslateUi

