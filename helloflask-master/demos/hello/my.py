# -*- coding:utf-8 -*-
###
# File: my.py
# Created Date: 2020-07-03
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Friday July 3rd 2020 4:37:17 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
from flask import Flask
from datetime import datetime
import re

my = Flask(__name__)

@my.route("/")
def home():
    return "Hello, Flask!"

@my.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content
if __name__ == "__main__":
    my.run(host='0.0.0.0')