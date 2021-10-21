"""
@author:ming
@file:sort_test.py
@time:2021/10/14
"""
"""
列表排序
    list.sort(reverse=True/False) 默认从小到大排序，指定reverse=True 则从大到小排序，reverse=False 则从小到大排序，在列表原基础上排序
    sorted(list,reverse=True/False) 默认从小到大排序，指定reverse=True 则从大到小排序，reverse=False 则从小到大排序，会生成新的列表
"""

l1 = [40, 20, 50, 60, 10, 30]
l1.sort(reverse=True)
print("l1.sort(reverse=True):", l1)  # l1.sort(reverse=True): [60, 50, 40, 30, 20, 10]

l2 = sorted(l1)
print("sorted(l1):", l2)
