# -*- coding: utf-8 -*-
'''
Created on 2017年7月8日

@author: anddy.liu
'''
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}
print(type(info))
print(info)
print(info["stu1101"])  #注意，这里要加引号

info["stu1102"] = "meizi"
print("修改：\n",info)

info["stu1104"] = "laoge"

print("添加: \n",info)

print("查找一个存在的key对应的值，存在则返回对应的值：\n",info.get("stu1103"))  #查找要用get方法

print("查找一个不存在的key对应的值，不存在则返回false：\n",info.get("stu1108"))

print("查找一个key是否存在，存在则返回true：\n----->","stu1103" in info)
print("查找一个不存在的key对应的值，不存在则返回false：\n ----->","stu1108" in info)

del info["stu1101"]

print("删除一：\n",info)

info.pop("stu1102")

print("删除二：\n",info)
