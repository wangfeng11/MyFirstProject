#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import os

from selenium import webdriver


class Base():
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()
