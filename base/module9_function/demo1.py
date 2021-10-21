"""
@author:ming
@file:demo1.py
@time:2021/10/17
"""
"""
函数参数指向可变对象，在函数体内修改参数的值，会影响到实参的值
        指向不可变对象，在函数体内修改参数的值，不会影响到实参的值

"""

def fun(arg1, arg2):
    print("arg1=", arg1)  # arg1= 20
    print("arg2=", arg2)  # arg2= [20, 30, 50]
    arg1 = 100
    arg2.append(10)
    print("arg1=", arg1)  # arg1= 100
    print("arg2=", arg2)  # arg2= [20, 30, 50, 10]
a = 20
b = [20, 30, 50]
fun(a, b)
print("a=", a)  # a= 20
print("b=", b)  # b= [20, 30, 50, 10]
