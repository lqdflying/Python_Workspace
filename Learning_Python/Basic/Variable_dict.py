# -*- coding: utf-8 -*-
'''
Created on 2017年8月11日

@author: anddy.liu
'''
info = {
    "stu1101": "TengLan Wu",
    "stu1102": "LongZe Luola",
    "stu1103": "XiaoZe Maliya",
}
print(type(info))
print(info)
print(info["stu1101"])  #注意，这里要加引号
print(info.get("dsf"))  #注意，这里要加引号
#使用get函数来获取一个值和直接使用[]来获取一个值的不同点在于，加入这个key不存在，[]方法会报错，而get方法会返回none
#字典值增加
info["other"] = 32
#字典值修改
info["stu1101"] = "change the value"
#字典值删除
info.pop("stu1103") #删除方法一
del info["stu1102"] #删除方法二
print("增删改后的字典最终形态",info)
print("查找一个key是否存在",("other" in info))

print("赋值在构建多级dict中的用法")
rdata = {'name': 'SDKT_SDKTAP3_7.68.213'}
# lastref = rdata.copy() #使用了copy()等同于是新创建一个dict,这时候不会和原dict联动
lastref = rdata
lastref['config'] = {}
lastref = lastref['config']
lastref['cpuhotaddenabled'] = False
print("dict没有浅copy,赋值效果就是浅copy:\n",rdata)
print("lastref实际上是指向rdata['config']的这个value的指针,它本身是也是一个dict,并且会导致rdata这个dict同步更新\n",lastref)