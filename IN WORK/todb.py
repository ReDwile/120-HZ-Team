from openpyxl import load_workbook,Workbook
wbSearch=Workbook()
wbSearch=load_workbook('data/.xlsx')#сюда напиши название своего екселя
wsSearch=wbSearch.active

def todb():
    maxrow = wsSearch.max_row
    row =maxrow+1
    wsSearch.cell(row=row, column=1).value =  256382523
    wsSearch.cell(row=row, column=3).value = "lox"
    wsSearch.cell(row=row, column=4).value = "lastname"


