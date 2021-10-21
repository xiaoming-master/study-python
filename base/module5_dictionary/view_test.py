"""
@author:ming
@file:view_test.py
@time:2021/10/14
"""
"""
获取字典的视图
    dict.keys() 获取字典中所有的key
    dict.values() 获取字典中所有的value
    dict.items() 获取字典中所有的键值对，以元组的形式存储
"""

score = {'张三': 83, '李四': 76, '小王': 90, '小五': 80, '小明': 100}
print(score)

print("\n字典的遍历：")
for key in score:
    print(key, score[key], score.get(key))
print("\n")
print("score.keys():", list(score.keys()))  # score.keys(): ['张三', '李四', '小王', '小五', '小明']

print("score.values():", list(score.values()))  # score.values(): [83, 76, 90, 80, 100]

print("score.items():",
      list(score.items()))  # score.items(): [('张三', 83), ('李四', 76), ('小王', 90), ('小五', 80), ('小明', 100)]
