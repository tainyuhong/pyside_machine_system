from peewee import *

my_db = {'host':'localhost','password':'123456','port':3306,'user':'root'}
db = MySQLDatabase('db_student',**my_db)


# 新建一个persion表
class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person,backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

db.connect()
db.create_tables([Person,Pet])