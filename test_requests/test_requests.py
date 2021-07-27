#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import requests

# get请求
r = requests.get('http://www.baidu.com')
# 响应状态
# print(r.status_code)
# # 编码
# print(r.encoding)
# # 响应内容
print(r.text)
# # 将编码设置成utf-8
# r.encoding = "utf-8"
# print(r.encoding)
# print(r.text)
# post请求
r_post = requests.post('http://httpbin.org/post', data={'key': 'value'})
print(r_post.text)
# put请求
r_put = requests.put('http://httpbin.org/put', data={'key': 'value'})
print(r_put.text)
r_delete = requests.delete('http://httpbin.org/delete')
print('r_delete:',r_delete)
r_head = requests.head('http://httpbin.org/get')
print('r_head:', r_head)
r_option = requests.options('http://httpbin.org/get')
print('r_option:', r_option)
