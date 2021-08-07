#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from time import sleep

from selenium import webdriver


class TestForm():
    def setup(self):
        # option = webdriver.ChromeOptions()
        # option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_form(self):
        self.driver.get("https://testerhome.com/account/sign_in")
        self.driver.find_element_by_id("user_login").send_keys("username")
        self.driver.find_element_by_id("user_password").send_keys("password")
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[3]/div/label").click()
        # self.driver.find_element_by_id("user_remember_me").click()
        self.driver.find_element_by_xpath("//*[@id='new_user']/div[4]/input")
        sleep(3)

