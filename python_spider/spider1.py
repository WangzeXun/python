#!/usr/bin/python3
# -*- coding: utf-8 -*-

import urllib.request
import http.cookiejar

url = 'http://www.baidu.com'

print('第一种方法')
response1 = urllib.request.urlopen(url)#直接请求
print(response1.getcode())
print(len(response1.read()))
#print(response1.read())

print('第二种方法')
request = urllib.request.Request(url)
request.add_header('user_agent','Mozilla/5.0')  #将爬虫伪装成Mozilla浏览器
response2 = urllib.request.urlopen(request)
print(response2.getcode())
print(len(response2.read()))

print('第三种方法')
cj=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
urllib.request.install_opener(opener) #使用带有cookie的urllib访问网页 
response3 = urllib.request.urlopen(url)
print(response3.getcode())
print(cj)
print(len(response3.read()))
#for i in range(1,1000):
print(response3.read())




