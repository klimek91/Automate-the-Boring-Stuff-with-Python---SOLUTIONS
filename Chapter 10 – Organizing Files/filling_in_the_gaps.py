#Write a program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on,
# in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no spam002.txt).
# Have the program rename all the later files to close this gap.

import os, re, shutil

fileRegex = re.compile(r'(spam)(\d\d\d)(.*)')

count = 1
for file in os.listdir(os.getcwd()):
    if fileRegex.search(file) is not None:
        mo = fileRegex.search(file)
        prefix = mo.group(1)
        number = mo.group(2)
        after = mo.group(3)

        if int(number) == count:
            count+=1
        else:
            new_base = prefix + '{0:03}'.format(count) + after
            fixed_path = os.path.join(os.getcwd(), new_base)
            print("Changig basename {} for {}".format(os.path.basename(file),new_base))
            shutil.move(file, fixed_path)
            count+=1