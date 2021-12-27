from openpyxl import *
from utils.PullData import PullData
from utils.PullDoi import PullDoi
from utils.Creating_Edge import *

if __name__ == '__main__':
    wb = load_workbook('digCon.xlsx')
    ws = wb.active
    doirecord = []  # change variable name here to avoid conflicts between the doi in line20
    noDOI = []

    for i in range(2, 8):
        d = ws.cell(row=i, column=12).value
        tit = ws.cell(row=i, column=4).value
        if d:
            doirecord.append(d)
        else:
            noDOI.append(tit)

    for a in noDOI:
        item = PullDoi(a).PullDoi()
        doirecord.append(item)

    g = Creating_Graph(doirecord)
    g.Create_Graph()
    print(g.Graph.number_of_nodes())
    print(g.Graph.number_of_edges())

    print("  ")
