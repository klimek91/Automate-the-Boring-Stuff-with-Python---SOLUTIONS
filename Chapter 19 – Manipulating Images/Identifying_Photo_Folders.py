#more than half of the files are photos
#photo: jpg or png and more then 500 width and height

import os
from PIL import Image

for mainfolder, subfolders, filenames in os.walk(r"C:\\"):
    no_image = []
    images = []
    for filename in filenames:
        if filename.lower().endswith('.jpg') or filename.lower().endswith('.png'):
            image = Image.open(os.path.join(mainfolder, filename))
            width, height = image.size
            if width > 500 and height > 500:
                images.append(filename)
        else:
            no_image.append(filename)

    if len(images) > len(no_image):
        print("This is image file {} with {} images and {} no-images".format(mainfolder, len(images), len(no_image)))