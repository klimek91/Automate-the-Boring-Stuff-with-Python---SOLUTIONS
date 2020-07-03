import os, PyPDF2

pdfFile = open("test.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFile)
pdfWriter = PyPDF2.PdfFileWriter()

for numPage in range(pdfReader.numPages):
    pageObj = pdfReader.getPage(numPage)
    pdfWriter.addPage(pageObj)

pdfWriter.encrypt("password")
resultPdf = open('text_encrypted.pdf','wb')
pdfWriter.write(resultPdf)
resultPdf.close()
pdfFile.close()