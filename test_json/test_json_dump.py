#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import json

# dump把数据类型转换成字符串并存储在文件中
info = [{
    "name": "Tom",
    "gender": "male",
    "other": None
}, {
    "name": "Tom",
    "gender": "male",
    "other": None
}]
print("读取json文件")
json.dump(info, open("../datas/json_dump.json", "w"))
