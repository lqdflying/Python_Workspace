# -*- coding: utf-8 -*-
'''
Created on 2018年3月11日

@author: anddy.liu
'''
import configparser
config = configparser.ConfigParser()
config.read("example.ini")
print(config.sections())