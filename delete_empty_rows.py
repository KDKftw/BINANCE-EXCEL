from openpyxl import load_workbook
pathTradeExport = r"C:\Users\KDK\Desktop\FOR testing binc2.xlsx"
wb = load_workbook(pathTradeExport)
ws = wb.worksheets[1]

index_row = []

# loop each row in column A
for i in range(1, ws.max_row):
    # define emptiness of cell
    if ws.cell(i, 1).value is None:
        # collect indexes of rows
        index_row.append(i)

# loop each index value
for row_del in range(len(index_row)):
    ws.delete_rows(idx=index_row[row_del], amount=1)
    # exclude offset of rows through each iteration
    index_row = list(map(lambda k: k - 1, index_row))
    wb.save(pathTradeExport)