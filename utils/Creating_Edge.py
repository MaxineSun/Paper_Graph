import networkx as nx
from utils.PullData import PullData

class Creating_Graph:
    def __init__(self, DoiList):
        self.DoiLIst = DoiList
        self.Graph = Graph = nx.DiGraph()

    def Create_node(self, item):
        try:
            pdoi, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, issn, isbn, loc, url, edt, anm = PullData(
                item).pullData()
            self.Graph.add_node(item, DOI=pdoi, type=typ, volume=vol, issue=iss, page=pgs, author=aut, title=tit,
                           publisher=pub, reference_count=cit, container_title=jnl, reference=ref, created=ymd,
                           ISSN=issn, ISBN=isbn, publisher_location=loc, URL=url, editor=edt, article_number=anm)
        except:
            return 1

    def Create_Graph(self):
        for item in self.DoiLIst:
            self.Create_node(item)
        for item in self.DoiLIst:
            pdoi, _, _, _, _, aut, tit, _, cit, _, ref, _, _, _, _, _, _, _ = PullData(item).pullData()
            cdoi=' '
            for i in range(cit):
                if 'DOI' in ref[i]:
                    cdoi = ref[i]['DOI']
                if cdoi != ' ':
                    if cdoi in self.DoiLIst:
                        self.Graph.add_edge(item, cdoi)
                        cdoi = ' '
                    else:
                        print(cdoi)
                        fig = 0
                        fig = self.Create_node(cdoi)
                        if(fig == 0):
                            self.Graph.add_edge(item, cdoi)
                        cdoi = ' '