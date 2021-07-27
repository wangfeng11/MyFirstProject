#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest


# content of test_sample.py
class TestDemo():

    def test_one(self):
        print("start to run test_one")
        x = "this"
        assert "h" in x
        pytest.assume(1 == 4)
        pytest.assume(2 == 4)

    def test_two(self):
        print("start to run test_two")
        x = "hello"
        assert hasattr(x, "check")

    def test_three(self):
        print("start to run test_three")
        x = "hello"
        y = "hello word"
        assert x != y


class TestDemo1():

    def test_a(self):
        print("start to run test_a")
        x = "this"
        assert "h" in x

    def test_b(self):
        print("start to run test_b")
        x = "hello"
        assert hasattr(x, "check")

    def test_c(self):
        print("start to run test_three")
        x = "hello"
        y = "hello word"
        assert x != y


if __name__ == '__main__':
    pytest.main()
    # pytest.main("-v -x TestDemo1::test_one")
    # pytest.main('-v', '-s', 'TestDemo')
