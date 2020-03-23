import os
import cv2
import pyautogui
import time
import numpy as np
import healing

if __name__ == '__main__':
    SS_HOTKEY = "f12"
    SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
    RING_HOTKEY = "b"
    FOOD_HOTKEY = "f10"
    SOFT_HOTKEY = "f9"
    time.sleep(1)
    healing.life_ring(SS_DIRPATH, SS_HOTKEY, RING_HOTKEY)
    time.sleep(1)
    healing.eat_food(SS_DIRPATH, SS_HOTKEY, FOOD_HOTKEY)
    time.sleep
    healing.soft_boots(SS_DIRPATH, SS_HOTKEY, SOFT_HOTKEY)