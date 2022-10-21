import requests
import re

m3u8_url = 'https://v5.cdtlas.com/20220623/9YhUyY1M/hls/index.m3u8'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

response = requests.get(m3u8_url,headers=headers)
# print('请求的URL',response.request.url)
print(response.text)
# 解析返回的html文件
url = re.compile('https.*ts')
ts_url = url.findall(response.text)

for i in ts_url:
    ts_data = requests.get(i,headers=headers)
    with open('D:\\vido\\{}'.format(i.split('/')[-1]),'wb') as f:
        f.write(ts_data.content)
        print('视频下载完成')

response.close()        # 获取完数据后关闭请求