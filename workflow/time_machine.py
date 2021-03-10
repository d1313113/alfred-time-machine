# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Cumelmell
Date: 2021-03-10 23:41:20
LastEditors: Cumelmell
LastEditTime: 2021-03-11 03:18:25
'''
import os

from .config import global_config


class TimeMachine:
  _is_throttle = False

  def __init__(self):
    self.get_throttle_status()

  @property
  def is_throttle(self):
    return self._is_throttle

  @is_throttle.setter
  def is_throttle(self, throttle):
    TimeMachine._is_throttle = throttle


  # 获取时间机器的节流状态
  @staticmethod
  def get_throttle_status():
    try:
      command_throttle = global_config.getRaw('command', 'commond_throttle')
      throttle_res = os.popen(command_throttle).read()
      TimeMachine._is_throttle = is_throttle = bool(int(throttle_res[-2]))
      return is_throttle
    except Exception as e:
      print(e)
      return False

time_machine = TimeMachine()