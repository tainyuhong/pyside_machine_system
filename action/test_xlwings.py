import xlwings as xw

app = xw.App(visible=False, add_book=False)
"""第2行代码启动Excel程序窗口，但不新建工作簿。其中的App()是 xlwings模块中的函数，该函数有两个常用参数：参数visible用于设置
Excel程序窗口的可见性，如果为True，表示显示Excel程序窗口，如果 为False，表示隐藏Excel程序窗口；参数add_book用于设置启动Excel程
 序窗口后是否新建工作簿，如果为True，表示新建一个工作簿，如果为 False，表示不新建工作簿"""
wb = app.books.add()  # 新建工作簿
ws = wb.sheets.add('第一个工作表')
# ws = wb.sheets.active
# ws.name = '第一个工作表'
# # ws = wb.sheets[0]     # 直接创建一个sheet页并命名
ws.name = '第一个工作表'
data = [['1', '5-1_A01_37', '10G带外管理接入3', '带内:\r\n带外:', '210235A2VEH2290CG00D'],
        ['13', '5-1_A03_30', '物理机服务器-1', '带内:\r\n带外:', '219385742824'],
        ['14', '5-1_A03_27', '宿主机服务器-8', '带内:\r\n带外:', '219385742837'],
        ['2', '5-1_A01_34', '10G业务管理交换机1', '带内:\r\n带外:', '210235A2TLH2290C001Y'],
        ['3', '5-1_A01_26', '文件存储网关服务器-1', '带内:6.40.130.35\r\n带外:', 'PR212K221024HN0004'],
        ['4', '5-1_A01_15', '负载均衡', '带内:\r\n带外:', ''],
        ['5', '5-1_A01_3', '信创-核心交换机1', '带内:\r\n带外:', '1022A5784470']]
ws.range((2,2),(7,5)).options(expand='table').api.NumberFormat='@'
ws.range('A1').value = data
rng = ws.range((6,5),(5,5))
rng.merge()  # 合并
print(rng.size)
ws.autofit('c')
# print('最后一列',ws.used_range.last_cell.column)
for i in range(7,13):
        ws.range('A1').expand().api.Borders(i).Weight=2
        # area.api.Borders(i).LineStyle = 1
        # area.api.Borders(i).Weight = 2


wb.save(r'C:\Users\zl\Desktop\112.xlsx')
wb.close()  # 关闭工作簿
app.quit()  # 退出EXCEL程序

# wb=xw.Book()
# sh = wb.sheets[0]
# for i in range(1,6):
#     for j in range(1,6):
#         sh.range(i,j).value='({}-{})'.format(i,j)
# # wb.save(r'C:\Users\zl\Desktop\111.xlsx')
# # wb.close()
