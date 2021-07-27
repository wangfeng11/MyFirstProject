#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import json

info = [{
    "name": "Tom",
    "gender": "male",
    "other": None
}, {
    "name": "Tom",
    "gender": "male",
    "other": None
}]
# dumps:将python中的字典转换为字符串
# sort_keys：按key值进行排序，indent以缩进4个空格的方式打印
data = json.dumps(info, sort_keys=True, indent=4)
print(data)
print(type(data))
