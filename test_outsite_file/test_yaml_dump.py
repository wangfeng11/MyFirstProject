#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import yaml

with open('test_yaml.yml', 'w') as f:
    print(yaml.dump({'a': [1, 2]}, stream=f))
print(yaml.dump({'a': 1, 'b': 2}))
