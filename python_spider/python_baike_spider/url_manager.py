#coding:utf8
class UrlManager():

	def __init__(self):		
		self.new_urls=set() #设定要爬虫的url和已经爬虫过的url
		self.old_urls=set()
	def add_new_url(self,url):
		if url is None:
			return
		if url not in self.new_urls and url not in self.old_urls:
			self.new_urls.add(url)

	def has_new_url(self):
		return len(self.new_urls) != 0

	def get_new_url(self):
		new_url =self.new_urls.pop() #集合元素是无序的。pop返回的是集合中任意一个，并将其删除 
		self.old_urls.add(new_url)
		return new_url

	def add_new_urls(self,urls):
		if urls is None or len(urls) == 0:
			return
		for url in urls:
			self.add_new_url(url)
		
