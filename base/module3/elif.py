"""
@author:ming
@file:elif.py
@time:2021/10/12
"""
# 90 -100 A
# 80- 89 B
# 70-79 C
# 60-69 D
# 0-60 E
# 非法数据

score = int(input("请输入一个分数："))
# if score >= 90 and score <= 100:
#     print("A级")
# elif score >= 80 and score <= 89:
#     print('B级')
# elif score >= 70 and score <= 79:
#     print('C级')
# elif score >= 60 and score <= 69:
#     print('D级')
# elif score >= 0 and score <= 59:
#     print('E级')
# else:
#     print('非法成绩')

if 90 <= score <= 100:
    print("A级")
elif 80 <= score <= 89:
    print('B级')
elif 70 <= score <= 79:
    print('C级')
elif 60 <= score <= 69:
    print('D级')
elif 0 <= score <= 59:
    print('E级')
else:
    print('非法成绩')
