#Write a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf). Copy these files from whatever location they are in to a new folder.

import os, shutil

os.makedirs('new_folder', exist_ok=True)
new_path = os.path.join(os.getcwd(), 'new_folder')

for mainfolder, subfolders, filenames in os.walk(os.getcwd()):
    if mainfolder != new_path:
        for filename in filenames:
            if filename.endswith('.pdf'):
                new_file = os.path.join(new_path, filename)
                old_file = os.path.join(mainfolder, filename)
                shutil.copy(old_file, new_path)