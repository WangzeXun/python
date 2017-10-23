#coding:utf-8

import os
import urllib.request
import url_manager,html_downloader,html_parser

class Spidermain():
    def __init__(self):
        self.urls=url_manager.Urlmanager()
        self.downloader=html_downloader.Htmldownloader()
        self.parser=html_parser.Htmlparser()
    def craw(self,root_url):
        count = 1
        self.urls.add_new_url(root_url)
        girl_dir = 'E:\girls2' #
        if not os.path.exists(girl_dir):  #
            os.mkdir(girl_dir)
        os.chdir(girl_dir)
        while self.urls.has_new_url():
            try:
                new_url=self.urls.get_new_url()
                print(new_url)
                html_cont=self.downloader.download(new_url)
                new_urls,all_img = self.parser.parse(new_url,html_cont)
                self.urls.add_new_urls(new_urls)
                for img in all_img:
                    src = img['src']
                    #print(src)
                    name = 'tupian' + str(count)
                    with open(name+ '.jpg','ab') as img_object:
                        img_content = urllib.request.urlopen(src).read()#
                        img_object.write(img_content) #
                        img_object.flush()
                    count += 1
            except urllib.request.URLError as e:
                print(e)
                
if __name__ == '__main__':
    root_url='http://iyangzi.com/?p=173'
    object_spider=Spidermain()
    object_spider.craw(root_url)
    print('craw end')