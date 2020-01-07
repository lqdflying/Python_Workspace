# -*- coding: utf-8 -*-
'''
Created on 2017年7月8日

@author: anddy.liu
'''

'''
for i in info.keys():
    print(i)
#只打印字典key，并且还是分行打印的办法
发现这种写法毫无意义
'''
info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}


for i in info:
    print(i)
    
#只打印key，这样写就行了
'''
for i in info:
    print(i,info[i])

print("\n")
 
for m,n in info.items():  #虽然结果一样，但这种方式不高效，实际情况会有性能问题，因为item有一个把字典转数组的过程，这个过程耗费资源
    print(m,n)
'''