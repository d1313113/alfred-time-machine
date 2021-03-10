# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Cumelmell
Date: 2021-03-10 23:30:12
LastEditors: Cumelmell
LastEditTime: 2021-03-11 00:06:30
'''
from time_machine import TimeMachine

class Workflows:
  """
  时间机器工作流
  """
  def __init__(self):
    self.check_throttle_status()

  """
  获取时间机器节流状态
  """
  def check_throttle_status():
    TimeMachine.get_throttle_status()