import openpyxl, random, smtplib

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog', 'dinner', 'shopping']

wb = openpyxl.load_workbook('duesRecords.xlsx')
sheet = wb.active

to_do = {}

for col in range(1,3):
    for row in range(2, sheet.max_row):
        name = sheet['A'+str(row)].value
        email = sheet['B'+str(row)].value
        to_do.setdefault(name, {})
        to_do[name].setdefault('email', email)
        to_do[name].setdefault('chores', [])

def choresAssignment(list, dict):
    new_list = list.copy()
    for person in dict:
        temp_chores = [chore for chore in new_list if chore not in dict[person]['chores']]
        chore = random.choice(temp_chores)
        new_list.remove(chore)
        dict[person]['chores'].append(chore)
    return dict

choresAssignment(chores,to_do)
choresAssignment(chores,to_do)

email = input("Please enter Your email address: ")
password = input("Please enter Your password: ")

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(email, password)

for person in to_do:
    email = to_do[person]['email']
    chores = ', '.join(to_do[person]['chores'])
    smtpObj.sendmail(email, 'Subject: Task to made\nDear {} You must make this tasks: {}, please'.format(person, chores))
smtpObj.quit()

