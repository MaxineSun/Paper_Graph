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
			c = ord(self.tit[i])
			if((c>=48 & c<=57)|(c>=65 & c<=90)|(c>=97 & c<=122)):
				link = link + self.tit[i]
			elif(c==32):
				link = link + '+'
		link = link + '&from_ui=yes'
		return link

	# def json(self) -> Dict[str, Any]:
	# 	"""Convert the response data to JSON.
    #     If the response data is not valid JSON, an error will be raised.
    #     Returns:
    #         The JSON data loaded into a Python dictionary.
    #     """
	# 	if isinstance(self.data, urllib3.HTTPResponse):
	# 		return json.loads(self.data.data)
	# 	try:
	# 		data = ast.literal_eval(self.data)
	# 	except Exception as e:
	# 		log.debug(f'failed literal eval of data {self.data} ({e})')
	# 		data = json.loads(self.data)
	# 	return data

	def PullDoi(self):
		url = self.GenerateLink()
		result = http.request('GET', url)
		print(result.data)
		# result_dict = json.loads(result)
		# result_dict['DOI']

		return doi


	# r = http.request('GET','https://search.crossref.org/?q=Compounding+Features+of+Special+Molding+Mixes+for+3D+Printing+Technologyn&from_ui=yes')
