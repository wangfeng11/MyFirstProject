#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest
import sys

# 参数化，前两个变量，后面是对应的数据
# 3+5->test input,8->expect
a = [("3+5", 8), ("2+5", 7), ("7*5", 30)]


@pytest.mark.parametrize("test_input,expected", a)
def test_eval(test_input, expected):
    # eval将字符串str当成有效的表达式来求值，并返回结果
    assert eval(test_input) == expected


# 参数组合
@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [8, 10, 11])
def test_foo(x, y):
    print(f"测试数据组合x:{x}, y:{y}")


# 方法名作为参数
test_user_data = ['Tone', 'Jerry']


@pytest.fixture(scope="module")
def login_r(request):
    user = request.param
    print(f"\n 打开首页准备登陆，登陆用户：{user}")
    return user


# 符合条件跳过执行
# @pytest.mark.skipif(sys.platform == 'win32', reason="此测试不在window执行")
# @pytest.mark.skip("此测试不执行")
# 功能没达到可测试程度，测试预留的用例
# @pytest.mark.xfail
# indirect=True, 可以把传过来的参数当函数来执行
@pytest.mark.parametrize("login_r", test_user_data, indirect=True)
def test_login(login_r):
    b = login_r
    print(f"测试用例中login的返回值：{b}")
    assert b != ""


if __name__ == '__main__':
    pytest.main('-v')
