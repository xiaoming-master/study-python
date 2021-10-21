"""
@author:ming
@file:parameter_summery.py
@time:2021/10/19
"""

# 函数参数总结
"""
使用 global 使函数中的局部变量变更成全局变量
"""


def fun(a, b, c):
    print("a=", a, ",b=", b, ",c=", c)
    return


def fun3(*args):
    print(args)
    return


fun(10, 20, 30)  # a= 10 ,b= 20 ,c= 30
l1 = [11, 22, 33]
fun(*l1)  # a= 11 ,b= 22 ,c= 33 使用* 将列表的元素转换为位置实参传入
fun3(l1)  # ([11, 22, 33],)
fun3(*l1)  # (11, 22, 33)

print("\n--------------------------\n")


def fun1(name, age, sex):
    print("name=", name, ",age=", age, ",sex=", sex)
    return


def fun2(**kwargs):
    print(kwargs)
    return


fun1('ming', 22, 1)  # name= ming ,age= 22 ,sex= 1
dic = {'name': 'luo', 'age': 21, 'sex': 0}
fun1(**dic)  # name= luo ,age= 21 ,sex= 0 使用 ** 将字典中的键值对转换为关键字形参传入
fun2(**dic)  # {'name': 'luo', 'age': 21, 'sex': 0}

print("------------------\n")


def fun4(a, b, *, c, d):  # * 限制后面的参数必须使用关键字参数传参
    print("a=", a, ",b=", b, ",c=", c, ",d=", d)
    return


fun4(10, 20, c=30, d=40)  # a= 10 ,b= 20 ,c= 30 ,d= 40


def fun5(a, b, *args, **kwargs):
    pass
