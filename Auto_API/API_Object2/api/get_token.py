#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from string import Template
import requests
# 在api package中是代表所有的接口信息的具体实现，使用一个公共方法代表一个接口
import yaml

from Auto_API.API_Object2.api.base_api import BaseApi


class GetToken(BaseApi):

    def get_token(self):
        req = self.template()
        r = self.request_http(req)
        return r

    def add_token(self):
        pass

#
# if __name__ == '__main__':
#     gt = GetToken()
#     gt.template()
