#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import time

from test_selenium.test_selenium_base import Base


class TestFile(Base):
    def test_file_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element_by_css_selector("#sttb > img.st_camera_off").click()
        self.driver.find_element_by_id("stfile").send_keys("D:/客户端小程序二维码.jpg")
        time.sleep(3)
