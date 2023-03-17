
import time
from appium import webdriver                                                    
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains                
from appium.webdriver.common.touch_action import TouchAction   
from selenium.webdriver.common.actions.action_builder import ActionBuilder      
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from selenium.common.exceptions import NoSuchElementException

desired_cap = {
    "appium:deviceName":"RFCMB029QWF",
    "appium:platformName":"android",
    "appium:appPackage":"com.nhn.android.search",
    "appium:appActivity":"com.nhn.android.search.ui.pages.SearchHomePage"
}

def webDriverCal():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    driver.implicitly_wait(10)
    return driver

"""
-자동화 테스트 시나리오- 

네이버 시작하기 버튼             > com.nhn.android.search.SearchMain:id/startNaverBtnLayout
아이디 입력하여 로그인           > com.nhn.android.search.SearchMain:id/goLoginBtn
네이버 로그인 페이지 id 필드     > com.nhn.android.search:id/text_id
네이버 로그인 페이지 pw 필드     > com.nhn.android.search:id/text_pw
로그인 버튼                     > com.nhn.android.search:id/button_sign_in
네이버 메인 페이지 홈 버튼       > com.nhn.android.search.SearchMain:id/dimmedCoachBottomBg                    
좌측메뉴 버튼                   > com.nhn.android.search.SearchMain:id/slideMenuView
로그아웃 버튼                   > com.nhn.android.search.SearchMain:id/footerLoginTextView

"""
try: 

    driver = webDriverCal()
    wait = WebDriverWait(driver, 10)
    
    # 네이버 시작하기
    driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/startNaverBtnLayout').click()
    driver.implicitly_wait(10)
    print("1")
    
    # 아이디 입력으로 로그인 진행
    driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/goLoginBtn').click()
    driver.implicitly_wait(10)
    print("2")
    
    # 로그인 id 필드 값 입력
    driver.find_element(By.ID, 'com.nhn.android.search:id/text_id').send_keys('nemogun21')
    driver.implicitly_wait(10)
    print("3")
    
    # 로그인 P/W 필드 값 입력
    driver.find_element(By.ID, 'com.nhn.android.search:id/text_pw').send_keys('20221130bin!')
    driver.implicitly_wait(10)
    print("4")

    # 로그인 버튼 선택 
    driver.find_element(By.ID, 'com.nhn.android.search:id/button_sign_in').click()
    driver.implicitly_wait(10)
    print("5")

    # 단말기 등록 팝업 
    driver.find_element(By.ID, 'new.dontsave').click()
    driver.implicitly_wait(10)
    print("6")

    driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/locationStartBtn').click()
    driver.implicitly_wait(10)
    print("7")

    # 기기위치 등록 팝업 허용 
    driver.find_element(By.ID, 'com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()
    driver.implicitly_wait(10)
    print("8")

    # 네이버 메인 페이지 홈 버튼
    driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/dimmedCoachBottomBg').click()
    driver.implicitly_wait(10)
    print("9")

    # 메인페이지 좌측 메뉴 버튼  
    driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/slideMenuView').click()
    driver.implicitly_wait(10)
    print("10")

    # 로그아웃 버튼 
    button1= driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/footerLoginTextView')
    print("button1",button1)
    driver.implicitly_wait(30)

except NoSuchElementException:
    print('No element found')

print("Mobile App AutoTest End")