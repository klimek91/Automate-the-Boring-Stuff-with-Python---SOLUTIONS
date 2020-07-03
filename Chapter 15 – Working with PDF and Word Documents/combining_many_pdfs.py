import PyPDF2, os

pdfs = []

for pdf in os.listdir(os.getcwd()):
    if pdf.endswith('.pdf'):
        pdfs.append(pdf)

pdfWriter = PyPDF2.PdfFileWriter()
pdfMergedFile = open("merged.pdf",'wb')

for file in pdfs:
    pdfFile = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)


    for pageNum in range(1, pdfReader.numPages):  #adding all pages without 1st page
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
        pdfWriter.write(pdfMergedFile)
    pdfFile.close()

pdfMergedFile.close()