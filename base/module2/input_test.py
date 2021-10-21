"""
@author:ming
@file:input_test.py
@time:2021/10/11
"""
from decimal import Decimal

# input 的返回值是一个字符串
name = input("what`s your name? ")
print("Hi", name, type(name))
age = input("How old are you?")
print(int(age), type(int(age)))

print("\n-----两数相加-------\n")
# 使用类型转换，将字符准换成数字
num1 = float(input("请输入一个数："))
num2 = float(input("请输入另外一个数"))
print(num1 + num2)

# 使用Decimal运算
num1 = input("请输入一个数：")
num2 = input("请输入另外一个数")
print(Decimal(num1) + Decimal(num2))
