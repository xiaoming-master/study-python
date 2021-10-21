"""
@author:ming
@file:variable.py
@time:2021/10/10
"""
name = "罗明强"
print("id:", id(name))
print("类型:", type(name))
print("值:", name)

"""
变量由三部分组成：id,type,value
变量经过多次赋值，会指向不同的地址空间，id值会发生改变
"""
print("----------\n")
name = "小明"
print("id:", id(name))
print("类型:", type(name))
print("值:", name)
