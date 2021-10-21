"""
@author:ming
@file:return_test.py
@time:2021/10/17
"""

'''
当函数返回多个值时，结果为元组
'''


def fun(arg):
    even = []  # 偶数
    odd = []  # 奇数
    for item in arg:
        if item % 2:
            even.append(item)
        else:
            odd.append(item)
    return even, odd  # 返回偶数数组和奇数数组


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
res = fun(a)
print(res)  # ([1, 3, 5, 7, 9], [2, 4, 6, 8])
