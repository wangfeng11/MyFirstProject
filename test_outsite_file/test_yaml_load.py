#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import yaml

print(yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epiplemidae
""", Loader=yaml.FullLoader))

print(yaml.load("""
a: 1 
b: 2
""", Loader=yaml.FullLoader))

print(yaml.load(open('test_yaml.yaml'), Loader=yaml.FullLoader))
