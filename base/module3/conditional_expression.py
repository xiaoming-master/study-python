"""
@author:ming
@file:conditional_expression.py
@time:2021/10/12
"""
# 条件表达式
# 类似于三元表达式
num1 = int(input("请输入第一个数字："))
num2 = int(input("请输入第二个数字:"))
print(str(num1) + '大于等于' + str(num2) if num1 >= num2 else str(num1) + '小于' + str(num2))
