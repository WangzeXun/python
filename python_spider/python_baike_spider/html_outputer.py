#coding:utf8

class HtmlOutputer():

	def __init__(self):
		self.datas = []

	def collect_data(self,data):
		if	data is None:
			return
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html','w',encoding='utf-8')
		
		fout.write('<html>')
		fout.write("<meta charset=\"utf-8\" />")
		fout.write('<body>')
		fout.write('<table>')  #表格

		for data in self.datas:
			fout.write('<tr>')
			fout.write('<td>%s</td>'% str(data['url'].encode('utf-8'),'utf-8'))
			fout.write('<td>%s</td>'% str(data['title'].encode('utf-8'),'utf-8'))
			fout.write('<td>%s</td>'% str(data['summary'].encode('utf-8'),'utf-8'))
			fout.write('</tr>')

		fout.write('</table>')
		fout.write('</body>')
		fout.write('</html>')
		fout.close()


