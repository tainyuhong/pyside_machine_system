import requests
import re
import asyncio
import aiohttp
import aiofiles     # 导入协程文件模块

m3u8_url = 'https://v5.cdtlas.com/20220623/9YhUyY1M/hls/index.m3u8'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

response = requests.get(m3u8_url,headers=headers)
# print('请求的URL',response.request.url)
# print(response.text)
# 解析返回的html文件
url = re.compile('https.*ts')
ts_urls = url.findall(response.text)

timeout = aiohttp.ClientTimeout(total=60*60)

async def download(url,session):
    # print('准备开始下载')
    # print(url)

    async with session.get(url) as ts_data:
        await asyncio.sleep(5)  # 网络请求，requests.get()  需要消耗很长时间
        async with aiofiles.open('D:\\vido\\{}'.format(url.split('/')[-1]), 'wb') as f:
            await f.write(await ts_data.content.read())
            await asyncio.sleep(1)  #
            print('视频读取完成')
        await asyncio.sleep(1)  #
        print('下载完成')

async def main():
    tasks = []
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for u in ts_urls:
            # 创建协和对象
            d = asyncio.create_task(download(u,session))
            tasks.append(d)
        await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
