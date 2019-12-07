from openpyxl import load_workbook,Workbook
wbSearch=Workbook()
wbSearch=load_workbook('data/.xlsx')#сюда напиши название своего екселя
wsSearch=wbSearch.active

def todb(id,name,lastname):
    maxrow = wsSearch.max_row
    row =maxrow+1
    wsSearch.cell(row=row, column=1).value=id
    wsSearch.cell(row=row, column=3).value = name
    wsSearch.cell(row=row, column=4).value = lastname


