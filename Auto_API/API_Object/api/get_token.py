#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import requests


# 在api package中是代表所有的接口信息的具体实现，使用一个公共方法代表一个接口
class GetToken:
    _corpid = "wwc2282c27e364ba7e"
    _corp_secret = "j2WclgLpY1zsnFq45WauPIp9gevwypfFrfMajQGEjxE"

    def get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self._corpid,
            "corpsecret": self._corp_secret
        }
        r = requests.get(url=url, params=params)
        # print(r.json())
        return r

    def add_token(self):
        pass
