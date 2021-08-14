from openpyxl import load_workbook, cell

pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc.xlsx"
ticker = "dot"
wb = load_workbook(pathTradeExport)


class Trade:
    def __init__(self, ticker):
        self.ticker = ticker()



    def getTicker(self, x):
        ws = wb.worksheets[0]
        ticker = ws.cell(row=x, column=2).value
        print(ticker)
        return(ticker)





def getDate(x):
    ws = wb.worksheets[0]
    date = ws.cell(row=x, column=1).value
    print(date)
    return (date)


def getTicker2(x):                          ##getTickerName.. x=row parametr x, column=Market , BTCBUSD
        ws = wb.worksheets[0]
        ticker = ws.cell(row=x, column=2).value
        print(ticker)
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
    getTicker2(x)
    getTypeoftrade(x)
    getPrice(x)
    getAmount(x)
    getTotalpaid(x)


getAllInfo(3)