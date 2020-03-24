import os
import cv2
import pyautogui
import time
import numpy as np
import settings
from PIL import Image
from win32api import GetSystemMetrics


def getPixelsHealth():
    pyautogui.press(SS_HOTKEY) # Take screenshot
    time.sleep(1) 
    # Get the latest snapshot on the imgpath dir
    pic_path = settings.get_latest_image(SS_DIRPATH, valid_extensions='png') 
    img_rgb = cv2.imread(pic_path)
    im = Image.open(pic_path)
    # im.show()
    red = 0

    for pixel in im.getdata():
        if pixel == (219, 79, 79):
            red += 1
    os.remove(pic_path)
    if red > 0:
        return red
    else:
        return 0

        


SS_HOTKEY = "f12"
SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
RING_HOTKEY = "f8"
FOOD_HOTKEY = "f10"
SOFT_HOTKEY = "f9"
CYCLE_TIME = 30
print("Width =", GetSystemMetrics(0))
print("Height =", GetSystemMetrics(1))
time.sleep(1)
count = 1
print(getPixelsHealth())