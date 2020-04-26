# -*- coding:utf-8 -*-
###
# File: class_new_feature.py
# Created Date: 2020-04-25
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Sunday April 26th 2020 11:36:08 am
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from dataclasses import dataclass, asdict, field

#传统类的定义方法
class first_old:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f'first_old{{name: {self.name}, age: {self.age}}}'
        

#使用了dataclasses的类定义的方法
@dataclass
class first_new:
    name: str
    age: int

@dataclass
class first_third:
    name: str = 'noname'
    age: int = 0

@dataclass(frozen = True)
class first_four:
    name: str = 'noname'
    age: int = 0

@dataclass
class first_five:
    name: str = 'noname'
    age: int = 0
    school: str = field(default='little school')

@dataclass
class first_six:
    name: str = 'noname'
    age: int = 0
    lesson: list = field(default_factory=list)


p1 = first_old('liuqd', 23)
p2 = first_new('liuqd', 23)
p3 = first_third()
p3.school = "good"
p4 = first_four()
# p4.school = "good" #这里去附变量会报错,提示dataclasses.FrozenInstanceError: cannot assign to field 'school'
p5 = first_five('liuqd', 23)
p6 = first_six('liuqd', 23, ['class1', 'class2', 'class3'])
p7 = first_six()

print(p1)
print(p2)
print(p3)
print(p3.school)
print(asdict(p3))
print(p5)
print(p6)
print(p6.lesson)
print(p7.lesson)