from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String,Index,ForeignKey,func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# 实现增删改查
# ORM方式连接管理
# 1、定义一个元类
Base= declarative_base()

# 2、定义一个用户表类
class User(Base):
    __tablename__ ='users'
    id = Column(Integer, primary_key=True)
    name=Column(String(32),index=True,nullable=True)
    addr = Column(String(32),nullable=True)

    def __repr__(self):
        return '用户编号：{}，姓名：{}，地址：{}'.format(self.id,self.name,self.addr)

# 查询数据
# 1、创建一个engine
engine = create_engine('mysql+pymysql://root:123456@localhost/db_student',echo=True)
# 2、创建一个session类
Session = sessionmaker(bind=engine)
# 3、创建一个session对象
session = Session()   # 也可以用conn

# 查询 Id为1的数据
# res = session.query(User).filter(User.id.in_((1,5))).all()
# res = session.query(func.count(User.name)).all()
# # 修改方法1
# user = User(id=6,name='太白金星')
# res = session.merge(user)
# 修改方法2
res=session.query(User).filter_by(id=7).update({User.name:'降龙'})

print('====>',res)
# 6、提交
session.commit()
session.close()
