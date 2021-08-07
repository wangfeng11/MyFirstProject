#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import time

import pytest

from test_selenium.test_selenium_base import Base


class TestJS(Base):

    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试实例")
        # 使用js获取元素，如果需要返回，一定要加return
        ele = self.driver.execute_script('return document.getElementById("su")')
        ele.click()
        # 滑动到底部
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(3)
        # 点击下一页
        self.driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()
        time.sleep(3)
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # print(self.driver.execute_script("return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index")
        train_date = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")
        time.sleep(3)
        self.driver.execute_script("document.getElementById('train_date').value='2021-12-30'")
        time.sleep(3)
        print(self.driver.execute_script("return document.getElementById('train_date').value"))
