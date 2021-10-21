"""
@author:ming
@file:else_test.py
@time:2021/10/13
"""

# Python的for…else、while…else、try..except…else等语法
# for、while是在循环体内触发break语句、没有return语句，或者没有异常出现时才执行else语句
# ，try..except…else是在try中无异常产生时执行，注意不包括continue。

# i = 0
# while i < 3:
#     if "8888" == input("请输入密码："):
#         print("密码正确")
#         break
#     else:
#         print("密码错误")
#     i += 1
# else:
#     print("你已经输错三次密码")


a = 0
for i in range(3):
    if "8888" == input("请输入密码："):
        print("密码正确")
        break
    else:
        print("密码错误")
    a += 1
else:
    print("你已经输错三次密码")
