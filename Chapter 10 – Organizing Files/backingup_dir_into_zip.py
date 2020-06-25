import os, zipfile

files = []
count = 1
while True:
    while os.path.exists('AlsPythonBook_{}.zip'.format(count)):      #new zip file name each time
        count+=1
    else:
        newZip = zipfile.ZipFile('AlsPythonBook_{}.zip'.format(count), 'w')
        for mainfolder, subfolders, filenames in os.walk(os.getcwd()):
            for filename in filenames:
                if not filename.endswith('.zip'):
                    file = os.path.join(mainfolder,filename)
                    newZip.write(file, compress_type=zipfile.ZIP_DEFLATED)
        newZip.close()
    break