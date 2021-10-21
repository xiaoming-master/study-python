"""
@author:ming
@file:exception_handle.py
@time:2021/10/19
"""
"""
异常处理
 1、try:
    except:
    
 2、try:
    except:
    else:
    
 3、try:
    except:
    else:
    finally:
 
"""

try:
    n1 = int(input("请输入一个整数："))
    n2 = int(input("请输入另外一个整数："))
    n3 = n1 / n2

except ValueError:
    print("请输入正确的数字")
except ZeroDivisionError:
    print("除数不能为0")
else:
    print(n3)
    1 / 0
finally:
    print("程序结束")
