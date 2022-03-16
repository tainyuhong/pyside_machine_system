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
        self.input_text.textChanged.connect(self.to_markdown)
        self.action_displaylist.changed.connect(self.hide_tabview)       # 显示与隐藏tabwidget预览窗口
        self.action_to_md.changed.connect(self.hide_textbrowser)    # 显示与隐藏markdown预览窗口
        self.action_save.triggered.connect(self.save)

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
        print(str)
        os.chdir('d:\\')
        with open('test.html','wb') as f :
            f.write(bytes(str),encoding='utf8')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()
    sys.exit(app.exec())