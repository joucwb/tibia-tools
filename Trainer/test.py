import os
import cv2
import pyautogui
import time
import numpy as np
import settings
from win32api import GetSystemMetrics
from PIL import Image


def mana_pixels():

	mana = os.path.join(os.path.dirname(__file__), 'imgs', 'mana_bar.png')
	pyautogui.press(SS_HOTKEY) # Take screenshot
	template = cv2.imread(mana,1)
	print(template.shape)
	print(template.shape[0])
	pic_path = settings.get_latest_image(SS_DIRPATH, valid_extensions='png') 
	img_rgb = cv2.imread(pic_path,1)
	res = cv2.matchTemplate(img_rgb,template,cv2.TM_CCOEFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	x_min, x_max, y_min, y_max = max_loc[0], max_loc[0]+template.shape[1], max_loc[1], max_loc[1]+template.shape[0]
	print(x_min, x_max, y_min, y_max)
	pixels_mana = img_rgb[round((y_min+y_max)/2),round((x_min+x_max)/2)]
	print(pixels_mana)
	crop_img = img_rgb[y_min:y_max,x_min:x_max]
	a = cv2.imwrite('teste.png', crop_img)
	# time.sleep(30)
	blue = 0
	im = Image.open('teste.png')
	for pixel in im.getdata():
		# time.sleep(10)
		if pixel == (83, 80, 218):
			blue+=1
	print(blue)
	

	# cv2.imshow("cropped", crop_img)
	# cv2.waitKey(0)
	print(max_loc[0], max_loc[0]+template.shape[1], max_loc[1], max_loc[1]+template.shape[0])
	# os.remove(pic_path)
	









	# pic_path = settings.get_latest_image(SS_DIRPATH, valid_extensions='png') 
	# manabar = cv2.imread(mana,0)
	# image = cv2.imread(pic_path,0)
	# res = cv2.matchTemplate(image,manabar,cv2.TM_CCOEFF_NORMED)
	# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
	# print(min_loc, max_loc)
	# print(max_loc[0], max_loc[1])
	# w, h = manabar.shape[::-1]
	# print(max_loc[0], max_loc[0] + w, max_loc[1], max_loc[1] + h)
	

	# threshold = 0.8
	# loc = np.where( res >= threshold)
	# print(loc)
	# time.sleep(500)
	
	# for pt in zip(*loc[::-1]):
	# 	print(pt, (pt[0] + w, pt[1] + h))
	# # crop_img = (pt[0]:pt[0]+w, pt[1]:pt[1]+h)
	# cv2.imshow("cropped", crop_img)
	# cv2.waitKey(0)



	# print(tmp)
	# print('COORDENADAS:')
	# print(tmp[0][0], tmp[0][-1], tmp[1][0], tmp[1][-1])
	# crop_rectangle = (1750, 227, 214 , 1777)
	# # crop_img = image[tmp[1][0]:tmp[1][-1], tmp[0][0]:tmp[0][-1]]
	# crop_img = image[214:227, 1750:1777]
	# cv2.imshow("cropped", crop_img)
	# cv2.waitKey(0)
	# # im = Image.open(pic_path)
	# # cropped_im = im.crop(crop_rectangle)
	# # cropped_im.show()
	# print('#'*10)

if __name__ == '__main__':
	SS_HOTKEY = "f12"
	SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
	RING_HOTKEY = "f8"
	FOOD_HOTKEY = "f10"
	SOFT_HOTKEY = "f9"
	CYCLE_TIME = 30
	print("Width =", GetSystemMetrics(0))
	print("Height =", GetSystemMetrics(1))
	time.sleep(1)
	count = 1
	mana_pixels()