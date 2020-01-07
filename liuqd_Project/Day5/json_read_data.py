# -*- coding: utf-8 -*-
'''
Created on 2017年7月18日

@author: anddy.liu
'''
import json
# with open("liuqd.json","r",encoding = "utf-8") as f:
#     data = f.read()
#     print(data,type(data))
#     data1 = eval(data)
#     print(data1,type(data1))
#这是一种错误的取得数据的正确格式并输出的方法，它的错误在于，在出入和输出的环节增加了太多的额外处理，比如dict到str然后再出入，这里又str到dict才输出
'''
Evaluate the given source in the context of globals and locals.

The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it.

Enter: apply completion.
  + Ctrl: remove arguments and replace current word (no Pop-
   up focus).
  + Shift: remove arguments (requires Pop-up focus).
'''
print("[两种]正确的json反序列化序列化方法".center(50,"+"))

with open("liuqd.json","r",encoding = "utf-8") as file:
    data = json.loads(file.read())
    print(data)

with open("liuqd1.json","r",encoding = "utf-8") as file1:
    print(json.load(file1))






