import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains



opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')


# 创建一个浏览器实例
web = Edge(options=opt)
# 打开百度网页
web.get('https://www.lagou.com')


# print(web.title)
# 在浏览器实例中查找全国的元素
pos = web.find_element(By.XPATH,'//*[@id="changeCityBox"]/p[1]/a')
# 点击这个元素
pos.click()

input_cont = web.find_element(By.XPATH,'//*[@id="search_input"]')
# 向搜索框中输入查找内容，并回车
input_cont.send_keys('python',Keys.ENTER)

time.sleep(1)

# 找到整体职位信息框
info_list = web.find_elements(By.XPATH,'//*[@id="jobList"]/div[1]/div')
# 从整体职位信息框中获取公司名，岗位，薪资

for i in info_list:                   # './div[1]/div[2]/div[1]/a'
    company = i.find_element(By.XPATH,'./div/div[2]/div[1]/a').text
    gw = i.find_element(By.XPATH,'./div/div[1]/div[1]/a').text
    gz = i.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    print('职位信息：',company,gw,gz)

    """
    思路：
        # 获取某个岗位位的职位描述
        # 1、需要先打开该职位页面
        # 2、在新页面中获取职位信息数据
        # 3、关闭职位信息页面，返回原页面
    """

    # 获取每个岗位的职位描述信息
    gw_web = i.find_element(By.XPATH, './div/div[1]/div[1]/a')
    gw_web.click()
    time.sleep(1)
    # 切换到新打开的窗口
    web.switch_to.window(web.window_handles[-1])

    gw_desc = web.find_element(By.XPATH, '//*[@id="job_detail"]/dd[2]/div').text
    print(gw_desc)
    web.close()
    web.switch_to.window(web.window_handles[0])
    time.sleep(2)
