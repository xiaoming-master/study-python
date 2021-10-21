"""
@author:ming
@file:test.py
@time:2021/10/20
"""

from urllib import request

res = request.urlopen(
    "https://baike.baidu.com/item/%E9%9D%92%E6%98%A5%E6%9C%89%E4%BD%A0%E7%AC%AC%E4%BA%8C%E5%AD%A3").read()
print(res)
