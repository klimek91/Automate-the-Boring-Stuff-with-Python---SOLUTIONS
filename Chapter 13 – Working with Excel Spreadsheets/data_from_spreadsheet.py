#data from censuspopdata.xlsx
#1. Reads the data from the Excel spreadsheet
#2. Counts the number of census tracts in each county
#3. Counts the total population of each county
#4. Prints the results

import openpyxl, pprint

sheet = openpyxl.load_workbook('censuspopdata.xlsx')
wb = sheet.active

state = {}

for i in range(2, wb.max_row+1):
    state_name = wb['B'+str(i)].value
    county_name = wb['C'+str(i)].value
    pop = wb["D"+str(i)].value

    state.setdefault(state_name, {})
    state[state_name].setdefault(county_name, {'count':0, 'pop':0})

    state[state_name][county_name]['count'] +=1
    state[state_name][county_name]['pop'] += pop

print('allData = ' + pprint.pformat(state))
