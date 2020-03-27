# -*- coding: utf-8 -*-
'''
Created on 2017年8月10日

@author: anddy.liu
'''
name = "liuqd"
other = "liuming" #变零也支持单引号创建，单引号和双引号是一致的
print(name)
print("liuming截图输出[1:3]，也就是第二个和第三个：\n",other[1:3])
print("字符串赋值".center(40,"+"))
namechange = name + "_change"
print(namechange)
a,b,c = 1,2,3  #批量赋值
print(a,b,c)
print("字符串运算".center(40,"+"))
print("+运算",name+other)
print("*运算",name*2)
print("[]截取运算，从0开始计算字符位置，顾头不顾尾，选取2、3字符，4号字符不选→ ",name[2:4])
print("[]截取运算，只留冒号，内容为空默认全部输出→ ",name[:])
print("[]截取运算，冒号前头部不写默认从第一个字符开始输出，直到冒号后边的字符的前一个位置，4号字符不选→ ",name[:4])
print("[]截取运算，冒号后边的不写，默认从序号3的字符开始一直输出到最后→ ",name[3:])
print("[]截取运算，冒号前边为负数，那么默认从后向前数，最后一个字符是-1，依然顾头不顾尾→ ",name[-4:-1])
print("in成员运算→ ","qd" in name)
print("not in成员运算→ ","qd" not in name)
strname = "liu\nqd\t"
r_strname = r"liu\nqd\t"
print("r原生运算→ ：\n","未原生展现时：",strname,"\n","使用r原生展现时",r_strname)
print("Python字符串原生格式化：".center(40,"+"))

name = "chen\twenxia"
password = "123"
age = 44#强制输入内容转整型
salary = "23467"
liufloat = 4.32366798
info = '''
============ info of %s ======
Name优先使用repr()函数进行字符串转换:%r
Name优先使用str()函数进行字符串转换:%s
Password,这里要右对齐:%15s
Password,这里要左对齐:%-10s
Age这里转换成有符号十进制数:%d
Salary:%s
小数截取小数位数：%.5f
============================
'''%(name,name,name,password,password,age,salary,liufloat) #注意这里的%不能换一行配置，会报错，只能接在'''后边
#%s是String的意思，如果是%d，那么就强制只接受数字，如果是%f就是只支持浮点,但用的最多的是%s和%d
print(info)
print("使用format函数实现字符串格式化：".center(40,"+"))
name = "my name is {},ang age is {}"
print("第一种format方法：",name.format("liuqd", 23))
name = "my name is {1},and age is {0}" #{}里的0或1是序号，用来代表format里的数据位置
print("第二种format方法：",name.format("liuqd", 23))  #这里我故意写错，你会在output里发现我的不同
name = "my name is {name},and age is {age}" #{}里写上名字，就像变量，下边可以赋值
print("第三种format方法：",name.format(name = "liuqd",age = 23))  #这里我故意写错，你会在output里发现我的不同
name = "my name is {name},and age is {age}" #{}里写上名字，就像变量，下边可以赋值
print("第四种format方法：",name.format_map({"name":"liuqd","age":23}))  #第四种是使用format_map的方法而不是format，语法也会有不同
print("另一个种多字符带格式的字符串进行format的方法".center(40,"+"))
name = "liuqd"
password = "123"
age = "44"#强制输入内容转整型
salary = "23000"
info2 = '''
============ info of {_name} ======
Name:{_name}
Password:{_password}
Age:{_age}
Salary:{_salary}
============================
'''.format(_name=name,
           _password=password,
           _age=age,
           _salary=salary)  #第二种定义变量并格式化输出的方法
print(info2)
