#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import time
import allure
import pytest
from selenium import webdriver


@allure.testcase("http://www.baidu.com", name="跳转到测试用例地址")
@allure.feature("百度搜索")
@pytest.mark.parametrize('test_data1', ['allure', 'pytest', 'unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度网页"):
        driver = webdriver.Chrome()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element_by_id('kw').send_keys(test_data1)
        time.sleep(2)
        driver.find_element_by_id("su").click()
        time.sleep(2)

    with allure.step("保存图片"):
        # pic = "./tmp/pictures/baidu.png"
        driver.save_screenshot("./tmp/pictures/baidu.png")
        allure.attach.file("./tmp/pictures/baidu.png", attachment_type=allure.attachment_type.PNG)

    with allure.step("保存HTML文件"):
        allure.attach('<head>"这是head"</head><body>首页</body>', 'Attach with HTML type', allure.attachment_type.HTML)

    with allure.step("关闭浏览器"):
        driver.quit()
