import urllib3
http = urllib3.PoolManager()

class PullDoi:	
	def __init__(self, tit):
		self.tit = tit

	def GenerateLink(self):
		link = 'https://api.crossref.org/works?rows=5&query.title='
		length = len(self.tit)
		for i in range(length):
			c = ord(self.tit[i])
			if((c>=48 & c<=57)|(c>=65 & c<=90)|(c>=97 & c<=122)):
				link = link + self.tit[i]
			elif(c==32):
				link = link + '+'
		# link = link + '&from_ui=yes'
		return link


	def PullDoi(self):
		url = self.GenerateLink()
		result = http.request('GET', url)
		# r = http.request('GET', 'https://api.crossref.org/works?rows=5&query.title=Advances+in+building+technology')
		strr = str(result.data, encoding="utf-8")
		global false, null, true
		false = null = true = ""
		dictr = eval(strr)
		odoi = dictr["message"]["items"][0]["DOI"]
		doi = odoi.replace('\\','')
		print(doi)
		return doi


	# r = http.request('GET','https://search.crossref.org/?q=Compounding+Features+of+Special+Molding+Mixes+for+3D+Printing+Technologyn&from_ui=yes')
