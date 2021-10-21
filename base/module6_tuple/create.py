"""
@author:ming
@file:create.py
@time:2021/10/15
"""
"""
创建元组：
    tuple=("hello",123,"world")
    tuple="hello",123,"world"
    tuple=("hello",) 当元组中只有一个元素时，需要在元素后面加上 ","
    tuple=tuple("hello","123")
    tuple=tuple(('hello',)) 当元组中只有一个元素时，需要在元素后面加上 ","
元组是不可变序列，元组中的元素是不能改变的，但是引用类型的元素是可变序列，那么该引用内的值可以改变（list,dict）

使用tuple[index] 获取元素
使用for in 遍历

"""

t1 = ("hello", "world", 123)
print(t1)  # ('hello', 'world', 123)
print(list(t1))  # ['hello', 'world', 123]

t2 = "hello",
print(t2, type(t2))  # ('hello',) <class 'tuple'>

t3 = "hello", "world"
print(t3)  # ('hello', 'world')

t4 = tuple(('hello',))
print(t4, type(t4))  # ('hello',) <class 'tuple'>

print("\n-------元组的遍历------\n")

print("t1:", t1)
print("t1[0]=", t1[0])  # t1[0]= hello
for item in t1:
    print(item)
