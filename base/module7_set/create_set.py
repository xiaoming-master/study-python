"""
@author:ming
@file:create_set.py
@time:2021/10/15
"""
"""
集合是一个可变序列，集合里面的元素不能重复
创建集合：
    set={"hello","world",23,123,3334,444}
    set=set(range(6))
    set=set(['hello','world'])
    set=set(('hello','world'))
    set=set('python')
    set=set() # 定义空集合
    set={i for i in range(6)} # 集合生成式
"""

s1 = {"hello", "world", 23, 123, 3334, 444}
print("s1=", s1)  # s1= {3334, 23, 'hello', 123, 444, 'world'}
s2 = set(range(6))
print("s2=", s2)  # s2= {0, 1, 2, 3, 4, 5}
s3 = set(['hello', 'world'])
print("s3=", s3)
s4 = set(('hello', 'world'))  # s3= {'hello', 'world'}
print("s4=", s4)  # s4= {'hello', 'world'}
s5 = set('python')  # s5= {'n', 't', 'h', 'o', 'p', 'y'}
print("s5=", s5)
s6 = set()  # 定义空集合

s7 = {i for i in range(9)}
print("s7=", s7) # s7= {0, 1, 2, 3, 4, 5, 6, 7, 8}
