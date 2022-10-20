import asyncio

# 协和使用模板

async def download(url):
    print('准备开始下载')
    await asyncio.sleep(3)      # 网络请求，requests.get()  需要消耗很长时间
    print('下载完成')

async def main():
    urls = ['http://www.baidu.com','http://www.bilibilicom','http://www.163.com']

    tasks = []
    for url in urls:
        # 创建协和对象
        d = asyncio.create_task(download(url))       # download(url)  DeprecationWarning: The explicit passing of coroutine objects to asyncio.wait() is deprecated since Python 3.8, and scheduled for removal in Python 3.11.
        tasks.append(d)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())