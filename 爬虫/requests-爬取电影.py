import requests
import re

m3u8_url = 'https://v5.cdtlas.com/20220623/9YhUyY1M/hls/index.m3u8'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

response = requests.get(m3u8_url,headers=headers)
# print('请求的URL',response.request.url)
print(response.text)
# 解析返回的html文件
url = re.compile('^https.*ts$')
print(url.search(response.text))

# for i in response.text:
    # title = i.xpath('./div/div[3]/a/text()')
    # price = i.xpath('./div/div[3]/div/span/text()')[0][1:]
    # service_comment = i.xpath('./div/div[3]/div[3]/div/span/text()')
    # print(i)

# with open('D:\\123.mp4','wb') as f:
#     f.write(video_data.content)
#     print('视频下载完成')

response.close()        # 获取完数据后关闭请求