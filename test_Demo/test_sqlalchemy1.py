from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Index,ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# # 原生方式连接查询
# # 实例化一个引擎
# engine = create_engine('mysql+pymysql://root:123456@localhost/db_student', echo=True)
# # 创建一个裸连接
# conn = engine.raw_connection()
# # 创建一个游标
# cur= conn.cursor()
# # 执行一条sql
# cur.execute('select * from tb_result ')
# # 获取查询结果
# result = cur.fetchall()
# print(result)

# ORM方式连接管理
# 1、定义一个元类
Base= declarative_base()

# 2、定义一个用户表类
class User(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True)
    name=Column(String(32),index=True,nullable=True)
    addr = Column(String(32),nullable=True)

# 利用引擎创建表
def create_table():
    engine = create_engine('mysql+pymysql://root:123456@localhost/db_student', echo=True)
    # 调用元类创建所有表
    Base.metadata.create_all(engine)        # 创建所有表
   #  Base.metadata.drop_all(engine)      # 删除所有表


if __name__ == '__main__':
    create_table()