import requests
import time
import csv
import asyncio
import aiohttp
import aiofiles  # 导入协程文件模块

"""
思路：
    1、从主页（https://shop.damanjinfu.com）中获取源页面信息内容转换成JSON
    2、从主页面信息中拼接每一页的地址，并获取每页商品的索引地址，及商品详细信息地址
    3、访问商品详细信息页面，从中获取所需要的信息
    4、保存信息成CSV格式
"""

# url = 'https://shop.damanjinfu.com/'
# 商品的每页地址
url = 'https://shop.damanjinfu.com/mall-portal/product/search?entranceCode=0001&productCategoryId=&brandId=&keyword=&sort=0&pageNum={}&pageSize=20&_t=1666665234695'
# 商品详细信息索引页面地址
detail_referrer_url = 'https://shop.damanjinfu.com/pages/goods/detail?id={}&channel={:0>4}'
# 商品详细信息展示地址
detail_url = 'https://shop.damanjinfu.com/mall-portal/product/detail/{}?_t=1666677503144'

# 商品主页面头部信息
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
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
async def get_web_data(page, session):
    data = []  # 商品信息
    async with session.get(url.format(page + 1), headers=headers) as response:
        # print(response.url)
        # print('网页返回状态：',response.status)
        await asyncio.sleep(2)
        web_json = await response.json()
        # print(web_json['data']['list'])
        for i in web_json['data']['list']:
            # print(i)
            goods_id = i['id']  # 商品ID
            channelid = i['channelId']  # 通道id
            goods_info = (detail_referrer_url.format(goods_id, channelid))
            data.append([goods_info,detail_url.format(goods_id)])
        # print(data)

        # 遍历商品页面列表，从页获取每个子页商品的全部详细页面，并保存至csv文件中
        for _ in data:
            # print('子页面索引地址，及页面地址',_)
            save_to_csv(await get_detail_info(_[1], _[0], session))


# 获取商品子页面的详细信息
async def get_detail_info(child_url,referer,session):
    # 子页面头部信息
    detail_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.52',
        'channel': '0001',
        'Connection': 'keep-alive',
        'Cookie': 'Hm_lvt_c61dad168cf8a66a8e1e76fcc4e61ffa=1666574776,1666578538,1666589235,1666663742; Hm_lpvt_c61dad168cf8a66a8e1e76fcc4e61ffa=1666674424',
        'Referer': referer
    }
    async with session.get(child_url, headers=detail_headers) as res:
        # print('子页面返回状态：', res.json())
        deatail_data = []
        # await asyncio.sleep(2)
        web_json = await res.json()
        web_data = web_json['data']

        product_id = web_data['product']['id']  # 商品ID
        name = web_data['product']['name']  # 商品名称
        areas = web_data['product']['productCategoryName']  # 产地
        stock = web_data['skuStockList'][0]['realStock']  # 库存
        price = web_data['skuStockList'][0]['price']  # 售价
        sale = web_data['product']['sale']  # 已售
        basedSales = web_data['product']['basedSales']  # 预销售
        costPrice = web_data['skuStockList'][0]['costPrice']  # 成本价
        specs = web_data['skuStockList'][0]['spData'][0]['value']  # 产品规格
        company = web_data['supplier']['account']       # 公司名
        contacts = web_data['supplier']['contacts']     # 联系人
        phone = web_data['supplier']['phone']     # 联系人电话
        backupContacts= web_data['supplier']['backupContacts']     # 联系人
        ratepayDiscernMark= web_data['supplier']['ratepayDiscernMark']   # 税务证号
        accountNumber= web_data['supplier']['accountNumber']     # 银行卡号
        bankDeposit=web_data['supplier']['bankDeposit']     # 银行卡开户地址

        page_data = (product_id,name, areas, stock, price,sale,basedSales, costPrice, specs, company,contacts,phone,backupContacts,ratepayDiscernMark,accountNumber,bankDeposit)
        deatail_data.append(page_data)
        # print(deatail_data)
        return deatail_data     # 返回每页商品的信息


# 保存到CSv文件中
def save_to_csv(d):
    # print(d)
    with open('d:\\csv\\goods.csv', 'a+', newline='', encoding='utf-8') as f:
        # csv.writer(f).writerow(('商品名称','商品ID','产地','库存','售价','成本价','产品规格'))
        csv.writer(f).writerows(d)
        # print('----->>>第 {} 页数据，保存成功！'.format(page_num))


# 创建并执行协程任务
async def muti_run():
    tasks = []
    # 循环获取每页数据
    async with aiohttp.ClientSession() as session:
        # 500页，执行500次
        for _ in range(500):
            t = asyncio.create_task(get_web_data(_, session))
            tasks.append(t)
        await asyncio.wait(tasks)


if __name__ == '__main__':
    start = time.time()
    # asyncio.run(muti_run())       # 该方式运行结束后会报 RuntimeError: Event loop is closed
    loop = asyncio.get_event_loop()
    loop.run_until_complete(muti_run())
    end = time.time()
    print('消耗时间：',end-start)
