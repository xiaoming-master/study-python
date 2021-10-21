"""
@author:ming
@file:del_test.py
@time:2021/10/14
"""
"""
删除操作
    list.remove(key) 一次删除一个元素，列表中有重复的元素时，只删除第一个，元素不存在就抛出异常
    list.pop(index) 删除指定索引的元素，如果索引不存咋，就抛出异常，不指定索引就删除最后一个元素
    list.clear() 清空列表
    list[start：end]=[] 删除区间[start,end)内的元素
    del list 删除列表
"""

l1 = [10, 20, 30, 40, 50, 60, 70, 80]
print("l1:", l1)  # l1: [10, 20, 30, 40, 50, 60, 70, 80]
l1.remove(40)
print('l1.remove(40):', l1)  # l1.remove(40): [10, 20, 30, 50, 60, 70, 80]
# l1.remove(90) # ValueError: list.remove(x): x not in list
l1.pop(0)
print("l1.pop(0):", l1)  # l1.pop(0): [20, 30, 50, 60, 70, 80]
l1.pop()
print("l1.pop():", l1)  # l1.pop(): [20, 30, 50, 60, 70]
l1[0:3] = []
print('l1[0:3]=[]:', l1)  # l1[0:3]=[]: [60, 70]
l1.clear()
print('l1.clear():', l1)  # l1.clear(): []
del l1
