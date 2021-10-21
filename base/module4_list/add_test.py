"""
@author:ming
@file:add_test.py
@time:2021/10/14
"""

"""
向列表中添加元素
    list.append() 在末尾添加一个元素
    list.extend(list) 在末尾添加至少一个元素
    list.insert(index,key) 在任意位置添加一个元素
    list[start:end]=list1 在任意位置添加至少一个元素 将区间[start,end)内的元素剪掉，用list1替换 
"""

l1 = [10, 20, 30, 40, 50]
print("l1:", l1)  # l1: [10, 20, 30, 40, 50]
l1.append(60)
print('l1.append(60):', l1)  # l1.append(60): [10, 20, 30, 40, 50, 60]
l2 = [70, 80]
print("l2:", l2)
l1.extend(l2)  # l2: [70, 80]
print('l1.extend(l2):', l1)  # l1.extend(l2): [10, 20, 30, 40, 50, 60, 70, 80]
l1.insert(1, 99)
print('l1.insert(1,99):', l1)  # l1.insert(1,99): [10, 99, 20, 30, 40, 50, 60, 70, 80]

l3 = ["hello", "world", 132]
print("l3:", l3)  # l3: ['hello', 'world', 132]
l1[2:5] = l3
print('l1[2:5] = l3:', l1)  # l1[2:5] = l3: [10, 99, 'hello', 'world', 132, 50, 60, 70, 80]
