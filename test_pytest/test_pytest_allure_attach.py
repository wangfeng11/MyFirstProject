#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import allure


def test_attach_text():
    allure.attach('这是一个纯文本', attachment_type=allure.attachment_type.TEXT)


def test_attach_html():
    allure.attach("<head></head><bode>这是一段html的body块</body>", name="html测试块", attachment_type=allure.attachment_type.HTML)


def test_attach_photo():
    allure.attach.file(r"D:\Work\Project\运营工具\截图\IOS通知标题.png", name="这是一个图片", attachment_type=allure.attachment_type.PNG)
