print("以a+方式打开文件并且想输出的话,必须使用seek(0)让指针回到文件句柄开始,否则不报错但也无输出")
with open("liuqdarticle.txt","a+",encoding = "utf-8") as liuqdfile: 
#注意，如果是追加，那么需要使用a的方式打开文件,也就是append，但是append的方式依然不能行写
    #liuqdfile.write("\n天安门上太阳升")
    liuqdfile.seek(0)
    print(liuqdfile.read()) #有这一行会报错
print("以a方式打开文件并且想输出的话,必须使用seek(0)让指针回到文件句柄开始,否则不报错但也无输出")
with open("liuqdarticle.txt","r+",encoding = "utf-8") as liuqdfile: 
#注意，如果是追加，那么需要使用a的方式打开文件,也就是append，但是append的方式依然不能行写
    #liuqdfile.write("\n天安门上太阳升")
    #liuqdfile.seek(0)
    print(liuqdfile.read()) #有这一行会报错

a = open("liuqdarticle.txt","a+",encoding = "utf-8")
a.seek(0)
print(a.read())
a.close()