import os
import cv2
import pyautogui
import time
import settings
from PIL import Image


class Mana:
	def __init__(self, SS_DIRPATH, mana_path):
		self.dir_path = SS_DIRPATH
		self.mana_path = mana_path


	def get_mana_loc(self):
		'''
		Get mana par screen position and count mana bar pixels (HAS to be full)
			@params
			null

			@return
			x_min, x_man: x-coordinates position
			y_min, y_max: y-coordinates position
			blue: mana bar pixels (quantity)
		'''
		mana = os.path.join(os.path.dirname(__file__), 'imgs', 'mana_bar.png') # Find mana_bar.png path
		mana = cv2.imread(mana,1) # Read mana_bar.png (rgb)
		img_rgb = cv2.imread(self.mana_path,1)
		res = cv2.matchTemplate(img_rgb,mana,cv2.TM_CCOEFF_NORMED) # Matching
		_, _, min_loc, max_loc = cv2.minMaxLoc(res) 
		x_min, x_max, y_min, y_max = max_loc[0], max_loc[0]+mana.shape[1],\
									 max_loc[1], max_loc[1]+mana.shape[0]
		crop_img = img_rgb[y_min:y_max,x_min:x_max]
		_ = cv2.imwrite('tmp.png', crop_img)
		im = Image.open('tmp.png')
		blue = 0
		for pixel in im.getdata():
			if pixel == (83, 80, 218):
				blue+=1
		os.remove('tmp.png')
		return x_min, x_max, y_min, y_max, blue


	def counting_pixels(self, x_min, x_max, y_min, y_max):
		'''
		Count mana bar pixels
			@params
			x, y coordinates (see get_mana_loc method)

			@return
			blue: mana bar pixels (quantity)
		'''
		img_rgb = cv2.imread(self.mana_path,1)
		crop_img = img_rgb[y_min:y_max,x_min:x_max]
		_ = cv2.imwrite('tmp.png', crop_img)
		im = Image.open('tmp.png')
		blue = 0
		for pixel in im.getdata():
			if pixel == (83, 80, 218):
				blue+=1
		os.remove('tmp.png')
		# os.remove(pic_path)
		return blue

	def percentage(self, mana_full, pixels_mana):
		'''
		Calculate percentage of mana
			@params
			mana_full: number of pixels mana full
			pixels_mana: number of pixels mana

			@return
			how many percentage of mana full the character has
		'''
		try:
			return pixels_mana*100/mana_full
		except ZeroDivisionError as error:
			print('#'*50)
			print('\nA MANA PRECISA ESTAR FULL ANTES DO TREINO! :)\n\n'+'#'*50)
			pyautogui.alert(text='ERRO NO TRAINER! VERIFIQUE O LOG', title='ATENÇÃO', button='OK')


	def rune(self, RUNES_PER_CYCLE, RUNE_HOTKEY):
		for _ in range(RUNES_PER_CYCLE):
			settings.idle(.5)
			pyautogui.press(RUNE_HOTKEY)
			settings.idle(1.5) # rune cd