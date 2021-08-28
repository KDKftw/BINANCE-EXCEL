from create_sheets_with_tickers_name import createSheetsTickers
from TRYING import copyValuesToSheets
from SetupFunctions import prepareTitlesAllSheets
from delete_empty_rows import deleteInAllSheets

pathTradeExport = r"C:\Users\KDK\Desktop\ALLINONE - Copy.xlsx"

createSheetsTickers(pathTradeExport)
copyValuesToSheets(pathTradeExport)
prepareTitlesAllSheets(pathTradeExport)
deleteInAllSheets(pathTradeExport)