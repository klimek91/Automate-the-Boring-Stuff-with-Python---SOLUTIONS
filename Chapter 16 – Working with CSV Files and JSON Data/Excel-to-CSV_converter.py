import openpyxl, csv, os
from openpyxl.utils import get_column_letter

for excelFile in os.listdir(os.getcwd()):
    if excelFile.endswith('.xlsx'):

        wb = openpyxl.load_workbook(excelFile)

        sheet = wb.active
        print(sheet.max_row, sheet.max_column)
        outFile = open('{}.csv'.format(excelFile.replace('.xlsx','_new.csv')),'w', newline='')
        outWriter = csv.writer(outFile)
        for rowNum in range(sheet.max_row):
            row = []
            for colNum in range(sheet.max_column):
                cell = sheet[get_column_letter(colNum+1) + str(rowNum+1)].value
                row.append(cell)
            outWriter.writerow(row)
        outFile.close()