#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from selenium import webdriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("htts://www.baidu.com")
        self.driver.implicitly_wait(3)

    def test_wait(self):
        sleep(2)
        print("测试sleep")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.driver.find_element_by_id('kw')))
        self.driver.find_element_by_id("kw").click()
