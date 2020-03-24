import os
import cv2
import pyautogui
import time
import numpy as np
import settings

# class Healing:

# 	# def __init__(self, SS_DIRPATH, SS_HOTKEY):
# 	# 	self.dirr = SS_DIRPATH
# 	# 	self.ss_screenshot = SS_HOTKEY


def life_ring(SS_DIRPATH, SS_HOTKEY, RING_HOTKEY):
	'''
	Check if there's some life ring equipped
	If so, equip it
		@params
		SS_DIRPATH: Tibia screenshots path folder
		SS_HOTKEY: screenshot hotkey
		RING_HOTKEY: hotkey to equip ring

		@return
		void
	'''
	template = cv2.imread('D:/Documents/git/tibia-tools/imgs/empty_ring.png',0)
	tmp = settings.is_visible(template, SS_DIRPATH, SS_HOTKEY, False)
	x = []
	for item in tmp:
		x.extend(item)
	if x == []:
		print('Ring slot not empty!')
		pyautogui.press('f7') ############# TEST ##############
	else:
		print('- RING EQUIPPED')
		pyautogui.press(RING_HOTKEY)
		# break



def soft_boots(SS_DIRPATH, SS_HOTKEY, SOFT_HOTKEY):
	'''
	Check if there's some some soft boots equipped
	If so, equip it
		@params
		SS_DIRPATH: Tibia screenshots path folder
		SS_HOTKEY: screenshot hotkey
		RING_HOTKEY: hotkey to equip ring

		@return
		void
	'''
	template = cv2.imread('D:/Documents/git/tibia-tools/imgs/soft_boots.png',0)
	tmp = settings.is_visible(template, SS_DIRPATH, SS_HOTKEY, False)
	x = []
	for item in tmp:
		x.extend(item)
	if x == []:
		print('Boots slot not empty!')
		pyautogui.press('f7') ############# TEST ##############
	else:
		print('SOFT EQUIPPED')
		pyautogui.press(SOFT_HOTKEY)
		# break


def eat_food(SS_DIRPATH, SS_HOTKEY, FOOD_HOTKEY):
	'''
	Check if you are hungry
	If so, eats food
		@params
		SS_DIRPATH: Tibia screenshots path folder
		SS_HOTKEY: screenshot hotkey
		RING_HOTKEY: hotkey to equip ring

		@return
		void
	'''
	template = cv2.imread('D:/Documents/git/tibia-tools/imgs/hungry.png',0)
	tmp = settings.is_visible(template, SS_DIRPATH, SS_HOTKEY, False)
	x = []
	for item in tmp:
		x.extend(item)
	if x == []:
		print('Not hungry!')
		pyautogui.press('r') ############# TEST ##############
	else:
		for _ in range(3):
			pyautogui.press(FOOD_HOTKEY)
			time.sleep(.25)
			# break

