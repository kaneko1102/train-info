# 鉄道の運行情報のLINE通知
## はじめに
鉄道の運行情報を取得し，LINEで通知をするプログラムです．

## 開発環境
- Python 3.9.2
- macOS

## 実行方法
LINEのトークンと取得する鉄道の情報のURLを環境変数に設定します．
URLは[Yahoo JAPANの路線情報](https://transit.yahoo.co.jp/traininfo/area/4/)から取得したい路線のURLを環境変数に設定します．
複数の路線を設定する場合はコンマ(,)区切りで設定します．

### 例
山手線と日暮里舎人ライナーを設定する場合

```
LINE_ACCESS_TOKEN=*******
TRAIN_INFO_URL=https://transit.yahoo.co.jp/traininfo/detail/21/0/,https://transit.yahoo.co.jp/traininfo/detail/541/0/
```

## 参考
[PythonによるスクレイピングでLifehack　運行情報を取得して通知する](https://qiita.com/Brutus/items/0a2e8d0c682d10c65a03)
