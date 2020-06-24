# -*- coding:utf-8 -*-
###
# File: test.py
# Created Date: 2020-06-24
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday June 24th 2020 5:58:23 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import pprint, ast, os, datetime, re


def regex_match(s, pattern):
    '''Custom filter for regex matching'''
    reg = re.compile(pattern)
    if reg.match(s):
        return True
    else:
        return False

type_linux = '^(rhel|sles).*'
type_win = '^win.*'

if __name__ == "__main__":
    start_time = datetime.datetime.now()
    with open ("%s/tmp_file/all_vm_facts.txt"%(os.path.dirname(__file__)),"r") as f:
        contents = f.read()
        result = ast.literal_eval(contents)
    with open ("%s/tmp_file/Linux_vm_facts.txt"%(os.path.dirname(__file__)),"w+") as f_linux, open ("%s/tmp_file/Windows_vm_facts.txt"%(os.path.dirname(__file__)),"w+") as f_windows, open ("%s/tmp_file/template_vm_facts.txt"%(os.path.dirname(__file__)),"w+") as f_temp,  open ("%s/tmp_file/other_vm_facts.txt"%(os.path.dirname(__file__)),"w+") as f_other:
        for k,v in result.items():
            for i in f_linux, f_windows, f_temp, f_other:
                i.write("\n")
                i.write(f"[{k}]\n")
            for n,m in v.items():
                if regex_match(str(m['guest']['guestid']), type_linux) and not m['config']['template']:
                    f_linux.write(f"{m['name'][:20]:25s}  ansible_host={str(m['guest']['ipaddress'])[:16]:25s} {'ansible_user=root'}  ostype={str(m['guest']['guestid']):25s}  hostname={str(m['guest']['hostname']).split('.')[0]:20s}  datastore={m['datastore'][0]['name']:20s} template={m['config']['template']}\n")
                elif regex_match(str(m['guest']['guestid']), type_win) and not m['config']['template']:
                    f_windows.write(f"{m['name'][:20]:25s}  ansible_host={str(m['guest']['ipaddress'])[:16]:25s} {'ansible_user=root'}  ostype={str(m['guest']['guestid']):25s}  hostname={str(m['guest']['hostname']).split('.')[0]:20s}  datastore={m['datastore'][0]['name']:20s} template={m['config']['template']}\n")
                elif m['config']['template']:
                    f_temp.write(f"{m['name'][:20]:25s}  ansible_host={str(m['guest']['ipaddress'])[:16]:25s} {'ansible_user=root'}  ostype={str(m['guest']['guestid']):25s}  hostname={str(m['guest']['hostname']).split('.')[0]:20s}  datastore={m['datastore'][0]['name']:20s} template={m['config']['template']}\n")
                else:
                    f_other.write(f"{m['name'][:20]:25s}  ansible_host={str(m['guest']['ipaddress'])[:16]:25s} {'ansible_user=root'}  ostype={str(m['guest']['guestid']):25s}  hostname={str(m['guest']['hostname']).split('.')[0]:20s}  datastore={m['datastore'][0]['name']:20s} template={m['config']['template']}\n")
    end_time = datetime.datetime.now()
    print('\n开始时间:%s ---> 结束时间:%s \n时间差为:%s'%(start_time, end_time, (end_time - start_time)))