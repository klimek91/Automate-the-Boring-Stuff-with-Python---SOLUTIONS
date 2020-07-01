#data from censuspopdata.xlsx
#1. Reads the data from the Excel spreadsheet
#2. Counts the number of census tracts in each county
#3. Counts the total population of each county
#4. Prints the results

import openpyxl, pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active

state = {}

for i in range(2, sheet.max_row+1):
    state_name = sheet['B'+str(i)].value
    county_name = sheet['C'+str(i)].value
    pop = sheet["D"+str(i)].value

    state.setdefault(state_name, {})
    state[state_name].setdefault(county_name, {'count':0, 'pop':0})

    state[state_name][county_name]['count'] +=1
    state[state_name][county_name]['pop'] += pop

print('allData = ' + pprint.pformat(state))
