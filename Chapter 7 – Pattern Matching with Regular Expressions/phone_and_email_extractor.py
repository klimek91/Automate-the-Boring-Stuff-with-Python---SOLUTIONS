import re, pyperclip

phoneRegex = re.compile(r"""(
(\(?\+?(\d\d))\))?          #country code
(\d\d\d)             #3 first digits
(\s | - | \.)?        #separator
(\d\d\d)
(\s | - | \.)?
(\d\d\d)""", re.VERBOSE)

emailRegex = re.compile(r"""(
[a-zA-Z0-9_.%+-]+      #prefix
@
[a-zA-Z0-9-.]+      #domain
(\.[a-zA-Z]{2,5})#after dot
)""", re.VERBOSE)

