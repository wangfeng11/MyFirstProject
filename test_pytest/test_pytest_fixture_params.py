#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest


@pytest.fixture(params=[1, 2, 3, 'linda'])
def test_data(request):
    return request.param


def test_one(test_data):
    print('\ntest data:%s' % test_data)
