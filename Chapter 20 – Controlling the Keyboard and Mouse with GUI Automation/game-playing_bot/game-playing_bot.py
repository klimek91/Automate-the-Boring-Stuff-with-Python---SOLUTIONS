# https://www.miniclip.com/games/sushi-go-round/pl/focus/
# opera size 1920x1080 size 125%

import pyautogui as pyg
import time, os
from PIL import ImageGrab, ImageOps
from numpy import *

os.makedirs('snap', exist_ok=True)
#pyg.mouseInfo()

x_pad = 450
y_pad = 226

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

def screenGrab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1001, y_pad + 747)
    im = ImageGrab.grab()
    im.save(os.path.join('snap', 'snap'+str(int(time.time())) + '.png'), 'PNG')
    return im

def startgame():
    pyg.click(939,547, duration=0.1)
    pyg.click(918,836, duration=0.1)
    pyg.click(1367,933, duration=0.1)
    pyg.click(940,814, duration=0.1)

class Cord:
    f_shrimp = 514, 751
    f_rice = 594, 745
    f_nori = 505, 831
    f_roe = 595, 821
    f_salmon = 507, 910
    f_unagi = 599, 902

    phone = 1371, 785

    menu_toppings = 1265, 656

    t_shrimp = 1222, 575
    t_nori = 1213, 659
    t_roe = 1360, 658
    t_salmon = 1222, 749
    t_unagi = 1349, 573
    t_exit = 1358, 760

    menu_rice = 1253, 686
    buy_rice = 1299, 668

    delivery_norm = 1221, 681

    fold_mat = 694,745

def makeFood(food):
    if food == 'onigiri':
        foodOnHand['rice'] -=2
        foodOnHand['nori'] -=1
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_nori)
        time.sleep(0.1)
        pyg.click(Cord.fold_mat)
        time.sleep(1.5)

    elif food == 'caliroll':
        foodOnHand['rice'] -=1
        foodOnHand['nori'] -=1
        foodOnHand['roe'] -=1
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_nori)
        time.sleep(0.1)
        pyg.click(Cord.f_roe)
        time.sleep(0.1)
        pyg.click(Cord.fold_mat)
        time.sleep(1.5)

    elif food == 'caliroll':
        foodOnHand['rice'] -=1
        foodOnHand['nori'] -=1
        foodOnHand['roe'] -=2
        pyg.click(Cord.f_rice)
        time.sleep(0.1)
        pyg.click(Cord.f_nori)
        time.sleep(0.1)
        pyg.click(Cord.f_roe)
        time.sleep(0.1)
        pyg.click(Cord.f_roe)
        time.sleep(0.1)
        pyg.click(Cord.fold_mat)
        time.sleep(1.5)

def buyFood(food):
    if food == 'rice':
        pyg.click(Cord.phone)
        time.sleep(0.1)
        pyg.click(Cord.menu_rice)
        time.sleep(0.1)
        s = screenGrab()
        if s.getpixel(Cord.buy_rice) != (127, 127, 127):
            time.sleep(0.1)
            print("Rice is available")
            time.sleep(0.1)
            pyg.click(Cord.buy_rice)
            time.sleep(0.1)
            pyg.click(Cord.delivery_norm)
            foodOnHand['rice']+=10
            time.sleep(2.5)
        else:
            print("No cash for rice")
            pyg.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)

    if food == 'nori':
        pyg.click(Cord.phone)
        time.sleep(0.1)
        pyg.click(Cord.menu_toppings)
        time.sleep(0.1)
        s = screenGrab()
        time.sleep(0.1)
        if s.getpixel(Cord.t_nori) != (53, 53, 39):
            time.sleep(0.1)
            print('Nori is available')
            time.sleep(0.1)
            pyg.click(Cord.t_nori)
            time.sleep(0.1)
            pyg.click(Cord.delivery_norm)
            foodOnHand['nori'] += 10
            time.sleep(1)
        else:
            print("No cash for nori")
            pyg.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)
    if food == 'roe':
        pyg.click(Cord.phone)
        time.sleep(0.1)
        pyg.click(Cord.menu_toppings)
        time.sleep(0.1)
        s = screenGrab()
        time.sleep(0.1)
        if s.getpixel(Cord.t_roe) != (101, 13, 13):
            time.sleep(0.1)
            print('Roe is available')
            time.sleep(0.1)
            pyg.click(Cord.t_roe)
            time.sleep(0.1)
            pyg.click(Cord.delivery_norm)
            foodOnHand['roe'] += 10
            time.sleep(1)
        else:
            print("No cash for roe")
            pyg.click(Cord.t_exit)
            time.sleep(1)
            buyFood(food)

def grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 1001, y_pad + 747)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolor())
    a = a.sum()
    return im

x1 = 508
x2 = 666
x3 = 824
x4 = 981
x5 = 1139
x6 = 1297
y1 = 307
y2 = 357

def get_seat_one():
    box = (x1, y1, x1+61, y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_one__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_two():
    box = (x2,y1, x2+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_two__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_three():
    box = (x3,y1,x3+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_three__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_four():
    box = (x4,y1,x4+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_four__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_five():
    box = (x5,y1,x5+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_five__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_seat_six():
    box = (x6,y1,x6+61,y2)
    im = ImageOps.grayscale(ImageGrab.grab(box))
    a = array(im.getcolors())
    a = a.sum()
    im.save(os.getcwd() + '\\seat_six__' + str(int(time.time())) + '.png', 'PNG')
    return a


def get_all_seats():
    print(get_seat_one() , ' seat one')
    print(get_seat_two(), ' seat two')
    print(get_seat_three(), ' seat three')
    print(get_seat_four(), ' seat foure')
    print(get_seat_five(), ' seat five ')
    print(get_seat_six(), ' seat six')

onigiri = []
caliroll = []
gunkan = []

for i in range(3850,4110):
    onigiri.append(i)

for i in range(4450,5100):
    caliroll.append(i)

for i in range(4120,4400):
    gunkan.append(i)

def sushiType(number):
    if number in onigiri:
        return 'onigiri'
    if number in caliroll:
        return 'caliroll'
    if number in gunkan:
        return 'gunkan'