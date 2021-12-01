import urllib3
import json
http = urllib3.PoolManager()

class PullDoi:	
	def __init__(self, tit):
		self.tit = tit


	def GenerateLink(self):
		link = 'https://api.crossref.org/works?rows=5&query.title='
		length = len(self.tit)
		for i in range(length):
			c = ord(tit[i])
			if((c>=48 & c<=57)|(c>=65 & c<=90)|(c>=97 & c<=122)):
				link = link + tit[i]
			elif(c==32):
				link = link + '+'
		return link
	
	def PullDoi(self):
		url = self.GenerateLink()
		result = http.request('GET', url)
		result_dict = json.loads(result)
		result_dict['DOI']

		return doi


	# r = http.request('GET','https://search.crossref.org/?q=Compounding+Features+of+Special+Molding+Mixes+for+3D+Printing+Technologyn&from_ui=yes')
