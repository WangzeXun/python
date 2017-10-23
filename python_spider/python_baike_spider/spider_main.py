#!/usr/bin/python3
#coding:utf-8
import url_manager,html_downloader,html_parser,html_outputer 

class SpiderMain():
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()
	def craw(self,root_url):
		count = 1
		self.urls.add_new_url(root_url)  #将初始url加入进行循环
		while self.urls.has_new_url(): #判断是否有可用的url
			try:  #可能url无效或者不能访问
				#print(self.urls.new_urls)
				new_url = self.urls.get_new_url() #url获取
				print('craw %d: %s'%(count,new_url))
				html_cont = self.downloader.download(new_url)  #html下载器
				new_urls,new_data = self.parser.parse(new_url,html_cont)  #html解析器，返回新的url以爬虫以及当前爬虫内容
				self.urls.add_new_urls(new_urls) #添加解析url
				self.outputer.collect_data(new_data) #添加解析内容
				#print(new_urls)
				#print('\n')
				if count == 100: #爬虫100个url
					break;
				count = count+1
			except:
				print('craw failed')
		self.outputer.output_html()  #输出爬虫内容

if __name__ == '__main__':
	root_url='https://baike.baidu.com/item/Python/407313?fr=aladdin'
	object_spider=SpiderMain()
	object_spider.craw(root_url)
