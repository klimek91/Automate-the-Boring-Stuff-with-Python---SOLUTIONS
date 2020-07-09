#size 1920x1080

import pyautogui, webbrowser, time, openpyxl

wb = openpyxl.load_workbook('data_for_the_form.xlsx')
sheet = wb.active

webbrowser.open("https://autbor.com/form")

for row in range(2, sheet.max_row +1):
    name = sheet['A'+str(row)].value
    fear = sheet['B'+str(row)].value
    power = sheet['C' + str(row)].value
    robocop = sheet['D' + str(row)].value
    comment = sheet['E' + str(row)].value

    time.sleep(2)
    pyautogui.click(735, 446)
    pyautogui.write(name),
    pyautogui.press('tab')
    pyautogui.write(fear)
    pyautogui.press('tab')
    if power.lower() == "wand":
        pyautogui.press('down')
    elif power.lower() == "amulet":
        pyautogui.press('down'), pyautogui.press('down')
    elif power.lower() == "ball":
        pyautogui.press('down'), pyautogui.press('down'), pyautogui.press('down')
    elif power.lower() == "money":
        pyautogui.press('down'), pyautogui.press('down'), pyautogui.press('down'), pyautogui.press('down')
    pyautogui.press('return')
    time.sleep(0.5)
    pyautogui.press('tab')
    if robocop == 1:
        pyautogui.press('right')
        pyautogui.press('left')
    elif robocop == 2:
        pyautogui.press('right')
    elif robocop == 3:
        pyautogui.press('right'), pyautogui.press('right')
    elif robocop == 4:
        pyautogui.press('right'), pyautogui.press('right'), pyautogui.press('right')
    elif robocop == 5:
        pyautogui.press('right'), pyautogui.press('right'), pyautogui.press('right'), pyautogui.press('right')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(comment)
    time.sleep(0.5)
    pyautogui.click('submit.png')
    if row == sheet.max_row:
        print("All forms completed")
        break
    time.sleep(0.5)
    pyautogui.click('next.png')
