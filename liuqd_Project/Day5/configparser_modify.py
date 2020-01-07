# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import configparser
conf = configparser.ConfigParser()
conf.read("example.ini")

conf.remove_section("bitbucket.org")
with open("example1.ini","w") as file1:
    conf.write(file1)
with open("example.ini","w") as file2:
    conf.write(file2)