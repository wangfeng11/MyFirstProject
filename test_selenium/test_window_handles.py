#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from time import sleep

from test_selenium.test_selenium_base import Base


class TestSwitchWindow(Base):

    def test_switch_window(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("s-top-loginbtn").click()
        print("登陆页面的句柄：", self.driver.current_window_handle)
        print("点击注册前所有页面的句柄：", self.driver.window_handles)
        self.driver.find_element_by_link_text('立即注册').click()
        print("注册页面的句柄：", self.driver.current_window_handle)
        print("点击注册后所有页面的句柄：", self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('15230500237')
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        username = self.driver.find_element_by_id('TANGRAM__PSP_11__userName')
        # username.clear()
        # username.click()
        username.send_keys('15200500237')
        password = self.driver.find_element_by_id('TANGRAM__PSP_11__password')
        # password.clear()
        # password.click()
        password.send_keys('15230500237')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').submit()
        sleep(3)