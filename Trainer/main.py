import os
import cv2
import pyautogui
import time
import numpy as np
import healing
import settings
import mana

if __name__ == '__main__':
    SS_HOTKEY = "f12"
    SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
    RING_HOTKEY = "f8"
    FOOD_HOTKEY = "f10"
    SOFT_HOTKEY = "f9"
    RUNE_HOTKEY = "0"
    CYCLE_TIME = 60


    time.sleep(.5)
    settings.get_tibia_active()
    time.sleep(.5)
    x_min, x_max, y_min, y_max, mana_full = mana.get_mana_loc(SS_HOTKEY,SS_DIRPATH) # mana coordinates
    count = 1
    cycle_break = 0
    pyautogui.press(RUNE_HOTKEY)
    while True:
        settings.get_tibia_active()
        print('Cycle:', count)
        pixels_mana = mana.counting_pixels(x_min, x_max, y_min, y_max, SS_HOTKEY, SS_DIRPATH)
        print('MANA PIXELS:', pixels_mana)
        percentage_mana = round(mana.percentage(mana_full, pixels_mana))
        print('PERCENTAGE MANA:', percentage_mana)
        time.sleep(.5)
        if percentage_mana == 100:
            cycle_break+=1
            print('CYCLE BREAK + 1')
            print('- DIDN\'T RUNED')
        elif percentage_mana > 50:
            pyautogui.press(RUNE_HOTKEY)
            print('- RUNED')
        else: print('- DIDN\'T RUNED')

        healing.ring(SS_DIRPATH, SS_HOTKEY, RING_HOTKEY)
        # print('\n')
        healing.eat_food(SS_DIRPATH, SS_HOTKEY, FOOD_HOTKEY)
        # print('\n')
        healing.soft_boots(SS_DIRPATH, SS_HOTKEY, SOFT_HOTKEY)
        count+=1
        print('#'*30)
        if cycle_break == 5:
            break
        time.sleep(CYCLE_TIME)