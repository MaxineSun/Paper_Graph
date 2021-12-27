import urllib3
http = urllib3.PoolManager()
r = http.request('GET','https://api.crossref.org/works?rows=5&query.title=Advances+in+building+technology')
strr = str(r.data,encoding = "utf-8")
global false, null, true
false = null = true = ""
dictr=eval(strr)
print(dictr["message"]["items"][0]["DOI"])
