"""
@author:ming
@file:create.py
@time:2021/10/14
"""
"""
字典：一种用于存储键值对的数据结构
{"张三":20,
"李四":21
}
创建字典：
    1、dict={"key":value}
    2、dict=dict(key=value)
    3、字典生成式
    
"""

score = {
    "张三": 85,
    "李四": 90,
    "小王": 95
}
print(score)
score.clear()
score = dict(张三=83, 李四=76, 小王=90)

print(score)

print("\n-------获取字典元素-----\n")
"""
1、dict["key"]   key一定要存在，不然就抛出异常
2、dict.get(key,default) key不存在时，返回None或者默认值
"""
print("score['张三']=", score["张三"])  # score['张三']= 83
# print("score['小五']=", score['小五'])  # KeyError: '小五'
print("score.get('李四')=", score.get('李四'))  # score.get('李四')= 76
print("score.get('小五')=", score.get('小五'))  # score.get('小五')= None
print("score:", score)  # score: {'张三': 83, '李四': 76, '小王': 90}

print("\n-------添加--------\n")  # score: {'张三': 83, '李四': 76, '小王': 90, '小五': 100}
score["小五"] = 100
print("score:", score)

print("\n------判断key是否存在-----\n")
print("张三" in score)  # True

print("\n-------修改------\n")  # score: {'张三': 83, '李四': 76, '小王': 90, '小五': 95}
score["小五"] = 95
print("score:", score)
score.update({"小五": 80, "小明": 100})  # dict.update(dict)如果字典中含有的key就更新，没有就新增
print("score:", score)  # score: {'张三': 83, '李四': 76, '小王': 90, '小五': 80, '小明': 100}

print("\n--------删除------\n")
del score['小明']
print('score:', score)  # score: {'张三': 83, '李四': 76, '小王': 90, '小五': 80}

print("\n----------生成式创建字典-----\n")
keys = ["张三", "李四", "小王"]
values = [70, 60, 80]
score = {key: value for key, value in zip(keys, values)}
print("score:", score)  # score: {'张三': 70, '李四': 60, '小王': 80}
