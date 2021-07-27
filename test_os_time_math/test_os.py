#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import os

# 创建一个目录
# os.mkdir("testdir")
# 删除一个目录
# os.removedirs("testdir")
# 打印路径下的文件
# print(os.listdir('./'))
# 打印当前所在路径
print(os.getcwd())

existDir = os.path.exists("./b")
existFile = os.path.exists("./b/test.txt")
if not existDir:
    os.makedirs("./b")
if not existFile:
    f = open('./b/test.txt', 'w')
    f.write("hello, os using")
    f.close()
else:
    f = open('./b/test.txt', 'w')
    f.write("input some words again")
    f.close()
