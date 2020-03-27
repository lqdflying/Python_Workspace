# -*- coding: utf-8 -*-
'''
Created on 2018年3月29日

@author: anddy.liu
'''
import configparser
config = configparser.ConfigParser()
#第一种写法
# config["DEFAULT"] = {'ServerAliveInterval': '45',
# 'Compression': 'yes',
# 'CompressionLevel': '9'}
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# topsecret = config['topsecret.server.com']
# topsecret['Host Port'] = '50022' # mutates the parser
# topsecret['ForwardX11'] = 'no' # same here
# config['DEFAULT']['ForwardX11'] = 'yes'
# #第二种写法
# config.add_section("section1")
# config.set("section1", "name", "jhao104")    # 修改指定section 的option
# config.set("section1", "age", "21")       # 增加指定section 的option
# config.add_section("section3")         # 增加section
# config.set("section3", "site", "oschina.net")  # 给新增的section 写入option
# with open('example.ini', 'w') as configfile:
#     config.write(configfile)
# with open("example.ini","r",encoding = "utf-8") as example:
#     config.read(example)
#     print(config.sections())
# config.read("example.ini")
# print("得到所有的section，并且以列表的形式返回：\n",config.sections())
# print("得到该section的所有option，同时还会额外包含DEFAULT的option，：\n",config.options("section1"))
# print("得到该section的所有键值对，同时还会额外包含DEFAULT的键值对：\n",config.items("section1"))
# print("得到section中option的值，返回为string类型：\n",config.get("section1","name"))
# print("得到section中option的值，返回为int类型：\n",config.getint("section1","age"))
# print("得到section中option的值，返回为float类型：\n",config.getfloat("section1","age"))
# print("得到section中option的值，返回为float类型：\n",config.getboolean("section1","good"))
#使用RawConfigParser新建一个裸的config文件
rawconfig = configparser.RawConfigParser()
rawconfig["name"] = {}
rawconfig["name"]["url"] = "http://%(host)s:%(port)s/Portal"
rawconfig["name"]["host"] = "localhost"
rawconfig["name"]["port"] = "8080"
with open("config.ini","w",encoding = "utf-8") as configfile:
    rawconfig.write(configfile)
#使用ConfigParser来演示通配符配置文件的使用
config.read("config.ini", encoding = 'utf-8')
print("发现通配符已经替换了：\n",config.get("name","url"))
config.set("name","display","I will display this :%(host)s:%(port)s")
print("新增一个option，也是可以使用通配符:\n",config.get("name","display"))

#使用SafeConfigParser来演示通配符配置文件的使用,发现和ConfigParser一样
configsafe = configparser.SafeConfigParser()
configsafe.read("config.ini", encoding = 'utf-8')
print("发现通配符已经替换了：\n",configsafe.get("name","url"))
configsafe.set("name","display","I will display this :%(host)s:%(port)s")
print("新增一个option，也是可以使用通配符:\n",configsafe.get("name","display"))