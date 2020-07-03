import PyPDF2, os

file = open('dictionary.txt') #This dictionary file contains over 44,000 English words (in capital letters) with one word per line.
passwords = file.readlines()

for mainfolder, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if filename.endswith('.pdf'):
            file = os.path.join(mainfolder, filename)
            pdfReader = PyPDF2.PdfFileReader(open(file, 'rb'))
            if not pdfReader.isEncrypted:
                print('{} is not encrypted'.format(filename))
            else:
                for password in passwords:
                    password = password.replace('\n','')
                    if pdfReader.decrypt(password) == 1:
                        print("{} PASSWORD IS : {}".format(filename, password))
                        break
                    if pdfReader.decrypt(password.lower()) == 1:
                        print("{} PASSWORD IS : {}".format(filename, password.lower()))
                        break