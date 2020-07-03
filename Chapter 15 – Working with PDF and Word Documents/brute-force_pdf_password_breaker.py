import PyPDF2

file = open('dictionary.txt')
passwords = file.readlines()

pdfReader = PyPDF2.PdfFileReader(open('test_encrypted.pdf', 'rb'))

for password in passwords:
    password = password.replace('\n','')
    if pdfReader.decrypt(password) == 1:
        print("WE FOUND THE PASSWORD: {}".format(password))
        break
    if pdfReader.decrypt(password.lower()) == 1:
        print("WE FOUND THE PASSWORD: {}".format(password.lower()))
        break

