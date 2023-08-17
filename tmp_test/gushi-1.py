# 从百度中爬取古诗

import requests
from lxml import etree

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            # 'Host': 'ug.baidu.com',
            # 'Origin': 'https://www.baidu.com',
            'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=2&tn=maxco7_dg&wd=%E6%B3%8A%E8%88%B9%E7%93%9C%E6%B4%B2&rsv_spt=1&oq=%25E6%25B3%258A%25E8%2588%25B9%25E7%2593%259C%25E6%25B4%25B2&rsv_pq=a66e4230000516a7&rsv_t=3068ZAvWeCj6EFTBihEIxYNNWh1Wb%2FUpa45qsVcvPeQkyKbZ1exVkr5jIrxF5hD0&rqlang=cn&rsv_enter=0&rsv_dl=tb&rsv_btype=t&inputT=1112456&rsv_sug4=1112457',
            # 'sec-ch-ua': '"Chromium";v="109", "Not_A Brand";v="99"',
            'sec-ch-ua-platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site'}
# name = input('请输入要搜索的古诗名字：')
name = '题西林壁'

# 百度汉语查询窗口
url = 'https://www.baidu.com/s?wd='    # 百度首页
search_url = url+ name
response = requests.get(search_url,headers=headers)
# print(response.text.encode('utf-8'))
# 解析返回的html文件
search_web = etree.HTML(response.text)
search_result = search_web.xpath('//*[@id="1"]/div/div[1]/div[3]/div[1]/div')
# search_result = search_web.xpath('//*[@id="1"]/div/div[1]/div[3]/div[1]/div[2]/div[1]/div[3]/span/audio')
# print('找到元素：',search_result)
                                # /div[1]/div[1]/text()
title = search_result[1].xpath('./div[1]/div[1]/text()')
print('标题：',title)
author = search_result[1].xpath('./div[1]/div[2]/text()')
print('作者：',author)
content = search_result[1].xpath('./div[2]/div[1]/div//span/text()')
print('诗文：',''.join(content))
audio = search_result[1].xpath('./div[1]/div[3]/span/audio/@src')
print('音频：',audio)  # /div[1]/div[3]/span/audio
# 获取诗文内容
# def get_content(resp):
#     title = search_result.xpath('./div[2]/div/text()')
#     print('标题：',title)
    # data_resp = resp.xpath('//*[@id="poem-detail-header"]')  # 诗的正文部分内容
    # for i in data_resp:
    #     title = i.xpath('./h1/text()')[0]
    #
    #     author = i.xpath('./div[1]/a//text()|./div[1]/span//text()')
    #     # 作者 朝代 由4个总分结合而成
    #     new_author = ''.join([a.strip() for a in author])
    #     print(new_author)
    #     gs_body = i.xpath('./div[3]//*[@id="body_p"]//text()')  # [@id="body_p"] 定位到原文一行
    #     gs_means = i.xpath('./div[3]//*[@id="means_p"]//text()')  # [@id="body_p"] 定位到译文一行
    #     # 去掉获取的文本中间空格及空字符
    #     new_gs_body = ''.join([b.strip() for b in gs_body])
    #     new_gs_means = ''.join([m.strip() for m in gs_means])
    #     print('诗句：', new_gs_body)  # ./div[3]/p[1]/span[1]/span[1]     |./div[3]/p[1]/*/text()
    #     print('译文：', new_gs_means)


# 根据搜索内容获取查询到的诗文内容
# if len(search_result)>0:
#     content = []    # 定义查询到的诗文的内容
#     # 查询到多个结果
#     for i in search_result:
#         # 只有文字链接和译文两行的情况
#         if len(i.xpath('./node()')) <= 2:
#             tmp=i.xpath('./div[1]/a/@href')+i.xpath('./div[2]/text()')       # 没有作者信息的第一行内容
#         # 有文字链接、作者朝代、诗文三行内容
#         else:
#             tmp = i.xpath('.//@href')+i.xpath('./div/span/text()')+i.xpath('./div[last()]/text()')
#             # 获取链接页面参数：'.//@href'   作者：'./div/span/text()'     第二行内容：'./div[last()]/text()'
#         # 去掉结果中的空格以及/n字符
#         content.append([t.strip() for t in tmp])
#     # print(content)
#     for n,c in enumerate(content):
#         print(n,c)
#     while True:
#         num = input('请选择需要下载的诗的序号：')
#         if num == 'exit':
#             break
#         elif num.isdigit() and int(num) <= len(content)-1:
#             # 下载音频文件
#             print(content[int(num)])
#             down_url = 'https://hanyu-poem-mp3.cdn.bcebos.com/'+content[int(num)][0][-32:]+'.mp3'
#             print('音频下载地址：',down_url)
#             with requests.get(down_url,headers=headers) as down:
#                 with open('D:\\txt\\{}.mp3'.format(name+content[int(num)][0][-6:]),'wb') as f:
#                     f.write(down.content)
#                     print('音频文件下载完成')
#                 down.close()
#             # 获取诗文内容信息
#             content_url = 'https://hanyu.baidu.com'+ content[int(num)][0]
#             print('诗正文页面：',content_url)
#             with requests.get(content_url, headers=headers) as cont_response:
#                 # 解析返回的html文件
#                 cont_web = etree.HTML(cont_response.text)
#                 # 获取诗文内容信息
#                 get_content(cont_web)
#                 cont_response.close()   # 关闭请求
#         else:
#             print(' 输入的数字大于序号或输入的非数字，请重新输入！')


# 查询到一个结果,页面会直接显示诗文的全部内容
# else:
#     get_content(search_web)

response.close()        # 获取完数据后关闭请求


# 古诗正文链接：
# https://hanyu.baidu.com/shici/detail?pid=2a8ba337af744ba1bc7d88b4a95eab20&srcid=51369
#
# # 音频文件链接
# http://hanyu-poem-mp3.cdn.bcebos.com/e1ee08f74e67482b97a6077aef2018de.mp3
