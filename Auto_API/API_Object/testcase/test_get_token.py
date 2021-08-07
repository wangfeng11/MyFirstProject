#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng

# testcase 是以pytest为测试框架，一个method就是一个case
from Auto_API.API_Object.api.get_token import GetToken


class TestToken:

    def setup(self):
        self.gettoken = GetToken()

    def test_get_token(self):
        assert self.gettoken.get_token().json()["errcode"] == 0
