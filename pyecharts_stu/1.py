# 导入包
from pyecharts.charts import Bar

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])     # x轴数据
bar.add_yaxis("商家A", [5, 20, 36, 10, 75,50])   # Y轴数据

# 将图生成HTML文件，默认保存在当前运行目录下，默认文件名为render.html
bar.render('D:\\test_pic\\1.html')