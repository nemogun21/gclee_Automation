

#import unittest
from appium import webdriver                                            #  pip install Appium-Python-Client > appium 라이브러리 설치 필요  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
# from configuration import webDriver
# from selenium.webdriver.common.action_chains import ActionChains      # ActionChains > 라이브러리 

desired_cap = {
    "appium:deviceName":"520048495a73b471",
    "appium:platformName":"android",
    # "appium:appPackage":"com.sec.android.app.sbrowser",
    # "appium:appPackage":"com.chartcross.gpstest",
    "appium:appPackage":"com.nhn.android.search",
    "appium:appActivity":"com.nhn.android.search.ui.pages.SearchHomePage"
    #"appium:appActivity":"com.chartcross.gpstest.MainActivity"
}

def cal():
    wd  = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    wd.implicitly_wait(10)
    return wd


wd = cal()

# appium이 돌아가고 있는 서버의 http 주소를 입력해줍니다.
# 현재를 local에서 실행하고 있기 때문에 아래처럼 작성하였습니다.
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
actionchains = webdriver.ActionChains(wd)

# selected_button = driver.find_element(By.CSS_SELECTOR,"div.pagination ul").text         
# serch_box = driver.find_element(By.CSS_SELECTOR,"div.green_window input#query")
# serch_button = driver.find_element(By.CSS_SELECTOR,"#search_btn")
# iframe = driver.find_element(By.CSS_SELECTOR, "div.notice_box")


# button1 = wd.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/startNaverBtnLayout')
# button1 = wd.find_element(By.XPATH, '//android.widget.TextView[@content-desc="네이버 시작하기 버튼"]')
wd.find_element(By.XPATH, '//android.widget.TextView[@content-desc="네이버 시작하기 버튼"]').click()

# button2 = wd.find_element(By.ID, 'com.nhn.android.search.SearchMain:id/locationStartBtn')
# button2 = wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[7]")
wd.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[7]").click()
# /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[7]



# actionchains.move_to_element(button1)\
#     .pause(3)\
#     .send_keys("selenium")\
#     .pause(10)\
#     .scroll_to_element(iframe)\
#     .pause(2)\
#     .move_to_element(serch_box)\
#     .pause(1)\
#     .click(serch_button)\
#     .pause(1)\
#     .perform()


print("1")


# driver.implicitly_wait(10)

