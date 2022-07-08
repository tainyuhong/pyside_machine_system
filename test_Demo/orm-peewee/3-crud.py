from peewee import *
from datetime import date

my_db = {'host': 'localhost', 'password': '123456', 'port': 3306, 'user': 'root'}
db = MySQLDatabase('db_student', **my_db)


# 新建一个persion表
class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db


# db.connect()
# db.create_tables([Person,Pet])

# # 添加记录 方法一save
# jim = Person(name='jim', birthday=date(1960, 1, 12))
# tom = Person(name='tom', birthday=date(1960, 1, 12))
# n = tom.save()   # 保存到数据库,返回执行的行数
# print(n)


# # 添加记录方法二create
# tony = Person.create(name='tony',birthday=date(1999,2,2))   # 返回主键id值
# print(tony)
#
# # 修改记录值
# tony.name = 'tony-1'
# tony.save()

# # 添加宠物记录
# tom_kitty = Pet.create(owner=2, name='kitty', animal_type='cat')
# # tony_laifu = Pet.create(owner=tony,name='laifu',animal_type='dog')
# jim_wangcai = Pet.create(owner=1, name='wangcai', animal_type='dog')
# print(jim_wangcai)

# 添加记录方法三insert
# tony_zidan = Pet.insert(owner=3, name='zidan', animal_type='dog').execute()
# print(tony_zidan)

# # 批量插入记录
# people = [('张三1','2000-02-02'),('李四1','2001-02-02')]
# data = Person.insert_many(people,['name','birthday']).execute()
# print(data)

# 修改
# save()方法
# tony_dog = Pet(id=6,name='peet')
# print(tony_dog.save())  # 返回修改记录的行数

# # update方法
# tom_modify = Person.update(name='tony',birthday=date(1111,3,3)).where(Person.id==3).execute()
# print(tom_modify)

#  查询
# p = Person.get_by_id('11')
# print(p)
#
# p, created = Person.get_or_create(name='赵六1', defaults={'Birthday': date(1940, 1, 1)})
# print(p, created)  # 如果name不存在，则新建一条记录

# a = Person.select().
# print(a)

# 删除
# d = Pet.delete().where(Pet.name == 'peet').execute()
# print(d)

p = Person.get(Person.name=='jim')
p.delete_instance(recursive=True)