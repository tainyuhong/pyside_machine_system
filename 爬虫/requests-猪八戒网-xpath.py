import requests
from lxml import etree

url = 'https://beijing.zbj.com/search/f/?type=new&kw=saas'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

response = requests.get(url,headers=headers)
# print('请求的URL',response.request.url)
# print(response.text)
# 解析返回的html文件
web_data = etree.HTML(response.text)
# divs = web_data.xpath('//*[@id="__layout"]/div/div[3]/div/div[3]/div[4]/div[1]/div[1]/div')
divs = web_data.xpath('/html/body/div/div/div/div[3]/div/div[3]/div[4]/div[1]/div')
print(divs)
for i in divs:
    title = i.xpath('./div/div[3]/a/text()')
    price = i.xpath('./div/div[3]/div/span/text()')[0][1:]
    service_comment = i.xpath('./div/div[3]/div[3]/div/span/text()')
    print(service_comment)

response.close()        # 获取完数据后关闭请求