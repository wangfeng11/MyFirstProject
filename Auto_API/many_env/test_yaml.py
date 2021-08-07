#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import yaml


def test_yaml():
    env = {
        "default": "dev",
        "testtest":
            {
                "dev": "127.0.0.1",
                "test": "127.0.0.2"
            }
    }
    with open("env.yaml", "w") as f:
        yaml.safe_dump(data=env, stream=f)
