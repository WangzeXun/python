#coding:utf-8
import urllib.request

class Htmldownloader():
    def download(self,url):
        if url is None:
            return
        response=urllib.request.urlopen(url)
        if response.getcode() == 200:
            return response.read()