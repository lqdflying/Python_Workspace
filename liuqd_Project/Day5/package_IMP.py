# -*- coding: utf-8 -*-
'''
Created on 2017年7月25日

@author: anddy.liu
'''
'''
import module1 #倒入一个package,导入package的本质就是在解释下边的__init.py__文件  # @UnresolvedImport  # @UnusedImport
#【注】：能这样导入的原因是，package_IMP文件在module1这个package的同级目录下，所以才能识别到
module1.liuqd_mode.say_hello()
module1.liuqd_mode.liuqd_print()
'''

from module1 import liuqd_mode  # @UnresolvedImport
#liuqd_mode.say_hello()
#from liuqd_mode import say_hello
hello_say = liuqd_mode.say_hello

'''
如果只是import module1，就必须在init.py文件里写上“from . import liuqd_mode,mode2”
如果不想在init.py里写东西，就像这样from …… import ……来用即可
'''
hello_say()
hello_say()
hello_say()