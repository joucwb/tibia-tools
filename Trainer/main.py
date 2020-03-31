import os
import cv2
import pyautogui
import time
from healing import Healing
from mana import Mana
import settings
import logging
# from interface import GUI
logging.basicConfig(filename='file.log',level=logging.INFO)
SS_HOTKEY = "f12"
SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
RING_HOTKEY = "f8"
FOOD_HOTKEY = "f10"
SOFT_HOTKEY = "-"
RUNE_HOTKEY = "0"
CHAR_NAME = "Gatitex"
CYCLE_TIME = 2
RUNES_PER_CYCLE = 3
###############
###############
# cycle_count = 1
# cycle_break = 0

class Main:
	def __init__(self):
		'''
		variables
		'''
		global SS_HOTKEY
		global SS_DIRPATH
		global RING_HOTKEY
		global FOOD_HOTKEY
		global SOFT_HOTKEY
		global RUNE_HOTKEY
		global CHAR_NAME
		global CYCLE_TIME
		global RUNES_PER_CYCLE

		###############
		###############
		# global cycle_count
		# global cycle_break

	def main(self):
		try:
			cycle_count = 1
			cycle_break = 0
			'''
	    	finding mana bar position
	    	'''
			settings.idle(.5)
			settings.get_tibia_active(CHAR_NAME)
			settings.take_screenshot(SS_HOTKEY) ########## SS
			settings.idle(1.5) #cd to del
			mana_full_path = settings.get_latest_image(SS_DIRPATH, valid_extensions='png')
			x_min, x_max, y_min, y_max, mana_full = Mana(SS_DIRPATH, mana_full_path)\
			.get_mana_loc() 
			settings.del_screenshot(mana_full_path)
			'''
			main loop
			'''
			pyautogui.press(RUNE_HOTKEY) # first rune
			while True:
				settings.get_tibia_active(CHAR_NAME)
				settings.idle(.5)
				settings.take_screenshot(SS_HOTKEY)
				settings.idle(1.5)
				cycle_pic = settings.get_latest_image(SS_DIRPATH, valid_extensions='png')

				logging.info('#'*30)
				logging.info('Cycle:', cycle_count)

				currentMana = Mana(SS_DIRPATH, cycle_pic)

				pixels_mana = currentMana.counting_pixels(x_min, x_max, y_min, y_max)
				logging.info('MANA PIXELS:', pixels_mana)
				percentage_mana = round(currentMana.percentage(mana_full, pixels_mana))
				logging.info('PERCENTAGE MANA:', percentage_mana)

				if percentage_mana == 100 or percentage_mana == 0:
					cycle_break+=1
					settings.get_tibia_active(CHAR_NAME)
					currentMana.rune(RUNES_PER_CYCLE, RUNE_HOTKEY)
					# for _ in range(RUNES_PER_CYCLE):
					# 	settings.idle(.5)
					# 	pyautogui.press(RUNE_HOTKEY)
					# 	settings.idle(1.5) # rune cd
					logging.info('100% MANA!!!')
					logging.info('- RUNED')
				elif percentage_mana >= 50:

					settings.get_tibia_active(CHAR_NAME)
					# for _ in range(RUNES_PER_CYCLE):
					# 	settings.idle(.5)
					# 	pyautogui.press(RUNE_HOTKEY)
					# 	settings.idle(1.5) # rune cd
					currentMana.rune(RUNES_PER_CYCLE, RUNE_HOTKEY)
					logging.info('- RUNED')
				else: logging.info('- DIDN\'T RUNED')

				healing = Healing(cycle_pic, CHAR_NAME)
				healing.ring(RING_HOTKEY)
				settings.idle(.25)
				healing.eat_food(FOOD_HOTKEY)
				# for _ in range(3):
				# 	pyautogui.press(FOOD_HOTKEY)
				# 	time.sleep(.5)
				# healing.eat_food(FOOD_HOTKEY)
				settings.idle(.5)
				healing.soft_boots(SOFT_HOTKEY)

				

				logging.info('#'*30)
				logging.info('  TECLE CRTL+C PARA CANCELAR  ')

				if cycle_break == 5:
					logging.info('ATENÇÃO: SEM BLANK RUNE OU SOUL POINTS!!!!')
					break

				cycle_count = settings.increment(cycle_count)
				settings.del_screenshot(cycle_pic)
				settings.idle(CYCLE_TIME*60)

		except KeyboardInterrupt:
			logging.info('#'*10+'  CANCELADO  '+'#'*10)


	# if __name__ == '__main__':
	# 	'''
	# 	variables
	# 	'''
	# 	SS_HOTKEY = "f12"
	# 	SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
	# 	RING_HOTKEY = "f8"
	# 	FOOD_HOTKEY = "f10"
	# 	SOFT_HOTKEY = "-"
	# 	RUNE_HOTKEY = "0"
	# 	CHAR_NAME = "Biel Huntedz"
	# 	CYCLE_TIME = 2
	# 	RUNES_PER_CYCLE = 3
	# 	###############
	# 	###############
	# 	cycle_count = 1
	# 	cycle_break = 0
	# 	main()
