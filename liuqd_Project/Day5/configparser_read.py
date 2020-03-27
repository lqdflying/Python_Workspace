# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import configparser
conf = configparser.ConfigParser()
conf.read("example.ini")
print(type(conf.defaults()))
print(conf.defaults())
print(conf.sections())
print(conf["bitbucket.org"]["user"])