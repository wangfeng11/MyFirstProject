#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option("w3c", False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_touch_action_scrollbottom(self):
        self.driver.get("https://www.baidu.com")
        ele_input = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")
        ele_input.send_keys("selenium测试")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()
        action.scroll_from_element(ele_input, 0, 10000).perform()
        sleep(3)
        self.driver.find_element_by_link_text("下一页").click()
