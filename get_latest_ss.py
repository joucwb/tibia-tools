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


def is_visible(template, imgpath, SS_HOTKEY):
    """
    Check if the image file is on the screen
    """
    pyautogui.press(SS_HOTKEY)
    time.sleep(1)

    pic_path = get_latest_image(imgpath, valid_extensions='png')
    image = cv2.imread(pic_path)

    res = cv2.matchTemplate(image,template,cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    time.sleep(1)

    os.remove(image)

    print(min_val, max_val, min_loc, max_loc)




if __name__ == '__main__':
    SS_HOTKEY = "f12"
    SS_DIRPATH = "D:/Games/Tibia/packages/Tibia/screenshots/"
    time.sleep(1)
    # pyautogui.press(SS_HOTKEY)
    # time.sleep(1)
    # Show latest screenshot
    pic_path = get_latest_image(r'D:/Games/Tibia/packages/Tibia/screenshots/', valid_extensions='png')
    
    print(pic_path)
    # img = cv2.imread(pic_path) 
    template = '/imgs/teste.png'
    # is_visible(template, SS_DIRPATH, SS_HOTKEY)
    # cv2.imshow('cu', img)
    # cv2.waitKey()
    # os.remove(pic_path)