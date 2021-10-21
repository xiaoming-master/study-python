"""
@author:ming
@file:print.py
@time:2021/10/10
"""

# 打印数字类型
print("整数", 520)

print("浮点数：", 3.14)

# 输出运算表达式
print('输出表达式2+3=', 2 + 3)

# 输出字符串
print("hello world")
print('hello world')
print("不换行输出：", "hello world", "hello world")

# 输出到文件
print("以追加的形式输出到文件：")
# 打开文件
fp = open(file="D:\\python project\\study\\file\\print.text", mode="a+")
print("hello world", file=fp)
fp.read()
# 关闭文件
fp.close()

print("---------分界线-----------\n\n")
print("转义符")
# \n换行符号
print("-----------")
print(r"\n换行符：hello\nworld=", 'hello\nworld')
print("-----------")

# \t制表符
print("-----------")
print(r"\t制表符：", 'hello\tworld')
print(r"\t制表符：", 'helloooo\tworld')
print("-----------")

# \r回车
print("-----------")
print(r"\回车：hello\rworld")
print('hello\rworld')
print("-----------")

# \b退格
print("-----------")
print(r"\退格：'hello\bworld=", 'hello\bworld')
print("-----------")
