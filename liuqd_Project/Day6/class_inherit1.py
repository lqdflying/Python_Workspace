# -*- coding: utf-8 -*-
'''
Created on 2017年8月30日

@author: anddy.liu
'''
#讲一个新的类的定义方法就是新式类,经典类和新式类的区别主要是继承上
class people(object): #新式类的写法
    def __init__(self,name,age,colour):
        self.name = name
        self.age = age
        self.colour = colour
    def eat(self):
        print("%s 会吃东西,people"%self.name)
    def sleep(self):
        print("%s 需要睡觉"%self.name)

class learn(object):
    def __init__(self,name,age,sex): #这个父类多个函数，但是没鸟用
        self.name = name
        self.age = age
        self.sex = sex
    def java_learn(self):
        print("%s 正在学习java，这个是第二个类"%self.name)
    def teach(self,teacher):
        print("%s 正在跟着老师%s，学习知识"%(self.name,teacher.name))
        self.friend.append(teacher.name)
    def showsex(self):
        print(self.sex)
    def eat(self):
        print("%s 会吃东西,learn"%self.name)

class other(people): #这个子类要传新的参数进来
    def __init__(self,name,age,addr): #这里一定要把父类的参数都得写一遍
        people.__init__(self, name, age) #写着是为了把父类的参数传进来← 这是经典类的写法
        self.addr = addr
    def other(self):
        print("子类传新参数了就是地址：%s"%self.addr)


class forother(people): #这个子类要传新的参数进来
    def __init__(self,name,age,colour,addr): #这里一定要把父类的参数都得写一遍
        super(forother,self).__init__(name,age,colour) #这里演示的是另一种方法来把父参数传进来，就使用内置的super函数，← 这中写法是新式类的写法
        self.addr = addr
    def other(self):
        print("子类传新参数了就是地址：%s"%self.addr)
    def sleep(self):
        people.sleep(self)
        print("子类为同名父类方法新增功能")

class man(learn,people): #多继承
    def __init__(self,name,age,sex,colour,addr): #这里一定要把父类的参数都得写一遍
        super(man,self).__init__(name,age,sex) #这里演示的是另一种方法来把父参数传进来，就使用内置的super函数，← 这中写法是新式类的写法
        #learn.__init__(self, name, age, sex) #这样的写法可以传递不同父类的非共有属性
        people.__init__(self, name, age, colour)
        self.addr = addr
        self.friend = [] #构造函数的参数也不一定都是从外边传进去的，这里我就硬写一个空list也是可以的
    def other(self):
        print("子类传新参数了就是地址：%s"%self.addr)

o1 = man("liu",32,"F","black","tianjin")
o2 = man("chenwx",33,"M","yellow","shanxi")
o1.sleep() #父类的方法依然可以用
o1.java_learn()
o1.other()
o1.teach(o2)
o1.showsex()
o1.eat()
#这时候，o1的属性friend也有了，是一个空的list，
#因此当o1调用teach的时候，
#self.friend.append(teacher.name)不会报错，而是正确的传个值进来
print(o1.friend)
for1 = forother("liuqd",32,"black","shanxi")
for1.sleep()