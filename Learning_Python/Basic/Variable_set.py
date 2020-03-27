# -*- coding: utf-8 -*-
'''
Created on 2017年8月16日

@author: anddy.liu
'''
list3 = {1:2,3:4}
list4 = ("liuquandong","liuming")


print(list3,type(list3))
print(list4,type(list4))

print("\n以上都没用，看下边")
print("看有用的".center(50,"+"))

list1 = [1,4,5,6,7,8,4]
list2 = set(list1)  #数组（list）转set
other_list2 = set([1,2,55,66,4])   #直接创建set


sub_list2 = set([1,4])
print(list1,type(list1))
print("集合：\n",list2,"\n它的数据类型是：",type(list2))  #会发现set自动去重了
print("取交集的效果：\n",list2.intersection(other_list2))  #intersection这个方法用来取交集，必须要同时存在于list2和other_list2的才算
print("取并集的效果：\n",list2.union(other_list2)) #union这个方法是取并集的，就是最大集，只要存在于list2或other_list2中的就都算
print("取差集的效果二：\n",other_list2.difference(list2))  #difference这个方法是取差集的，差集就是只在other_list2里有，不存在于list2里的部分
print("判断某个集合是否是另一个集合的子集：\n",list2.issubset(other_list2))
print("无耻的分割线".center(50,"+"))

print("判断某个集合是否是另一个集合的子集：\n",sub_list2.issubset(list2)) #判断sub_list2是不是list2的子集
print("判断某个集合是否是另一个集合的父集： \n",list2.issuperset(sub_list2))  #判断list2是不是sub_list2的父集

print("取差集的效果一：\n",list2.difference(other_list2))  #difference这个方法是取差集的，差集就是只在list2里有，不存在于other_list2里的部分
print("取交集的效果：\n",list2.intersection(other_list2))  #intersection这个方法用来取交集，必须要同时存在于list2和other_list2的才算
print("对称差集的效果一：\n",list2.symmetric_difference(other_list2))  
#symmetric_difference这个方法是对称差集，所谓对称差集就是首先取得交集，然后取得并集，最后从并集中去掉交集以后得到的部分

print("验证两个集合直接是不是没有交集，是的返回true，不是（也就是证明有交集）则返回false： \n",list2.isdisjoint(other_list2))

print("第二道无耻的分割线，下边讲数字操作符方法".center(50,"+"))
print("\n")

print("数字操作符取交集的效果：\n",list2 & other_list2)  #intersection这个方法用来取交集，必须要同时存在于list2和other_list2的才算
print("数字操作符取并集的效果：\n",list2 | other_list2) #union这个方法是取并集的，就是最大集，只要存在于list2或other_list2中的就都算
print("数字操作符取差集的效果二：\n",other_list2 - list2)  #difference这个方法是取差集的，差集就是只在other_list2里有，不存在于list2里的部分
print("数字操作符取对称差集的效果一：\n",list2 ^ other_list2)

print("第三道无耻的分割线，下边讲集合的增删改查".center(50,"+"))
print("\n")

setname = set([1,2,3,4,6])

#print(setname,type(setname))

setname.add(7)

setname.remove(1)
setname.pop()
print(setname,len(setname),"\n in被用作判断某个原始是否在集合里，如果是，就反馈True：\n",4 in setname)