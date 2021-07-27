#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import urllib.request
import requests

# urllib比较老，用的人少，官网推荐使用requests库
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response)
# print(response.status)
# print(response.geturl())
# print(response.getcode())

print(requests.get('http://www.baidu.com'))

