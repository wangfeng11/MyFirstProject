#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest


# 登录login方法在conftest.py中，是pytest规定的一个公共模块，在脚本同目录下会自动调用
def test_case1(login):
    print("test_case1,要登陆")
    pass


def test_case2():
    print("test_case2,不需要登录")
    pass


def test_case3(login):
    print("test_case3,要登陆")
    pass


if __name__ == '__main__':
    pytest.main()
