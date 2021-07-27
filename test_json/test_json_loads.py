#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import json
# loads:将字符串转化为json
str1 = '''
[{
    "name": "Tom",
    "gender": "male"
}, {
    "name": "Tom",
    "gender": "male"
}]
'''
print(type(str1))
data = json.loads(str1)
print(type(data))
print(data)
