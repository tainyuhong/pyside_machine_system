# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'machine_import.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_import_machine(object):
    def setupUi(self, import_machine):
        if not import_machine.objectName():
            import_machine.setObjectName(u"import_machine")
        import_machine.resize(781, 478)
        self.horizontalLayout_2 = QHBoxLayout(import_machine)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 0, 10, -1)
        self.label = QLabel(import_machine)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 1, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.label_3 = QLabel(import_machine)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)

        self.horizontalLayout.addWidget(self.label_3)

        self.path_le = QLineEdit(import_machine)
        self.path_le.setObjectName(u"path_le")
        self.path_le.setFont(font1)
        self.path_le.setReadOnly(False)

        self.horizontalLayout.addWidget(self.path_le)

        self.select_btn = QPushButton(import_machine)
        self.select_btn.setObjectName(u"select_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_btn.sizePolicy().hasHeightForWidth())
        self.select_btn.setSizePolicy(sizePolicy)
        self.select_btn.setFont(font1)

        self.horizontalLayout.addWidget(self.select_btn)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 8)
        self.horizontalLayout.setStretch(2, 2)

        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 4)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 4, 0, 1, 1)

        self.import_btn = QPushButton(import_machine)
        self.import_btn.setObjectName(u"import_btn")
        self.import_btn.setFont(font1)

        self.gridLayout.addWidget(self.import_btn, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(338, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 5, 0, 1, 3)

        self.lb_stat = QLabel(import_machine)
        self.lb_stat.setObjectName(u"lb_stat")
        self.lb_stat.setStyleSheet(u"color:red")

        self.gridLayout.addWidget(self.lb_stat, 6, 0, 1, 4)

        self.bt_download = QPushButton(import_machine)
        self.bt_download.setObjectName(u"bt_download")
        self.bt_download.setStyleSheet(u"color:blue")

        self.gridLayout.addWidget(self.bt_download, 5, 3, 1, 1)

        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setRowStretch(2, 2)
        self.gridLayout.setRowStretch(3, 1)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setRowStretch(5, 1)
        self.gridLayout.setRowStretch(6, 1)
        self.gridLayout.setColumnStretch(0, 2)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)
        self.gridLayout.setColumnStretch(3, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout)


        self.retranslateUi(import_machine)

        QMetaObject.connectSlotsByName(import_machine)
    # setupUi

    def retranslateUi(self, import_machine):
        import_machine.setWindowTitle(QCoreApplication.translate("import_machine", u"Form", None))
        self.label.setText(QCoreApplication.translate("import_machine", u"\u6279\u91cf\u5bfc\u5165\u8bbe\u5907\u4fe1\u606f", None))
        self.label_3.setText(QCoreApplication.translate("import_machine", u"\u8def\u5f84\uff1a", None))
#if QT_CONFIG(tooltip)
        self.path_le.setToolTip(QCoreApplication.translate("import_machine", u"\u8bf7\u9009\u62e9\u9700\u8981\u5bfc\u5165\u7684\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.path_le.setText("")
        self.path_le.setPlaceholderText(QCoreApplication.translate("import_machine", u"\u8bf7\u9009\u62e9\u9700\u8981\u5bfc\u5165\u7684\u6587\u4ef6", None))
        self.select_btn.setText(QCoreApplication.translate("import_machine", u"\u9009\u62e9", None))
        self.import_btn.setText(QCoreApplication.translate("import_machine", u"\u5bfc\u5165", None))
        self.lb_stat.setText(QCoreApplication.translate("import_machine", u"\u6ce8\uff1a\u7528\u4e8e\u5927\u91cf\u6570\u636e\u5bfc\u5165\uff0c\u4e14\u6570\u636e\u4ece\u7b2c\u4e09\u884c\u7b2c\u4e00\u5217\u5185\u5bb9\u5f00\u59cb\u8bfb\u53d6", None))
        self.bt_download.setText(QCoreApplication.translate("import_machine", u"\u6a21\u677f\u4e0b\u8f7d", None))
    # retranslateUi

