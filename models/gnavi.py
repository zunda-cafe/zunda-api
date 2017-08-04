# -*- coding: utf-8 -*-
import urllib
import requests


class Gnavi(object):

    def category_small_search(self, **params):
        url = "master/CategorySmallSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def category_large_search(self, **params):
        url = "master/CategoryLargeSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def garea_small_search(self, **params):
        url = "master/GAreaSmallSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def garea_middle_search(self, **params):
        url = "master/GAreaMiddleSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def garea_large_search(self, **params):
        url = "master/GAreaLargeSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def pref_search(self, **params):
        url = "master/PrefSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def area_search(self, **params):
        url = "master/AreaSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def search_rest(self, **params):
        url = "RestSearchAPI/20150630/"
        result = self.__request(url, params)
        return result

    def __request(self, url, params):

        keyid = "c30154caa70f058b30f5349f28030382"
        url_base = "https://api.gnavi.co.jp/"

        query = [
            ("format", "json"),
            ("keyid", keyid),
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

