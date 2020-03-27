name = input("name:")
password = input("passwd:")
age = int(input("age:")) #强制输入内容转整型
salary = input("salary")

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