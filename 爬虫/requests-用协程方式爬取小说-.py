import requests
import re
from lxml import etree
import asyncio
import aiohttp
import aiofiles     # 导入协程文件模块


url = 'https://www.777zw.net/book/ac/fee61de03f/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            # 'Accept-Encoding':"gzip, deflate, br"
           }
"""
思路：
    1、从小说主目录中提取章节的地址信息，并进行拼接成标准地址
    2、利用协程发送每章节页面信息请求
    3、保存每章节内容信息
"""

# 获取章节目录信息
def get_menu():
    response = requests.get(url,headers=headers)
    # print('请求的URL',response.request.url)

    # 解析返回的html文件
    web = etree.HTML(response.text.encode('iso-8859-1').decode('utf-8'))
    # print(web)
    item_list = web.xpath('/html/body/div[3]/div[2]/div/div/ul/li')
    new_url_list = []   # 章节链接地址
    for i in item_list:
        name = i.xpath('./a/text()')  # 章节名称
        href = i.xpath('./a/@href')  # 章节链接地址
        # print(href)
        new_url_list.append(url + '/' + href[0])

    return new_url_list

# 用协程方式写入数据
async def save_file(item_url,session):
    async with session.get(item_url, headers=headers) as item:
        await asyncio.sleep(2)
        item_data = etree.HTML(await item.text())  # .encode('iso-8859-1').decode('utf-8')
        # 获取内容位置
        content_list = item_data.xpath('//*[@id="container"]/div/div/div[2]')
        for x in content_list:
            title = x.xpath('./h1/text()')[0]
            # print(title)
            data = x.xpath('./div[2]/p/text()')  # 每一章内容
            # print('章节信息：',''.join(data))    # 将列表拼接成字符串
            # 保存每一章小说内容
            async with aiofiles.open('d:\\txt\\{}'.format(title),'w+') as f:
                await f.write(''.join(data))
                print('{}保存成功！'.format(title))

# 获取每章节的连接及章节名
async def get_xiaoshou():
    menu_list = get_menu()      # 获取章节信息
    # print('章节总数：',len(menu_list))
    # 获取个章节的内容信息
    tasks = []
    for item_url in menu_list:
        async with aiohttp.ClientSession() as session:
            # 创建协程任务获取小说内容
            t = asyncio.create_task(save_file(item_url,session))
            tasks.append(t)
            await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(get_xiaoshou())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_xiaoshou())
