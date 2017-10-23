#coding:utf8
from bs4 import BeautifulSoup
import re
import urllib.parse

class HtmlParser():

	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		#/item/AE2%E 
		links = soup.find_all('a',href=re.compile(r'/item/[A-Za-z1-9\%][A-Za-z1-9\%]*'))#匹配所有的链接
		for link in links:
			new_url = link['href']  #查看链接网址
			new_full_url = urllib.parse.urljoin(page_url,new_url) #对链接网址进行拼接成完整网址 
			new_urls.add(new_full_url)
		return new_urls
	def _get_new_data(self,page_url,soup):
		res_data = {}

		#url
		res_data['url']=page_url

		#<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>>>"">
		title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1') #两次查询
		#print(title_node.get_text())
		res_data['title'] = title_node.get_text()

		#</div><div class="lemma-summary" label-module="lemmaSummary">
		summary_node=soup.find('div',class_='lemma-summary')
		#print(summary_node.get_text())
		res_data['summary'] = summary_node.get_text()
		
		return res_data
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return

		soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data


