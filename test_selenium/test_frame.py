#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
from test_selenium.test_selenium_base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get("https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        # 切换到frame
        self.driver.switch_to.frame("iframeResult")
        # self.driver.switch_to_frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        # 切换回原frame，也是父frame，默认frame(打开url时的frame)，两种方式：
        # self.driver.switch_to.parent_frame()
        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id("submitBTN").text)
