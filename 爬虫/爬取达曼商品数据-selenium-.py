import requests
from lxml import etree
import time
import csv
import asyncio
import aiohttp
import aiofiles  # 导入协程文件模块
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options




"""
思路：
    1、从小说主目录中提取章节的地址信息，并进行拼接成标准地址
    2、利用协程发送每章节页面信息请求
    3、保存每章节内容信息
"""


opt = Options()
opt.add_argument('--headless')      # 无头浏览器方式访问
# opt.add_argument('--disable-gpu')     # 禁用GPU
opt.add_argument('--disable-blink-features=AutomationControlled')   # 去掉浏览器自动化提示“正受到自动测试软件的控制”
opt.add_experimental_option('excludeSwitches',['enable-automation'])   # 去掉浏览器自动化提示“正受到自动测试软件的控制”

# 创建一个浏览器实例
web = Edge(options=opt)
# 打开百度网页
web.get('https://shop.damanjinfu.com/')
# print(web.title)
time.sleep(1)

# 获取页面数据
def get_web_data(num):
    # print('num:',num,num*10,10*(num+1))
    page_data = []
    # 在浏览器实例中查找全国的元素                '//*[@id="u-left-column"]'
    all_procuct = web.find_elements(By.XPATH,'//*[@class="u-column"]')
    for a in all_procuct:
        product = a.find_elements(By.XPATH, './uni-view')
        # print(len(product))
        for i in product[num*10:(num+1)*10]:
            name = i.find_element(By.XPATH,'./uni-view[2]/uni-view[1]').text
            price = i.find_element(By.XPATH,'./uni-view[2]/uni-view[2]/uni-view[1]/uni-text/span').text
            sold = i.find_element(By.XPATH,'./uni-view[2]/uni-view[3]').text
            print('商品名称：{}  ,价格：{},  已售：{}'.format(name,price,sold))
            page_data.append((name,price,sold))
    return page_data

#

# time.sleep(2)
# # 第11个商品
# print('11个商品')
# product1 = web.find_elements(By.XPATH, '//*[@id="u-left-column"]/uni-view')
# for i in product1[10:]:
#     name = i.find_element(By.XPATH,'./uni-view[2]/uni-view[1]').text
#     price = i.find_element(By.XPATH,'./uni-view[2]/uni-view[2]/uni-view[1]/uni-text/span').text
# # '//*[@id="u-left-column"]/uni-view[1]/uni-view[2]/uni-view[1]/text()'
# # '//*[@id="u-left-column"]/uni-view[2]/uni-view[2]/uni-view[1]/text()'
#  #   '//*[@id="u-right-column"]/uni-view[1]/uni-view[2]/uni-view[1]/uni-view[2]'
#     print('商品名称：',name,'价格：',price)

if __name__ == '__main__':
    # 取10页数据
    for i in range(100):
        with open('d:\\csv\\1.csv', 'a+', newline='') as f:
            data = get_web_data(i)
            csv.writer(f).writerows(data)
            print('保存完成')
            # 滚动web页面JS命令
            s = web.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
            print('------> 第{}页商品'.format(i+1))