###
# File: enclousing.py
# Created Date: 2020-10-30
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday October 30th 2020 3:34:01 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
def make(n):
    x = []
    for i in range(n):
        x.append(lambda: print(i))
    return x

if __name__ == "__main__":
    a = make(3)
    for i in a:
        i()