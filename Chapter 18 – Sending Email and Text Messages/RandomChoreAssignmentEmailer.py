import openpyxl, random
from openpyxl.utils import get_column_letter
chores = ['dishes', 'bathroom', 'vacuum', 'walk dog', 'dinner', 'shopping']

wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.active

to_do = {}

for col in range(1,3):
    for row in range(2, sheet.max_row):
        name = sheet['A'+str(row)].value
        email = sheet['B'+str(row)].value
        to_do.setdefault(name, {})
        to_do[name].setdefault(email, [])

