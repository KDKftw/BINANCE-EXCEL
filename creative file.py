import pandas as pd
import time
import openpyxl
from selenium import webdriver
from openpyxl import load_workbook, cell
pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc2.xlsx"
pathTradeExport2 = r"C:\Users\KDK\Desktop\12.6 - 1.8 2021 ALL TRADES2.xlsx"
df = pd.read_excel(pathTradeExport2)
wb = load_workbook(pathTradeExport2)
ws = wb.worksheets[0]

skipTicker = ["EURBUSD"]

##starting everytime on row 2 based on bnc export
def createSheetsTickers():
    numeroOfRows = ws.max_row
    x=2
    while numeroOfRows > 1:
      tickerName = ws.cell(row=x, column=2).value
      ##print(tickerName)
      if tickerName in (wb.sheetnames):
          pass
      else:
          wb.create_sheet(tickerName)
      x = x+1
      numeroOfRows = numeroOfRows-1
      wb.save(pathTradeExport2)

createSheetsTickers()