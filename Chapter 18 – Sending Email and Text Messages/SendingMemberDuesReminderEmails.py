import smtplib, openpyxl
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.active

dues = {}

for col in range(1,sheet.max_column+1):
    for row in range(1,sheet.max_row):
        if sheet[get_column_letter(col) + str(row)].value == None:
            dues.setdefault(sheet['A'+str(row)].value, {})
            dues[sheet['A'+str(row)].value].setdefault(sheet['B'+str(row)].value, [])
            dues[sheet['A' + str(row)].value][sheet['B'+str(row)].value].append(sheet[get_column_letter(col) + "1"].value)

            #print(sheet[get_column_letter(col) + str(row)])

print(dues)
