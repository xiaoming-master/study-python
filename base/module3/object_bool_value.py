"""
@author:ming
@file:object_bool_value.py
@time:2021/10/12
"""
# 对象布尔值
# 使用bool()获取对象的布尔值
# 空对象的布尔值一般为False
print("bool(False)=", bool(False))
print("bool(0)=", bool(0))
print("bool(0.0)=", bool(0.0))
print("bool(None)", bool(None))
print("bool('')=", bool(''))
print("bool(\"\")=", bool(""))
print("bool([])=", bool([]))  # 空列表
print("bool(list())=", bool(list()))  # 空列表
print("bool(())=", bool(()))  # 空元组
print("bool(tuple())=", bool(tuple()))  # 空元组
print("bool({})=", bool({}))  # 空字典
print("bool(dict())=", bool(dict()))  # 空字典
print("bool(set())=", bool(set()))  # 空集合
