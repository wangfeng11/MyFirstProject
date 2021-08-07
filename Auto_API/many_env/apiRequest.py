#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import requests
import yaml

"""
1.	需要二次封装requests，对请求进行定制化
2.	将请求的结构体的url从一个写死的ip地址改为一个任意的域名
3.	使用一个env配置文件，存放各个环境的配置信息
4.	然后将请求结构体中的url替换为“env”配置文件中个人选择的url
5.	将env配置文件使用yaml进行管理
"""


class Api:
    env = yaml.safe_load(open("env.yaml"))

    def sendrequest(self, data: dict):
        # 替换                                              self.env["testtest"]["dev"]
        data["url"] = str(data["url"]).replace("testtest", self.env["testtest"][self.env["default"]])
        r = requests.request(method=data["method"], url=data["url"], headers=data["headers"])
        return r
