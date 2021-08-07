#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com")
        self.driver.implicitly_wait(3)

    @pytest.mark.skip()
    def test_wait(self):
        sleep(2)
        print("测试sleep")
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(self.driver.find_element_by_id('kw')))
        self.driver.find_element_by_id("kw").click()
        self.driver.find_element_by_id()
        self.driver.find_elements_by_name()
        self.driver.find_element_by_xpath()
        self.driver.find_element_by_css_selector()

    def test_wait1(self):
        # self.driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("软件测试工程师")
        # self.driver.find_element(By.ID, 'kw').send_keys("selenium定位")
        # self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys("心理医生")
        self.driver.find_element(By.CSS_SELECTOR, '[id=kw]').send_keys("心理医生")
        # self.driver.find_element(By.ID, 'su').clear()
        self.driver.find_element(By.ID, 'su').click()

