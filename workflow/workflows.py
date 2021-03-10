# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: Cumelmell
Date: 2021-03-10 23:30:12
LastEditors: Cumelmell
LastEditTime: 2021-03-11 03:59:58
'''
import os

from .env import import_env
from .time_machine import time_machine
from .config import global_config

class Workflows:
  """
  时间机器工作流
  """
  def __init__(self):
    self.status = self.check_throttle_status()
    self.execute_toggle()
    # self.output_text()

  """
  获取时间机器节流状态
  """
  def check_throttle_status(self):
    return time_machine.is_throttle

  def execute_toggle(self):
    try:
      open = 1
      if self.status:
        open = 0
      command = ''
      password = os.environ.get('PASSWORD')
      if len(password) > 0:
        command += 'echo ' + password + ' | '
      command = command + global_config.getRaw('command', 'command_switch') + '=' + str(open)
      print(command)
      # os.popen(command)
    except Exception as e:
      print(e)

  """
  获取提示文本
  """
  def output_text(self):
    tips = global_config.getRaw('messages', 'close_tips' if self.status else 'open_tips')
    print(tips)
