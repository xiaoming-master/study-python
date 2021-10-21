"""
@author:ming
@file:nested_branch_structure.py
@time:2021/10/12
"""
# 嵌套分支结构
"""
 会员：
    金额>=200 ,打8折
    100<=金额<200,打九折
 非会员：
    金额>=200,打9折
    <200，不打折
"""

money = int(input("金额："))
vip = input("是否是会员？y/n：")
if vip == 'y':
    print("是会员")
    if money >= 200:
        print("打8折,应付金额为：", money * 0.8)
    elif money >= 100:
        print("打9折，应付金额为：", money * 0.9)
    else:
        print("不打折,应付金额为：", money)

else:
    print("不是会员")
    if money > 200:
        print("打9折，应付金额为：", money * 0.9)
    else:
        print("不打折，应付金额为：", money)
