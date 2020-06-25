#deleting files with size over 50MB

import os, send2trash

for mainfolder, subfolders, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        file = os.path.join(mainfolder, filename)
        if os.path.getsize(file) > 50000000:
            print("Deleting file: "+  filename + " size: " + str(os.path.getsize(file)))
            send2trash.send2trash(file)