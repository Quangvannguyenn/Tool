import pyautogui as pg
from pynput.mouse import Controller
import time

# mouse = Controller()
time.sleep(5)

# print(mouse.position)

count = 0

for i in range(1000):
    pg.click(187, 312)
    pg.click(870, 312)
    pg.click(191, 695)
    pg.click(870, 696)
    time.sleep(10)
    pg.click(348, 266)
    pg.click(1033, 266)
    pg.click(354, 651)
    pg.click(1033, 651)
    count = count+1
    time.sleep(10)
    pg.click(85, 59)
    pg.click(768, 58)
    pg.click(86, 443)
    pg.click(768, 442)
    time.sleep(3)
    pg.click(395, 21)
    pg.click(1080, 24)
    pg.click(397, 408)
    pg.click(1079, 409)
    time.sleep(3)
    if count == 8:
        pg.click(114, 247)
        pg.click(797, 248)
        pg.click(114, 633)
        pg.click(800, 632)
        count = 0
        time.sleep(4)
