from crossref_commons.retrieval import get_entity
from crossref_commons.types import EntityType, OutputType

class PullData:
	def __init__(self, doi):
		self.doi = doi

	def getInitials(self, str):
		allNames = str.split()
		initials = [names[0] for names in allNames]
		initialsProcessced = ". ".join(initials) + "."
		return initialsProcessced

	def pullData(self, doi):
		art = get_entity(doi,
						 EntityType.PUBLICATION,
						 OutputType.JSON)

		if 'DOI' in art:
			doi = art[ 'DOI' ]
		else:
			doi = None

		if 'type' in art:
			typ = art[ 'type' ]   #book-chapter
		else:
			typ = 'None'

		if 'volume' in art:
			vol = art[ 'volume' ]
		else:
			vol = None

		if 'issue' in art:
			iss = art[ 'issue' ]
		else:
			iss = None

		if 'page' in art:
			pgs = art[ 'page' ]
		else:
			pgs = None

		if 'author' in art:
			aut__ = art[ 'author' ]

			aut = []
			for a in aut__:
				firstName = a[ 'given' ]
				aut.append(self.getInitials(firstName) + ' ' + a[ 'family' ])

		else:
			aut = None


		if 'title' in art:
			tit = art[ 'title' ][ 0 ]
		else:
			tit = None

		if 'publisher' in art:
			pub = art[ 'publisher' ]
		else:
			pub = None

		if 'reference-count' in art:
			cit = art[ 'reference-count' ]
		else:
			cit = 'None'

		if 'container-title' in art and not len(art['container-title']) == 0: #prevents empty lists
			jnl = art[ 'container-title' ][ 0 ]
		else:
			jnl = None

		if 'reference' in art:
			ref = art[ 'reference' ]
		else:
			ref = None

		if 'created' in art:
			ymd = art[ 'created' ][ 'date-time' ][ 0:10 ]
		else:
			ymd = None

		if 'reference-count' in art:
			rct = art[ 'reference-count' ]
		else:
			rct = None

		if 'ISSN' in art:
			issn = art[ 'ISSN' ]
		else:
			issn = None

		if 'ISBN' in art:
			isbn = art[ 'ISBN' ]
		else:
			isbn = None

		if 'publisher-location' in art:
			loc = art[ 'publisher-location' ]
		else:
			loc = None

		if 'URL' in art:
			url = art[ 'URL' ]
		else:
			url = None

		if 'editor' in art:
			edt = art[ 'editor' ]
		else:
			edt = None

		if 'article-number' in art:
			anm = art[ 'article-number' ]
		else:
			anm = None

		return doi, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, art, rct, issn, isbn, loc, url, edt, anm
