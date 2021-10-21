"""
@author:ming
@file:traceback_test.py
@time:2021/10/19
"""

import traceback

try:
    print("-------------")
    1 / 0
except:
    traceback.print_exc()
