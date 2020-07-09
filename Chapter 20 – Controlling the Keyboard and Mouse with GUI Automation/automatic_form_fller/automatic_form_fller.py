#https://autbor.com/form
#size 1920x1080

import pyautogui, webbrowser, time

webbrowser.open("https://autbor.com/form")
time.sleep(2)
pyautogui.click(735,446)
pyautogui.write("Name")
pyautogui.press('tab')
pyautogui.write("Fear")
pyautogui.press('tab')
pyautogui.press('down')
pyautogui.press('down')
pyautogui.press('return')
time.sleep(1)
pyautogui.press('tab')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.write('comment')
time.sleep(1)
pyautogui.click('submit.png')
time.sleep(1)
pyautogui.click('next.png')
