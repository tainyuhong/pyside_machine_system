# -*- coding: utf-8 -*-
import paramiko
import telnetlib
import logging
import time
import pathlib
import subprocess
# from db.db_handler import *
from db.db_orm import database

# 定义日志格式
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s', filename='checkrun.log')  # , filename='checkrun.log'

# 创建数据库对象实例
# db = DBMysql()


# 建立连通性及检查类
class SshToHost(object):
    # 检查主机22端口是否能正常访问
    @staticmethod
    def host_connectivity(host, good_host):
        """
        检测主机22端口是否正常,返回正常主机列表信息
        :param good_host: # 存放检测后正常的主机列表信息
        :param host: 主机信息 格式('hostname','ip','user','passwd')
        """
        t = telnetlib.Telnet()  # 用telnet检测IP、端口是否能正常访问
        try:
            t.open(host[1], 22, timeout=5)  # 打开一个远程连接，超时时间为2S
        except Exception as e:
            # logging.error('连接错误：'.format(e))
            logging.warning('{}:{} IP或端口异常,将不执行巡检任务！！！'.format(host[0], host[1]))
            return '  {}:{}  IP或端口异常,将不执行巡检任务！！！'.format(host[0], host[1])
        else:
            logging.info(' {}:{}  网络及22端口正常！'.format(host[0], host[1]))
            good_host.append(host)  # 添加到正常主机列表中
            return '  {} : {}  网络及22端口正常！'.format(host[0], host[1])
        finally:
            t.close()  # 关闭连接

    # 检查主机存活状态
    @staticmethod
    def is_alive(ip, up, down):
        """
        用ping命令检查主机存活状态
        :param ip_: ip为元组格式('hostname','ip','user','passwd')
        :return: 正常主机列表host_up和不可达主机列表host_down
        """
        ip_ping = subprocess.run(['ping', '-n', '2', '-w', '5', ip[1]], shell=True, stdin=subprocess.PIPE,
                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding='gb18030')
        # print('ping信息', ip_ping)
        if ip_ping.returncode == 1:
            logging.info(' {}:{} 网络不可达!!'.format(ip[0], ip[1]))
            # print('{} {} 网络不可达!!'.format(ip[0], ip[1]))
            down.append(ip)
            return '\t{} : {}  网络不可达 !!'.format(ip[0], ip[1])
        else:
            logging.info('{}:{} 主机在线'.format(ip[0], ip[1]))
            # print('{} {} 主机在线\n'.format(ip[0], ip[1]))
            up.append(ip)
            return '\t{} : {}  主机在线'.format(ip[0], ip[1])

    # ssh到主机执行命令，并发送到终端
    def exec_cmd(self, host, cmd_sql, args):
        """
        ssh到主机执行命令，并发送到终端，必须传入4元元组数据
        :param host: 传入22端口能正常访问的主机，格式('hostname','ip','user','passwd')
        :param cmd_sql:巡检命令查询SQL
        :param args:巡检命令传入参数 ，需要传入ip,命令类型
        :return:
        """
        count = 0  # 计数巡检主机数
        hostname, ip, username, password = host
        try:
            self.trans = paramiko.Transport((ip, 22))  # 使用Transport方式连接
            self.trans.start_client(timeout=0.5)
            # paramiko.util.log_to_file('paramiko-log.log')  # 记录执行日志
            # 用户名密码方式
            self.trans.auth_timeout = 5
            self.trans.auth_password(username=username, password=password, fallback=True)
        except paramiko.ssh_exception.AuthenticationException as pass_err:
            logging.error('{}:{} {}'.format(hostname, ip, pass_err))
            print('{}:{} 用户名或密码错误，跳过巡检'.format(hostname, ip))
            # continue
        except Exception as e:
            logging.error('连接错误：', e)
        else:
            logging.info('连接主机:{}:{}正常'.format(hostname, ip))
            # 打开一个通道
            self.channel = self.trans.open_session()
            self.channel.settimeout(100)
            # 获取一个终端
            self.channel.get_pty()
            # 激活器
            self.channel.invoke_shell()
            # 根据配置文件定义command项执行脚本
            # 获取脚本命令内容
            print('cmd_sql',cmd_sql)
            print('args',args)
            cmd_file = database.execute_sql(cmd_sql,args)     # 查看有几个可执行的脚本配置文件
            # cmd_file = db.query_single(cmd_sql,args)     # 查看有几个可执行的脚本配置文件
            print('cmd_file',cmd_file)
            if len(cmd_file) > 0:
                # print('cmd_file',cmd_file)
                for i in cmd_file:      # 遍历脚本配置文件
                    single_cmd = i[0].split('\n')     # 提取配置文件中脚本命令
                    # print('single_cmd',single_cmd)
                    for c in single_cmd:        # 遍历每个命令
                        # print('命令c：', c,type(c))
                        # 发送要执行的命令
                        time.sleep(0.1)
                        logging.info('执行命令：【{}】'.format(c))     # 记录需要执行的命令到日志
                        self.channel.send(c + '\n')             # 在每一个命令后加上换行
                        # time.sleep(1)
                        self.out_print(ip)  # 调用输出命令结果函数
                    print()
                    print('=' * 80)

                count += 1  # 执行一个脚本后+1
            else:
                print('没有配置相关命令！，请配置检查脚本命令后再操作！！')
                return
            self.channel.close()
            self.trans.close()
        print('\n')
        return count    # 返回执行成功数

    # 输出命令执行结果
    def out_print(self, host_ip):
        """
        输出命令执行结果
        :param host_ip:主机IP地址，字符串格式
        :return:
        """
        if not pathlib.Path('result').exists():
            pathlib.Path('result').mkdir()
        end_symbol = ('# ', '$ ', '$', '> ', '>')  # 设置我们定义的结束符
        # 将命令执行结果保存到文件
        command_result = open(
            'result\\exec_result-{}-{}.log'.format(time.strftime('%Y%m%d', time.localtime()), host_ip), 'a')
        # 回显很长的命令可能执行较久，通过循环分批次取回回显
        time.sleep(1.5)
        while True:
            result = self.channel.recv(1024)
            try:
                result = result.decode('utf-8')
                logging.warning('使用UTF-8编码！')
            except:
                result = result.decode('gb18030')
                logging.warning('使用gb18030编码！')
            if result.endswith(end_symbol):
                command_result.write(result)  # 将小于1024的部分输出保存到执行结果文件中，并跳出循环
                print(result, end='')  # 输出到日志显示窗口
                break
            else:
                command_result.write(result)  # 将大于1024的部分输出保存到执行结果文件中
                print(result, end='')  # 输出到日志显示窗口
        command_result.close()
