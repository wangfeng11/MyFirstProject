#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import time

from selenium.webdriver import ActionChains

from test_selenium.test_selenium_base import Base


class TestAlert(Base):
    def test_alert(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to_frame("iframeResult")
        drag = self.driver.find_element_by_id("draggable")
        drop = self.driver.find_element_by_id("droppable")
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        time.sleep(3)
        # print("点击alert确认")
        self.driver.switch_to.alert.accept()
        self.driver.switch_to.default_content()
        time.sleep(3)
        self.driver.find_element_by_id("submitBTN").click()
        time.sleep(3)
