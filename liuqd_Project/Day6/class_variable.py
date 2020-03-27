# -*- coding: utf-8 -*-
'''
Created on 2017年8月30日

@author: anddy.liu
'''
class persion:
    cn = "中国" #也可以在def __init__里定义默认函数来实现cn = "中国",但写成类变量只在内存中存一份， 写成构造函数里的默认变量那么实例有多少，就占多少份内存
    def __init__(self,name,age,addr):
        self.name = name
        self.age = age
        self.__addr = addr #这里就变成一个私有属性，外界无法访问到
    def __showall(self):
        pass
    def show(self):
        print(("姓名:%s"%self.name).center(30,"+"),"\n国籍:",self.cn)
    def othershow(self):
        print(("姓名:%s"%self.name).center(30,"+"),"\n年龄:",self.age)    
    def showaddr(self):
        print(("姓名:%s"%self.name).center(30,"+"),"\n地址:",self.__addr)
    def __del__(self):#这是一个析构函数,实例释放或销毁的时候自动执行：一定是最后实行
        print("%s game over"%self.name)

p1 = persion("liuqd",32,"tianjin")
p1.show()
p1.othershow()
#print(p1.__addr) #打印会失败，因为__addr是私有属性，外界不能访问，被隐藏了
del p1
p2 = persion("chenwx",32,"tianjin")
p2.show()
p2.othershow()
p2.showaddr() #想访问私有变量，只能构建一个函数，通过访问函数的方式去访问私有变量