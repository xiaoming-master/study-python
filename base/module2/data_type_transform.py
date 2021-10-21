"""
@author:ming
@file:data_type_transform.py
@time:2021/10/11
"""

# 字符类型转换

print("------str()-------")
# str()函数是将其他字符转换成字符串
# python中的连字符’+‘，不能将非字符串类型连接起来，需要使用str()将非字符串类型转换成字符串
name = 'ming'
age = 22
weight = 60.5
b = True
print('我的名字是' + name + ',年龄:' + str(age) + ',体重：' + str(weight) + str(b))

print("\n--------int()-------\n")
# int()函数可以将整型数字字符串转换成整数，将浮点数转换成整数，浮点数小数部分会被抹去，将布尔类型转换成整数，True->1,False->0
# 不能转换非整数字符串外的其他字符串
s1 = "128"
s2 = "12.3"
s3 = "hello"
num = 123
f1 = 3.14
print("int('128')=", int(s1))  # int('128')= 128
# print("int(12.3)=", int(s2)) #报错
print("int(3.14)=", int(f1))  # int(3.14)= 3
print("int(123)=", int(num))  # int(123)= 123
# print("int(hello)=", int(s3)) # 报错
print("int(True)=", int(True))  # int(True)= 1
print("int(False)=", int(False))  # int(False)= 0

print("\n-------float()-------\n")
# float()将将其他类型转换成浮点型
print("float('3.14')=", float('3.14'))  # float('3.14')= 3.14
print("float('98')=", float('98'))  # float('98')= 98.0
print("float(58)=", float(58))  # float(58)= 58.0
print("float(True)=", float(True))  # float(True)= 1.0
# print("float('hello')=", float('hello'))  # 报错


