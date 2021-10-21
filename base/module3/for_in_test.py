"""
@author:ming
@file:for_in_test.py
@time:2021/10/13
"""
# for in 迭代遍历
# 遍历字符串
# ss="hello"
# for s in ss:
#     print(s)

# 遍历range()
# for key in range(0,10):
#     print(key)

# 寻找100-999的水仙花数
for item in range(100, 1000):
    n1 = item % 10
    n2 = (item // 10) % 10
    n3 = (item // 100) % 10
    if (n1 ** 3 + n2 ** 3 + n3 ** 3) == item:
        print(item)
