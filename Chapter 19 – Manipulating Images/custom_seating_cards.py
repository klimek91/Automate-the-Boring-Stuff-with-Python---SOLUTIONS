from PIL import Image, ImageFont, ImageDraw
import os

img = Image.open("flowers.jpg")
img = img.resize((288,360))
img.save('flowers.jpg')

draw = ImageDraw.Draw(img)

fontsFolder = 'C:\Windows\Fonts'
arialFont = ImageFont.truetype(os.path.join(fontsFolder,'arial.ttf'),26)
