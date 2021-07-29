#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from selenium import webdriver


class TestBaidu():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 增加隐式等待
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id("kw").send_keys("软件测试工程师")
        self.driver.find_element_by_id("su").click()
