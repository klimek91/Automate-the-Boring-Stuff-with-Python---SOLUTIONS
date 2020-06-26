#! python3
# extending_mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe extending_mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe extending_mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe extending_mcb.pyw list - Loads all keywords to clipboard.
#        py.exe extending_mcb.pyw delete all - delete all keywords from clipboard.
#        py.exe extending_mcb.pyw delete <keyword> - delete keyword from clipboard

import sys, pyperclip, shelve

mcbShelf = shelve.open('mcb')


if len(sys.argv) > 2 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) > 2 and sys.argv[1].lower() == 'delete' and sys.argv[2].lower() != 'all':
    del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete' and sys.argv[2].lower() == 'all':
    mcbShelf.clear()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    else:
        print("No such keyword, try 'list' to check keywords")

mcbShelf.close()