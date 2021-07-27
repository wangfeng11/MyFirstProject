#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import time

# 国外时间格式
# print(time.asctime())
# # 纪元时间 可生成时间戳
# print(time.time())
# # 默认为当前时间，传入纪元秒值就是转换后对应的时间
# print(time.localtime())
# # 时间格式转换
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 获取两天前的时间
now = time.time()
two_days_before_second = now - 60 * 60 * 24 * 2
two_days_before = time.localtime(two_days_before_second)
print(two_days_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", two_days_before))
# 获取三天后的时间
three_days_after_second = now + 60 * 60 * 24 * 3
three_days_after = time.localtime(three_days_after_second)
print(time.strftime("%Y-%m-%d %H:%M:%S", three_days_after))
