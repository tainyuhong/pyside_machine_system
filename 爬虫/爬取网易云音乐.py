# 从铜钟音乐爬取音乐
import random
import requests
import re
import time
from pathlib import Path

# https://tonzhon.com/hot

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36', }

# 从铜钟音乐爬取音乐
# # 以JSON格式获取返回的html页面内容
# response = requests.get('https://tonzhon.com/secondhand_api/hot_list/netease', headers=headers).json()
# # 获取歌曲格式
# song_data = response['data']['songs']
# # print(song_data)
# song_list = []
# for i in song_data:
#     song_list.append((i['originalId'], i['name'], i['requiringPayment']))
# # print(song_list)
# print('--->共有{}首歌曲'.format(len(song_list)))
def music_top():
    url = 'https://music.163.com/discover/toplist?id=19723756'
    # 以JSON格式获取返回的html页面内容
    response_song = requests.get(url, headers=headers)
    # song_data = response_song['result']['songs']  # 歌曲查询结果返回数据
    response_song.encoding='utf-8'

    result = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', response_song.text)  # 通过正则查找歌曲名及信息
    print(result)
    # print(result)
    song_list = []  # 定义歌曲列表
    num = 0
    # 格式化获取歌曲信息
    # for i in song_data:
    #     song_id = i['id']  # 歌曲ID
    #     song_name = i['name']  # 歌名
    #     song_art = i['artists'][0]['name']  # 艺术家
    #     song_album = i['album']['name']  # 歌曲专辑
    #     song_time = time.strftime('%M:%S', time.localtime(i['duration'] / 1000))  # 将毫秒时间转换成标准时间格式
    #     num += 1
    #     info = (num, song_id, song_name, song_art, song_album, song_time)
    #     song_list.append(info)
    #     print(info)
    # print(song_list)

def download_song(song_list,num):
    # 外部接口地址'https://music.163.com/song/media/outer/url?id='
    song_api = 'https://music.163.com/song/media/outer/url?id='
    if Path('D:\\music').exists():
        # print(Path.cwd())
        # print('搜索到的歌曲列表：',song_list)   # 格式 (1, 1807799505, '唯一', '告五人', '运气来得若有似无', '04:30')
        print('选择的下载信息：',song_list[num-1])
        # 判断是否存在相同的歌曲，存在则不下载
        song_name = re.sub('[/*]','',song_list[num-1][2])
        if not Path('D:\\music\\' + song_name + '.mp3').exists():
            # 解析请求
            new_url = song_api + str(song_list[num-1][1])
            response_mp3 = requests.get(new_url, headers=headers)
            # 获取音乐的二进制数据
            music_data = response_mp3.content
            # 保存至文件
            with open('D:\\music\\' + song_name + '.mp3', 'wb') as f:
                f.write(music_data)
                print(song_name, '下载完成')
                time.sleep(random.randint(1, 5))
        else:
            print('{}  歌曲已经存在，不需要再下载'.format(song_name))

        print('全部下载完成')
    else:
        Path('D:\\music').mkdir()
        # print('创建目录')
        # 判断是否存在相同的歌曲，存在则不下载
        song_name = re.sub('[/*]', '', song_list[num - 1][2])
        if not Path('D:\\music\\' + song_name + '.mp3').exists():
            # 解析请求
            new_url = song_api + str(song_list[num - 1][1])
            response_mp3 = requests.get(new_url, headers=headers)
            # 获取音乐的二进制数据
            music_data = response_mp3.content
            # 保存至文件
            with open('D:\\music\\' + song_name + '.mp3', 'wb') as f:
                f.write(music_data)
                print(song_name, '下载完成')
                time.sleep(random.randint(1, 5))
        else:
            print('{}  歌曲已经存在，不需要再下载'.format(song_name))

        print('全部下载完成')


def download_song_hot(song_list):
    # 外部接口地址'https://music.163.com/song/media/outer/url?id='
    song_api = 'https://music.163.com/song/media/outer/url?id='
    for song_id, song_name, payment in song_list:
        # 判断是否存在相同的歌曲，存在则不下载
        song_name = re.sub('[/*]','',song_name)
        if not Path('D:\\music\\' + song_name + '.mp3').exists():
            # 解析请求
            new_url = song_api + str(song_id)
            response_mp3 = requests.get(new_url, headers=headers)
            # 获取音乐的二进制数据
            music_data = response_mp3.content
            # 保存至文件
            with open('D:\\music\\' + song_name + '.mp3', 'wb') as f:
                f.write(music_data)
                print(song_name, '下载完成')
            # time.sleep(random.randint(1,5))
        else:
            print('{}  歌曲已经存在，不需要再下载'.format(song_name))

    print('全部下载完成')

# 搜索歌曲功能
def search_song(song_name):
    url = 'http://music.163.com/api/search/get/web?csrf_token=hlpretag=&hlposttag=&s={}&type=1&offset=0&total=true&limit=20'.format(
        song_name)
    """
    使用技巧：
    limit：返回数据条数（每页获取的数量），默认为20，可以自行更改
    offset：偏移量（翻页），offset需要是limit的倍数
    
    type：搜索的类型
    type=1 单曲
    type=10 专辑
    type=100 歌手
    type=1000 歌单
    type=1002 用户
    type=1004 MV
    type=1006 歌词
    type=1009 主播电台"""
    # print(url)
    # 以JSON格式获取返回的html页面内容
    response_song = requests.get(url, headers=headers).json()
    song_data = response_song['result']['songs']  # 歌曲查询结果返回数据
    # print(song_data)
    song_list = []  # 定义歌曲列表
    num = 0
    # 格式化获取歌曲信息
    for i in song_data:
        song_id = i['id']                       # 歌曲ID
        song_name = i['name']                   # 歌名
        song_art = i['artists'][0]['name']      # 艺术家
        song_album = i['album']['name']         # 歌曲专辑
        song_time = time.strftime('%M:%S', time.localtime(i['duration'] / 1000))  # 将毫秒时间转换成标准时间格式
        copyrightId = '免费' if i['copyrightId'] == 0 else '收费'       # 版权ID，如果有版权ID则收费，为0则免费
        num += 1
        info = (num, song_id, song_name, song_art, song_album, song_time,copyrightId)
        song_list.append(info)
        print(info)
    return song_list


if __name__ == '__main__':
    name = input('请输入要查询的歌曲名字:').strip()
    song = search_song(name)
    num = int(input('请选择需要下载的序号：'))
    download_song(song,num)
    # music_top()
