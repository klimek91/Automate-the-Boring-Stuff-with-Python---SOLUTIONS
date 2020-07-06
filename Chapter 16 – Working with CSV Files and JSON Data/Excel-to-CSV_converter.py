import openpyxl
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('kalkulator.xlsx')

print(len(wb.sheetnames))

sheet = wb.active

rows = []
for rowNum in range(sheet.max_row):
    row = []
    for colNum in range(sheet.max_column):
        cell = sheet[get_column_letter(colNum+1) + str(rowNum+1)].value
        row.append(cell)
    rows.append(row)

print(rows)