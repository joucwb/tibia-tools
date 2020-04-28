import os
import sys
import cv2
import pyautogui
import time
import settings

global EXERCISE_WEAPON_HOTKEY
global CHAR_NAME

class Dummy:
	def __init__(self, EXERCISE_WEAPON_HOTKEY, CHAR_NAME, dummy_pos):
		'''
		variables
		'''
		self.EXERCISE_WEAPON_HOTKEY = EXERCISE_WEAPON_HOTKEY
		self.CHAR_NAME = CHAR_NAME
		self.dummy_pos = dummy_pos

	def main(self):
		weapons = 0
		try:
			self.display()
			while True:
				settings.get_tibia_active(self.CHAR_NAME)
				settings.idle(.5)
				self.hit_dummy()
				weapons+=1
				print('-*'*16)
				print('Dummy position:', self.dummy_pos)
				print('Exercises Weapons utilizadas:', weapons)
				settings.idle(100)
				
		except KeyboardInterrupt:
			print('#'*10+'  CANCELADO  '+'#'*10)


	def hit_dummy(self):
		pyautogui.press(self.EXERCISE_WEAPON_HOTKEY)
		settings.idle(.5)
		pyautogui.click(self.dummy_pos[0], self.dummy_pos[1])  

	def display(self):
		print('~'*30)
		print('TREINAMENTO COM DUMMYS:')
		print('Char - '+(self.CHAR_NAME))
		print('Exercise Weapon Hotkey - '+str(self.EXERCISE_WEAPON_HOTKEY))
		print('~'*30)
		print('PRESSIONE CRTL+C PARA CANCELAR!!')
