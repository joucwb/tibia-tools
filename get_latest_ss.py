import os
import cv2
import pyautogui
import time
import numpy as np

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


def is_visible(template, imgpath, SS_HOTKEY, keep_diff=False):
    """
    Check if the image file is on the screen.
    After check, remove the png file.
    """
    pyautogui.press(SS_HOTKEY) # Take screenshot
    time.sleep(1)
    # Get the latest snapshot on the imgpath dir
    pic_path = get_latest_image(imgpath, valid_extensions='png') 
    # Read the snapshot
    img_rgb = cv2.imread(pic_path)
    # Changing: rgb -> grayscale
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # Looking for the template
    res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    threshold = 0.8
    loc = np.where( res >= threshold)

    if keep_diff == True:
        w, h = template.shape[::-1]
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        cv2.imwrite('diff.png',img_rgb)
        
    print(loc)
    os.remove(pic_path)

    



if __name__ == '__main__':
    SS_HOTKEY = "f12"
    SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
    time.sleep(1)
    # pyautogui.press(SS_HOTKEY)
    # time.sleep(1)
    # Show latest screenshot
    # pic_path = get_latest_image(r'D:/Games/Tibia/packages/Tibia/screenshots/', valid_extensions='png')
    
    # print(pic_path)
    # img = cv2.imread(pic_path) 
    template = cv2.imread('D:/Documents/git/tibia-tools/imgs/teste.png',0)
    is_visible(template, SS_DIRPATH, SS_HOTKEY, True)
    # cv2.imshow('cu', img)
    # cv2.waitKey()
    # os.remove(pic_path)