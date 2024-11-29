"""This is the decorator lecture in python programming"""
"""A decorator is a design pattern that allows to modify the functionality of a function by wrapping it in another functions"""

def make_pretty(func):
    # define the inner function
    def inner():
        print("I got decorated")

        func()
    return inner

def ordinary():
    print("I am ordinary")

decorated_func = make_pretty(ordinary)

print(decorated_func())

print(type(decorated_func))

print(id(ordinary))
print(id(make_pretty))

def divide(x,y):
    print(x/y)

def outer_div(func):
    def inner(x, y):
        if(x < y):
            x,y = y,x
            return func(x,y)
    return inner
try:
    divide1 = outer_div(divide)
    print(divide1(4 , 0))
except :
    print("0 divide is not possible !")