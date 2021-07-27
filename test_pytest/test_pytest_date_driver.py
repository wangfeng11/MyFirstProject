#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import pytest
import yaml


class TestDateDriver():
    @pytest.mark.parametrize("env", yaml.safe_load(open("./env.yml")))
    def test_env(self, env):
        if "test" in env:
            print("这是测试环境")
            print("测试环境的ip:", env['test'])
        elif "dev" in env:
            print("这是开发环境")
            print("开发环境的ip:", env['dev'])

    def test_yml(self):
        print(yaml.safe_load(open("./env.yml")))

# if __name__ == '__main__':
#     pytest.main()
