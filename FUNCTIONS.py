from openpyxl import load_workbook

pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc.xlsx"
pathTradeExport2 = r"C:\Users\KDK\Desktop\12.6 - 1.8 2021 ALL TRADES2.xlsx"
wb = load_workbook(pathTradeExport)


def getDate(x):         ##class v ktery se bude dedit ws = wb wrksheets ?
    ws = wb.worksheets[0]
    date = ws.cell(row=x, column=1).value
    ##print(date)
    return (date)


def getTicker(x):                          ##getTickerName.. x=row parametr x, column=Market , BTCBUSD
        ws = wb.worksheets[0]
        ticker = ws.cell(row=x, column=2).value
        ##print(ticker)
        return(ticker)


def getTypeoftrade(x):                  #sell or buy
    ws = wb.worksheets[0]
    Typeoftrade = ws.cell(row=x, column=3).value
    print(Typeoftrade)
    return (Typeoftrade)

def getPrice(x):                  #price
    ws = wb.worksheets[0]
    price = ws.cell(row=x, column=4).value
    print(price)
    return (price)


def getAmount(x):                  #amount
    ws = wb.worksheets[0]
    amount = ws.cell(row=x, column=5).value
    print(amount)
    return (amount)

def getTotalpaid(x):                  #totalPaid
    ws = wb.worksheets[0]
    total = ws.cell(row=x, column=6).value
    print(total)
    return (total)
x=4


def getAllInfo(x):
    getDate(x)
    getTicker(x)
    getTypeoftrade(x)
    getPrice(x)
    getAmount(x)
    getTotalpaid(x)


getAllInfo(2)