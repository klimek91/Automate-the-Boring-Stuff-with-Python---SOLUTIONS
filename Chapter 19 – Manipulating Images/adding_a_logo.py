from PIL import Image
import os

logo = Image.open('catlogo.png')

for image in os.listdir():
    if (image.endswith('.png') or image.endswith('.jpg')) and image != 'catlogo.png':
        img = Image.open(image)
        width, height = img.size
        if width > 300 or height > 300:


            if width > height:
                img = img.resize((300, int((height*300)/width)))
                img.save(image)

            elif height > width:
                img = img.resize((int((width*300)/height), 300))
                img.save(image)

