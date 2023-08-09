import configparser
from pathlib import Path
from peewee import *
from playhouse.shortcuts import ReconnectMixin
import logging

# 定义日志格式
logging.basicConfig(level=logging.WARN, format='%(asctime)s %(levelname)s %(message)s', filename='machine-sys.log')

cf = configparser.ConfigParser(allow_no_value=True)
base_file = Path(__file__).parent  # 获取文件的绝对路径
cf.read(base_file / 'db.ini')  # 动态读取ini文件
host = cf.get('db', 'host')
password = cf.get('db', 'password')
user = cf.get('db', 'user')
db_name = cf.get('db', 'database')
port = cf.getint('db', 'port')
charset = cf.get('db', 'charset')

db_config = {'host': host, 'user': user, 'password': password, 'port': port, 'database': db_name, 'charset': charset}


# db = MySQLDatabase(db, **db_config)


# 同步数据库断线重连类
class ReconnectMySQLDatabase(ReconnectMixin, MySQLDatabase):
    pass


# 数据库实例
db = ReconnectMySQLDatabase(**db_config)


class UnknownField(object):
    def __init__(self, *_, **__): pass


class BaseModel(Model):
    class Meta:
        database = db


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
    asset_id = CharField(null=True)  # 资产编号
    system_name = CharField(null=True)  # 业务系统

    class Meta:
        table_name = 'machine_infos'


class MachineCheckUser(BaseModel):
    """
        巡检用户信息表
    """
    user = CharField(null=True)
    password = CharField(null=True)
    cmd_id = IntegerField(null=True)
    comment = CharField(null=True)
    machine = ForeignKeyField(column_name='machine_id', field='machine_id', model=MachineInfos)

    class Meta:
        table_name = 'machine_check_user'


class MachineList(BaseModel):
    """
    设备信息视图表
    """
    machine_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    room_id = IntegerField(null=True)
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
    bmc_ip = CharField(null=True)
    machine_admin = CharField(null=True)
    comments = CharField(null=True)
    run_state = CharField(null=True)

    class Meta:
        table_name = 'machine_list'
        primary_key = False


class MachinePassword(BaseModel):
    pid = AutoField()
    machine_name = CharField(null=True)
    ip = CharField()
    sn = CharField(null=True)
    room = CharField(null=True)
    user = CharField()
    password = CharField()
    machine_type = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_id = IntegerField(null=True)
    remark = CharField(null=True)

    class Meta:
        table_name = 'machine_password'


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
    cmd = CharField(null=True)
    cmd_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    cmd_name = CharField(null=True)
    hostname = CharField(null=True)
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    ip = CharField(null=True)
    machine_id = IntegerField()
    password = CharField(null=True)
    user = CharField(null=True)

    class Meta:
        table_name = 'view_check_cmd'
        primary_key = False


class ViewDownshelf(BaseModel):
    """
        设备下架信息视图
    """
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_name = CharField(null=True)
    postion = CharField(null=True)
    machine_sort_name = CharField(null=True)
    model = CharField(null=True)
    machine_factory = CharField(null=True)
    machine_sn = CharField(null=True)
    mg_ip = CharField(null=True)
    date = DateField(null=True)
    operator = CharField(null=True)
    machine_admin = CharField(null=True)
    comments = CharField(null=True)

    class Meta:
        table_name = 'view_downshelf'
        primary_key = False


class ViewUpshelf(BaseModel):
    """
        设备上架信息视图
    """
    id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    machine_name = CharField(null=True)
    postion = CharField(null=True)
    machine_sort_name = CharField(null=True)
    model = CharField(null=True)
    machine_factory = CharField(null=True)
    machine_sn = CharField(null=True)
    mg_ip = CharField(null=True)
    date = DateField(null=True)
    operator = CharField(null=True)
    machine_admin = CharField(null=True)
    comments = CharField(null=True)

    class Meta:
        table_name = 'view_upshelf'
        primary_key = False


class ViewWarranty(BaseModel):
    """
    维保信息查询视图
    """
    bmc_ip = CharField(null=True)
    cabinet_name = CharField(null=True)
    comment = CharField(null=True)
    end_date = DateField(null=True)
    how_long = IntegerField(null=True)
    is_under = CharField(null=True)
    machine_id = IntegerField()
    machine_name = CharField(null=True)
    mg_ip = CharField(null=True)
    machine_sn = CharField(null=True)
    room_name = CharField()
    start_date = DateField(null=True)
    start_position = IntegerField(null=True)
    w_id = IntegerField(constraints=[SQL("DEFAULT 0")])
    w_type = CharField(null=True)
    run_state = CharField(null=True)

    class Meta:
        table_name = 'view_warranty'
        primary_key = False


class WarrantyInfos(BaseModel):
    """
    维保信息表
    """
    comment = CharField(null=True)
    end_date = DateField(null=True)
    how_long = IntegerField(null=True)
    is_under = IntegerField(null=True)
    machine = ForeignKeyField(column_name='machine_id', field='machine_id', model=MachineInfos)
    start_date = DateField(null=True)
    w_type = IntegerField(null=True)
    w_id = AutoField()

    class Meta:
        table_name = 'warranty_infos'
