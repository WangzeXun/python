#coding:utf-8
import re
from bs4 import BeautifulSoup

class Htmlparser():
    def get_new_urls(self,soup):
        new_urls=set()
        links=soup.find_all('a',href=re.compile(r'http://iyangzi.com/\?p=\d+$'))
        for link in links:
            new_urls.add(link['href'])
        return new_urls
    def get_imgs(self,soup):
        imgs = soup.find('div',class_='post-content').find_all('img')
        return imgs
    def parse(self,url,html_cont):
        if url is None or html_cont is None:
            return
        soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
        new_urls=self.get_new_urls(soup)
        imgs=self.get_imgs(soup)
        return new_urls,imgs
    