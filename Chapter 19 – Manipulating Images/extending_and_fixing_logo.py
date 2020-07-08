from PIL import Image
import os

logo = Image.open('catlogo.png')
wlogo, hlogo = logo.size
os.makedirs('logo', exist_ok=True)

for image in os.listdir():
    if (image.lower().endswith('.png') or image.lower().endswith('.jpg')\
    or image.lower().endswith('.gif') or image.lower().endswith('.bmp'))\
    and image != 'catlogo.png':
        img = Image.open(image)
        width, height = img.size
        if width > 300 or height > 300:
            if width > height:
                img = img.resize((300, int((height*300)/width)))
                img.save(image)

            elif height > width:
                img = img.resize((int((width*300)/height), 300))
                img.save(image)
        width, height = img.size

        if width > wlogo*2 and height > hlogo*2:
            print("Adding logo to {}.. ".format(image))
            img.paste(logo,(width-wlogo,height-hlogo), logo)
            img.save(os.path.join('logo',image))
        else:
            print("{} is to small".format(image))
