import os
import sys
import cv2
import pyautogui
import time
from healing import Healing
from mana import Mana
import settings

# SS_HOTKEY = "f12"
# SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
# RING_HOTKEY = "f8"
# FOOD_HOTKEY = "f10"
# SOFT_HOTKEY = "-"
# RUNE_HOTKEY = "0"
# CHAR_NAME = "Biel Huntedz"
# CYCLE_TIME = 2
# RUNES_PER_CYCLE = 3
###############
###############
# cycle_count = 1
# cycle_break = 0
global SS_HOTKEY
global SS_DIRPATH
global RING_HOTKEY
global FOOD_HOTKEY
global SOFT_HOTKEY
global RUNE_HOTKEY
global CHAR_NAME
global CYCLE_TIME
global RUNES_PER_CYCLE

class Main:
	def __init__(self, SS_HOTKEY, SS_DIRPATH, RING_HOTKEY, FOOD_HOTKEY, SOFT_HOTKEY, 
		RUNE_HOTKEY, CHAR_NAME, CYCLE_TIME, RUNES_PER_CYCLE):
		'''
		variables
		'''
		self.SS_HOTKEY = SS_HOTKEY
		self.SS_DIRPATH = SS_DIRPATH
		self.RING_HOTKEY = RING_HOTKEY
		self.FOOD_HOTKEY = FOOD_HOTKEY
		self.SOFT_HOTKEY = SOFT_HOTKEY
		self.RUNE_HOTKEY = RUNE_HOTKEY
		self.CHAR_NAME = CHAR_NAME
		self.CYCLE_TIME = CYCLE_TIME
		self.RUNES_PER_CYCLE = RUNES_PER_CYCLE

	def main(self):
		try:
			self.displayInit()
			cycle_count = 1
			cycle_break = 0
			'''
	    	finding mana bar position
	    	'''
			settings.idle(.5)
			settings.get_tibia_active(self.CHAR_NAME)
			settings.take_screenshot(self.SS_HOTKEY) ########## SS
			settings.idle(1.5) #cd to del
			mana_full_path = settings.get_latest_image(self.SS_DIRPATH, valid_extensions='png')
			x_min, x_max, y_min, y_max, mana_full = Mana(self.SS_DIRPATH, mana_full_path)\
			.get_mana_loc() 
			settings.del_screenshot(mana_full_path)
			'''
			main loop
			'''
			pyautogui.press(self.RUNE_HOTKEY) # first rune
			while True:
				settings.get_tibia_active(self.CHAR_NAME)
				settings.idle(.5)
				settings.take_screenshot(self.SS_HOTKEY)
				settings.idle(1.5)
				cycle_pic = settings.get_latest_image(self.SS_DIRPATH, valid_extensions='png')

				print('#'*30)
				print('Cycle:', cycle_count)

				currentMana = Mana(self.SS_DIRPATH, cycle_pic)

				pixels_mana = currentMana.counting_pixels(x_min, x_max, y_min, y_max)
				print('MANA PIXELS:', pixels_mana)
				percentage_mana = round(currentMana.percentage(mana_full, pixels_mana))
				print('PERCENTAGE MANA:', percentage_mana)

				if percentage_mana == 100 or percentage_mana == 0:
					cycle_break+=1
					settings.get_tibia_active(self.CHAR_NAME)
					currentMana.rune(int(self.RUNES_PER_CYCLE), self.RUNE_HOTKEY)
					print('SUA MANA ESTÁ {}%!'.format(percentage_mana))
					print('Verifique seu tempo de ciclo e/ou numero de runas.\n')
					print('- RUNED')
				elif percentage_mana >= 50:

					settings.get_tibia_active(self.CHAR_NAME)
					currentMana.rune(int(self.RUNES_PER_CYCLE), self.RUNE_HOTKEY)
					print('- RUNED')
				else: print('- DIDN\'T RUNED')

				healing = Healing(cycle_pic, self.CHAR_NAME)
				healing.ring(self.RING_HOTKEY)
				settings.idle(.25)
				healing.eat_food(self.FOOD_HOTKEY)
				settings.idle(.5)
				healing.soft_boots(self.SOFT_HOTKEY)

				print('#'*30)
				print('  TECLE CRTL+C PARA CANCELAR  ')

				if cycle_break == 5:
					print('ATENÇÃO: 5 CICLOS COM MANA ESTÁTICA!')
					break

				cycle_count = settings.increment(cycle_count)
				settings.del_screenshot(cycle_pic)
				settings.idle(int(self.CYCLE_TIME)*60)

		except KeyboardInterrupt:
			print('#'*10+'  CANCELADO  '+'#'*10)

	def displayInit(self):
		print('~'*30)
		print('Char - '+(self.CHAR_NAME))
		print('Diretório - '+(self.SS_DIRPATH))
		print('Food Hotkey - '+str(self.FOOD_HOTKEY))
		print('Ring Hotkey - '+str(self.RING_HOTKEY))
		print('Soft Hotkey - '+str(self.SOFT_HOTKEY))
		print('Rune Hotkey - '+str(self.RUNE_HOTKEY))		
		print('Screenshot Hotkey - '+str(self.SS_HOTKEY))
		print('~'*30)
