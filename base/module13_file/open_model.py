"""
@author:ming
@file:open_model.py
@time:2021/10/20
"""

import os

"""
python文件操作打开方式：
    1、r 以只读的方式打开文件
    2、w 以只写的方式打开文件，如果文件不存在就创建，如果存在写入的内容会覆盖文件里面的原内容
    3、a 以追加的形式打开文件，如果文件不存在就创建，如果存在写入文件时以追加的形式写入
    4、b 以二进制的方式打开文件，不能单独使用，需要与其他模式一起使用，rb,wb
    5、+ 以读写的方式打开文件，不能单独使用，需要与其他模式配合使用 a+,w+
    
with 上下文管理器
"""

f1 = open("D:\\python project\\study\\file\\f1.txt", encoding='UTF-8', mode="w")
f1.write("hello world ")
f1.flush()
f1.close()

with open("D:\\python project\\study\\file\\img.png", mode='rb') as source:
    with open("D:\\python project\\study\\file\\img_copy.png", mode='wb') as target:
        target.write(source.read())
