###
# File: code_object.py
# Created Date: 2020-10-29
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Thursday October 29th 2020 3:12:03 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
def make(n):
    ret = []

    for i in range(n):
        def test(x, y=10): # test = make_function(code)
            x += 10
            print(x, y)
        print(id(test), id(test.__code__))
        ret.append(test)
        
    return ret

if __name__ == "__main__":
    make(3)