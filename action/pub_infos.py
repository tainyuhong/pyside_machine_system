from db.db_orm import *


class PubSwitch:
    """
    通过get_room方法从数据库中获取机房信息生成字典
    使用room_swap_id方法实现机房名称与机房ID自由转换
    """
    def __init__(self):
        self.cabinet_and_roomid = None
        self.room_and_id = None

    # 获取机房信息
    def get_room(self):
        """
        获取数据库中机房信息显示至机房下拉菜单中
        :return: 机房ID与机房名称的映射字典
        """
        room_data = MachineRoom.select(MachineRoom.room_name, MachineRoom.room_id)  # 查询父类不为空的分类
        # 将机房信息取出作为公共变量
        self.room_and_id = {}  # 定义一个机房ID与机房名称的映射字典
        # 生成机房ID与机房名称的映射字典
        for i in room_data:
            self.room_and_id[i.room_id] = i.room_name
        # print('机房信息字典',self.room_and_id)
        return self.room_and_id

    # 机房名与id互转
    def room_swap_id(self,name=None, room_id=None):
        """
        通过将传入的机房名或机房id转换为对应的id或机房名
        :param name: 机房名称
        :param room_id: 机房ID
        :return: 机房名或机房id
        """
        # 生成字典与机房Id的映射
        room_id_dict = dict(map(reversed, self.room_and_id.items()))
        # print('room_id_dict',room_id_dict)
        # print('名称-->机房ID',room_id_dict)    # {'ZB-1': 1, 'ZB-2': 2, 'ZB-3': 3, 'ZB-4': 4}
        # 如果传入机房名称为空，则返回id，如果传入的为id,则返回机房名称
        if name is None and room_id is not None:
            return self.room_and_id[room_id]
        elif room_id is None and name is not None:
            return room_id_dict[name]
        else:
            return '未传入name或room_id'

# 获取机柜信息
    def get_cabinet(self):
        """
        获取数据库中每个机房中机柜的信息按ID进行获取
        :return: 机房ID与机房名称的映射字典
        """
        cabinet_data = Cabinet.select(Cabinet.room_id,Cabinet.cab_num ).where(Cabinet.is_use==1).tuples()  # 查询父类不为空的分类
        # 将机房信息取出作为公共变量
        # self.cabinet_and_roomid = {}  # 定义一个机房ID与机房名称的映射字典
        # 生成机房ID与机房名称的映射字典
        for i in cabinet_data:
            print('机柜信息：',i)
            # self.cabinet_and_roomid[i.room_id] = i.room_name
        # print('机房信息字典',self.cabinet_and_roomid)
        # return self.cabinet_and_roomid

    # 机房名与id互转
    # def room_swap_id(self,name=None, room_id=None):
    #     """
    #     通过将传入的机房名或机房id转换为对应的id或机房名
    #     :param name: 机房名称
    #     :param room_id: 机房ID
    #     :return: 机房名或机房id
    #     """
    #     # 生成字典与机房Id的映射
    #     room_id_dict = dict(map(reversed, self.room_and_id.items()))
    #     # print('room_id_dict',room_id_dict)
    #     # print('名称-->机房ID',room_id_dict)    # {'ZB-1': 1, 'ZB-2': 2, 'ZB-3': 3, 'ZB-4': 4}
    #     # 如果传入机房名称为空，则返回id，如果传入的为id,则返回机房名称
    #     if name is None and room_id is not None:
    #         return self.room_and_id[room_id]
    #     elif room_id is None and name is not None:
    #         return room_id_dict[name]
    #     else:
    #         return '未传入name或room_id'


if __name__ == '__main__':
    data = PubSwitch()
    cabinet = data.get_cabinet()
    print(cabinet)
    # room_id = data.room_swap_id()
    # print('room_id',room_id)