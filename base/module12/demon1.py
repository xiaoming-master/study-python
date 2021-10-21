"""
@author:ming
@file:demon1.py
@time:2021/10/20
"""

import sys
import time
import urllib.request as request

"""
python中常用的包：
    1、sys 与python解释器及其环境相关的操作库
    2、time 提供与时间相关的各种函数的标准库
    3、os 提供了访问操作系统服务功能的标准库
    4、 calendar 提供与日期相关的各种函数标准库
    5、urllib 用于读取来自网上的数据标准库
    6、json 用于使用json序列化与反序列化
    7、re 用于在字符串中执行正则表达式
    8、math提供标准的算数运算的函数库
    9、decimal 
    10、logging 日志

"""

print(sys.version)
print(sys.path)
print(sys.getsizeof(24))
print(time.time())
print(time.localtime(time.time()))

response = request.urlopen("http://120.24.213.6:8080/swagger-ui.html").read()
print(type(response))
print(response)
