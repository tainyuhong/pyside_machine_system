import configparser
import os
from peewee import *
import logging


# database = MySQLDatabase('equipment_mg',
#                          **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True, 'host': '127.0.0.1',
#                             'port': 3306, 'user': 'root', 'password': '123456'})
cf = configparser.ConfigParser(allow_no_value=True)
base_file = os.path.dirname(os.path.abspath(__file__))      # 获取文件的绝对路径

cf.read(os.path.join(base_file,'db.ini'))       # 动态读取ini文件
host = cf.get('db', 'host')
password = cf.get('db', 'password')
user = cf.get('db', 'user')
database = cf.get('db', 'database')
port = cf.getint('db', 'port')
charset = cf.get('db', 'charset')
database = MySQLDatabase(database, **{'host':host, 'user':user, 'password':password,  'port':port, 'charset':charset})


# 检查数据库是否连通
def get_db_status():
    try:
        database.connect(True)
    except Exception as e:
        logging.error('--->数据库连接错误：{}'.format(e))
        print('数据库连接失败')
        # QtWidgets.QMessageBox.critical(self,'数据库连接错误', '无法连接到数据库，请检查数据库配置信息是否正确！')
        return False
    else:
        print('数据库连接成功')
        return True


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = database


class CabPosition(BaseModel):
    """
    U位信息表
    """
    num = IntegerField(index=True)
    position_name = CharField(index=True)
    use = CharField(null=True)
    is_frame = IntegerField(null=True)
    comment = CharField(null=True)

    class Meta:
        table_name = 'cab_position'


class MachineRoom(BaseModel):
    """
        机房信息表
    """
    room_id = AutoField()
    room_name = CharField(unique=True)
    room_alias = CharField(null=True)
    comment = CharField(null=True)

    class Meta:
        table_name = 'machine_room'


class Cabinet(BaseModel):
    """
        机柜信息表
    """
    cab_id = AutoField()
    cab_num = CharField(index=True)
    cab_name = CharField(index=True)
    room = ForeignKeyField(column_name='room_id', field='room_id', model=MachineRoom)
    is_use = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    pdu_num = IntegerField(null=True)
    count_position = IntegerField(null=True)
    free = IntegerField(null=True)
    comment = CharField(null=True)

    class Meta:
        table_name = 'cabinet'


class CmdFile(BaseModel):
    """
        shell脚本信息表
    """
    cmd_id = AutoField()
    cmd_name = CharField(null=True)
    cmd = CharField(null=True)

    class Meta:
        table_name = 'cmd_file'


class MachineSort(BaseModel):
    """
    设备分类表
    """
    sort_id = AutoField()
    sort_name = CharField(index=True)
    part_sort = ForeignKeyField(column_name='part_sort_id', field='sort_id', model='self', null=True)
    part_sort_name = CharField(index=True, null=True)
    conments = CharField(null=True)

    class Meta:
        table_name = 'machine_sort'


class MachineInfos(BaseModel):
    """
        设备信息表
    """
    machine_id = AutoField()
    machine_name = CharField(null=True)
    machine_sort_name = ForeignKeyField(column_name='machine_sort_name', field='sort_name', model=MachineSort,
                                        null=True)
    machine_sn = CharField(null=True)
    machine_factory = CharField(null=True)
    model = CharField(null=True)
    machine_roomid = ForeignKeyField(column_name='machine_roomid', field='room_id', model=MachineRoom, null=True)
    cabinet_name = ForeignKeyField(column_name='cabinet_name', field='cab_num', model=Cabinet, null=True)
    start_position = ForeignKeyField(backref='cab_position_start_position_set', column_name='start_position',
                                     field='num', model=CabPosition, null=True)
    end_position = ForeignKeyField(column_name='end_position', field='num', model=CabPosition, null=True)
    factory_date = DateField(constraints=[SQL("DEFAULT 2000-01-01")], null=True)
    end_ma_date = DateField(constraints=[SQL("DEFAULT 2000-01-01")], null=True)
    work_are = CharField(null=True)
    run_state = IntegerField(constraints=[SQL("DEFAULT 1")], null=True)
    machine_admin = CharField(null=True)
    app_admin = CharField(null=True)
    mg_ip = CharField(null=True)
    app_ip1 = CharField(null=True)
    bmc_ip = CharField(null=True)
    install_date = DateField(null=True)
    uninstall_date = DateField(null=True)
    single_power = IntegerField(constraints=[SQL("DEFAULT 0")], null=True)
    comments = CharField(null=True)

    class Meta:
        table_name = 'machine_infos'


