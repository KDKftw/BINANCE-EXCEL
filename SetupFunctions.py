##from FUNCTIONS import *
from openpyxl import load_workbook

pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc3.xlsx"
##df = pd.read_excel(pathTradeExport)
wb = load_workbook(pathTradeExport)
##ws = wb.worksheets[2]
##"TICKER","B",
titles = ["A",  "C", "D", "E", "F"]
values = ["DATE" , "TYPE", "PRICE" , "AMOUNT" , "TOTAL" ]

sheet_number = len(wb.worksheets)

def prepareTitles(ws):
    column = 1
    position = 0
    sheet_number = len(wb.worksheets)
    print(sheet_number)
    for _ in values:
                ##sheet_number = sheet_number - 1
                ##ws = wb.worksheets[sheet_number]
                ws.cell(row=1, column=column).value = values[position]
                ws.column_dimensions[titles[position]].width = 22


                ##print(position)
                ##print(column)
                print(sheet_number)

                ##sheet_number = sheet_number - 1
                column = column + 1
                position = position + 1
                ##wb.save(pathTradeExport)


    wb.save(pathTradeExport)

for ws in wb.worksheets:
    sheet_number=sheet_number-1
    ws = wb.worksheets[sheet_number]
    prepareTitles(ws)

