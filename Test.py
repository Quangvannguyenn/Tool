import undetected_chromedriver as uc

if __name__ == '__main__':
    driver = uc.Chrome()
    driver.get("https://tiktok.com")
    input("Enter!")
    try:
        driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div/div[1]/button').click()
    except:
        print("Not Found")
    input("Enter to continue!")