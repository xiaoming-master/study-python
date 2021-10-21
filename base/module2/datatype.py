"""
@author:ming
@file:datatype.py
@time:2021/10/10
"""

# 整数
from decimal import Decimal

print("-----整数-----")
num = 128
print(num, type(num))

# 二进制表示
print('二进制表示：0b10101011=', 0b10101011)

# 八进制表示
print('八进制表示：0o1234567=', 0o1234567)

# 十六进制表示
print('十六进制：0x12abcdef=', 0x12abcdef, "\n")

print("------浮点数------\n")
f1 = 3.14
f2 = 3.2
print(f1 + f2, type(f1))

print("存在误差,3.1+3.2=", 3.1 + 3.2)

print("使用Decimal,3.1+3.2=", Decimal('3.1') + Decimal('3.2'), "\n")

print("------布尔---------\n")
# true=1
# false=0

b1 = True
b2 = False
print("b1:", b1, type(b1))
5
print("b2:", b2, type(b1))

print("True+1=", True + 1)
print("False+1=", False + 1, "\n")

print("--------字符串-------\n")

# 单引号'',双引号""，字符串在同一行输出
# 单引号的三引号''' ''',双引号的三引号 ”“” “”“，字符串可以换行输出

print('单引号的使用:', 'hello， world')
print("双引号的使用:", "hello world")
print('''单引号的三引号使用：''', '''hello
 world''')
print("""双引号的三引号使用：""", """hello
 world""")
