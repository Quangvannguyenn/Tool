import json
import requests as r
from selenium import webdriver
import webbrowser
import time
import pyautogui


fileToken = open("accessToken.txt", "r")
access_token = fileToken.read()


numOfJob = 10
countJob = 0

time.sleep(5)
for j in range(10):

    rq = r.get(
        f'https://traodoisub.com/api/?fields=tiktok_follow&access_token={access_token}')
    dataJobs = (json.loads(rq.text))["data"]
    done_jobs = (json.loads(rq.text))["cache"]
    for i in range(len(dataJobs)):
        id_job = dataJobs[i]["id"]
        r.get(
            f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW_CACHE&id={id_job}&access_token={access_token}')
        webbrowser.open((dataJobs[i])["link"])
        time.sleep(10)
        pyautogui.click()
        time.sleep(10)
        pyautogui.hotkey('ctrl', 'w')
        countJob = countJob + 1
        if countJob == numOfJob:
            r.get(
                f'https://traodoisub.com/api/coin/?type=TIKTOK_FOLLOW&id=TIKTOK_FOLLOW_API&access_token={access_token}')
            countJob = 0
            profile = r.get(
                f'https://traodoisub.com/api/?fields=profile&access_token={access_token}')
            dataProfile = ((json.loads(profile.text))["data"])["xu"]
            print("Coin: "+dataProfile)
        pyautogui.hotkey('f5')
        time.sleep(3)
