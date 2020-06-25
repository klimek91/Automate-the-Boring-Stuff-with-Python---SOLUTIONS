#! python3
# updatable_multiclipboard.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe updatable_multiclipboard.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe updatable_multiclipboard.pyw <keyword> - Loads keyword to clipboard.
#        py.exe updatable_multiclipboard.pyw list - Loads all keywords to clipboard.

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')


if len(sys.argv) > 2 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print("No such keyword, try 'list' to check keywords")

mcbShelf.close()