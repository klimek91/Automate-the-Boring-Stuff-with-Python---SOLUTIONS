import os, re, pyinputplus

text_files = []
for file in os.listdir(os.getcwd()):
    if file.endswith('.txt'):
        text_files.append(file)
searching = pyinputplus.inputStr("Enter regular expression what You are searching for:")
inputRegex = re.compile(r'{}'.format(searching))


for text_file in text_files:
    file = open(text_file)
    lines = file.readlines()
    for line in lines:
        if inputRegex.search(line) is not None:
            print(line, end='')