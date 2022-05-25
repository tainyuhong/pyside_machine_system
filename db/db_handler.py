import pymysql
import configparser
import logging
import os

# 定义日志格式
logging.basicConfig(level=logging.WARN, format='%(asctime)s %(levelname)s %(message)s', filename='machine.log')


class DBMysql(object):
    def __init__(self, **kwargs):
        cf = configparser.ConfigParser(allow_no_value=True)
        base_file = os.path.dirname(os.path.abspath(__file__))      # 获取文件的绝对路径
        try:
            cf.read(os.path.join(base_file,'db.ini'))       # 动态读取ini文件
            self.host = cf.get('db', 'host')
            self.password = cf.get('db', 'password')
            self.user = cf.get('db', 'user')
            self.database = cf.get('db', 'database')
            self.port = cf.getint('db', 'port')
            self.charset = cf.get('db', 'charset')
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,
                                        port=self.port, charset=self.charset, **kwargs)
        except Exception as e:
            # print('数据库错误：',e)
            logging.error('数据库连接错误：{}'.format(e))
        else:
            self.cursor = self.conn.cursor()
            # print('数据库连接成功')
            logging.info('数据库连接正常')


    def __del__(self):
        if self.conn is not None:
            self.cursor.close()  # 关闭游标
            self.conn.close()  # 关闭连接
            logging.info('退出数据库连接...')
        else:
            return

    # 查询数据函数，并返回查询条数
    def query(self, sql, args=None):
        '''
        查询数据函数，并返回查询条数
        :param sql: sql查询语句
        :param args: 需要传入的SQL参数
        :return: 返回二元组数据，（记数条数，查询到的数据）
        '''
        data = ''
        count = 0
        if self.is_connected():
            try:
                self.cursor.execute(sql, args)
                # print('传入的sql:',select_all_sql)
            except Exception as e:
                logging.error('数据库错误：{}'.format(e))
            else:
                data = self.cursor.fetchall()  # 获取所有查询记录
                count = self.cursor.rowcount
                self.conn.commit()
                logging.info('执行成功！{}'.format(self.cursor.rowcount))
            return count, data
        else:
            pass

    # 不返回查询数量的函数
    def query_single(self, sql, args=None):
        '''
        不返回查询记录条数的函数
        :param sql: sql查询语句
        :param args: 需要传入的SQL参数
        :return: 返回二元组数据，格式：（（第一条记录）,（第二条记录））
        '''
        # print('数据库中args：',args,sql)
        if self.is_connected():
            try:
                self.cursor.execute(sql, args)
                # print('传入的sql:',sql)
                # print('传入的args:',args)
            except Exception as e:
                logging.error('数据库错误：{}'.format(e))
            else:
                data = self.cursor.fetchall()  # 获取所有查询记录
                # count = self.cursor.rowcount
                self.conn.commit()
                logging.info('执行成功！{}'.format(self.cursor.rowcount))
                # print('DB',data)
            return data
        else:
            pass

    def alter(self, sql, args=None):
        # 修改、插入、删除数据
        if self.is_connected():
            try:
                self.cursor.execute(sql, args)
            except Exception as e:
                logging.error('数据库错误：{}'.format(e))
                self.conn.rollback()
            else:
                self.conn.commit()  # 提交记录
                #
                logging.info('-->{} 条记录执行成功！'.format(self.cursor.rowcount))
            return self.cursor.rowcount
        else:
            pass

    def alter_many(self, sql1, sql2, args1, args2):
        # 修改、插入、删除数据 多条记录
        if self.is_connected():
            try:
                self.cursor.execute(sql1, args1)
                self.cursor.execute(sql2, args2)
            except Exception as e:
                logging.error('数据库错误：{}'.format(e))
                self.conn.rollback()
            else:
                self.conn.commit()  # 提交记录

                logging.info('-->{} 条记录执行成功！'.format(self.cursor.rowcount))
            return self.cursor.rowcount
        else:
            pass

    def alter_multi(self, sql, args=None):
        # 修改、插入、删除数据
        if self.is_connected():
            try:
                self.cursor.executemany(sql, args)
                # print(args)
            except Exception as e:
                logging.error('数据库错误：{}'.format(e))
                self.conn.rollback()
            else:
                self.conn.commit()  # 提交记录

                logging.info('-->{} 条记录执行成功！'.format(self.cursor.rowcount))
            return self.cursor.rowcount
        else:
            pass

    def is_connected(self):
        """Check if the server is alive"""
        try:
            self.conn.ping(reconnect=True)
            print('db is connecting')
            return True
        except BaseException as e:
            print('数据库连接异常：{}'.format(e))
            return False
