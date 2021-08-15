

from FUNCTIONS import wb

x=7
def getTicker(x):  ##getTickerName.. x=row parametr x, column=Market , BTCBUSD
    ws = wb.worksheets[0]
    ticker = ws.cell(row=x, column=2).value
    print(ticker)
    return (ticker)


sheetPosition = wb.worksheets.index(wb[getTicker(x)])
print(sheetPosition)