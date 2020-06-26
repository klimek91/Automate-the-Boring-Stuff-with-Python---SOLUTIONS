#! python3
import pyperclip

Text = """Lists of animals
Lists of aquarium life
Lists of biologists by author abbreviation
Lists of cultivars"""


text = pyperclip.paste()

lines = text.split('\n')
withMarkups = ''

for line in lines:
    withMarkups += '* '+line + '\n'

pyperclip.copy(withMarkups)