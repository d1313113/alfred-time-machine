#!/usr/bin/env python
# -*- encoding=utf8 -*-
'''
Author: Cumelmell
Date: 2021-03-11 03:51:01
LastEditors: Cumelmell
LastEditTime: 2021-03-11 03:57:10
'''
import os

#注意：.env中变量的写法一般是 TEST_KEY = TEST_VALUE。最好去除每个字符两边的空格，否则加到环境变量里也读取不到
def import_env():
  for line in open('.env'):
    var = line.strip().split('=')
    if len(var) == 2:
        key, value = var[0].strip(), var[1].strip()
        os.environ[key] = value

import_env()