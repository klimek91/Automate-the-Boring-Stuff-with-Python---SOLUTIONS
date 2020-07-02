import openpyxl, os

file1= open('text.txt')
lines1 = file1.readlines()
file2 = open('text2.txt')
lines2 = file2.readlines()

wb = openpyxl.Workbook()
sheet = wb.active

for row in range(len(lines1)):
        sheet['A'+str(row+1)].value = lines1[row]

for row in range(len(lines2)):
        sheet['B'+str(row+1)].value = lines2[row]

wb.save("textToExcel.xlsx")