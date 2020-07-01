#!python

import openpyxl, sys
from openpyxl.utils import get_column_letter

if len(sys.argv) > 1:
    wb = openpyxl.Workbook()
    sheet = wb.active

    size = int(sys.argv[1]) + 1

    for row in range(1,size):
        sheet['A'+str(row+1)] = row
        sheet[get_column_letter(row+1)+str(1)] = row
        for col in range(1,size):
            sheet[get_column_letter(col+1)+str(row+1)] = row*col


    wb.save('multiplication_table.xlsx')
    wb.close()