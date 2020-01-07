# -*- coding: utf-8 -*-
'''
Created on 2018年3月4日

@author: anddy.liu
'''
import zipfile
# x=zipfile.ZipFile('test1.zip',mode='w')
# x.write('os_module.py')
# x.write('tesliuqdtest')
# x.close()
   
# with zipfile.ZipFile('test1.zip',mode='w') as y:
#     y.write('sys_module.py')
# with zipfile.ZipFile('test1.zip') as z:
#     print(z.read('sys_module.py').decode('utf-8'))
with zipfile.ZipFile('copy.zip') as x:
    info=x.getinfo('lqdfile')
    print('获取文件名称：',info.filename)
    print('压缩类型：',info.compress_type)
    print('获取创建该zip文档的系统：',info.create_system)