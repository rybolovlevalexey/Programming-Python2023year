import openpyxl

wb = openpyxl.load_workbook("DEALER_PRICE_LIST.xlsx")
print(wb["A1"])