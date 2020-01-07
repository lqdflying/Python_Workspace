# -*- coding: utf-8 -*-
'''
Created on 2017年8月10日

@author: anddy.liu
'''
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
print(names)

print("取一个值：",names[0]) #0代表第一个位置和数据
print("取连续多个值1：",names[0:2]) #[0:2]，顾头不顾尾，取头值不取尾值，
print("取连续多个值2：",names[:2]) #[0:2]，的话，可以把前边的0也省略掉
#这个动作就叫切片
print("取最后一个值1：",names[-1])
print("倒序取多个值1：",names[-1:-3])  #这种写法会取不到值
print("倒序取多个值2：",names[-3:-1])  #这种写法才是正确的
print("倒序取多个值3：",names[-2:])  #想倒着取最后就一个值，并且顾头不顾尾的解释情况下，最后不要写-0，而是省略即可

product = [['usr1', 3000], ['usr2', 4000], ['usr4', 300], ['china1', 500], ['uar90', 90]]
print("第一种打印子数组第一列的方法：")
for m in product:
    print(m[0])

print("第二种打印子数组第一列的方法：")    
for m,n in product:
    print(m)

print(product.index(['usr2', 4000]))  #打印数组下标,也就是索引index编号
print("追加，插入，修改的操作".center(40,"+"))
names.append("append") #追加
print("追加操作：",names)
names.insert(1, "insert before 1")  #【注】：一次只能插入一个值，不能批量插入
print("在第一个值之前插入一个新值：",names)
names[2] = "chenwenxia"
print("修改值：",names)

print("删除操作".center(40,"+"))
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
del names[1] #删除序号为1的元素
names.remove("name2")#选择删除名字为name2的元素
names.pop() #删除列表最后一个值 
print("打印删除后的列表",names)

print("列表的拼接、拷贝和截取".center(40,"+"))
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
other = [1,2,3]
names = names + other
print("拼接方法一：",names)
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
other = [1,2,3]
names.extend(other)
print("拼接方法二：",names)
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
names = names*2
print("成倍复制方法：",names)
names = ["LiuQuandong","LiuMing","name2","liuqd2","WuHongwei",32]
names = names*2
print("成倍复制方法：",names)
names = [['usr1', 3000], ['usr2', 4000], ['usr4', 300], ['china1', 500], ['uar90', 90]]
import copy
name_copy = names.copy()
name_deepcopy = copy.deepcopy(names)
names[2] = "中午"   #copy传递后原数组改变后，copy的数组不会同时修订，会保持不变
names[3][0] = "子组改名"  #我们发现，子数组change值后，之前的copy传递后的数组会同时进行修订
print("原列表修改后的结果：",names)
print("浅copy：",name_copy)
print("深copy：",name_deepcopy)

print("统计、翻转和获取下标".center(40,"+"))
names = ["LiuQuandong","chenwenxia","name2","justsoso","WuHongwei"]
print("统计列表中元素的数量",names.count("name2"))
print("统计列表中元素的数量",len(names))
names.sort() #排序,sort does not return anything. So, if we try to assign names.sort() to a variable, our new variable would be None
print("排序后的列表",names)
names_for_sort = sorted(names)
'''
sorted is different from .sort() in several ways:
It comes before a list, instead of after.
It generates a new list.
'''
print("新生成的排序列表", names_for_sort)
names.reverse()# 翻转
print("翻转后的列表",names)
print("展示justsoso的下标",names.index("justsoso")) #【注】：第一个元素是0，因此第二个元素的下标是1

