import os
import cv2
import pyautogui
import time
import numpy as np
import healing
import settings
import test

if __name__ == '__main__':
    SS_HOTKEY = "f12"
    SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
    RING_HOTKEY = "f8"
    FOOD_HOTKEY = "f10"
    SOFT_HOTKEY = "f9"
    CYCLE_TIME = 30
    time.sleep(1)
    count = 1

    while True:
        print('Cycle:', count)
        settings.get_tibia_active()
        test.get_pixels_mana(SS_HOTKEY,SS_DIRPATH)
        time.sleep(500)
        healing.ring(SS_DIRPATH, SS_HOTKEY, RING_HOTKEY)
        # print('\n')
        healing.eat_food(SS_DIRPATH, SS_HOTKEY, FOOD_HOTKEY)
        # print('\n')
        healing.soft_boots(SS_DIRPATH, SS_HOTKEY, SOFT_HOTKEY)
        count+=1
        print('#'*30)
        time.sleep(CYCLE_TIME)