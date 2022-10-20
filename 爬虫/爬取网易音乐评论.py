import re
import requests
from lxml import etree

"""
爬取百度小说，雪中悍刀行
思路：
1、从目录页中获取章节信息
2、获取章节内容
3、下载数据
"""

# 小说地址
url = 'https://boxnovel.baidu.com/boxnovel/wiseapi/chapterList?bookid=4295084047&pageNum=1&order=asc&site='

# headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    'Referer': 'https://www.pearvideo.com/video_1706850'}
response = requests.get(url, headers=headers)
html_dict = response.json()
chapter = html_dict['data']['chapter']['chapterInfo']
print(chapter)
for i in chapter:
    book_id =i['book_id']
    chapter_id=i['chapter_id']
    title=i['chapter_title']
    price=i['price']
    info = (book_id,chapter_id,title,price)
    print(info)

response.close()  # 获取完数据后关闭请求
