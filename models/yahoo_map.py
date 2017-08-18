# -*- coding: utf-8 -*-
import urllib
import requests
import os


class YahooMap(object):

    def geo_coder(self, **params):
        url = "geocode/V1/geoCoder"
        result = self.__request(url, params)
        return result

    def __request(self, url, params):

        appid = os.environ.get('YAHOO_APP_ID', None)
        url_base = "https://map.yahooapis.jp/"

        query = [
            ("output", "json"),
            ("appid", appid),
        ]
        for k, v in params.items():
            query.append((k, v))
        url += "?{0}".format(urllib.parse.urlencode(query))
        try:
            data = requests.get(url_base + url)
        except ValueError:
            print("APIアクセスに失敗しました。")
        json = data.json()
        return json
