# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Cumelmell
Date: 2021-03-10 23:41:20
LastEditors: Cumelmell
LastEditTime: 2021-03-11 00:00:01
'''
import os


class TimeMachine:
  def __init__(self):
    self.get_throttle_status()

  @staticmethod
  def get_throttle_status():
    print(1)
    print(os.popen('ls').readlines())
    # return