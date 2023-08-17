from pprint import pp
import psutil as pst


# # CPU信息
def get_cpu_stat():
    cpu_count = pst.cpu_count()  # 逻辑CPU数 ，即线程数
    cpu_time_perc = pst.cpu_times_percent(0.1)  # user, system, idle, interrupt, dpc)
    cpu_info = cpu_count, pst.cpu_percent(0.1), cpu_time_perc.user, cpu_time_perc.system, cpu_time_perc.idle
    return cpu_info  # 逻辑CPU的数量，cpu的使用率，cpu用户使用率，系统使用率，idel使用率


# # 磁盘空间信息
def get_partition():
    disk_part = pst.disk_partitions()
    part_info = []  # 格式(分区，挂载点，文件系统类型，磁盘总大小G，使用大小G,剩余大小G，使用率%)
    for i in disk_part:
        disk_used = pst.disk_usage(i.device)
        if pst.WINDOWS:
            part_info.append((i.device, i.fstype, round(disk_used.total / 1024 / 1024 / 1024, 2),
                              round(disk_used.used / 1024 / 1024 / 1024, 2),
                              round(disk_used.free / 1024 / 1024 / 1024, 2),
                              disk_used.percent))
        else:
            part_info.append((i.device, i.mountpoint, i.fstype, round(disk_used.total / 1024 / 1024 / 1024, 2),
                              round(disk_used.used / 1024 / 1024 / 1024, 2),
                              round(disk_used.free / 1024 / 1024 / 1024, 2),
                              disk_used.percent))
    # pp(part_info)
    return part_info


# # 内存
def get_mem_info():
    mem_used = pst.virtual_memory()
    res = round(mem_used.total / 1024 / 1024 / 1024, 2), round(mem_used.used / 1024 / 1024 / 1024, 2), round(
        mem_used.free / 1024 / 1024 / 1024, 2), round(mem_used.available / 1024 / 1024 / 1024, 2), mem_used.percent
    # 总内存，使用内存，剩余内存，可用内存，使用率
    # print(res)
    return res




# # 进程
def get_process_info(first='cpu_percent',second='memory_percent',reverse=False):
    """
    获取进程信息
    :param first:  默认第一排序CPU使用率
    :param second: 默认第二排序按内存使用率
    :param reverse: 默认按升序排序 为True时是降序排列
    :return:
    """
    process_list = pst.process_iter(['pid',  'cpu_percent', 'memory_percent','name', 'status', 'num_threads'])
    p = [i.info for i in process_list]
    p.sort(key=lambda p:(p[first],p[second]),reverse=reverse)
    # p1 = sorted(p,key=lambda p:(p['memory_percent'],p['cpu_percent']),reverse=True)
    pp(p)
    return p


# 获取网络接口信息
def net_if():
    # 获取所有网络接口信息
    net = pst.net_if_addrs()
    # pp(net)
    # 获取网络接口状态
    net_stat = pst.net_if_stats()
    # 从网络接口信息中获取网卡名
    net_names = net.keys()
    net_if_stat = []  # 所有网卡状态及速率信息
    # 按网卡名遍历每个网卡的信息
    for name in net_names:
        # 从网络接口net信息中获取每个接口的信息
        net_info = net[name]
        tmp = []  # 临时存放MAC/IP/

        for i in net_info:
            # family = '{}--->{}'.format(i.family.name, i.family.value)
            if i.family.name == 'AF_LINK' or i.family.name == 'AF_PACKET':  # linux底下AF_PACKET表示MAC地址
                family = 'MAC：'
            elif i.family.name == 'AF_INET':
                family = 'IPv4：'
            elif i.family.name == 'AF_INET6':
                family = 'IPv6：'
            else:
                family = i.family.name

            # 'AF_LINK:-1' 表示MAC信息： '64-6C-80-C4-88-64'
            # linux底下AF_PACKET表示MAC地址
            # ('AF_INET:2'表示IP地址'169.254.210.92', '255.255.0.0', None)
            # ('AF_INET6:23',   表示IPV6地址 'fe80::3ac3:a9a5:36eb:b8ba', None, None)
            addr = i.address
            netmask = i.netmask
            # broadcat = i.broadcast    # 广播地址
            inf = (family, addr, netmask)  # MAC,IP,子网掩码
            # print(inf)
            tmp.append(inf)
        # print('*'*50,'\n')
        net_info_stat = (name, net_stat[name].isup, net_stat[name].speed, net_stat[name].duplex, tmp)
        # net_stat[name].isup：网卡状态，net_stat[name].speed：网卡速率，net_stat[name].duplex：网卡双工模式
        # print('{}-->状态：{}  速率：{} 双工模式：{}'.format(name,*net_info_stat))
        # 显示的数据格式：以太网-->状态：False  速率：0 双工模式：2
        net_if_stat.append(net_info_stat)  # 网卡
    return net_if_stat

print('CPU',get_cpu_stat())
print('内存',get_mem_info())
print('磁盘',get_partition())
print('网卡',net_if())
print('进程',get_process_info())

# # 当前用户
# user = pst.users()
# print(user,pst.boot_time())
#
# # 当前负载
# loadavg = pst.getloadavg()
# print(loadavg)
