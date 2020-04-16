# -*- coding: utf-8 -*-
'''
Created on 2017年10月23日

@author: anddy.liu
'''
from collections.abc import Iterable
from collections.abc import Iterator
#查看字符串是否是迭代器或可迭代对象
var_string="name"
print(var_string,isinstance(var_string,Iterable)) #是可迭代对象
print(var_string,isinstance(var_string,Iterator)) #不是迭代器对象
print(dir(var_string))
#查看数字是否是迭代器或可迭代对象
var_num=123
print(var_num,isinstance(var_num,Iterable)) #不是是可迭代对象
print(var_num,isinstance(var_num,Iterator)) #不是迭代器对象
#查看列表是否是迭代器或可迭代对象
var_list=["liu",123,"nage"]
print(var_list,isinstance(var_list,Iterable)) #是可迭代对象
print(var_list,isinstance(var_list,Iterator)) #不是迭代器对象
#查看字典是否是迭代器或可迭代对象
var_dict={"name":"liuqd","age":23}
print(var_dict,isinstance(var_dict,Iterable)) #是可迭代对象
print(var_dict,isinstance(var_dict,Iterator)) #不是迭代器对象
#查看生成器是否是迭代器或可迭代对象
var_generator=(x for x in range(10))
print(var_generator,isinstance(var_generator,Iterable)) #是可迭代对象
print(var_generator,isinstance(var_generator,Iterator)) #是迭代器对象

#改造str、list、dict为迭代器对象
var_string_iterator=iter(var_string)
var_list_iterator=iter(var_list)
var_dict_iterator=iter(var_dict)
print(var_string_iterator,isinstance(var_string_iterator,Iterator)) #将str对象改造为迭代器对象
print(var_list_iterator,isinstance(var_list_iterator,Iterator)) #将list对象改造为迭代器对象
print(var_dict_iterator,isinstance(var_dict_iterator,Iterator)) #将dict对象改造为迭代器对象


