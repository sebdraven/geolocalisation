import urllib2
import re
class dschield(object):
	
	def __init__(self,url):
		self.url=url	
	
	def response(self,ip):
		dschieldContent=urllib2.urlopen(self.url+ip)
		value=dschieldContent.read()
		patern='country= (\w+)'
		
		reg =re.compile(patern)
		m = reg.search(value)
		country=''
		if m:
			 country=m.group(1)
		patern='asname= (.+)'		
		reg =re.compile(patern)
		m = reg.search(value)
		asname=''
		if m:
			asname=m.group(1)		
		if country != '' and asname !='':		
			return (ip,country,asname)
