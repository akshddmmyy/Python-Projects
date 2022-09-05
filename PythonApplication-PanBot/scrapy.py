from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime as dt


options=webdriver.ChromeOptions()
options.set_headless(True)
options.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path="F:\\chromedriver_win32\\chromedriver.exe",options=options)


def scrapeinitial():
    driver.get('https://pancakeswap.finance/prediction')
    try:
        disclaimer=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.ID,"predictions-risk-disclaimer")))
        temp=driver.find_element_by_id("beta-checkbox")
        if(temp.is_selected() !=True):
            temp.click()

        temp=driver.find_element_by_id('responsibility-checkbox')
        if(temp.is_selected()!=True):
            temp.click()
          
        temp=driver.find_element_by_id('prediction-disclaimer-continue')  
        if(temp.is_selected()!=True):
            temp.click()

        return 1

    except:
        driver.close()
        return 0

def scrapedata(bet_at,panvalue):
    try:
        value=WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.swiper-slide.swiper-slide-active > div > div > div:nth-child(3) > div:nth-child(2) > div > div:nth-child(2) > div:nth-child(1) > div ")))
        while True:
            tvalue=value.text
            panvalue[0]=tvalue
            if(dt.now()>=bet_at):
                return
        
    except Exception as e:
        return 0


