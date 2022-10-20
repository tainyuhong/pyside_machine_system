# 从百度翻译获取翻译信息，以post方式传入值
import requests

url = 'https://fanyi.baidu.com/sug'
# url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
head = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
i = input('请输入要翻译的单词：')

data = {'kw': i}

response = requests.post(url,data=data,headers=head)

print(response.json())