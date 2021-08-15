from FUNCTIONS import *

pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc.xlsx"
##df = pd.read_excel(pathTradeExport)
wb = load_workbook(pathTradeExport)
ws = wb.worksheets[2]

titles = ["A", "B", "C", "D", "E", "F"]
values = ["DATE" ,"TICKER", "TYPE", "PRICE" , "AMOUNT" , "TOTAL" ]

def prepareTitles():
    column = 1
    position = 0

    for _ in values:
            ws.cell(row=1, column=column).value = values[position]
            ws.column_dimensions[titles[position]].width = 22


            print(position)
            print(column)



            column = column + 1
            position = position + 1


    wb.save(pathTradeExport)

prepareTitles()