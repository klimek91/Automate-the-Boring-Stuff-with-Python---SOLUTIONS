import re

upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
digitRegex = re.compile(r'[0-9]')

def stronPassword(password):
    if len(password) < 8:
        print("Password has to be min. 8 char long")
        return False
    if upperRegex.search(password) is None:
        print("No uppercase letter")
        return False
    if lowerRegex.search(password) is None:
        print("No lowercase letter")
        return False
    if digitRegex.search(password) is None:
        print("No digit")
        return False
    else:
        return True