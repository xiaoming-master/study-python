"""
@author:ming
@file:relation.py
@time:2021/10/16
"""

# 集合中的数据相同，那么集合的就相等，与元素位置没有关系
set1 = {10, 20, 30, 40}
set2 = {40, 30, 20, 10}
print(set1 == set2)  # True
print(set1 != set2)  # False

s1 = {10, 20, 30, 40, 50, 60, 70, 80, 90}
s2 = {30, 40, 60}
s3 = {70, 80, 100}
print("s1 是 s2 的超集:", s1.issuperset(s2))  # s1 是 s2 的超集: True
print("s2 是 s1 的子集:", s2.issubset(s1))  # s2 是 s1 的子集: True
print("s1 与 s3 没有交集：", s1.isdisjoint(s3))  # s1 与 s3 有交集： False
