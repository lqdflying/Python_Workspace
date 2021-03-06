###
# File: scoping_rules.py
# Created Date: 2020-12-28
# Author: anddy.liu
# Contact: <lqdflying@gmail.com>
# 
# Last Modified: Monday January 4th 2021 6:27:23 pm
# 
# Copyright (c) 2020 personal
# <<licensetext>>
# -----
# HISTORY:
# Date      	 By	Comments
# ----------	---	----------------------------------------------------------
###

# %%
def f(x):
    v = x.split(",")
    v = v[1:]
    return v

r = f("a,b,c")
print(r)

# %%
y = "+"

def f(x):
    v = x.split(",")
    v = y.join(v)
    return v

r = f("a,b,c")
print(r)

# %%
def f(x):
    v = x.split(",")
    v = y.join(v)
    return v

y = "+"

r = f("a,b,c")
print(r)

# %%
y = "+"

def f(x):
    v = x.split(",")
    v = y.join(v)
    return v

r = f("a,b,c")
print(r)

y = "-"

r = f("a,b,c")
print(r)

# %%
y = 5

def f():
    return y + 1

def g(f):
    y = 10
    print(f())
g(f)

# %%
y = 3

def f():
    y = 5
    def g():
        return y
    r = g()
    print(r)

f()
# %%
y = 3
def f():
    def g():
        return y
    r = g()
    print(r)
f()

# %%
def f(y):
    z = 3 * y
    def g():
        return z
    return g

g = f(3)
r = g()
print(r)
# %%
i = 3

for i in range(5):
    pass

print(i)

# %%
info = True
baz = 10
def foo(info):
    naz = 3

foo(info)

if naz < baz:
    print("1")

# %%
def foo():
    print("a")

def foo():
    print("b")
foo()

