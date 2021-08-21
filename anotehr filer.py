def getTypeoftrade(x):                  #sell or buy
    wb = load_workbook(pathTradeExport)
    ws = wb.worksheets[0]
    Typeoftrade = ws.cell(row=x, column=3).value
    print(Typeoftrade)
    return (Typeoftrade)

    def getTicker(x):  ##getTickerName.. x=row parametr x, column=Market , BTCBUSD
        wb = load_workbook(pathTradeExport)
        ws = wb.worksheets[0]
        ticker = ws.cell(row=x, column=2).value
        ##print(ticker)
        return (ticker)

def getDate(x):
    wb = load_workbook(pathTradeExport)
    ws = wb.worksheets[0]
    date = ws.cell(row=x, column=1).value
    ##print(date)
    return (date)


from FUNCTIONS import wb

x=7
def getTicker(x):  ##getTickerName.. x=row parametr x, column=Market , BTCBUSD
    ws = wb.worksheets[0]
    ticker = ws.cell(row=x, column=2).value
    print(ticker)
    return (ticker)


sheetPosition = wb.worksheets.index(wb[getTicker(x)])
print(sheetPosition)