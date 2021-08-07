#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from Auto_API import test_apiRequest


class TestApiRequest():
    req_data = {
        "method": "get",
        "url": "http://127.0.0.1:9999/demo1.txt",
        "headers": None,
        "encoding": "base64"
    }

    def test_send(self):
        ar = test_apiRequest.ApiRequest()
        print(ar.send(self.req_data))
