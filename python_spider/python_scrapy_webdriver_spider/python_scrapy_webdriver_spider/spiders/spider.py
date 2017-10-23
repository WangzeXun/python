# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import scrapy,re
from python_scrapy_webdriver_spider.items import  ImageItem
from scrapy import Request
from selenium import webdriver

#定义spider组件，继承自scrapy.Spider
class Spider(scrapy.Spider):
    print('enter spider')
    
    name='spider_web_girl' #必须是唯一的
    allowed_domains=['tieba.baidu.com']
#    start_urls=['http://tieba.baidu.com/p/4721853678#!/l/p1'] #起始url
    start_urls=['https://user.qzone.qq.com/991773508?ptlang=2052&source=aiostar'] #起始url
    
#    crawed_urls={'http://tieba.baidu.com/p/4721853678#!/l/p1'} #去重的集合,首先将起始网址添加
    
    #设置cookies
    cookies={}
    #设置headers
    headers={
        'Connection':'keep - alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    
    #构造一个webdriver对象
    def __init__(self):
        self.browser=webdriver.Chrome(executable_path='D:\Program Files\Chromedriver\chromedriver.exe')
    #释放webdriver对象
    def __del__(self):
        self.browser.close()
    
    #重写该函数，在函数中返回Request对象，可以设置cookies,headers参数
    def start_requests(self):
        self.browser.get(self.start_urls[0])
        yield Request(self.start_urls[0],callback=self.parse,headers=self.headers)
    #只需要重写该函数即可，框架会自动回调该函数
    def parse(self,response):
       # print('start parse')
        soup = BeautifulSoup(self.browser.page_source,'html.parser',from_encoding='utf-8')
        all_a = soup.find_all('a',class_="img-item  ")
        
        for a in all_a:
            src=a.find('img')['src']
            item=ImageItem()
            item['img_src']=src
            yield item
            
   
    
    
    
    
    
    