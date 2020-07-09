from PIL import Image, ImageFont, ImageDraw
import os


fontsFolder = 'C:\Windows\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder,'arial.ttf'),26)

file = open('guests.txt', encoding='utf8')
names = file.readlines()

for i in range(len(names)):
    img = Image.open("flowers.jpg")
    img = img.resize((288, 360))
    img.save('flowers.jpg')
    draw = ImageDraw.Draw(img)

    draw.text((10,150), names[i].replace('\n',''), fill='black', font=arialFont)
    img.save('invitation{}.jpg'.format(i))