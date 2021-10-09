from dotenv import load_dotenv
load_dotenv()

# 環境変数を参照
import os

TOKEN = os.getenv('LINE_ACCESS_TOKEN')

# https://transit.yahoo.co.jp/traininfo/area/4/
urls = os.getenv('TRAIN_INFO_URL').split(',')
