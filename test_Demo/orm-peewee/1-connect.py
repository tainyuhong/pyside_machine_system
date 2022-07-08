from peewee import *

my_db = {'host':'localhost','password':'123456','port':3306,'user':'root'}
try:
    db = MySQLDatabase('db_student',**my_db)
    db.connect()
    db.is_closed()
except Exception as e:
    print(e)
else:
    print('数据库连接成功')
