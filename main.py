from openpyxl import *
from utils.PullData import PullData

if __name__ == '__main__':
    wb = load_workbook('digCon.xlsx')
    ws = wb.active
    doi = []
    noDOI = []

    for i in range(2, 8):
        d = ws.cell(row = i, column = 12).value
        if d:
            doi.append(d)
            print(d)
        else:
            noDOI.append(d)

    for dx in doi:
        item = PullData(doi)
        doi, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, art, rct, issn, isbn, loc, url, edt, anm = item.pullData(doi)
