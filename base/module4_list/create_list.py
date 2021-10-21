"""
@author:ming
@file:create_list.py
@time:2021/10/13
"""
"""
 创建list 两种方式
     1、使用[]
        l1=[...]    
     2、使用list()
        l1=list([...])
     3、列表生成式
        l1=[i for i in range(1,10)]
 list 性质：
    1、列表元素按顺序有序排列
    2、索引映射唯一一个数据
    3、列表可以存储重复数据
    4、任意数据类型混存
    5、根据需要动态分配和回收内存
"""

l1 = ['hello', 'world', 123]
print(id(l1))
for item in l1:
    print("id:", id(item), "value:", item)

# 获取索引为0的对象
print(l1[0])  # hello
# 获取最后一个对象
print(l1[-1])  # 123

l1 = ['hello', 'world', '111', 'hello']
# 获取元素的下标,如果列表中有两个相同值的元素，则只返回第一个元素的下标
print("the index of hello:", l1.index('hello'))  # the index of hello: 0
# 获取一个不存在的元素的下标
# print("the index of 'python': ", l1.index('python'))  # ValueError: 'python' is not in list
# 获取区间内的元素索引
print("the index of 'hello' which is its index is between 2 and 4 :",
      l1.index('hello', 2, 4))  # the index of 'hello' which is its index is between 2 and 4 : 3

l1 = list(['jj', 'kk'])
l1.append(1)
for item in l1:
    print(item)

l1 = [i if i % 2 == 0 else '' for i in range(1, 11)]
print(l1)
