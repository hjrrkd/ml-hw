from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import os

def createDirectory(directory):
    try:
        if not os.path.exists(directory):
            os.mkdir(directory)
    except OSError:
        print("Error: Failed to create the directory")

def crawling_img(name):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.google.co.kr/imghp?hl=ko&tab=wi&authuser=0&ogbl")
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(name)
    elem.send_keys(Keys.RETURN)
    
    SCROLL_PAUSE_TIME = 1
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height

    imgs = driver.find_elements(By.CSS_SELECTOR, ".mNsIhb")
    save_folder = os.path.join(r"D:\Images", name.replace(" ", "_"))
    createDirectory(save_folder)
    
    count = 1  # 카운트를 1부터 시작
    for img in imgs:
        try:
            driver.execute_script("arguments[0].click();", img)
            time.sleep(2)
            
            # 이미지 URL 가져오기
            img_url = driver.find_element(By.CSS_SELECTOR, ".sFlh5c.pT0Scc.iPVvYb").get_attribute("src")
            
            if img_url.startswith('http'):
                file_name = f"{name.replace(' ', '_')}{count}.jpg"  # 파일명을 카운트를 사용하여 생성
                
                path = os.path.join(save_folder, file_name)
                urllib.request.urlretrieve(img_url, path)
                print(f"Downloaded: {path}")
                
                count += 1
                if count > 140:  # 140장의 이미지를 다운로드하면 종료
                    break
        except Exception as e:
            print(f"Error: {e}")
            pass

    driver.close()

categories = ["pc chair"]

for category in categories:
    crawling_img(category)
