# 从网易云音乐爬取音乐
import random
import requests
import re
import time

# 爬取汽车相关信息，并下载至本地，需要将需要的小说链接进行替换
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',}

response = requests.get('https://music.163.com/discover/toplist?id=3778678', headers=headers)       # 小说目录页
response.encoding= 'utf-8'    # 转换为utf-8
# html页面内容
html_data = response.text
# print(html_data)
result = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>',html_data)   # 通过正则查找歌曲名及信息
# print(result)
url = 'https://music.163.com/song/media/outer/url?id='     # 外部接口地址https://music.163.com/song/media/outer/url?id=475479888
url_list = []
for id,name in result:
    # url_list.append({name:url+id})
    # 解析请求
    new_url = url+id
    response_mp3 = requests.get(new_url,headers=headers)
    # 获取音乐的二进制数据
    music_data = response_mp3.content
    # 保存至文件
    with open('D:\\music_download\\'+name+'.mp3','wb') as f:
        f.write(music_data)
        print(name,'下载完成')
    time.sleep(random.randint(1,5))

print('全部下载完成')




