# coding: utf-8
import os, sys
import time, re

from logging import getLogger, StreamHandler, INFO, DEBUG
from box import Box

import commons.functions as common

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def scraping(args, config):
  """
  お問い合わせ機能で最初に実行される
  @param args コマンドライン引数
  @param config 読み込まれたconfigファイル
  """
  logger.debug("## %s()", sys._getframe().f_code.co_name)
  logger.debug(args)
  logger.debug(config)

if __name__ == '__main__':
  pass