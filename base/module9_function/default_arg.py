"""
@author:ming
@file:default_arg.py
@time:2021/10/17
"""
"""
函数的默认参数
"""


def fun(a, b=100):
    return a + b


print(fun(10))  # 110  参数10 赋值给形参a,b使用默认值100
print(fun(10, 20))  # 30
