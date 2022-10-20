from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 创建一个浏览器实例
web = Edge()
# 打开百度网页
web.get('https://www.lagou.com')
print(web.title)
# 在浏览器实例中查找全国的元素
pos = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
# 点击这个元素
pos.click()

input_cont = web.find_element(By.XPATH,'//*[@id="search_input"]')
# 向搜索框中输入查找内容，并回车
input_cont.send_keys('python',Keys.ENTER)
