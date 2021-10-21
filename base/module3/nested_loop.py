"""
@author:ming
@file:nested_loop.py
@time:2021/10/13
"""

# 嵌套循环

# 输出一个长方形
endWidth = 3
endLength = 5
for i in range(endWidth):
    for j in range(endLength):
        if i % endWidth - 1:
            print("*", end="\t")
        else:
            if not bool(j % (endLength - 1)):
                print("*", end="\t")
            else:
                print(" ", end="\t")
    print("\n")

print("\n-------九九乘法表--------\n")
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + "*" + str(i) + "=" + str(i * j), end="|\t")
    print("\n")
