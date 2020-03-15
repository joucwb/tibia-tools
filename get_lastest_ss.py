import os
import cv2
import pyautogui
import time

def get_latest_image(dirpath, valid_extensions=('jpg','jpeg','png')):
    """
    Get the latest image file in the given directory
    """

    # get filepaths of all files and dirs in the given dir
    valid_files = [os.path.join(dirpath, filename) for filename in os.listdir(dirpath)]
    # filter out directories, no-extension, and wrong extension files
    valid_files = [f for f in valid_files if '.' in f and \
        f.rsplit('.',1)[-1] in valid_extensions and os.path.isfile(f)]

    if not valid_files:
        raise ValueError("No valid images in %s" % dirpath)

    return max(valid_files, key=os.path.getmtime) 


if __name__ == '__main__':

	time.sleep(1)
	pyautogui.press("f12")
	time.sleep(1)
	# Show latest screenshot
    pic_path = get_latest_image(r'D:/Games/Tibia/packages/Tibia/screenshots/', valid_extensions='png')
	
    img = cv2.imread(pic_path) 
    
	cv2.imshow('cu', img) # s
	cv2.waitKey()

	