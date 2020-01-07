# -*- coding: utf-8 -*-
'''
Created on 2018年3月20日

@author: anddy.liu
'''
import yaml
#以下操作是读取
with open("house.yml","r",encoding = "utf-8") as house:
    f = yaml.load(house)
    print("除非纯量，否则yaml对象其实是一个字典:",type(f))
    print(f)
#以下操作是新建
with open("project.yml","a",encoding = "utf-8") as project:
    content = {'house': {'family': {'name': 'Doe', 'parents': ['John', 'Jane']}, 'address': {'number': 34, 'street': 'Main Street'}}}
    yaml.dump(content,project)
