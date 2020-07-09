import pyautogui,pyperclip

fw = pyautogui.getWindowsWithTitle('Notatnik')[0]
fw.activate()
fw.maximize()
pyautogui.click(100,100)
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')
text = pyperclip.paste()

print(text)