import requests

url = 'https://movie.douban.com/j/chart/top_list'
# 重新封装url'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100:90&action=&start=0&limit=20'
# url 问号后的为参数，对其参数进行重新封装
pars = {'type': 24,
        'interval_id': '100:90',
        'action': '',
        'start': 0,
        'limit': 20}

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

response = requests.get(url,headers=headers,params=pars)
print('请求的URL',response.request.url)
print(response.json())
response.close()        # 获取完数据后关闭请求