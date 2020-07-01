#updating produceSales.xlsx

import openpyxl

newPrice = {'Celery': 1.19, 'Garlic': 3.07, 'Lemon' : 1.27}


wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

for i in range(2,sheet.max_row+1):
    itemName = sheet['A' + str(i)].value
    if itemName in newPrice:
        sheet['B' + str(i)].value = newPrice[itemName]

wb.save('updatedProduceSales.xlsx')