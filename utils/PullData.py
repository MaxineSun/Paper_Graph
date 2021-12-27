from crossref_commons.retrieval import get_entity
from crossref_commons.types import EntityType, OutputType

class PullData:	#transform this function as a class
	def __init__(self, doi):
		self.doi = doi

	def getInitials(self, str):	#Put getInitials brfore as a alone function instead of part of pullData
		allNames = str.split()
		initials = [names[0] for names in allNames]
		initialsProcessced = ". ".join(initials) + "."
		return initialsProcessced

	def pullData(self):
		try:
			self.art = get_entity(self.doi, EntityType.PUBLICATION, OutputType.JSON)
			if 'DOI' in self.art:
				doi1 = self.art[ 'DOI' ]
			else:
				doi1 = None

			if 'type' in self.art:
				typ = self.art[ 'type' ]   #book-chapter
			else:
				typ = 'None'

			if 'volume' in self.art:
				vol = self.art[ 'volume' ]
			else:
				vol = None

			if 'issue' in self.art:
				iss = self.art[ 'issue' ]
			else:
				iss = None

			if 'page' in self.art:
				pgs = self.art[ 'page' ]
			else:
				pgs = None

			if 'author' in self.art:
				aut__ = self.art[ 'author' ]
				aut = []
				for a in aut__:
					if 'given' in a:
						firstName = a[ 'given' ]
						aut.append(self.getInitials(firstName) + ' ' + a[ 'family' ])
					elif 'family' in a:
						aut.append(a['family'])
					else:
						aut = None
			else:
				aut = None

			if 'title' in self.art:
				tit = self.art[ 'title' ][ 0 ]
			else:
				tit = None

			if 'publisher' in self.art:
				pub = self.art[ 'publisher' ]
			else:
				pub = None

			if 'reference-count' in self.art:
				cit = self.art[ 'reference-count' ]
			else:
				cit = 'None'

			if 'container-title' in self.art and not len(self.art['container-title']) == 0:	#prevents empty lists
				jnl = self.art[ 'container-title' ][ 0 ]
			else:
				jnl = None

			if 'reference' in self.art:
				ref = self.art[ 'reference' ]
			else:
				ref = None

			if 'created' in self.art:
				ymd = self.art[ 'created' ][ 'date-time' ][ 0:10 ]
			else:
				ymd = None

			# if 'reference-count' in self.art:
			# 	rct = self.art[ 'reference-count' ]
			# else:
			# 	rct = None

			if 'ISSN' in self.art:
				issn = self.art[ 'ISSN' ]
			else:
				issn = None

			if 'ISBN' in self.art:
				isbn = self.art[ 'ISBN' ]
			else:
				isbn = None

			if 'publisher-location' in self.art:
				loc = self.art[ 'publisher-location' ]
			else:
				loc = None

			if 'URL' in self.art:
				url = self.art[ 'URL' ]
			else:
				url = None

			if 'editor' in self.art:
				edt = self.art[ 'editor' ]
			else:
				edt = None

			if 'article-number' in self.art:
				anm = self.art[ 'article-number' ]
			else:
				anm = None

			return doi1, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, issn, isbn, loc, url, edt, anm

		except:
			pass

