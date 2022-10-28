# 导入包
from pyecharts.charts import Bar
from pyecharts import options as opts   # 导入配置选择包
from pyecharts.render import make_snapshot  # 导入截图包
from snapshot_selenium import snapshot      # selenium图片渲染包

bar = Bar()
# x轴数据
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
# Y轴数据
bar.add_yaxis("商家A", [5, 20, 36, 10, 75,50])
bar.set_global_opts(title_opts=opts.TitleOpts(title='主标题',subtitle='子标题'))

# 将图生成HTML文件，默认保存在当前运行目录下，默认文件名为render.html
# bar.render('D:\\test_pic\\2.html')
make_snapshot(snapshot,bar.render('D:\\test_pic\\3.html'),'D:\\test_pic\\bar.png',browser="Edge")

# make_snapshot使用格式
# make_snapshot(
#     html_path: str,   # 生成的html图片路径
#     file_type: str,   # 生成的图片文件位置
#     pixel_ratio: int = 2,
#     delay: int = 2,       # selenium sleep时间
#     browser="Chrome",     # 浏览器驱动，默认为Chrome，其它浏览器驱动需要自行在包文件中配置添加
#     driver: Any = None,
# )