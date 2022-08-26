# coding:utf-8
#!/usr/bin/env python

import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible.errors import AnsibleError
import ansible.constants as C

class ResultCallback(CallbackBase):
    """结果回调"""
    def __init__(self, *args, **kwargs):
        super(ResultCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}
        self.ret = {
            'host_ok': '',
            'host_unreachable': '',
            'host_failed': ''
        }

    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result
        self.ret['host_unreachable'] = {result._host.name: result._result}

    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.host_ok[result._host.get_name()] = result
        self.ret['host_ok'] = {result._host.name: result._result}

    def v2_runner_on_failed(self, result, *args, **kwargs):
        self.host_failed[result._host.get_name()] = result
        self.ret['host_failed'] = {result._host.name: result._result}



class AnsibleApi():
    def __init__(self, sources='conf/ansible/hosts', name="ansible Play",hosts=None,actions=None):
        '''
        创建参数，为保证每个参数都被设置，ansible使用可命名元组
        '''
        self.Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
        self.options = self.Options(connection='ssh', module_path=['/to/mymodules'], forks=30, become=None, become_method=None, become_user=None, check=False, diff=False)

        '''初始化loader类'''
        self.loader = DataLoader()  # 用于读取与解析yaml和json文件
        self.passwords = dict(vault_pass='secret')

        '''初始化结果回调方法，用于接收返回的结果'''
        self.results_callback = ResultCallback()

        '''指定inventory，即我们的ansible hosts文件，使用路径指定一个host文件，或者一个逗号分割host的字符串'''
        self.inventory = InventoryManager(loader=self.loader, sources=sources)

        '''合并所有不同的资源成一个统一的变量管理视图，这些由变量管理器完成'''
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        '''play_source 创建我们任务的数据结构，tasks里面就是我们定义的yaml文件所做的步骤'''

        if actions == None:
            print("no actions")
            raise AnsibleError
        if hosts == None:
            print( "no hosts" )
            raise AnsibleError
        self.play_source = dict(
            name=name,
            hosts=hosts,
            gather_facts='no',
            tasks=actions,
                #dict(action=dict(module='shell', args='ls'), register='shell_out'),
                #dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
        )

    def _run_task(self):
        '''run task'''
        play = Play().load(self.play_source, variable_manager=self.variable_manager, loader=self.loader)
        tqm = None
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
                passwords=self.passwords,
                stdout_callback=self.results_callback,
                # Use our custom callback instead of the ``default`` callback plugin, which prints to stdout
            )
            result = tqm.run(play)  # most interesting data for a play is actually sent to the callback's methods
        finally:
            # we always need to cleanup child procs and the structres we use to communicate with them
            if tqm is not None:
                tqm.cleanup()

            # Remove ansible tmpdir
            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)


if __name__ == '__main__':
    '''
    使用举例, ip：,号分割
    '''
    ip = 'localhost,'
    test_key = "key1\n \
                key2"

    actions = [
        dict(action=dict(module='shell', args='ls', register='shell_out')),
        dict(action=dict(module='authorized_key', args='user=brick key="%s"' % test_key))
    ]
    ansible_actions = AnsibleApi(sources='../conf/ansible/hosts', name="ansible test", hosts=ip, actions=actions)
    ansible_actions._run_task()