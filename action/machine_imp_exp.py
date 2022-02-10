import os
import sys
import openpyxl
from PySide6 import QtWidgets, QtGui, QtCore
from ui.machine_import import *
from db.db_handler import *


class UiImport(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(UiImport, self).__init__(parent)
        self.setupUi(self)
        self.select_btn.clicked.connect(self.open_file)
        self.import_btn.clicked.connect(lambda :self.imp_file(self.path_le.text()))
        self.template_lb.linkActivated.connect(self.download_template)

    def open_file(self):
        # 创建文件选择框实例，并接收文件路径信息
        filename, filetype = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', os.getcwd(),
                                                                   'excel文件 (*.xlsx) ')
        print(filename)
        self.path_le.setText(filename)  # 将获取的选择的文件路径显示至文本框

    def imp_file(self,path):
        # 导入excel文件

        if path != '':
            _ = QtWidgets.QMessageBox.information(self, '设备信息导入', '是否需要导入设备信息！',
                                                  QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            if _ == QtWidgets.QMessageBox.Ok:
                print('路径',path)
                try:
                    wb = openpyxl.load_workbook(r'{}'.format(path))
                    print('path', path)
                    sh = wb.active
                except Exception as e:
                    QtWidgets.QMessageBox.critical(self,'导入失败', '错误：{}'.format(e))
                    logging.error(e)
                else:
                    # 定义导入SQL
                    import_sql = '''insert into machine_infos
                        (machine_id, machine_name, machine_sort_id, machine_sort_name, machine_sn, machine_factory, model,
                        machine_roomid, cabinet_id, cabinet_name, start_position, end_position, factory_date, end_ma_date,
                        work_are, run_state, redundancy_mode, machine_admin, app_admin, mg_ip, app_ip1, app_ip2, app_ip3,
                        app_ip4, bmc_ip, machine_use, issinglepower, install_date, uninstatll_date,comments)
                        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
                    rowdata = []
                    data = []
                    # num = 0
                    for row in range(2, sh.max_row + 1):
                        for col in range(1, sh.max_column + 1):
                            rowdata.append(sh.cell(row, col).value)  # 将单元格数据添加到行列表中
                        print(rowdata)
                        data.append(rowdata)
                        rowdata = []  # 置空列表添加新的行
                    print(data)
                    db = DBMysql()  # 创建数据库实例
                    num = db.alter_multi(import_sql, data)
                    print(num)
                    if num in (-1, 0):
                        # print('-->{}行记录需要导入，插入成功{}行记录，{} 行插入失败！！'.format(len(data), 0, len(data)))
                        QtWidgets.QMessageBox.information(self, '设备信息导入', '导入失败，未导入任何信息！')
                    else:
                        # print('-->{}行记录需要导入，插入成功{}行记录，{} 行插入失败！！'.format(len(data), num, len(data)-num))
                        QtWidgets.QMessageBox.information(self, '设备信息导入',
                                                          '{}条记录需要导入，插入成功 {} 行记录'.format(len(data), num))
            else:
                print('取消导入')
        else:
            QtWidgets.QMessageBox.warning(self, '设备信息导入', '请选择需要导入的文件！')

    def download_template(self):
        print('点击了模板下载')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    import_win = UiImport()
    import_win.show()
    sys.exit(app.exec())
