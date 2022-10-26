import requests
from lxml import etree
import time
import csv
import asyncio
import aiohttp
import aiofiles  # 导入协程文件模块


"""
思路：
    1、从小说主目录中提取章节的地址信息，并进行拼接成标准地址
    2、利用协程发送每章节页面信息请求
    3、保存每章节内容信息
"""


# url = 'https://shop.damanjinfu.com/'
url = 'https://shop.damanjinfu.com/mall-portal/product/search?entranceCode=0001&productCategoryId=&brandId=&keyword=&sort=0&pageNum={}&pageSize=20&_t=1666665234695'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            # 'Accept-Encoding':"gzip, deflate, br"
            'channel': '0001',
            'Connection': 'keep-alive',
            'Cookie': 'Hm_lvt_c61dad168cf8a66a8e1e76fcc4e61ffa=1666574776,1666578538,1666589235,1666663742; Hm_lpvt_c61dad168cf8a66a8e1e76fcc4e61ffa=1666663742',
            'Referer': 'https://shop.damanjinfu.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin'
           }

# 获取每页商品数据
async def get_web_data(page,session):
    data = []       # 商品信息
    async with session.get(url.format(page+1), headers=headers) as response:
        # print(response.url)
        # print('网页返回状态：',response.status)
        await asyncio.sleep(2)
        web_json = await response.json()
        # print(web_json['data']['list'])
        for i in web_json['data']['list']:
            # print(i)
            name = i['name']    # 商品名称
            goods_id = i['id']  # 商品ID
            areas = i['productCategoryName']    # 产地
            stock = i['defaultSkuStock']['realStock']   # 库存
            price = i['defaultSkuStock']['price']   # 售价
            costPrice = i['defaultSkuStock']['costPrice']  # 成本价
            specs = i['defaultSkuStock']['spData'][0]['value'] # 产品规格
            page_data = (name,goods_id,areas,stock,price,costPrice,specs)
            data.append(page_data)
        # print(data)
    save_to_csv(data,page)

        # 保存到CSv文件中
def save_to_csv(d,page_num):
    # print(d)
    with open('d:\\csv\\goods.csv', 'a+', newline='',encoding='utf-8') as f:
        # csv.writer(f).writerow(('商品名称','商品ID','产地','库存','售价','成本价','产品规格'))
        csv.writer(f).writerows(d)
        print('----->>>第 {} 页数据，保存成功！'.format(page_num))


# 创建并执行协程任务
async def muti_run():
    tasks = []
    # 循环获取每页数据
    async with aiohttp.ClientSession() as session:
        for _ in range(500):
            t = asyncio.create_task(get_web_data(_, session))
            tasks.append(t)
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(muti_run())
    loop = asyncio.get_event_loop()
    loop.run_until_complete(muti_run())