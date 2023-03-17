
import requests as rq
import json
import time
import re                                                       # Regular Expression > 정규식
from bs4 import BeautifulSoup as bs                             # from 모듈 명 import 해당 모듈의 함수명 > 모듈 명 없이 함수명으로만 사용가능 구문
from selenium import webdriver                                  # selenium version 확인  > 터미널 창에서 > pip list 
from selenium.webdriver.common.by import By                  
from selenium.webdriver.chrome.service import Service as ChromeService 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager        # pip install webdriver_manager  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

def chromewebdriver():
    chrome_service = ChromeService(executable_path = ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option("detach",True)                              # 브라우저 즉시 닫힘 방지 
    options.add_experimental_option("excludeSwitches",["enable-logging"])       # 불필요한 오류 메시지 제거 > "시스템에 부착된 장치가 작동하지 않습니다."  

    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver

"""
selenium v4 메소드 포맷 
driver.find_element(By.XPATH, '//button[text()="Some text"]')
driver.find_element(By.XPATH, '//button')
driver.find_element(By.ID, 'loginForm')
driver.find_element(By.LINK_TEXT, 'Continue')
driver.find_element(By.PARTIAL_LINK_TEXT, 'Conti')
driver.find_element(By.NAME, 'username')
driver.find_element(By.TAG_NAME, 'h1')
driver.find_element(By.CLASS_NAME, 'content')
driver.find_element(By.CSS_SELECTOR, 'p.content')

========================================================================================================================================

driver = chromewebdriver()
url = "https://pjt3591oo.github.io/"
driver.get(url)
driver.maximize_window()

# time.sleep(5)
driver.implicitly_wait(10)

# selected_selectoor = driver.find_element(By.CSS_SELECTOR,"div.p h3 a").text                            # 해당 태그의 값 가져 오기 
# selected_selectoor = driver.find_element(By.CSS_SELECTOR,"div.p h3 a").get_attribute("a")
selected_Link_Text = driver.find_element(By.LINK_TEXT,"[programming] [react] react 작업환경 설")
selected_button = driver.find_element(By.CSS_SELECTOR,"div.pagination ul").text         

"""
"""
ActionChains 동작 리스트
.click_and_hold() : 해당 요소 마우스 길게 누르기 

# 요소로 스크롤
iframe = driver.find_element(By.TAG_NAME, "iframe")
.scroll_to_element(iframe)\

"""
# ---------------------------------------------------------------------------------------------------------------------------
# 네이버 검색기능 확인 
driver = chromewebdriver()
url = "https://naver.com/"
driver.get(url)
driver.maximize_window()
actionchains = webdriver.ActionChains(driver)

# selected_button = driver.find_element(By.CSS_SELECTOR,"div.pagination ul").text         
serch_box = driver.find_element(By.CSS_SELECTOR,"div.green_window input#query")
serch_button = driver.find_element(By.CSS_SELECTOR,"#search_btn")
iframe = driver.find_element(By.CSS_SELECTOR, "div.notice_box")

actionchains.move_to_element(serch_box)\
    .pause(3)\
    .send_keys("selenium")\
    .pause(10)\
    .scroll_to_element(iframe)\
    .pause(2)\
    .move_to_element(serch_box)\
    .pause(1)\
    .click(serch_button)\
    .pause(1)\
    .perform()
    
print("1", serch_box)
print("2", serch_button)
print("3", iframe)

driver.implicitly_wait(10)
