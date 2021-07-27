#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
try:
    num1 = int(input("请输入一个除数"))
    num2 = int(input("请输入一个被除数"))
    print(num1 / num2)
# except ZeroDivisionError:
#     print("被除数不能为0")
# except ValueError:
#     print("输入的数需要是数值型整数")
# 如果不知道有什么异常类型，直接写except
except:
    print("这是一个通用性异常")
else:
    print("程序没有发生异常")
    # print(num1 / num2)
finally:
    print("无论是否发生异常都执行")

x = 10
if x > 5:
    raise Exception("这是抛出的异常信息")


# 自定义异常
class MyException(Exception):
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2


raise MyException("value1", "value2")
