import re, pyperclip


text = str(pyperclip.paste())

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

matches = []

for groups in phoneRegex.findall(text):
    phoneNum = ''.join([groups[3], groups[5], groups[7]])
    matches.append(phoneNum)

for groups in emailRegex.findall(text):
    matches.append(groups[0])

string = '\n'.join(matches)

pyperclip.copy(string)