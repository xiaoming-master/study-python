"""
@author:ming
@file:range_test.py
@time:2021/10/13
"""

# range()函数用于生成一个整数序列
# range(end) 生成一个[0,end)的整数序列，步长为1
# range(start,end) 生成一个[start,end)的整数序列，步长为1
# range(start,end,step) 生成一个[start,end)的整数序列，步长为step
# 不管是生成多长的序列，在使用range生成的迭代对象之前，它占用的内存空间是一样的，仅仅需要存储start，end,step,
# 只有个用到时才会去计算序列

r = range(10)
print(list(r))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10)
print(list(r))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

r = range(1, 10, 2)
print(list(r))  # [1, 3, 5, 7, 9]

print("10 in r:", 10 in r)  # 10 in r: False
print("7 in r:", 7 in r)  # 7 in r: True
