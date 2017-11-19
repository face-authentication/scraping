# coding: utf-8
import os, sys
import argparse, json

from logging import getLogger, StreamHandler, INFO, DEBUG

import scraping as scraping

logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)

def main(args):
  """
  最初に実行される関数.
  @param args コンソールで渡された引数をdict型にしたもの
  """

  # 設定ファイルのロード
  config = read_config(args)

  # プログラムの実行
  if args.module_name == "scraping":
    scraping.scraping(args, config)

def read_config(args):
  """
  設定ファイルを読み込む。指定がない場合は、デフォルトの設定ファイルを読み込む。
  @param args コマンドライン引数
  @return 読み込んだ設定ファイルのdict型オブジェクト
  """
  logger.debug("## %s()", sys._getframe().f_code.co_name)

  file_path = ""

  # 指定がない場合は、モジュール名の設定ファイルを読み込む
  if args.config == None:
    file_path = "config/" + args.module_name + ".json"

  # 指定された場合
  else:
    file_path = args.config

  # json形式でロード
  logger.debug(file_path)
  r_file = open(os.path.abspath(os.path.dirname(__file__)) + "/../" + file_path, 'r')
  j_dict = json.load(r_file)

  return j_dict

if __name__ == '__main__':
  # 引数のチェック、dictの作成
  parser = argparse.ArgumentParser()

  #parser.add_argument("-project_name", "-p", help="", required=True)
  parser.add_argument("-module_name", "-m", help="", required=True)
  parser.add_argument("-config", "-c", help="config/scraping.json", default=None)
  #parser.add_argument("-stage", "-s", help="local, staging, production", default="local")

  args = parser.parse_args()

  # main実行
  main(args)

