from pynput.mouse import Controller
import pyautogui
import time


count = 0
time.sleep(15)
for i in range(1000):
    pyautogui.click(265, 395)
    time.sleep(1)
    pyautogui.click(1225, 398)
    time.sleep(10)
    pyautogui.click(421, 339)
    pyautogui.click(1374, 345)
    time.sleep(10)
    pyautogui.click(102, 71)
    pyautogui.click(1064, 74)
    time.sleep(3)
    pyautogui.click(586, 27)
    pyautogui.click(1548, 30)
    count = count+1
    time.sleep(2)
    if count == 8:
        time.sleep(2)
        pyautogui.click(147, 315)
        pyautogui.click(1098, 315)
        count = 0
        time.sleep(1)
        pyautogui.click(102, 71)
        pyautogui.click(1064, 74)
        time.sleep(3)
