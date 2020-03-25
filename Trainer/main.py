import os
import cv2
import pyautogui
import time
import numpy as np
from healing import Healing
import settings
from mana import Mana

if __name__ == '__main__':
    try:
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
        x_min, x_max, y_min, y_max, mana_full = Mana(SS_DIRPATH, SS_HOTKEY)\
            .get_mana_loc() # mana coordinates
        count = 1
        cycle_break = 0
        pyautogui.press(RUNE_HOTKEY)
        while True:
            settings.get_tibia_active()
            print('#'*30)
            print('Cycle:', count)
            pixels_mana = Mana(SS_DIRPATH, SS_HOTKEY).\
                counting_pixels(x_min, x_max, y_min, y_max)
            print('MANA PIXELS:', pixels_mana)
            percentage_mana = round(Mana(SS_DIRPATH, SS_HOTKEY).\
                percentage(mana_full, pixels_mana))
            print('PERCENTAGE MANA:', percentage_mana)
            time.sleep(.5)
            if percentage_mana == 100:
                cycle_break+=1
                print('CYCLE BREAK + 1')
                print('- DIDN\'T RUNED')
            elif percentage_mana > 50:
                settings.get_tibia_active()
                pyautogui.press(RUNE_HOTKEY)
                print('- RUNED')
            else: print('- DIDN\'T RUNED')
            settings.get_tibia_active()
            Healing(SS_DIRPATH, SS_HOTKEY).ring(RING_HOTKEY)
            Healing(SS_DIRPATH, SS_HOTKEY).eat_food(FOOD_HOTKEY)
            settings.get_tibia_active()
            Healing(SS_DIRPATH, SS_HOTKEY).soft_boots(SOFT_HOTKEY)
            count+=1
            print('#'*30)
            if cycle_break == 5:
                print('ATENÇÃO: SEM BLANK RUNE OU SOUL POINTS!!!!')
                break
            time.sleep(CYCLE_TIME)
    except KeyboardInterrupt:
        print('#'*10+'  CANCELADO  '+'#'*10)