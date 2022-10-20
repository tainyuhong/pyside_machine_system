from selenium.webdriver import Edge

# 创建一个浏览器实例
web = Edge()
# 打开百度网页
web.get('https://www.baidu.com')
print(web.title)

