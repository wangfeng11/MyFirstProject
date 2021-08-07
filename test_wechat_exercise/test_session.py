#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import shelve
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestDemo():
    def setup(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://www.baidu.com")
        # print(self.driver.get_cookies())
        # shelve可以理解成一个小型的数据库,创建一个名为cookies的小型数据库
        db = shelve.open("cookies")
        # 将获取到的数据写入cookie
        db['cookie'] = self.driver.get_cookies()
        # 打开数据库
        db = shelve.open("cookies")
        # 获取已保存的cookie
        cookies = db["cookie"]
        # 访问网址
        self.driver.get("https://www.baidu.com")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        time.sleep(3)
        # 再次访问网址
        self.driver.get("https://www.baidu.com")
        # 关闭数据库
        db.close()
