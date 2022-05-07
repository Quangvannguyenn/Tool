from multiprocessing import freeze_support
freeze_support()

import undetected_chromedriver as uc
import time
import pyautogui as pg
import requests as r

if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://tiktok.com")
    input("Enter to continue!")
    for i in range(100):
        s = r.session()
        s.headers.update({
            "Host":"tuongtaccheo.com",
            "x-requested-with":"XMLHttpRequest",
            "content-type":"application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        })
        data = {"access_token":"c193616cb65d7e87ed3eb5e47189f46c"}
        dataLog = r.post("https://tuongtaccheo.com/logintoken.php", data=data, headers={
            "Host":"tuongtaccheo.com",
            "upgrade-insecure-requests":"1",
            "x-requested-with":"XMLHttpRequest",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }, allow_redirects=False)
        
        cookieAccount = dataLog.cookies
        tempCookie = cookieAccount.items()
        cookiettc = "_fbp=fb.1.1650854537394.470839682; __gads=ID=2ed5d539f54526a3-22eeca2e6cd200e8:T=1650854514:RT=1650854514:S=ALNI_MZhS7v90q29OF5wnZnP5eO4_u0cmA; PHPSESSID="+tempCookie[0][1]+"; _gid=GA1.2.2004913131.1651804665; __gpi=UID=0000052e4f328e8d:T=1651817863:RT=1651817863:S=ALNI_MbNdwFwsBHQK0ZWnP0rQvXFC9Wj_Q; _ga_6RNPVXD039=GS1.1.1651817892.6.1.1651820349.0; _ga=GA1.2.674422149.1650854537; _gat_gtag_UA_88794877_6=1"
        
        dataJob = s.get("https://tuongtaccheo.com/tiktok/kiemtien/subcheo/getpost.php", cookies=cookieAccount).json()
        
        getMoney = {
            "Host":"tuongtaccheo.com",
            "x-requested-with":"XMLHttpRequest",
            "upgrade-insecure-requests": "1",
            "content-type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
            "referer": "https://tuongtaccheo.com/tiktok/kiemtien/subcheo",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "cookie":cookiettc
        }

        db = "id="
        count = 0
        for i in range(len(dataJob)):
            idpost = dataJob[i]['idpost']
            linkUser = dataJob[i]['link']
            driver.get("https://tiktok.com/@"+linkUser)
            time.sleep(8)
            try:
                driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/button').click()
                print("FOLLOW id "+idpost)
            except:
                print("User Not Found!")
                continue
            time.sleep(10)
            db = db+idpost+","
            count = count+1
            if count == 8:
                getCoin = s.post("https://tuongtaccheo.com/tiktok/kiemtien/subcheo/nhantien.php", headers=getMoney, data=db).json()
                print(getCoin['mess'])
                count = 0
                db = "id="