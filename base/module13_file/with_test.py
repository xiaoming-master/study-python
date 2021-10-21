"""
@author:ming
@file:with_test.py
@time:2021/10/20
"""
"""
with 上下文管理器
    定义一个类实现 __enter__(self)和__exit__方法，这个类对象就可以被上下文管理器管理，两个方法都是自动执行
"""


class Context:
    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
