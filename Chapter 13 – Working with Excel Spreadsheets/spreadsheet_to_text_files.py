import openpyxl

wb = openpyxl.load_workbook('textToExcel.xlsx')
sheet = wb.active

for row in range(sheet.max_row):
    file = open('textFromExcel01.txt', 'a')
    file.write(sheet['A'+str(row+1)].value)
