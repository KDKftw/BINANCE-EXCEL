from FUNCTIONS import *

pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc.xlsx"
wb = load_workbook(pathTradeExport)
ws = wb.worksheets[1]
ws.cell(row=x, column=6).value= getTotalpaid(x)
wb.save(pathTradeExport)
