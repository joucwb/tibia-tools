import os
import cv2
import pyautogui
import time
import numpy as np
import settings
from win32api import GetSystemMetrics
from PIL import Image


class Mana:
	def __init__(self, SS_DIRPATH, SS_HOTKEY):
		self.dir_path = SS_DIRPATH
		self.htk = SS_HOTKEY


	def get_mana_loc(self):
		mana = os.path.join(os.path.dirname(__file__), 'imgs', 'mana_bar.png') # Find mana_bar.png path
		mana = cv2.imread(mana,1) # Read mana_bar.png (rgb)
		pyautogui.press(self.htk) # Screenshot
		time.sleep(1)
		mana_path = settings.get_latest_image(self.dir_path, valid_extensions='png') # Latest ss path
		img_rgb = cv2.imread(mana_path,1)
		res = cv2.matchTemplate(img_rgb,mana,cv2.TM_CCOEFF_NORMED) # Matching
		_, _, min_loc, max_loc = cv2.minMaxLoc(res) 
		x_min, x_max, y_min, y_max = max_loc[0], max_loc[0]+mana.shape[1],\
									 max_loc[1], max_loc[1]+mana.shape[0]

		# loc = [x_min, x_max, y_min, y_max]
		# print(loc)
		
		crop_img = img_rgb[y_min:y_max,x_min:x_max]
		_ = cv2.imwrite('tmp.png', crop_img)
		im = Image.open('tmp.png')
		blue = 0
		for pixel in im.getdata():
			# print(pixel)
			if pixel == (83, 80, 218):
				blue+=1
		os.remove('tmp.png')
		os.remove(mana_path)
		return x_min, x_max, y_min, y_max, blue


	def counting_pixels(self, x_min, x_max, y_min, y_max):
		pyautogui.press(self.htk)
		time.sleep(1)
		pic_path = settings.get_latest_image(self.dir_path, valid_extensions='png') 
		img_rgb = cv2.imread(pic_path,1)
		crop_img = img_rgb[y_min:y_max,x_min:x_max]
		_ = cv2.imwrite('tmp.png', crop_img)
		im = Image.open('tmp.png')
		blue = 0
		for pixel in im.getdata():
			if pixel == (83, 80, 218):
				blue+=1
		os.remove('tmp.png')
		os.remove(pic_path)
		return blue

	def percentage(self, mana_full, pixels_mana):
		try:
			return pixels_mana*100/mana_full
		except ZeroDivisionError as error:
			print('#'*50)
			print('\nA MANA PRECISA ESTAR FULL ANTES DO TREINO! :)\n\n'+'#'*50)
			pyautogui.alert(text='ERRO NO TRAINER! VERIFIQUE O LOG', title='ATENÇÃO', button='OK')