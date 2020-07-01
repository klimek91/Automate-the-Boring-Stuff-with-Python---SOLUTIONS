#!python

import openpyxl, sys
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('test.xlsx')
sheet = wb.active

n = 3
m = 2

for row in range(sheet.max_row+m,n,-1):
    for col in range(1,sheet.max_column+1):
        sheet[get_column_letter(col) + str(row)].value = sheet[get_column_letter(col) + str(row-m)].value

wb.save('updTest.xlsx')