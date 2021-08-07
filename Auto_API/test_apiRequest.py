#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import base64
import json

import requests


class ApiRequest():

    def send(self, data: dict):
        res = requests.request(data["method"], data["url"], headers=data["headers"])
        if data["encoding"] == "base64":
            return json.loads(base64.b64decode(res.content))
        # 把加密过后的响应值发给第三方服务，让第三方去做解密然后返回
        elif data["encoding"] == "testtest":
            return requests.post("url", data=res.content)
