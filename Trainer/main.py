import os
import cv2
import pyautogui
import time
# import numpy as np
from healing import Healing
from mana import Mana
import settings


if __name__ == '__main__':
	try:
		'''
		variables
		'''
		SS_HOTKEY = "f12"
		SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
		RING_HOTKEY = "f8"
		FOOD_HOTKEY = "f10"
		SOFT_HOTKEY = "-"
		RUNE_HOTKEY = "0"
		CYCLE_TIME = 60
		###############
		###############
		cycle_count = 1
		cycle_break = 0

		'''
    	finding mana bar position
    	'''
		settings.idle(.5)
		settings.get_tibia_active()
		settings.take_screenshot(SS_HOTKEY) ########## SS
		settings.idle(1)
		mana_full_path = settings.get_latest_image(SS_DIRPATH, valid_extensions='png')
		# mana_obj = Mana(DIR_PATH, mana_path)
		x_min, x_max, y_min, y_max, mana_full = Mana(SS_DIRPATH, mana_full_path)\
		.get_mana_loc() 

		'''
		main loop
		'''
		pyautogui.press(RUNE_HOTKEY) # first rune
		while True:
			settings.get_tibia_active()
			settings.idle(.25)
			settings.take_screenshot(SS_HOTKEY)
			cycle_pic = settings.get_latest_image(SS_DIRPATH, valid_extensions='png')

			print('#'*30)
			print('Cycle:', cycle_count)

			pixels_mana = Mana(SS_DIRPATH, cycle_pic).\
			counting_pixels(x_min, x_max, y_min, y_max)
			print('MANA PIXELS:', pixels_mana)
			percentage_mana = round(Mana(SS_DIRPATH, cycle_pic).\
				percentage(mana_full, pixels_mana))
			print('PERCENTAGE MANA:', percentage_mana)

			settings.idle(.5)

			if percentage_mana == 100:
				cycle_break+=1
				print('CYCLE BREAK + 1')
				print('- DIDN\'T RUNED')
			elif percentage_mana > 50:
				settings.get_tibia_active()
				pyautogui.press(RUNE_HOTKEY)
				print('- RUNED')
			else: print('- DIDN\'T RUNED')

			healing = Healing(SS_DIRPATH, cycle_pic)
			Healing(SS_DIRPATH, cycle_pic).ring(RING_HOTKEY)
			Healing(SS_DIRPATH, cycle_pic).eat_food(FOOD_HOTKEY)
			Healing(SS_DIRPATH, cycle_pic).soft_boots(SOFT_HOTKEY)

			settings.increment(cycle_count)
			os.remove(cycle_pic)

			print('#'*30)
			print('  TECLE CRTL+C PARA CANCELAR  ')

			if cycle_break == 5:
				print('ATENÇÃO: SEM BLANK RUNE OU SOUL POINTS!!!!')
				break
				settings.idle(CYCLE_TIME)

	except KeyboardInterrupt:
		print('#'*10+'  CANCELADO  '+'#'*10)