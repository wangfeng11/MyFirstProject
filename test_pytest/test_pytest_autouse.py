#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest


# 批量自动引用open前置条件
@pytest.fixture(autouse=True)
def open():
    print("打开浏览器")


def test_search1():
    print("test_search1")
    raise NameError
    pass


def test_search2():
    print("test_search2")
    pass


def test_search3():
    print("test_search3")
    pass


if __name__ == '__main__':
    pytest.main()

