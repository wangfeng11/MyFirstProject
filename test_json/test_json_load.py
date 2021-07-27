#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import json

# load把文件打开从字符串转成json
jsObj = json.load(open('../datas/test.json', 'r'))
print(jsObj)
print(type(jsObj))
print(jsObj[0]['name'])
