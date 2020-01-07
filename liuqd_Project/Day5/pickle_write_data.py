# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

@author: anddy.liu
'''
import pickle

info = {
    "name":"liuqd",
    "age":"23"
    }

my = {
    "name":"quandong",
    "age":"55"
    }

print("[两种]正确的pickle序列化方法".center(50,"+"))
with open("liuqd.pickle","wb") as file:
    file.write(pickle.dumps(my))


#    file.write(pickle.dumps(info))  #注意，这是错误的写法，json或pickle都没有办法像str文件数据流那样追加，否则json会报错，其实有多余的数据
#而pickle则不会报错，但是只能读到第一份数据。json或pickle进行数据的追加只能：读出旧数据→ 合并→ 重新写入新数据
#【注】：pickle进行序列化，存入的文件不是str格式的，要以二进制形式打开并写入文件

with open("liuqd1.pickle","wb") as file1:
    pickle.dump(my,file1)