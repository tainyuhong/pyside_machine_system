import sys
import PySide6.QtWidgets as QtWidgets

def Change():
    textBrow.setMarkdown(textEdit.toPlainText())

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
hbox = QtWidgets.QHBoxLayout()
textEdit = QtWidgets.QTextEdit()
textBrow = QtWidgets.QTextBrowser()
textEdit.textChanged.connect(Change)
hbox.addWidget(textEdit)
hbox.addWidget(textBrow)
widget.setLayout(hbox)
widget.show()
sys.exit(app.exec())
