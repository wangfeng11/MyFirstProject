#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:wangfeng
#open 一个文件之后一定要closed
f = open('datas/txtfile', 'rt')
# 打印读取所有数据
# print(f.read())
# 打印读取一行数据
# print(f.readline())
# print(f.readline())
# 打印读取所有数据，以列表的形式
# print(f.readlines())
f.close()

# 使用with打开文件不用关闭，实际运用中使用with更安全、优雅
with open('datas/txtfile', 'rt') as f:
    # 判断文件是否可读
    # print(f.readable())
    # print(f.readlines())
    # 实际工作中读取所有文件内容
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break
