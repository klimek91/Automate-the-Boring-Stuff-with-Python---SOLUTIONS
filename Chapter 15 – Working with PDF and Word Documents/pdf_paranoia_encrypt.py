import os, PyPDF2

for mainfolder, subfolders, filenames in os.walk(os.getcwd()):
    for pdf in filenames:
        if pdf.endswith('.pdf'):
            filename = os.path.join(mainfolder, pdf)
            pdfFile = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            pdfWriter = PyPDF2.PdfFileWriter()

            for numPage in range(pdfReader.numPages):
                pageObj = pdfReader.getPage(numPage)
                pdfWriter.addPage(pageObj)


            print("Encrypting {}.. ".format(filename))
            pdfWriter.encrypt("password")
            resultPdf = open(filename.replace('.pdf','_encrypted.pdf'), 'wb')
            pdfWriter.write(resultPdf)
            resultPdf.close()
            pdfFile.close()