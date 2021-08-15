import openpyxl
from openpyxl import load_workbook
pathTradeExport2 = r"C:\Users\KDK\Desktop\FOR testing binc.xlsx"
pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc2.xlsx"
def getDate(x):
    wb = load_workbook(pathTradeExport)
    ws = wb.worksheets[0]
    date = ws.cell(row=x, column=1).value
    ##print(date)
    return (date)

def getTicker(x):  ##getTickerName.. x=row parametr x, column=Market , BTCBUSD
        wb = load_workbook(pathTradeExport)
        ws = wb.worksheets[0]
        ticker = ws.cell(row=x, column=2).value
        ##print(ticker)
        return (ticker)


def copyValuesToSheets():
        wb = load_workbook(pathTradeExport)
        ws = wb.worksheets[0]
        numeroOfRows = ws.max_row
        print(numeroOfRows)
        x = 2
        while numeroOfRows > 1:
            sheetPosition = wb.worksheets.index(wb[getTicker(x)])
            ws = wb.worksheets[sheetPosition]
            ws.cell(row=x, column=1).value = getDate(x)

            x = x + 1
            numeroOfRows = numeroOfRows - 1
            wb.save(pathTradeExport)
        wb.save(pathTradeExport)


copyValuesToSheets()