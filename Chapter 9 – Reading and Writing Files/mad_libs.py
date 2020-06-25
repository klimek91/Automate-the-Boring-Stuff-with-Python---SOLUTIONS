import pyinputplus as pyinp
import re

#Text in text.txt: "The ADJECTIVE panda walked to the NOUN and then ADVERB. A nearby VERB was unaffected by these events."

file = open('text.txt')
file_read = file.read()

print(file_read)

madlibRegex = re.compile(r'(ADJECTIVE|NOUN|ADVERB|VERB)')
madlibs = madlibRegex.findall(file_read)

for word in madlibs:
    new_word = pyinp.inputStr("Enter an {}:".format(word.lower()))
    file_read = file_read.replace(word, new_word,1)

print(file_read)
new_file = open("new_text.txt", 'w')
new_file.write(file_read)