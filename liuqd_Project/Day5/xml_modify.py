# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import xml.etree.ElementTree as et
tree = et.parse("liuqd.xml")
root = tree.getroot()
print(root)
for node in root.iter("year"):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("updated","yes")

for country in root.findall("country"):
    rank = int(country.find("rank").text)
    if rank > 50:
        root.remove(country)


tree.write("liuqdnew.xml", encoding = "utf-8") #这里不光修改，还新增了一个文件出来，其他未修改的属性会自动复制过去