# -*- coding: utf-8 -*-
'''
Created on 2018年3月15日

@author: anddy.liu
'''
import xml.etree.ElementTree as ET
tree=ET.parse("movie.xml")
root=tree.getroot()
# print('根节点的tag：',root.tag)
# print('根节点的attrib：',root.attrib)
# print("这个xml的深度：",len(root))
# print('列出所有子节点的名字及参数(包含key/value的字典)'.center(30,"+"))
# for n in root:
#     print(n.tag,":",n.attrib)
# print('列出所有子节点的名字及参数(仅仅包含参数的名字)'.center(30,"+"))
# for n in root:
#     print(n.tag,":",n.keys())
# print('列出所有节点的所有key和value'.center(40,"+"))
# for name in root:
#     print("第一层结构".center(30,"="))
#     print(name.tag,":",name.text)
#     for subname in name:
#         print("第二层结构".center(30,"-"))
#         print(subname.tag,":",subname.text)
#     print("".center(30,"="))
# print('列出第一个movie节点的所有key和value'.center(40,"+"))
# for movie_format in root.iter('format'):
#     print(movie_format.tag,"|",movie_format.attrib,":",movie_format.text)
# print("iter的另一种用法".center(30,"+"))
# iter_format=root.iter('format')
# print("直接调用iter，就是一个xml的生成器",iter_format)
# 
# while True:
#     try:
#         print("%s这个tag的值是："%(iter_format.__next__().tag),iter_format.__next__().text)
#     except StopIteration:
#         break    
# print("使用find寻找元素".center(30,"+"))
# for movie_format in root.findall('movie'):
#     m = movie_format.find('type').text
#     n = movie_format.get('title')
#     print("列出这一段的顶tag的所有的属性键值对：\n",movie_format.items())
#     print(type(m),"->>",m,":","这个节点的title的属性的值是：",n)
# 
# movie_type=root.find('movie')
# print(type(movie_type))
# print('xml属性的修改'.center(40,"+"))
# 
# for movie_year in root.findall('movie'):
#     title_old=movie_year.get('title')
#     year_old=movie_year.iter('year').__next__().text
#     desp=movie_year.find('description').text
#     print("%s这个段修改前的的属性的值:"%(movie_year.tag),title_old)
#     print("%s这个电影描述的段的年这个tag的初始的值:"%(desp),year_old)
#     print("修改%s这个段的属性的值:"%(movie_year.tag))
#     movie_year.attrib['title']=title_old+'--attrib--'
#     print("%s这个段新增一个属性:"%(movie_year.tag))
#     movie_year.set('name','liuqd_change') #新增一个参数
# #     movie_year.set('title','liuqd_change') #set也可以修改已有参数的值，实验是成功的，这里先忽略
#     print("修改%s这个电影描述的段的年这个tag的初始的值:"%(desp))
#     year_new=int(year_old)+1
#     movie_year.iter('year').__next__().text=str(year_new)
#     print("".center(30,"-"))
# tree.write('movie.xml', encoding='UTF-8')
'''
以上是所以注释掉，1、是因为会不断地修改xml，2、是因为会产生大量输出。
注释取消就能运行，代码无错
'''

# print('xml节点/元素相关'.center(40,"+"))
# print('第一种删除节点的方法')
# movie=root.find('movie')
# print(movie.tag,":",movie.attrib)
# root.remove(movie)
#  
# print('第二种删除节点的方法')
# movie=root.iter('movie')
# for n in movie:
#     print("删掉%s节点的rating字段"%(n.get('name')))
#     rating=n.find('rating')
#     n.remove(rating)
# print('添加子元素的方法：')
# item = ET.Element("item", {'sid' : '1713', 'name' : 'ityouhui'})
# item.text="new jpeg"
# item1 = ET.Element("item1", {'sid' : '1713', 'name' : 'ityouhui'})
# item1.text="new jpeg1"
# root.extend((item,item1))
# print("子节点里新增key-value")
# movie=root.find('movie')
# movie.append(item)
# item2=ET.Element("lqdgo",{"sid":'9908','name':"liuquangong"})
# item2.text="we are here!"
# root.insert(1,item2)
# tree.write('movie.xml', encoding='UTF-8')
'''
以上注释掉的代码不是不能运行，是因为会持续针对xml进行修改，所以去掉了，功能实验完了即可
'''
print("gogogo")

new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
#下边函数是美化XML用的，使用方法就是在保存前调用一次即可,但是要注意，这个函数调用传入的必须是节点使用getroot()函数处理过的
def indent( elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for e in elem:
            indent(e, level+1)
        if not e.tail or not e.tail.strip():
            e.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i
    return elem
root_et=et.getroot()
indent(root_et)
et.write("new.xml", encoding="utf-8",xml_declaration=True)