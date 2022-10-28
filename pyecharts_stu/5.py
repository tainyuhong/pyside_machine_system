import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from pyecharts import options as opts
from pyecharts.charts import Tree



# 生产图片网页
def creat_html():
    data = [
        {
            "name": "python变量",
            "children": [
                {"name": "字符串",
                "children": [{"name": "实例1：'abc'"}, {"name": "实例2：'123abc'"}]},
                {"name": "列表",
                "children": [{"name": "实例1：[a,b,c]"}, {"name": "实例2：'[1,2,3]"}]},
                {"name": "字典",
                "children": [{"name": "实例1：{1:'a','2':'b'}}"}, {"name": "实例2：'{a:[1,2,3],'2':(1,2))}"}]},
                {"name": "元组",
                 "children": [{"name": "实例1：(1,2,3)}"}, {"name": "实例2：(a,b,c)"}]}
    ]}
    ]
    c = (Tree().add("思维导图", data))
    # c.render_notebook()
    c.render('D:\\test_pic\\5.html')


# 创建一个Icon类，继承QWidget类
class Icon(QWidget):
    def __init__(self):
        super(Icon, self).__init__()
        self.initUI()

    # 初始化窗口
    def initUI(self):
        self.resize(900,1000)
        self.setWindowTitle('程序图标')
        t = Qw
        with open('D:\\test_pic\\5.html') as f:
            t.insertHtml(f.read())
            # print(f.read())
            # t.setHtml(f.read())
        t.toHtml()
        layout = QHBoxLayout()
        layout.addWidget(t)
        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = Icon()
    icon.show()
    sys.exit(app.exec())