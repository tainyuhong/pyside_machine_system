# 导入包
from pyecharts.charts import Bar
from pyecharts import options as opts   # 导入配置选择包

bar = Bar()
# x轴数据
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# Y轴数据
bar.add_yaxis("商家A", [5, 20, 36, 10, 75,50])
bar.set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='子标题'))

# 将图生成HTML文件，默认保存在当前运行目录下，默认文件名为render.html
bar.render('D:\\test_pic\\2.html')