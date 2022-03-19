import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


# from PySide6.QtGui import QPixmap, QPainter, QPoint, QPaintEvent, QMouseEvent, QPen,QColor, QSize


class ColorCombox(QWidget):
    # 发送颜色更改信号，类型为Qcolor的object类型
    signal = Signal(object)
    thick_signal = Signal(object)
    style_signal = Signal(object)

    def __init__(self):
        super().__init__()
        # 设置场景颜色，大小是6*10二维列表
        theme_colors = [
            [QColor(255, 255, 255, 255), QColor(0, 0, 0, 255), QColor(231, 230, 230, 255), QColor(64, 84, 106, 255),
             QColor(91, 155, 213, 255), QColor(237, 124, 48, 255), QColor(165, 165, 165, 255), QColor(255, 192, 0, 255),
             QColor(68, 114, 196, 255), QColor(112, 173, 71, 255)],

            [QColor(242, 242, 242, 255), QColor(127, 127, 127, 255), QColor(208, 206, 206, 255),
             QColor(214, 220, 228, 255),
             QColor(222, 235, 246, 255), QColor(251, 229, 213, 255), QColor(237, 237, 237, 237),
             QColor(255, 242, 204, 255), QColor(217, 226, 243, 255), QColor(226, 239, 217, 255)],

            [QColor(216, 216, 216, 255), QColor(89, 89, 89, 255), QColor(174, 171, 171, 255),
             QColor(173, 185, 202, 255),
             QColor(189, 215, 238, 255), QColor(247, 203, 172, 255), QColor(219, 219, 219, 255),
             QColor(254, 229, 153, 255), QColor(180, 198, 231, 255), QColor(197, 224, 179, 255)],

            [QColor(191, 191, 191, 255), QColor(63, 63, 63, 255), QColor(117, 112, 112, 255),
             QColor(132, 150, 176, 255),
             QColor(156, 195, 229, 255), QColor(244, 177, 131, 255), QColor(201, 201, 201, 255),
             QColor(255, 217, 101, 255), QColor(142, 170, 219, 255), QColor(168, 208, 141, 255)],

            [QColor(165, 165, 165, 255), QColor(38, 38, 38, 255), QColor(58, 56, 56, 255), QColor(50, 63, 79, 255),
             QColor(39, 112, 179, 255), QColor(197, 90, 17, 255), QColor(123, 123, 123, 255), QColor(191, 144, 0, 255),
             QColor(47, 84, 150, 255), QColor(83, 129, 53, 255)],

            [QColor(124, 124, 124, 255), QColor(12, 12, 12, 255), QColor(23, 22, 22, 255), QColor(34, 42, 53, 255),
             QColor(34, 81, 123, 255), QColor(124, 48, 2, 255), QColor(82, 82, 82, 255), QColor(127, 96, 0, 255),
             QColor(31, 56, 100, 255), QColor(55, 86, 35, 255)]
        ]

        # 设置基础颜色，大小是1*10一维列表
        basic_colors = [
            QColor(192, 0, 0, 255), QColor(255, 0, 0, 255), QColor(255, 192, 0, 255),
            QColor(255, 255, 0, 255), QColor(146, 208, 80, 255), QColor(0, 176, 80, 255),
            QColor(0, 176, 240, 255), QColor(0, 112, 192, 255), QColor(0, 32, 96, 255),
            QColor(112, 48, 160, 255)
        ]

        # 设置下拉框总按钮
        self.ColorCombox = QToolButton()
        self.ColorCombox.setAutoRaise(True)
        self.ColorCombox.setPopupMode(QToolButton.InstantPopup)  # 设置下拉框按钮按下时弹出菜单窗口
        self.ColorCombox.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.ColorCombox.setArrowType(Qt.NoArrow)
        self.ColorCombox.setText("画笔颜色")
        # self.ColorCombox.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        # self.ColorCombox.setMinimumSize(100, 30)
        self.ColorCombox.setAutoFillBackground(True)
        # 利用setStyleSheet设置QToolButton不显示下箭头
        self.ColorCombox.setStyleSheet("QToolButton::menu-indicator {image: none;} QToolButton{font:bold 9pt '微软雅黑'}")

        # 设置颜色下拉按钮的自定义图标Icon，这里是初始化
        qp = QPixmap(30, 30)  # 设置QPixmap场景大小
        qp.fill(Qt.transparent)
        self.pix = QPixmap()
        self.pix.load("noun_Pen.png")  # 这是画笔Icon，请替换成自己的图片或者利用QPainter画出笔也行
        pixfixed = self.pix.scaled(25, 25, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        target = QRect(0, 0, 20, 20)
        source = QRect(0, 0, 20, 20)
        painter = QPainter(qp)  # 设置QPainter在自己设的QPixmap上画
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(target, pixfixed, source)
        painter.fillRect(QRect(0, 22, 22, 5), Qt.red)
        painter.end()
        self.ColorCombox.setIcon(QIcon(qp))
        self.ColorCombox.setIconSize(QSize(30, 30))

        # 设置主题色标签
        title = QLabel(u"主题颜色")
        title.setStyleSheet("QLabel{background:lightgray;color:black;font:bold 8pt '微软雅黑'}")

        # 设置颜色6*10大小的主题颜色框架，利用QGridLayout布局放置颜色块
        pGridLayout = QGridLayout()
        pGridLayout.setAlignment(Qt.AlignCenter)
        pGridLayout.setContentsMargins(0, 0, 0, 0)
        pGridLayout.setSpacing(2)
        for i in range(6):
            for j in range(10):
                action = QAction()
                action.setData(theme_colors[i][j])
                action.setIcon(self.createColorIcon(theme_colors[i][j]))
                pBtnColor = QToolButton()
                pBtnColor.setFixedSize(QSize(20, 20))
                pBtnColor.setAutoRaise(True)
                pBtnColor.setDefaultAction(action)
                action.triggered.connect(self.OnColorChanged)
                pBtnColor.setToolTip(str(theme_colors[i][j].getRgb()))
                pGridLayout.addWidget(pBtnColor, i, j)

        # 设置标准色标签
        btitle = QLabel(u"标准色")
        btitle.setStyleSheet("QLabel{background:lightgray;color:black;font:bold 8pt '微软雅黑'}")

        # 设置颜色1*10大小的标准色框架，利用QGridLayout布局放置颜色块
        bGridLayout = QGridLayout()
        bGridLayout.setAlignment(Qt.AlignCenter)
        bGridLayout.setContentsMargins(0, 0, 0, 0)
        bGridLayout.setSpacing(2)
        for m in range(10):
            baction = QAction()
            baction.setData(basic_colors[m])
            baction.setIcon(self.createColorIcon(basic_colors[m]))
            bBtnColor = QToolButton()
            bBtnColor.setFixedSize(QSize(20, 20))
            bBtnColor.setAutoRaise(True)
            bBtnColor.setDefaultAction(baction)
            baction.triggered.connect(self.OnColorChanged)
            bBtnColor.setToolTip(str(basic_colors[m].getRgb()))
            bGridLayout.addWidget(bBtnColor, 0, m)

        # 设置分割水平线，利用QFrame
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Plain)

        # 设置“无边框（透明色）”按钮功能
        pBtnTransparent = QToolButton()
        pBtnTransparent.setArrowType(Qt.NoArrow)
        pBtnTransparent.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        pBtnTransparent.setFixedSize(218, 20)
        pBtnTransparent.setAutoRaise(True)
        pBtnTransparent.setStyleSheet("QToolButton{font:bold 8pt '微软雅黑'}")
        pBtnTransparent.setText("无边框颜色")
        pBtnTransparent.setIcon(QIcon("Frame.png"))
        pBtnTransparent.setIconSize(QSize(20, 20))
        pBtnTransparent.clicked.connect(self.set_pen_Transparent)

        # 设置“选择其他颜色”按钮功能
        othercolor_btn = QToolButton()
        othercolor_btn.setArrowType(Qt.NoArrow)
        othercolor_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        othercolor_btn.setFixedSize(218, 20)
        othercolor_btn.setAutoRaise(True)
        othercolor_btn.setIcon(QIcon("color.png"))
        othercolor_btn.setText(u"选择其他颜色")
        othercolor_btn.setIconSize(QSize(15, 15))
        othercolor_btn.setStyleSheet("QToolButton{font:bold 8pt '微软雅黑'}")
        othercolor_btn.clicked.connect(self.on_colorboard_show)

        # 将设置好的颜色框架，用QWidget包装好
        widget = QWidget()
        widget.setLayout(pGridLayout)
        bwidget = QWidget()
        bwidget.setLayout(bGridLayout)

        #  将上述设置的这些所有颜色框架，小组件窗口，用QVBoxLayout包装好
        pVLayout = QVBoxLayout()
        pVLayout.setSpacing(1)
        pVLayout.addWidget(title)
        pVLayout.addWidget(widget)
        pVLayout.addWidget(btitle)
        pVLayout.addWidget(bwidget)
        pVLayout.addWidget(line)
        pVLayout.addWidget(pBtnTransparent)
        pVLayout.addWidget(othercolor_btn)

        # 设置分割水平线，利用QFrame
        line2 = QFrame()
        line2.setFrameShape(QFrame.HLine)
        line2.setFrameShadow(QFrame.Plain)
        pVLayout.addWidget(line2)

        # 画笔粗细按钮
        self.thicknessbtn = QToolButton(self, text="粗细")
        self.thicknessbtn.setFixedSize(218, 20)
        self.thicknessbtn.setAutoRaise(True)
        self.thicknessbtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 自定义画笔粗细的QIcon
        thickIcon = QPixmap(30, 30)
        thickIcon.fill(Qt.white)
        thickpainter = QPainter(thickIcon)
        d = 5
        for k in range(4):
            thickpainter.setPen(QPen(Qt.black, k + 1, Qt.SolidLine))
            thickpainter.drawLine(0, (d + 1) * k + 5, 30, (d + 1) * k + 5)
        thickpainter.end()
        self.thicknessbtn.setIcon(QIcon(thickIcon))

        self.thicknessbtn.setPopupMode(QToolButton.InstantPopup)
        self.thicknessbtn.setArrowType(Qt.NoArrow)
        self.thicknessbtn.setStyleSheet(
            "QToolButton::menu-indicator {image: none;} QToolButton{font:bold 8pt '微软雅黑'}")

        tLayout = QVBoxLayout()
        tLayout.setSpacing(0)
        self.thicknessmenu = QMenu(self)
        for i in range(10):
            action = QAction(parent=self.thicknessmenu)
            action.setData(i)
            action.setIcon(self.set_width_Icon(i + 1))
            action.setText("{}磅".format(i + 1))
            pBtnWidth = QToolButton()
            pBtnWidth.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            pBtnWidth.setIconSize(QSize(100, 10))
            pBtnWidth.setStyleSheet(
                "QToolButton::menu-indicator {image: none;}")
            pBtnWidth.setAutoRaise(True)
            pBtnWidth.setDefaultAction(action)
            action.triggered.connect(self.OnWidthChanged)
            pBtnWidth.setToolTip(str("粗细:{}磅".format(i + 1)))
            tLayout.addWidget(pBtnWidth, i)
        self.twidget = QWidget()
        self.twidget.setLayout(tLayout)
        tVLayout = QVBoxLayout()
        tVLayout.setSpacing(1)
        tVLayout.setContentsMargins(1, 1, 1, 1)
        tVLayout.addWidget(self.twidget)
        self.thicknessmenu.setLayout(tVLayout)
        self.thicknessbtn.setMenu(self.thicknessmenu)
        self.thicknessmenu.showEvent = self.thickness_show
        pVLayout.addWidget(self.thicknessbtn)

        # 画笔虚线设定
        style = [Qt.NoPen, Qt.SolidLine, Qt.DashLine, Qt.DotLine,
                 Qt.DashDotLine, Qt.DashDotDotLine, Qt.CustomDashLine]
        name = ["无", "实线", "虚线", "点线", "点虚线", "点点虚线", "自定义"]

        # 画笔虚线按钮
        self.stylebtn = QToolButton(self, text="虚线")
        self.stylebtn.setFixedSize(218, 20)
        self.stylebtn.setAutoRaise(True)
        self.stylebtn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        # 自定义画笔虚线的QIcon
        styleIcon = QPixmap(30, 30)
        styleIcon.fill(Qt.white)
        stylepainter = QPainter(styleIcon)
        f = 5
        for k in range(4):
            stylepainter.setPen(style[k + 1])
            stylepainter.drawLine(0, (f + 1) * k + 5, 30, (f + 1) * k + 5)
        stylepainter.end()
        self.stylebtn.setIcon(QIcon(styleIcon))
        self.stylebtn.setPopupMode(QToolButton.InstantPopup)
        self.stylebtn.setArrowType(Qt.NoArrow)
        self.stylebtn.setStyleSheet(
            "QToolButton::menu-indicator {image: none;} QToolButton{font:bold 8pt '微软雅黑'}")

        sLayout = QVBoxLayout()
        sLayout.setSpacing(0)
        self.stylemenu = QMenu(self)
        for j in range(7):
            saction = QAction(parent=self.stylemenu)
            saction.setData(style[j])
            saction.setIcon(self.set_style_Icon(style[j]))
            saction.setText(name[j])
            sBtnStyle = QToolButton()
            sBtnStyle.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            sBtnStyle.setIconSize(QSize(100, 10))
            sBtnStyle.setStyleSheet(
                "QToolButton::menu-indicator {image: none;}")
            sBtnStyle.setAutoRaise(True)
            sBtnStyle.setDefaultAction(saction)
            saction.triggered.connect(self.OnStyleChanged)
            sBtnStyle.setToolTip(str(style[j]))
            sLayout.addWidget(sBtnStyle, j)

        self.swidget = QWidget()
        self.swidget.setLayout(sLayout)
        sVLayout = QVBoxLayout()
        sVLayout.setSpacing(1)
        sVLayout.setContentsMargins(1, 1, 1, 1)
        sVLayout.addWidget(self.swidget)
        self.stylemenu.setLayout(sVLayout)
        self.stylebtn.setMenu(self.stylemenu)
        self.stylemenu.showEvent = self.style_show
        pVLayout.addWidget(self.stylebtn)

        # 设置弹出菜单，菜单打上上述打包好所有颜色框架、窗口的pVLayout内容
        self.colorMenu = QMenu(self)
        self.colorMenu.setLayout(pVLayout)

        # 设置下拉框按钮菜单为上述菜单
        self.ColorCombox.setMenu(self.colorMenu)

        ### 将所有上述打包好的内，用本类设置的QWidget打包成窗口控件 ###
        alLayout = QVBoxLayout()
        alLayout.setSpacing(0)
        alLayout.addWidget(self.ColorCombox)
        self.setLayout(alLayout)

    ### ——以下为本类所用到的函数—— ###

    # 重设画笔粗细按钮按下后菜单出现在右侧
    def thickness_show(self, e):
        parent = self.colorMenu.pos()
        pos = self.thicknessbtn.geometry()
        m = self.thicknessmenu.geometry()
        w = pos.width()
        self.thicknessmenu.move(parent.x() + w + 16, m.y() - pos.height())

    # 重设画笔虚线按钮按下后菜单出现在右侧
    def style_show(self, e):
        parent = self.colorMenu.pos()
        pos = self.stylebtn.geometry()
        m = self.stylemenu.geometry()
        w = pos.width()
        self.stylemenu.move(parent.x() + w + 16, m.y() - pos.height())

    # 设置画笔粗细菜单栏中的所有Icon图标
    def set_width_Icon(self, width):
        color = Qt.black
        pix = QPixmap(100, width)
        pix.fill(QColor(color))
        return QIcon(pix)

    # 设置画笔粗细选中时的操作
    def OnWidthChanged(self):
        width = self.sender().data() + 1
        # print(width)
        self.thicknessmenu.close()
        self.colorMenu.close()
        self.thick_signal.emit(width)

    # 设置画笔虚线菜单栏中的所有Icon图标
    def set_style_Icon(self, style):
        # print(style)
        color = Qt.black
        pix = QPixmap(100, 6)
        pix.fill(Qt.white)
        painter = QPainter(pix)
        pp = QPen()
        pp.setStyle(style)
        pp.setColor(color)
        pp.setWidth(3)
        painter.setPen(pp)
        painter.drawLine(0, 3, 100, 3)
        painter.end()
        return QIcon(pix)

    # 设置画笔虚线形状选中时的操作
    def OnStyleChanged(self):
        style = self.sender().data()
        # print(Qt.PenStyle(style))
        self.stylemenu.close()
        self.colorMenu.close()
        self.style_signal.emit(style)

    # 用于设置QAction颜色块的槽函数
    def createColorIcon(self, color):
        pixmap = QPixmap(18, 18)
        pixmap.fill(QColor(color))
        return QIcon(pixmap)

    # 当透明色设置按钮按下后的槽函数
    def set_pen_Transparent(self):
        color = Qt.transparent
        self.colorMenu.close()
        self.signal.emit(color)

    # 设置颜色下拉按钮的自定义图标Icon，这里是颜色变化时改变图标下层矩形填充颜色
    def createColorToolButtonIcon(self, color):
        # print(color)
        qp = QPixmap(30, 30)
        qp.fill(Qt.transparent)
        self.pix = QPixmap()
        self.pix.load("noun_Pen.png")
        pixfix = self.pix.scaled(25, 25, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        target = QRect(0, 0, 20, 20)
        source = QRect(0, 0, 20, 20)
        painter = QPainter(qp)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setRenderHint(QPainter.SmoothPixmapTransform)
        painter.drawPixmap(target, pixfix, source)
        painter.fillRect(QRect(0, 22, 22, 5), color)
        painter.end()
        self.ColorCombox.setIcon(QIcon(qp))
        self.ColorCombox.setIconSize(QSize(30, 30))

    # 当颜色色块QAction按下后的槽函数
    def OnColorChanged(self):
        color = self.sender().data()
        self.colorMenu.close()
        self.signal.emit(color)

    # 当其他颜色按钮按下时弹出Qt自带的颜色选择器
    def on_colorboard_show(self):
        color = QColorDialog.getColor(Qt.black, self)
        if color.isValid():
            self.signal.emit(color)
            return color


def main():
    app = QApplication([])
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    window = ColorCombox()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
