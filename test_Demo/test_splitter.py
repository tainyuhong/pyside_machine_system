import sys
from test_Demo.doc_viewer import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from markdown2 import Markdown


class MainUi(Ui_MainWindow,QMainWindow):

    def __init__(self,parent=None):
        super(MainUi, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.to_markdown)
        self.html_btn.clicked.connect(self.tohtml)

    def to_markdown(self):
        str = self.textEdit.toPlainText()
        self.textEdit.setMarkdown(str)

    def tohtml(self):
        str = self.textEdit.toPlainText()
        self.textEdit.toHtml(str)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainUi()
    win.show()
    sys.exit(app.exec())