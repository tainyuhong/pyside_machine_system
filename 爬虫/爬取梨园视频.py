import re

import requests
from lxml import etree

"""
思路：
1、通过url获取contId
2、通过video_status 来获取视频SRC地址,注意解决防盗链问题
3、将src地址拼接转换成真实视频地址  systime -->contId
4、下载保存视频数据
"""
# video_status = 'https://www.pearvideo.com/videoStatus.jsp?contId=1706850&mrd=0.48287876624738213'
# video_status 中src地址 'https://video.pearvideo.com/mp4/adshort/20201113/1666142235042-15481634_adpkg-ad_hd.mp4'
# 视频真实地址            'https://video.pearvideo.com/mp4/adshort/20201113/cont-1706850-15481634_adpkg-ad_hd.mp4'

url = 'https://www.pearvideo.com/video_1706850'
# 获取contid
contId = url.split('_')[1]
video_status = 'https://www.pearvideo.com/videoStatus.jsp?contId={}'.format(contId)

# headers中加入Referer(溯源，上一级目录是哪) 解决防盗链问题
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47',
    'Referer': 'https://www.pearvideo.com/video_1706850'}
response = requests.get(video_status, headers=headers)
html_dict = response.json()
print(html_dict)
systemTime = html_dict['systemTime']
video_src = html_dict['videoInfo']['videos']['srcUrl']
# 转换成真实视频地址
new_video = video_src.replace(systemTime,'cont-'+contId)
print('真实视频地址：',new_video)

# 下载视频
video_data = requests.get(new_video)
with open('D:\\123.mp4','wb') as f:
    f.write(video_data.content)
    print('视频下载完成')
response.close()  # 获取完数据后关闭请求
