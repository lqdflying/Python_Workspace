# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import xml.etree.ElementTree as ET

'''
###最终要生成一个这样的东西###
<?xml version='1.0' encoding='utf-8'?>
<namelist>
    <name enrolled="yes">
        liuqd
        <age checked="no" />
        <sex>33</sex>
    </name>
    <name enrolled="no">
        mmkli
        <age>19</age>
    </name>
</namelist>
'''
new_xml = ET.Element("namelist")
name = ET.SubElement(new_xml,"name",attrib={"enrolled":"yes"})
name.text = "liuqd"
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
sex.text = '33'
name2 = ET.SubElement(new_xml,"name",attrib={"enrolled":"no"})
name2.text = "mmkli"
age = ET.SubElement(name2,"age")
age.text = '19'

et = ET.ElementTree(new_xml) #生成文档对象
et.write("test.xml", encoding="utf-8",xml_declaration=True)

ET.dump(new_xml) #打印生成的格式