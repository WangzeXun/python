#coding:utf-8

import urllib.request
from bs4 import BeautifulSoup
import re,os,time

root_url='http://iyangzi.com/?p=173'
new_urls=set() #新增的网页集合
old_urls=set() #爬取过的网页集合

girl_dir = 'E:\girls' #
if not os.path.exists(girl_dir):  #
    os.mkdir(girl_dir)
os.chdir(girl_dir)
count=1
new_urls.add(root_url)
start_time=time.time()
while len(new_urls)!=0:
    new_url=new_urls.pop()
    old_urls.add(new_url)
    print(new_url)
    try:
        response=urllib.request.urlopen(new_url)
        if response.getcode() == 200:
            soup = BeautifulSoup(response.read(),'html.parser',from_encoding='utf-8')
            
            urls=soup.find_all('a',href=re.compile(r'http://iyangzi.com/\?p=\d+$'))#以数字为结尾的网址
            for url in urls:
                if url['href'] not in new_urls and url['href'] not in old_urls:
                    new_urls.add(url['href'])
            all_img = soup.find('div',class_='post-content').find_all('img')
            for img in all_img:
                src = img['src']
                #print(src)
                name = 'tupian' + str(count)
                with open(name+ '.jpg','ab') as img_object:
                    img_content = urllib.request.urlopen(src).read()#
                    img_object.write(img_content) #
                    img_object.flush()
                count += 1
            if count ==1000:  #爬取1000张图片
                break;
    except urllib.request.URLError as e:
        print(e)
end_time=time.time()
print('craw end')               
print('The total time is: %s'%str(end_time-start_time))
    