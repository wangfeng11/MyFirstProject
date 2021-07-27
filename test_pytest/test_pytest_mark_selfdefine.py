#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
# 直接执行会有warning，因为mark标记是自定义的，pytest中没有，需要在conftest.py文件中定义，以消除warning
import pytest


@pytest.mark.search
def test_search1():
    print("test_search1")
    raise NameError
    pass


@pytest.mark.search
def test_search2():
    print("test_search2")
    pass


@pytest.mark.search
def test_search3():
    print("test_search3")
    pass


@pytest.mark.login
def test_login1():
    print("test_login1")
    pass


@pytest.mark.login
def test_login2():
    print("test_login2")
    pass


if __name__ == '__main__':
    pytest.main()
