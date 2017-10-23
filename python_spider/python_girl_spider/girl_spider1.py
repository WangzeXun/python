#!/usr/bin/python3
#conding:utf-8

import os
import urllib.request
from bs4 import BeautifulSoup
import re

root_url = 'http://iyangzi.com/?p=169'
#root_url = 'https://user.qzone.qq.com/991773508/main'
try:
	reques=urllib.request.Request(root_url)
	reques.add_header('user_agent','Mozilla/5.0')  #将爬虫伪装成Mozilla浏览器
	response = urllib.request.urlopen(reques)
	#response = urllib.request.urlopen(root_url)
	#print(response.getcode())
	if response.getcode() == 200:
		girl_dir = 'E:\girls1' #
		if not os.path.exists(girl_dir):  #
			os.mkdir(girl_dir)
		os.chdir(girl_dir)
		soup = BeautifulSoup(response.read(),'html.parser',from_encoding='utf-8')
		all_img = soup.find('div',class_='post-content').find_all('img')
		#all_img = soup.find('li',class_='f-single f-s-s').find_all('img')#re.compile(r'<img src="http://(.*)" style='))
		#<div class="imgwall-item imgwall-item-t4-l" style="cursor: default;"> <a href="javascript:;"><img
		count = 1
		for img in all_img:
			src = img['src']
			print(src)
			name = 'tupian' + str(count)
			with open(name+ '.jpg','ab') as img_object:
				img_content = urllib.request.urlopen(src).read()#
				
				img_object.write(img_content) #
				img_object.flush()
			if count ==100:
				break;
			count +=1

			
except urllib.request.URLError as e:
	print(e)
print('craw end')
