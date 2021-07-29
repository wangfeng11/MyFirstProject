#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import allure


@allure.link("http://www.baidu.com", name="链接")
def test_with_link():
    print("这是一条加了链接的测试")
    pass


TEST_CASE_LINK = 'http://www.baidu.com'


@allure.testcase(TEST_CASE_LINK, 'Test case title')
def test_with_testcase_link():
    print("这是一条测试用例的链接，链接到测试用例里面")
    pass


# 下方注释的一行代码为allure自动检测issue的机制,可以链接到bug的地址，{}中取的就是bugID
# --allure-link-pattern=issue:http://www.mytesttracker.com/issue/{}
@allure.issue('140(bugID)', '这是一个issue')
def test_with_issue_link():
    pass
