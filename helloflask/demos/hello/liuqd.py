###
# File: liuqd.py
# Created Date: 2020-11-04
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Wednesday November 4th 2020 5:07:51 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###
import click
from flask import Flask

wang = Flask(__name__)
wang.config['ENV'] = 'development'

# the minimal Flask application
@wang.route('/liuqd')
def index():
    return '<h1>Hello, World! first /</h1>'