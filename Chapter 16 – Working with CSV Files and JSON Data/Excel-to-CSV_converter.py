import openpyxl, csv, os
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('kalkulator.xlsx')

sheet = wb.active

outFile = open('kalkulator_{}.csv'.format(wb.sheetnames[0]),'w', newline='')
outWriter = csv.writer(outFile)
for rowNum in range(sheet.max_row):
    row = []
    for colNum in range(sheet.max_column):
        cell = sheet[get_column_letter(colNum+1) + str(rowNum+1)].value
        row.append(cell)
    outWriter.writerow(row)
outFile.close()