import sys
import os
from test_Demo.doc_viewer import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from markdown2 import Markdown


class MainUi(Ui_MainWindow,QMainWindow):

    def __init__(self,parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.display_text.setHidden(True)
        self.add_tool()     # 添加按钮工具至工具栏中
        self.font_size=''

        self.tree_file.setContextMenuPolicy(Qt.CustomContextMenu)   # 文件列表右键菜单
        self.tree_file.customContextMenuRequested.connect(self.tree_file_menu)

        self.input_text.textChanged.connect(self.to_markdown)
        self.action_displaylist.changed.connect(self.hide_tabview)       # 显示与隐藏tabwidget预览窗口
        # self.action_to_md.changed.connect(self.hide_textbrowser)    # 显示与隐藏markdown预览窗口
        self.action_save.triggered.connect(self.save)               # 保存数据
        self.action_clip.triggered.connect(self.display_clip)      # 显示粘贴板信息
        self.color.clicked.connect(self.chioce_color)

    # 隐藏显示文件大纲tab窗口
    def hide_tabview(self):
        if self.action_displaylist.isChecked():
            self.tabWidget.setHidden(False)
        else:
            self.tabWidget.setHidden(True)

    def to_markdown(self):
        str = self.input_text.toPlainText()
        self.display_text.setHidden(False)
        # self.display_text.setMarkdown(str)
        self.display_text.setHtml(str)

    # 隐藏文本预览窗口
    def hide_textbrowser(self):
        if self.action_to_md.isChecked():
            self.display_text.setHidden(False)
        else:
            self.display_text.setHidden(True)

    # 保存文档
    def save(self):
        str = self.input_text.document().toHtml()
        # print(type(str))
        # print(str)
        os.chdir('d:\\')
        with open('test.html','wb+') as f:
            f.write(bytes(str,encoding='utf8'))

    def display_clip(self):
        clip = QApplication.clipboard()
        print('剪贴板内容：',clip)        # 显示剪贴板对象地址
        print(clip.mimeData().formats())    # 显示包含mime内容格式
        print(clip.mimeData().text())       # 显示mime文本
        print('是否有HTML',clip.mimeData().hasHtml(),clip.mimeData().html())   # 判断是否包含html，并打印
        print('是否有hasUrls',clip.mimeData().hasUrls(),clip.mimeData().urls())    # 判断是否包含url，并打印
        print('是否有hasImage', clip.mimeData().hasImage(), 'data', clip.mimeData().imageData())   # 判断是否包含图片，并打印
        cur = self.display_text.textCursor()    # 设定文本游标
        cur.insertImage(clip.mimeData().text())  # 根据图片地址插入图片

    def add_tool(self):
        self.font_size = QComboBox()
        for _ in range(9,50):
            self.font_size.addItem(str(_))
        self.font_size.setCurrentText('12')  # 设置默认字号
        self.toolBar_quick.addWidget(self.font_size)
        self.font = QFontComboBox()
        self.font.setMaximumWidth(100)      # 设置字体选择下拉框的最大宽度
        self.toolBar_quick.addWidget(self.font)
        self.color = QPushButton('颜色')        # 颜色
        self.color.setMaximumSize(40,40)
        self.toolBar_quick.addWidget(self.color)


    # 颜色选择
    def chioce_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.color.setStyleSheet("background-color:{}".format(color.name()))

    # 文件列表框右键菜单
    def tree_file_menu(self,pos):
        self.tree_file_menu = QMenu()
        self.tree_file_menu.addAction('新建文件夹')
        self.tree_file_menu.addAction('新建文件')
        self.tree_file_menu.addAction('修改文件名')
        self.tree_file_menu.move(QCursor.pos())
        self.tree_file_menu.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()
    sys.exit(app.exec())
