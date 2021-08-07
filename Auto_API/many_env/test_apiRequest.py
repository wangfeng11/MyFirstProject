#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from Auto_API.many_env import apiRequest


class TestApi:
    data = {
        "method": "get",
        "url": "http://testtest:9999/demo1.txt",
        "headers": None
    }

    def test_sendrequest(self):
        api = apiRequest.Api()
        print(api.sendrequest(self.data).text)