class MachineCheckUser(BaseModel):
    """
        巡检用户信息表
    """
    hostname = CharField(null=True)
    ip = CharField()
    user = CharField(null=True)
    password = CharField(null=True)
    cmd_id = IntegerField(null=True)
    comment = CharField(null=True)
    machine = ForeignKeyField(column_name='machine_id', field='machine_id', model=MachineInfos, null=True)

    class Meta:
        table_name = 'machine_check_user'


class MachineList(BaseModel):
    """
    设备信息视图表
    """
    machine_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    room_name = CharField()
    cab_name = CharField(null=True)
    start_position = IntegerField(null=True)
    postion_u = BigIntegerField(null=True)
    machine_sort_name = CharField(null=True)
    machine_factory = CharField(null=True)
    model = CharField(null=True)
    machine_sn = CharField(null=True)
    machine_name = CharField(null=True)
    mg_ip = CharField(null=True)
    machine_admin = CharField(null=True)

    class Meta:
        table_name = 'machine_list'
        primary_key = False


class Manufacturer(BaseModel):
    """
        设备厂商信息表
    """
    manufacturer_name = CharField(null=True)
    comment = CharField(null=True)

    class Meta:
        table_name = 'manufacturer'


class ShelfManage(BaseModel):
    """
        设备上下架信息表
    """
    machine = ForeignKeyField(column_name='machine_id', field='machine_id', model=MachineInfos)
    up_or_down = IntegerField()
    operator = CharField(null=True)
    date = DateField(null=True)
    reason = CharField(null=True)
    comments = CharField(null=True)

    class Meta:
        table_name = 'shelf_manage'


class ViewCheckCmd(BaseModel):
    """
        设备巡检命令视图
    """
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    hostname = CharField(null=True)
    ip = CharField()
    user = CharField(null=True)
    password = CharField(null=True)
    cmd_id = IntegerField()
    cmd = CharField(null=True)
    cmd_name = CharField(null=True)
    machine_id = IntegerField(null=True)

    class Meta:
        table_name = 'view_check_cmd'
        primary_key = False


class ViewDownshelf(BaseModel):
    """
        设备下架信息视图
    """
    comments = CharField(null=True)
    date = DateField(null=True)
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_admin = CharField(null=True)
    machine_factory = CharField(null=True)
    machine_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_name = CharField(null=True)
    machine_sn = CharField(null=True)
    machine_sort_name = CharField(null=True)
    mg_ip = CharField(null=True)
    model = CharField(null=True)
    operator = CharField(null=True)
    postion = CharField(null=True)

    class Meta:
        table_name = 'view_downshelf'
        primary_key = False


class ViewUpshelf(BaseModel):
    """
        设备上架信息视图
    """
    comments = CharField(null=True)
    date = DateField(null=True)
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_admin = CharField(null=True)
    machine_factory = CharField(null=True)
    machine_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_name = CharField(null=True)
    machine_sn = CharField(null=True)
    machine_sort_name = CharField(null=True)
    mg_ip = CharField(null=True)
    model = CharField(null=True)
    operator = CharField(null=True)
    postion = CharField(null=True)

    class Meta:
        table_name = 'view_upshelf'
        primary_key = False

