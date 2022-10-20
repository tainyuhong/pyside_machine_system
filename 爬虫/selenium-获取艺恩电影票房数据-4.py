import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

"""
思路：
    1、打开年度排行榜页面
    2、获取下拉菜单，并封装成selenium下拉菜单对象
    3、获取每页表格数据
"""


# 创建一个浏览器实例
web = Edge()
# 打开票房排行旁网页
web.get('https://www.endata.com.cn/Boxoffice/bo/year/index.html')
# print(web.title)
# 在浏览器获取年度下拉菜单元素  '//*[@id="OptionDate"]'
select_data = web.find_element(By.XPATH,'//*[@id="OptionDate"]')
# print(select_data.text)

# 对获取的下拉菜单元素进行封装，封装成下拉菜单
sel = Select(select_data)

# 对每个下拉菜单中内容进行提取
pick_data = []
for i in range(len(sel.options)):    # sel.options 下拉菜单选项内容
    sel.select_by_index(i)  # 下拉菜单按索引进行切换
    time.sleep(1)

    #按表中每一行数据的爬取
    table = web.find_elements(By.XPATH,'//*[@id="TableList"]/table/tbody/tr/td')
    # print(table.text)
    page_data = []
    for i in table:
        row_data = i.find_element(By.XPATH,'.')
        page_data.append(row_data.text)
    print('页数据：', page_data)
    pick_data.append(page_data)
    time.sleep(1)

print('所有页数据：',pick_data)
web.close()     # 关闭窗口
