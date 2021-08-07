#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import requests


class TestToken:
    corpid = "wwc2282c27e364ba7e"
    corp_secret = "j2WclgLpY1zsnFq45WauPIp9gevwypfFrfMajQGEjxE"

    def test_get_token(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid": self.corpid,
            "corpsecret": self.corp_secret
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0
