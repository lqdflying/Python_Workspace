# -*- coding: utf-8 -*-
'''
Created on 2017年7月7日

@author: liuqd
'''

import copy

#name = "ZhangYang"
names = ["LiuQuandong","LiuMing",["name1","name2"],"WuHongwei"]
print("取一个值：",names[0]) #0代表第一个位置和数据
print("取连续多个值1：",names[0:2]) #[0:2]，顾头不顾尾，取头值不取尾值，
print("取连续多个值2：",names[:2]) #[0:2]，的话，可以把前边的0也省略掉
#这个动作就叫切片
print("取最后一个值1：",names[-1])
print("倒序取多个值1：",names[-1:-3])  #这种写法会取不到值
print("倒序取多个值2：",names[-3:-1])  #这种写法才是正确的
print("倒序取多个值3：",names[-2:])  #想倒着取最红就一个值，并且顾头不顾尾的解释情况下，最后不要写-0，而是省略即可

name_append = names.append("append")
names.insert(1, "insert before 1")  #【注】：一次只能插入一个值，不能批量插入
print("在第一个值之前插入一个新值：",names)
name_copy = names.copy()
name_deepcopy = copy.deepcopy(names)
print("复制数组：",name_copy)
names[2] = "中午"   #copy传递后不会的数组不会同时修订，会保持不变
names[3][0] = "子组改名"  #我们发现，子数组change值后，之前的copy传递后的数组会同时进行修订
name_copy[3][1] = "copy后的数组中改子数组"

'''
以上这种copy是“浅copy”，也就是只copy第一层，如果还有下一层，那么会做指针引用

'''

print("数组修改值:",names)
print("复制数组again：",name_copy)
print("深copy，子数组不会跟着变化：",name_deepcopy)

