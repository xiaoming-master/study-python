"""
@author:ming
@file:while_test.py
@time:2021/10/13
"""
# 计算100 以内的偶数和

a = 1
sum = 0
while a <= 100:
    # 两种写法
    # if a % 2 == 0:
    if not bool(a % 2):
    # if a%2: 求奇数和
        sum += a
    a += 1
print("和为：", sum)
