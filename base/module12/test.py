"""
@author:ming
@file:test.py
@time:2021/10/20
"""

"""
使用import可以导入包，模块
from ....import 导入包，模块，函数，变量
"""
import module12.calc as calc
from calc import div

res = calc.add(1, 2)
print(res)

res2 = div(4, 2)
print(res2)
