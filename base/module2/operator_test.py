"""
@author:ming
@file:operator_test.py
@time:2021/10/11
"""
print("-------算数运算符-------")
# 运算符 + - * /  //(整除运算符)
# % 取余
# ** 幂运算 2**3=2^3
print("2+3=", 2 + 3)
print("1-2=", 1 - 2)
print("2*3=", 2 * 3)
print("1/2=", 1 / 2)
print("9//4=", 9.0 // 4)  # 9//4= 2.0 整除 向下取整，及靠近数轴右侧取整
print("-9//4=", -9 // 4)  # -9//4= -3
print("9//-4=", 9 // -4)  # 9//-4= -3

# 余数=被除数-除数*商（整除得到的商）
print("9%4=", 9 % 4)  # 9%4= 1 9-4*2=1
print("9%-4=", 9 % (-4))  # 9%-4= -3 9-(-4)*(-3)=9-12=-3
print("-9%4=", -9 % 4)  # -9%4= 3  -9-(4*(-3))=-9-(-12)=-9+12=3

print("\n------赋值运算符------\n")
# 链式赋值，引用指向同一个对象，id相同
a = b = c = 10
print("a=", a, ",id=", id(a))  # a= 10 ,id= 2680045922896
print("b=", b, ",id=", id(b))  # b= 10 ,id= 2680045922896
print("c=", c, ",id=", id(c))  # c= 10 ,id= 2680045922896

# 参数赋值
# +=、-=、*=、/=、//=、%=

# 系类解包赋值,= 左右两边参数个数要相等
print("\n系类解包赋值")
a, b, c = 10, 20, 30
print("a=", a)
print("b=", b)
print("c=", c)

# 交换变量
print("\n交换变量的值")
a, b = 10, 20
print("交换之前：", "a=", a, ",b=", b)
a, b = b, a
print("交换之后：", "a=", a, ",b=", b)

print("\n-------比较运算符-------\n")
# 比较运算符
# ==比较对象的值，is、is not 用来比较标识 id
a = 10
b = 10
# a b为常量值，他们指向同一个内存空间
print("a==b:", a == b, "\na ：id=", id(a), ",b：id=", id(b))  # a==b: True
print("a is b:", a is b)  # a is b: True
print("a is not b:", a is not b, "\n")  # a is not b: False

#
#
#
l1 = [10, 20, 30, 40]
l2 = [10, 20, 30, 40]
print("l1:", l1, ",l1:id=", id(l1), ";l2:", l2, ",l2:id=", id(l2))
print("l1==l2:", l1 == l2)  # l1==l2: True 数组内的数据相同
print("l1 is l2:", l1 is l2)  # l1 is l2: False 数组的id不同
print("l1 is not l2:", l1 is not l2)  # l1 is not l2: True

print("\n---------布尔运算--------\n")

# and 逻辑与
# or 逻辑或
# not 逻辑非

b = True
b = not b
print(b)

# in
# not in
s1 = "abc"
s2 = "a"
print("s1=", s1, "s2=", s2)
print("s2 in s1:", s2 in s1)  # s2 in s1: True s1中包含s2结果为True
print("s2 not in s1:", s2 not in s1)  # s2 not in s1: False s1中不包含s2结果为False

print("\n--------位运算符--------\n")
# & 位与，对应位同为1，才是1，否则就是0
# | 位或，对应位有1，结果就是1，同为0，才是0
# << 左移位运算符，高位益处舍弃，低位补0
# >> 右移位运算符，低位益处舍弃，高位补0

print("4 & 8=", 4 & 8)  # 4 & 8= 0
print("4 | 8=", 4 | 8)  # 4 | 8= 12
print("4>>1=", 4 >> 1)  # 4>>1= 2
print("4<<1=", 4 << 1)  # 4<<1= 8
