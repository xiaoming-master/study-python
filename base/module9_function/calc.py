"""
@author:ming
@file:calc.py
@time:2021/10/17
"""


def calc(a, b):
    return a + b


result = calc(10, 20)
print("result=", result)  # result= 30

res = calc(b=20, a=10)
print("res=", res)  # res= 30
