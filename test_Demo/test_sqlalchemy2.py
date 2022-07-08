from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Index,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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


# 添加数据
# 1、创建一个engine
engine = create_engine('mysql+pymysql://root:123456@localhost/db_student', echo=True)
# 2、创建一个session类
Session = sessionmaker(bind=engine)
# 3、创建一个session对象
session = Session()   # 也可以用conn
# 4、创建一个对象
obj = User(name='zs')

# 5、把对象通过add添加到表中
session.add(obj)
# 6、提交
session.commit()
