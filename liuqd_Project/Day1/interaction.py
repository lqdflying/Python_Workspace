name = input("name:")
password = input("passwd:")
age = int(input("age:")) #强制输入内容转整型
salary = input("salary")

info = '''
============ info of %s ======
Name:%s
Password:%s
Age:%d
Salary:%s
============================
'''%(name,name,password,age,salary) #注意这里的%不能换一行配置，会报错，只能接在'''后边
#%s是String的意思，如果是%d，那么就强制只接受数字，如果是%f就是只支持浮点,但用的最多的是%s和%d
print(info)