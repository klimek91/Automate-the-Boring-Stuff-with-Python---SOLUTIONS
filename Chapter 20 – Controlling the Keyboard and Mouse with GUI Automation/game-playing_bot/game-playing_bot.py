# https://www.miniclip.com/games/sushi-go-round/pl/focus/
# opera size 1920x1080 size 125%

import pyautogui as pyg
import time
#pyg.mouseInfo()

foodOnHand = {'shrimp':5,
              'rice':10,
              'nori':10,
              'roe':10,
              'salmon':5,
              'unagi':5}

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