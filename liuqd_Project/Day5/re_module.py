# -*- coding: utf-8 -*-
'''
Created on 2017年8月4日

@author: anddy.liu
'''
import re
##match,从开头开始匹配，因此这里的^aa和直接写aa没有区别，因为都是从开始匹配的
res = re.match("^liuqd","liuqdasdf")
print(res) #只要有输出。就证明匹配成功，匹配失败无输出
print("group是输出匹配到的东西:\n",res.group()) 
res = re.match("^liuqd\d","liuqd123asdf")
print("匹配liuqd和后边的321这个数字中的第一个数字:\n",res.group())
res = re.match("^liuqd\d+","liuqd123asdf")
print("匹配liuqd和后边的321这个数字中的一个或多个数字:\n",res.group())
res = re.match(".\d+","liuqd123asdf")
print("点号是匹配一个字符，\d要求一个字符后边跟一个或多个数字，这自然不满足:\n",res)
res = re.match(".+\d+","liuqd123asdf")
print("点号+是匹配一个或多个字符，\d要求一个字符后边跟一个或多个数字，这自然不满足:\n",res.group())
res = re.match(".+","liuqd123asdf")
print("点号+匹配所有:\n",res.group())
res = re.match(".","liuqd123asdf")
print("点号匹配一个字符:\n",res.group())
res = re.match(".","liuqd123asdf")
print("点号匹配一个字符:\n",res.group())
##match,从开头开始匹配，而search是全局寻找符合正则规则的字符串，但是如果有多段字符串符合规则，则只返回第一次找到的部分
res = re.search("as\w.","liuqd123asdf32ascf")  #这里如果写match则会报错，因为match是从开头或结尾开始匹配，search则是全局寻找
print("\w匹配一个任意字母，点号又匹配了一个:\n",res.group())
res = re.search("aa?.","liuqd123asdf32ascf")
print("?是匹配前一个字符1次或0次，如果是匹配0次，那么就是任意第一个字符会被匹配上:\n",res.group())
res = re.search("a\w{3}","liuqd123aaasdf32ascf")
print("第一个字符是a，然后第二个是任意的字母或数字，{3}的意思是连续匹配三次:\n",res.group())
res = re.search("[0-9]{3}","liuqd123aaasdf32ascf")
print("返回三个连续数字:\n",res.group())
res = re.search("LIU|liu","liuqd123aaasdf32ascf")
print("先尝试匹配LIU，发现匹配不到，又尝试匹配liu，发现成功了，于是返回:\n",res.group())
res = re.search("aaa|scf","liuqd123aaasdf32ascf")
print("先尝试匹配aaa，发现匹配到，就不会去尝试scf了，直接返回:\n",res.group())
res = re.search("(liu){2}(\|\|=){2}","123aaasdf32ascfliuliu||=||=")
print("分组匹配演示:\n",res.group())
res = re.search("\Aliu","liuqd123aaasdf32ascf")
print("\A等同于^,匹配行首:\n",res.group())
res = re.search("f\Z","liuqd123aaasdf32ascf")
print("\Z等同于$,匹配行尾:\n",res.group())
##findall会匹配正则表达式，全局找出所有符合正则规则的字符串，并全部返回,返回结果是一个list
res = re.findall("a\w{3}","liuqd123aaasdf32ascf")
print("第一个字符是a，然后第二个是任意的字母或数字，{3}的意思是连续匹配三次——符合这样规则的有两个:\n",res)
res = re.findall("aaa|scf","liuqd123aaasdf32ascf")
print("先尝试匹配aaa，发现匹配到，因为是findall，所以又回去尝试scf了，自后一起返回:\n",res)
print("高级装逼技巧之秒变字典".center(50,"+"))
res = re.search("(?P<id>[0-9]+)(?P<other>[0-9]+)","liuqd1345323aaasdf32ascf")
print("高级装逼技巧之秒变字典，另外注意这句的结果是(?P<id>[0-9]+)(?P<other>[0-9]+)一起瓜分了1345323这个数字串，:\n",res.groupdict())

'''
  ● '\A' 只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
  ● '\Z' 匹配字符结尾，同$
  ● '\d' 匹配数字0-9
  ● '\D' 匹配非数字，也包含特殊字符
  ● '\w' 匹配[A-Za-z0-9]
  ● '\W' 匹配非[A-Za-z0-9]
  ● '\s' 匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'''
##split会使用将正则匹配到的字符串作为分隔符
res = re.split("\d+","liuqd123aaasdf32ascf")
print("split会使用将正则匹配到的字符串作为分隔符:\n",res)
##sub会将正则匹配到的字符串进行替换
res = re.sub("\d+","|+|","liuqd123aaasdf32ascf",count = 1)
print("sub会将正则匹配到的字符串进行替换,count = 1表示只替换一次，如果不写，就是全局替换:\n",res)

















