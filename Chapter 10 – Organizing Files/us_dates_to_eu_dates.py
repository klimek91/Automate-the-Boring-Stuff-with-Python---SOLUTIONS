#1. It searches all the filenames in the current working directory for American-style dates.
#2. When one is found, it renames the file with the month and day swapped to make it European-style.

import re, os, shutil

usRegex = re.compile(r'([^0-1]*)?([0-1]?\d)-([0-3]?\d)-([1-2]\d\d\d)(.*)?')

#example files in dir: ['02-29-1999inny.txt', '04-19-2000plik.txt', '1-20-2019.txt', '10-8-2020.txt', 'something01-15-2019.txt', 'short9-1-2008.txt', 'plik06-13-2020.txt']
workingDir = os.path.abspath('.')

for us_file in os.listdir(os.getcwd()):

    if usRegex.search(us_file) is not None:

        before = usRegex.search(us_file).group(1)
        month = usRegex.search(us_file).group(2)
        day = usRegex.search(us_file).group(3)
        year = usRegex.search(us_file).group(4)
        after = usRegex.search(us_file).group(5)

        new_name = before + day + '-' + month + '-' + year + after

        print('Renaming "{}" to "{}"...\n'.format(os.path.join(workingDir, us_file), os.path.join(workingDir, new_name)))

        shutil.move(us_file, new_name)