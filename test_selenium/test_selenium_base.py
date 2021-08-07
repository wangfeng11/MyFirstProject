#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from selenium import webdriver


class Base():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        # pass
        self.driver.quit()
