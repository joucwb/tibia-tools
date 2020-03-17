import random
import time
import pyautogui


# Variables
soft_boots = 14400
life_ring = 1200
time_ring, time_soft = 0, 0

# Booleans
use_soft = False
use_lifering = True

soft_equipped = False
lifering_equipped = False

# Hotkeys
hk_softboots = "f8"
hk_lifering = "f9"
hk_food = "f10"
hk_heal = "f11"

# 4 minutes cycles:
time.sleep(4)
print('Starting 4 minutes cycles:')
start = time.clock()
cycles = 0
while True:
	print('Começo CICLO:')
	if use_soft == True and soft_equipped == False:
		pyautogui.press(hk_softboots)
		time.sleep(1)
		soft_equipped = True
		time_soft = 0

	if use_lifering == True and lifering_equipped == False:
		print('Life Ring Equipado!')
		pyautogui.press(hk_lifering)
		time.sleep(1)
		lifering_equipped = True
		time_ring = 0
		
	pyautogui.press(hk_heal)
	time.sleep(1)
	pyautogui.press(hk_food)
	time.sleep(1)
	pyautogui.press(hk_food)

	if time_ring > 1200:
		lifering_equipped = False
		print('Life ring acabou')
	if time_soft > 14400:
		soft_equipped = False


	time.sleep(237) # Loop each 2 minutes
	cycles += 1
	print('FIM DO ' + str(cycles) + 'o CICLO.')
	time_ring += 240 
	time_soft += 240
