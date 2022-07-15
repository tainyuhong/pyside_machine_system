from peewee import *

database = MySQLDatabase('db_student', **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '123456'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Person(BaseModel):
    birthday = DateField()
    name = CharField()

    class Meta:
        table_name = 'person'

class Pet(BaseModel):
    animal_type = CharField()
    name = CharField()
    owner = ForeignKeyField(column_name='owner_id', field='id', model=Person)

    class Meta:
        table_name = 'pet'

class TbClass(BaseModel):
    class_id = AutoField(column_name='classID')
    class_name = CharField(column_name='className', null=True)
    grade_id = IntegerField(column_name='gradeID')

    class Meta:
        table_name = 'tb_class'

class TbExamkinds(BaseModel):
    kind_id = AutoField(column_name='kindID')
    kind_name = CharField(column_name='kindName', null=True)

    class Meta:
        table_name = 'tb_examkinds'

class TbGrade(BaseModel):
    grade_id = AutoField(column_name='gradeID')
    grade_name = CharField(column_name='gradeName', null=True)

    class Meta:
        table_name = 'tb_grade'

class TbResult(BaseModel):
    id = AutoField(column_name='ID')
    kind_id = IntegerField(column_name='kindID', null=True)
    result = FloatField(constraints=[SQL("DEFAULT 0")], null=True)
    stu_id = CharField(column_name='stuID', null=True)
    sub_id = IntegerField(column_name='subID', null=True)

    class Meta:
        table_name = 'tb_result'

class TbStudent(BaseModel):
    address = CharField(null=True)
    age = IntegerField(null=True)
    class_id = IntegerField(column_name='classID', null=True)
    grade_id = IntegerField(column_name='gradeID', null=True)
    phone = CharField(null=True)
    sex = CharField(null=True)
    stu_id = CharField(column_name='stuID', constraints=[SQL("DEFAULT 'SID00101001'")], primary_key=True)
    stu_name = CharField(column_name='stuName', null=True)

    class Meta:
        table_name = 'tb_student'

class TbSubject(BaseModel):
    sub_id = AutoField(column_name='subID')
    sub_name = CharField(column_name='subName', null=True)

    class Meta:
        table_name = 'tb_subject'

class TbUser(BaseModel):
    user_name = CharField(column_name='userName', primary_key=True)
    user_pwd = CharField(column_name='userPwd', null=True)

    class Meta:
        table_name = 'tb_user'

class Users(BaseModel):
    addr = CharField(null=True)
    name = CharField(index=True, null=True)

    class Meta:
        table_name = 'users'

