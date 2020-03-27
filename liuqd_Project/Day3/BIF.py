# -*- coding: utf-8 -*-
'''
Created on 2017年7月17日

@author: anddy.liu
'''
#import functools
'''
print(abs(-5)) #答案是5

print(all([1,2,3])) #答案是True
print(all([-1,2,3])) #答案是True
print(all([0,2,3])) #答案是False

print(any([]))#答案是False
print(any([1,0,3])) #答案是True
print(any([1,2])) #答案是True

print(hex(60)) #把十进制转十六进制,结果是0x3c
print(oct(60)) #把十进制转十六进制，结果是0o74
print(bin(60)) #把十进制转十六进制，结果是0b111100

print(callable(abs))

print(chr(98))  #返回数字代表的ASCII
print(ord("b")) #返回ASCII对应的数字

'''
# code = '''
# info = {
#     'stu1101': "TengLan Wu",
#     'stu1102': "LongZe Luola",
#     'stu1103': "XiaoZe Maliya",
# }
# 
# 
# for i in info:
#     print(i)
# '''
# py_obj = compile(code,"err.log","exec")  #编译code为可执行可执行模块
# 
# print(py_obj)
# 
# exec(py_obj)
'''
a = [1,2,3,4]

print(dir())

print(dir(a))


print(divmod(5, 2))

s = "1+2+3"
print(s,type(s))
print(eval(s))


res = filter(lambda n:n > 5,range(10))
for i in res:
    print(i)

res = map(lambda n:n*2,range(10) )
for i in res:
    print(i)


res = functools.reduce(lambda n,m:n+m,range(10) )
print(res)

print(globals())  #返回当前全局变量的字典


res = reversed([2,3,4,5])
for i in res:
    print(i)


a = {6:2,8:0,1:4,15:6,99:11,4:22}
print(a,type(a))
print("sorted(a):",sorted(a)) #只展示了key
print("sorted(a.items()):",sorted(a.items())) #这句字典转列表（列表里是2值元组），并且按照key来排序
print("按照值来排序：sorted(a.items()):",sorted(a.items(),key = lambda x:x[1])) #这句字典转列表（列表里是2值元组），并且按照key来排序
'''
a = [1,2,3,4]
b = ["liuqd","liuquan","laowang"]



for i in zip(a,b):
    print(i)

