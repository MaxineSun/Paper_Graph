from openpyxl import *
from utils.PullData import PullData

if __name__ == '__main__':
    wb = load_workbook('digCon.xlsx')
    ws = wb.active
    doirecord = []  #change variable name here to avoid conflicts between the doi in line20
    noDOI = []

    for i in range(2, 8):
        d = ws.cell(row = i, column = 12).value
        tit = ws.cell(row = i, column = 4).value
        if d:
            doirecord.append(d)
            print(d)
        else:
            noDOI.append(tit)

    for dx in doirecord:
        item = PullData(dx)
        doi, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, art, rct, issn, isbn, loc, url, edt, anm = item.pullData()

    for dx in doirecord:
        item = PullData(dx)
        doi, typ, vol, iss, pgs, aut, tit, pub, cit, jnl, ref, ymd, art, rct, issn, isbn, loc, url, edt, anm = item.pullData()
