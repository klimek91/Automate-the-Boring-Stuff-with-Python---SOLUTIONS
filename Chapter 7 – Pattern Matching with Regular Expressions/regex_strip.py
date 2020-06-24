import re

def stripRe(string, delete=''):

    if delete=='':
        emptyRegex = re.compile(r'^(\s*)(\w*)(\s*)$')
        word = emptyRegex.search(string)
        return word.group(2)
    else:
        return string.replace(delete,'')