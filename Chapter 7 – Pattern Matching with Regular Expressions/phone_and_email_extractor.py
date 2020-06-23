import re, pyperclip

phoneRegex = re.compile(r"""(
(\(?\+?(\d\d))\))?          #country code
(\d\d\d)             #3 first digits
(\s | - | \.)?        #separator
(\d\d\d)
(\s | - | \.)?
(\d\d\d)""", re.VERBOSE)