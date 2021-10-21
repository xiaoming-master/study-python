"""
@author:ming
@file:date_operation.py
@time:2021/10/16
"""
s1 = {10, 20, 30, 40, 50}
s2 = {30, 40, 50, 60, 70, 80, 90}
print("s1:", s1)
print("s2:", s2)

# 交集
print("s1 与 s2 的交集:", s1.intersection(s2))  # s1 与 s2 的交集: {40, 50, 30}
print("s1 & s2 :", s1 & s2)  # s1 & s2 : {40, 50, 30}

# 并集

print("s1 与 s2 的并集:", s1.union(s2))  # s1 与 s2 的并集: {70, 40, 10, 80, 50, 20, 90, 60, 30}
print("s1 | s2 :", s1 | s2)  # s1 | s2 : {70, 40, 10, 80, 50, 20, 90, 60, 30}

# 差集
print("s1 与 s2的差集:", s1.difference(s2))  # s1 与 s2的差集: {10, 20}
print("s1 - s2:", s1 - s2)  # s1 - s2: {10, 20}

# 对称差
print("s1 与 s2 的对称差:", s1.symmetric_difference(s2))  # s1 与 s2 的对称差: {70, 10, 80, 20, 90, 60}
print("s1 ^ s2:", s1 ^ s2)  # s1 ` s2: {70, 10, 80, 20, 90, 60}
