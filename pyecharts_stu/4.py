from pyecharts import options as opts
from pyecharts.charts import Tree
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
c.render('D:\\test_pic\\4.html')