import json
import gtts
import requests as r
from selenium import webdriver
import webbrowser
import time
import pyautogui
import pyttsx3
from gtts import gTTS
import playsound

profile = r.get(
    f'https://traodoisub.com/api/?fields=profile&access_token=TDS0nI1IXZ2V2ciojIyVmdlNnIsIST4FWN5klUiN2QIZVeR5URiojIyV2c1Jye')
dataProfile = ((json.loads(profile.text))["data"])["xu"]
print(dataProfile)

obj = gTTS(lang='vi', text=dataProfile)
obj.save("datacoin.mp3")
playsound.playsound("datacoin.mp3")
