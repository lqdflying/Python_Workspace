# -*- coding:utf-8 -*-
###
# File: __init__.py
# Created Date: 2020-04-30
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday April 30th 2020 3:49:38 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

import sys
def main():
    print("执行了__init__.py")
    print('sys.path', sys.path)
    print('__init__.py的__name__变量: ', __name__)
    print('__init__.py的__package__变量: ', __package__)