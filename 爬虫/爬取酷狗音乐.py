# 从酷狗音乐爬取音乐
import random
import requests
import re
import time
from lxml import etree
from pathlib import Path

# https://tonzhon.com/hot

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', }


def music_top():
    # top 500歌曲
    url = 'https://www.kugou.com/yy/rank/home/1-8888.html?from=homepage'
    # 以JSON格式获取返回的html页面内容
    response_song = requests.get(url, headers=headers)
    # song_data = response_song['result']['songs']  # 歌曲查询结果返回数据
    response_song.encoding='utf-8'
    # print(response_song.text)
    web_data = etree.HTML(response_song.text)
    song_list = web_data.xpath('//*[@id="rankWrap"]/div[2]/ul')
    song_features = web_data.xpath('//*[@type="text/javascript" ]')
    # print(song_features)
    for x in song_features:
        print(x.text)
    # song_info = []  # 接收歌名及链接地址
    # for i in song_list:
    #     song = i.xpath('./li/a')       # //*[@id="rankWrap"]/div[2]/ul/li[1]/a
    #     # print(song,song_href)
    #     for _ in song:
    #         song_name = _.xpath('./@title')[0]    # 歌名
    #         song_link = _.xpath('./@href')[0]      # 歌曲播放链接
    #         song_info.append((song_name,song_link))
    # print(song_info)

    # 获取每首歌的信息
    # for l in song_info[0]:
    #     print('link',l)
    # response = requests.get(song_info[2][1], headers=headers)
    # print(response.text)


if __name__ == '__main__':

    music_top()
