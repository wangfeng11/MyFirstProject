#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
# 验证各级setup/teardown优先级
import pytest


def setup_module():
    print("setup_module方法")


def teardown_module():
    print("teardowm_module方法")


def setup_function():
    print("setup_function方法")


def teardown_function():
    print("teardown_funciton方法")


def test_login():
    print("这是一个外部的方法login")


class TestDemo():
    def setup_class(self):
        print("setup_class方法")

    def setup_method(self):
        print("setup_method方法")

    def setup(self):
        print("setup方法")

    def teardown_class(self):
        print("teardown_class方法")

    def teardown_method(self):
        print("teardown_method方法")

    def teardown(self):
        print("teardown方法")

    def test_two(self):
        print("start to run test_three")
        x = "hello"
        y = "hello word"
        assert x != y

    def test_three(self):
        print("start to run test_three")
        x = "hello"
        y = "hello word"
        assert x != y


def test_logout():
    print("这是一个外部的方法logout")


if __name__ == '__main__':
    pytest.main("-v -s")
