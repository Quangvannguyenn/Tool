from pynput.mouse import Controller
import pyautogui as pg
import time

mouse = Controller()
time.sleep(10)


count = 0
for i in range(1000):
    pg.click(344, 370)
    time.sleep(10)
    pg.click(624, 328)
    count = count+1
    time.sleep(8)
    pg.hotkey("f5")
    time.sleep(3)
    pg.hotkey("ctrl", "w")
    time.sleep(2)
    if count == 8:
        pg.click(302, 292)
        count = 0
        time.sleep(3)
        pg.hotkey("f5")
        time.sleep(4)
