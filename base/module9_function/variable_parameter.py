"""
@author:ming
@file:variable_parameter.py
@time:2021/10/19
"""
"""
个数可变的位置形参 一个函数只能定义一个

def fun(*args): 以元组的方式接收不定数量的参数

fun(1, 2, 3, 4, 5)

res=(1, 2, 3, 4, 5)
"""


def fun(*args):
    print(args)
    return


fun(1, 2, 3, 4, 5)  # (1, 2, 3, 4, 5)

"""
个数可变的关键字参数 一个函数只能定义一个

def fun2(**kwargs): # 以字典的形式接收多个键值对

fun2(name="ming", age=22, sex=1)
{'name': 'ming', 'age': 22, 'sex': 1}
"""


def fun2(**kwargs):
    print(kwargs)
    return


fun2(name="ming", age=22, sex=1)

"""
一个函数同时定义数量可变的位置参数和数量可变的关键字参数
位置参数要放在关键字参数之前
"""


def fun3(*args, **kwargs):
    print(args)  # (1, 2, 3, 4, 5)
    print(kwargs)  # {'name': 'ming', 'age': 22}
    return


fun3(1, 2, 3, 4, 5, name='ming', age=22)
