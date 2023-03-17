
import time
from appium import webdriver                                                    #  pip install Appium-Python-Client > appium 라이브러리 설치 필요  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains                # ActionChains > 라이브러리 
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction   
from selenium.webdriver.common.actions.action_builder import ActionBuilder      # https://github.com/appium/python-client/blob/master/appium/webdriver/extensions/action_helpers.py
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
id_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.login-container__login-input')))
id_box.send_keys('codeit')

시나리오 1 
네이버 시작하기 버튼 id  >  com.nhn.android.search.SearchMain:id/startNaverBtnLayout
아이디 입력하여 로그인   >  com.nhn.android.search.SearchMain:id/goLoginBtn
네이버 로그인 페이지 id 필드    > com.nhn.android.search:id/text_id
네이버 로그인 페이지 pw 필드    > com.nhn.android.search:id/text_pw
로그인 버튼                    > com.nhn.android.search:id/button_sign_in
뒤로가기 버튼                  > com.nhn.android.search:id/button_back

시나리오 2
나중에 할게요 버튼             > com.nhn.android.search.SearchMain:id/laterLoginBtn
네이버 시작하기 버튼           > com.nhn.android.search.SearchMain:id/locationStartBtn
기기위치 팝업 창               > com.android.permissioncontroller:id/permission_allow_foreground_only_button
네이버 메인 페이지 홈 버튼      > com.nhn.android.search.SearchMain:id/dimmedCoachBottomBg
기기등록 페이지 미 등록 버튼    > new.dontsave                    

"""
try: 

    driver = webDriverCal()
    wait = WebDriverWait(driver, 30)
    # action = TouchAction(driver)

    driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/startNaverBtnLayout').click()
    driver.implicitly_wait(30)
    print("1")

    # driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/goLoginBtn').click()
    # driver.implicitly_wait(10)
    # print("2")

    # driver.find_element(By.ID, 'com.nhn.android.search:id/text_id').send_keys('nemogun21')
    # driver.implicitly_wait(10)
    # print("3")s

    # driver.find_element(By.ID, 'com.nhn.android.search:id/text_pw').send_keys('20221130bin!')
    # driver.implicitly_wait(10)
    # print("4")

    # 로그인 버튼 선택 
    # driver.find_element(By.ID, 'com.nhn.android.search:id/button_sign_in').click()
    # driver.implicitly_wait(10)
    # print("5")

    # # 단말기 등록 팝업 
    # driver.find_element(By.ID, 'new.dontsave').click()
    # driver.implicitly_wait(10)
    # print("6")

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
    # button1= driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/footerLoginTextView')
    # print("button1",button1)
    # driver.implicitly_wait(30)


    # start1= driver.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/headerTitleView')
    # ds1= driver.find_element(By.ID, '//android.widget.LinearLayout[@content-desc="패션타운 버튼"]/android.widget.TextView')


    # driver.refresh()
    driver.implicitly_wait(10)

    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(x = 535,y = 1000)  # 835
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(x = 535,y = 3000)  # 1020
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()


    # driver.drag_and_drop(start1,ds1)
    # driver.scroll(start1,ds1,10)
    # driver.swipe(start_x=535,start_y=835,end_x=635,end_y=1020)
    # driver.flick(start_x=535,start_y=1000,end_x=535,end_y=10000)

    print("Test end")

except NoSuchElementException:
    print('No element found')

