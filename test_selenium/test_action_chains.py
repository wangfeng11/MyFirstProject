#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip()
    # 点击、双击、右键
    def test_case_click(self):
        self.driver.get('http://sahitest.com/demo/clicks.htm')
        element_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        element_doubleclick = self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        element_rightclick = self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)
        action.click(element_click)
        sleep(2)
        action.double_click(element_doubleclick)
        sleep(2)
        action.context_click(element_rightclick)
        sleep(2)
        action.perform()

    @pytest.mark.skip()
    # 鼠标移动到一个元素上
    def test_case_move_to_element(self):
        self.driver.get("https://www.baidu.com")
        settings = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(settings)
        action.perform()
        sleep(3)

    # 将一个元素拖拽到
    def test_case_drag_and_drop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        dragger = self.driver.find_element_by_id("dragger")
        drop = self.driver.find_element_by_xpath("/html/body/div[2]")
        drop2 = self.driver.find_element_by_xpath("/html/body/div[3]")
        action = ActionChains(self.driver)
        action.drag_and_drop(dragger, drop)
        action.perform()
        sleep(3)
        # 下边两个方法相当于上边一个方法
        # action.click_and_hold(dragger).release(drop).perform()
        # 下边三个方法相当于上边一个方法
        # action.click_and_hold(dragger).move_to_element(drop2).release().perform()
        sleep(3)

    def test_case_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        ele.click()
        action = ActionChains(self.driver)
        action.send_keys("username").pause(1)
        action.send_keys(Keys.SPACE)
        action.send_keys("tom").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)


if __name__ == '__main__':
    pytest.main(['-v', '-s', 'test_action_chain.py'])
