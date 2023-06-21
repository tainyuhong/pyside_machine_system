from pprint import pp
import psutil as pst

# # CPU信息
# cpu_count = pst.cpu_count()  # 逻辑CPU数 ，即线程数
# cpu_time_perc = pst.cpu_times_percent(0.1)  # user, system, idle, interrupt, dpc)
#
# print(cpu_count, pst.cpu_percent(0.1), cpu_time_perc.user, cpu_time_perc.system, cpu_time_perc.idle)
#
# # 磁盘空间信息
# disk_part = pst.disk_partitions()
# part_info = []  # 格式(分区，挂载点，文件系统类型，磁盘总大小G，使用大小G,剩余大小G，使用率%)
# for i in disk_part:
#     disk_used = pst.disk_usage(i.device)
#     if pst.WINDOWS:
#         part_info.append((i.device, i.fstype, round(disk_used.total / 1024 / 1024 / 1024, 2),
#                           round(disk_used.used / 1024 / 1024 / 1024, 2), round(disk_used.free / 1024 / 1024 / 1024, 2),
#                           disk_used.percent))
#     else:
#         part_info.append((i.device, i.mountpoint, i.fstype, round(disk_used.total / 1024 / 1024 / 1024, 2),
#                           round(disk_used.used / 1024 / 1024 / 1024, 2), round(disk_used.free / 1024 / 1024 / 1024, 2),
#                           disk_used.percent))
# pp(part_info)
#
# # 内存
# mem_used = pst.virtual_memory()
# print(round(mem_used.total / 1024 / 1024 / 1024, 2), round(mem_used.used / 1024 / 1024 / 1024, 2),
#       round(mem_used.free / 1024 / 1024 / 1024, 2), round(mem_used.available / 1024 / 1024 / 1024, 2), mem_used.percent)


# # 进程
# process_list = pst.process_iter(['pid',  'cpu_percent', 'memory_percent','name', 'status', 'num_threads'])
# p = [i.info for i in process_list]
# p.sort(key=lambda p:(p['memory_percent'],p['cpu_percent']),reverse=True)
# # p1 = sorted(p,key=lambda p:(p['memory_percent'],p['cpu_percent']),reverse=True)
# pp(p)

# 网络接口
net = pst.net_if_addrs()
# pp(net)
# 网络接口状态
net_stat = pst.net_if_stats()
# 网卡名
net_names = net.keys()
for name in net_names:
    net_info = net[name]
    net_info_stat = (net_stat[name].isup,net_stat[name].speed,net_stat[name].duplex)
    # net_stat[name].isup：网卡状态，net_stat[name].speed：网卡速率，net_stat[name].duplex：网卡双工模式
    print('{}-->状态：{}  速率：{} 双工模式：{}'.format(name,*net_info_stat))
    for i in net_info:
        # family = '{}--->{}'.format(i.family.name, i.family.value)
        if i.family.name == 'AF_LINK'  or i.family.name == 'AF_PACKET': # linux底下AF_PACKET表示MAC地址
            family='MAC地址：'
        elif i.family.name == 'AF_INET':
            family='IPv4地址：'
        elif i.family.name == 'AF_INET6':
            family='IPv6地址：'
        else:
            family = i.family.name

        # 'AF_LINK:-1' 表示MAC信息： '64-6C-80-C4-88-64'
        # linux底下AF_PACKET表示MAC地址
        # ('AF_INET:2'表示IP地址'169.254.210.92', '255.255.0.0', None)
        # ('AF_INET6:23',   表示IPV6地址 'fe80::3ac3:a9a5:36eb:b8ba', None, None)
        addr = i.address
        netmask = i.netmask
        broadcat = i.broadcast
        inf =(family,addr,netmask)
        print(inf)
    print('*'*50,'\n')

# 当前用户
user = pst.users()
print(user,pst.boot_time())

# 当前负载
loadavg = pst.getloadavg()
print(loadavg)