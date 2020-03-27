# -*- coding: utf-8 -*-
'''
Created on 2017年8月30日

@author: anddy.liu
'''
#这些类的定义方法都是叫做经典类
class people:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def eat(self):
        print("%s 会吃东西"%self.name)
    def sleep(self):
        print("%s 需要睡觉"%self.name)

class man(people): #这就是子类，就继承了
    def talk(self): #子类可以有自己的方法
        print("%s 正在说话"%self.name)
    def sleep(self):
        people.sleep(self)
        print("子类为同名父类方法新增功能")

class woman(people):
    def shopping(self):
        print("%s 正在购物，女性特有"%self.name)

class other(people): #这个子类要传新的参数进来
    def __init__(self,name,age,addr): #这里一定要把父类的参数都得写一遍
        people.__init__(self, name, age) #写着是为了把父类的参数传进来
        self.addr = addr
    def other(self):
        print("子类传新参数了就是地址：%s"%self.addr)

class forother(people): #这个子类要传新的参数进来
    def __init__(self,name,age,addr): #这里一定要把父类的参数都得写一遍
        super(forother,self).__init__(name, age) #这里演示的是另一种方法来把父参数传进来，就使用内置的super函数，好处是不用写多个people
        self.addr = addr
    def other(self):
        print("子类传新参数了就是地址：%s"%self.addr)

m1 = man("liuqd",32)
m1.eat() #子类继承了父类的对象
m1.talk() #子类可以有自己的对象
m1.sleep() #子类可以重构父类的对象

w1 = woman("chenwx",33)
w1.shopping()


o1 = other("liu",32,"tianjin") #子类添加新的参数
o1.sleep() #父类的方法依然可以用
o1.other()