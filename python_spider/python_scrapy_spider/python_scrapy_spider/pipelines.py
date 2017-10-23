# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import urllib.request
from python_scrapy_spider.items import ImageItem

class PythonScrapySpiderPipeline(object):
    print('enter piplines')
    count=1
    girl_dir='E:\girls11'
    if not os.path.exists(girl_dir):  #
        os.mkdir(girl_dir)
    os.chdir(girl_dir)
    
    def process_item(self, item, spider):
        if isinstance(item, ImageItem):
            src=item['img_src']
            name = 'tupian' + str(self.count)
            with open(name+ '.jpg','ab') as img_object:
                img_content = urllib.request.urlopen(src).read()#
                img_object.write(img_content) #
                img_object.flush()
            self.count += 1
        return item
