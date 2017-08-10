zunda-cafe で利用するWeb-APIのためのリポジトリです。LINE/Slackボット等から利用してください。

Heroku で稼働しています。

# ぐるなび検索

## レストラン検索

https://zunda-api.herokuapp.com/api/gnavi/search_rest?latitude=38.24920826076629&longitude=140.89660249650478&category_s=RSFST08008&range=5&hit_per_page=100

クエリパラメータに「ぐるなびレストラン検索API（http://api.gnavi.co.jp/api/manual/restsearch/）」の全てのパラメータが設定可能です。

## 大業態マスタ取得API

https://zunda-api.herokuapp.com/api/gnavi/category_large_search

## 小業態マスタ取得API

https://zunda-api.herokuapp.com/api/gnavi/category_small_search

