# -*- coding:utf-8 -*-
###
# File: exception_custom.py
# Created Date: 2020-05-02
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Saturday May 2nd 2020 2:53:36 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
try:
    raise MyError(2*2)
except MyError as e:
    print('报错了,值是:', e.value)
    raise
   