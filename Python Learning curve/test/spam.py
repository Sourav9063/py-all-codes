import pyautogui

import time
time.sleep(15)
f = open("E:/py all codes/Python Learning curve/test/spam", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(3)
