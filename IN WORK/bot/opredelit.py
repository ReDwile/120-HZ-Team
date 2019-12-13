import datetime
from openpyxl import load_workbook



def opredelit():
    wb = load_workbook('Data/test.xlsx')
    wbSearch = wb
    wsSearch = wbSearch.active
    now = datetime.datetime.now()
    value_1 = wsSearch.cell(row=wsSearch.max_row , column=2)
    value_2 = wsSearch.cell(row=wsSearch.max_row, column=3)
    value_3 = wsSearch.cell(row=wsSearch.max_row, column=4)
    if now.day > value_1 & now.month==value_2 & now.year == value_3:
        return ()# ретёрни что нужно
    elif now.day < value_1:
        return ()# здесь ретёрни тоже самое что в перовм пункте
    else:
        return None
