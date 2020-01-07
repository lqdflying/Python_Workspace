# -*- coding: utf-8 -*-
'''
Created on 2017年7月8日

@author: anddy.liu
'''
#names = ["LiuQuandong","LiuMing","name2",["liuqd1","liuqd2"],"WuHongwei"] #我发现这样的写法报错

names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei"] #这样才可以正确的打印成功，这说明，join的方法不适用于拥有子数组的数组
print("第一种合并方法：","+-+-+".join(names))

join_name = "+-+-+".join(names)

print("第一种拆分方法",join_name.split(sep="+-+-+"))
print("第二种拆分方法",join_name.split(sep="+-+-+", maxsplit=8))  #maxsplit表示拆分几次，如果其数值大于实际的最大拆分可能性，那么他的效果和忽略此参数类似
print("第三种拆分方法",join_name.split(sep="+-+-+", maxsplit=2))  #这里代表拆分两次