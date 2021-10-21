"""
@author:ming
@file:schedule_test.py
@time:2021/10/20
"""
import schedule
import time


def show():
    print("hello")
    return


schedule.every(3).seconds.do(show)
while True:
    schedule.run_pending()
    time.sleep(1)

