"""
@author:ming
@file:slice.py
@time:2021/10/13
"""
"""
 分片截取
    list[start:stop:step]
        从列表中截取一段，区间[start,stop),生成新的列表
        step>0 从start开始向右截取，直到stop前一个
        step<0 从start开始向左截取，直到stop后一个
"""

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("-------步长step>0------")
# 截取区间[1,6)的元素，步长为1
l2 = l1[1:6:]
print('l1:', list(l1), 'id:', id(l1))  # l1: [10, 20, 30, 40, 50, 60, 70, 80, 90] id: 1603836446080
print('l2:', list(l2), 'id:', id(l2))  # l2 [20, 30, 40, 50, 60] id: 1603833385152

# 截取区间为[1,6)的元素，步长为2
l2 = l1[1:6:2]
print('l2:', list(l2), 'id:', id(l2))  # l2 [20, 40, 60]

# start=1,stop=默认值,step=1
l2 = l1[1::]
print('l2:', list(l2), 'id:', id(l2))  # l2: [20, 30, 40, 50, 60, 70, 80, 90] id: 2201104699520

# start=默认值,stop=6,step=1
l2 = l1[:6:]
print('l2:', list(l2), 'id:', id(l2))  # l2: [10, 20, 30, 40, 50, 60] id: 2201104699776

print("\n------步长step<0-------\n")
print("截取前：", l1)

# start 默认值，stop 默认值，step -1
print(l1[::-1])  # [90, 80, 70, 60, 50, 40, 30, 20, 10]

# start 默认值，stop:3,step；-1
print(l1[:3:-1])  # [90, 80, 70, 60, 50]

# start 6 ,stop=0,step=-2
print(l1[6:0:-2])  # [70, 50, 30]
