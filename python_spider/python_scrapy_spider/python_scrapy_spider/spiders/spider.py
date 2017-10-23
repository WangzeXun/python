# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import scrapy,re
from python_scrapy_spider.items import  ImageItem
from scrapy import Request

#定义spider组件，继承自scrapy.Spider
class Spider(scrapy.Spider):
    print('enter spider')
    
    name='spider_girl' #必须是唯一的
    allowed_domains=['iyangzi.com']
    start_urls=['http://iyangzi.com/?p=173'] #起始url
    
    crawed_urls={'http://iyangzi.com/?p=173'} #去重的集合,首先将起始网址添加
    
    #设置cookies
    cookies={}
    #设置headers
    headers={
        'Connection':'keep - alive',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    #重写该函数，在函数中返回Request对象，可以设置cookies,headers参数
    def start_requests(self):
        yield Request(self.start_urls[0],callback=self.parse,headers=self.headers)
    #只需要重写该函数即可，框架会自动回调该函数
    def parse(self,response):
        print('start parse')
        soup = BeautifulSoup(response.text,'html.parser',from_encoding='utf-8')
        all_img = soup.find('div',class_='post-content').find_all('img')
        
        for img in all_img:
            src=img['src']
            item=ImageItem()
            item['img_src']=src
            yield item
            
        urls = soup.find_all('a',href=re.compile(r'http://iyangzi.com/\?p=[0-9]+$'))
        for url in urls:
            next_url=url['href']
            if next_url not in self.crawed_urls:
                self.crawed_urls.add(next_url)
                #print(next_url)
                yield Request(next_url,self.parse)
        
'''    #只需要重写该函数即可，框架会自动回调该函数
    def parse(self,response):
        print('start parse')
        soup = BeautifulSoup(
            response.text,'html.parser',from_encoding='utf-8')
        all_img = soup.find('div',class_='post-content').find_all('img')
        
        img_items=[]
        for img in all_img:
            src=img['src']
            item=ImageItem()
            item['img_src']=src
            img_items.append(item)
        return img_items
'''
   
    
    
    
    
    
    