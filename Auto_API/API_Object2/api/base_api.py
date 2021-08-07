#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from string import Template

import requests

# from Auto_API.API_Object2.api.get_token import GetToken
import yaml


class BaseApi:
    # def setup(self):
    #     self.gettoken = GetToken()

    def request_http(self, req):
        # 2.	直接使用python关键字传参的方式，将请求结构体传给requests.request方法
        r = requests.request(**req)
        # print(r.json())
        return r

    _corpid = "wwc2282c27e364ba7e"
    _corp_secret = "j2WclgLpY1zsnFq45WauPIp9gevwypfFrfMajQGEjxE"

    # 最好写在base_api中
    def template(self):
        with open("../api/get_token.yml") as f:
            data = {
                "corpid": self._corpid,
                "corpsecret": self._corp_secret
            }
            # 对写死的数据做替换
            re = Template(f.read()).substitute(data)
            return yaml.safe_load(re)
