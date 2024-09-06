
'''
Mobile Automation Test 참고자료 


Kakao Game SDK Test App
Device: V10 (LGF600Kb1134738)
'''
import unittest
import os
from appium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
 
class KakaoGameSDKLoginOutTest(unittest.TestCase):
 
    def setUp(self):
        
        # Kakao Game SDK Test App 경로
        app = os.path.join(os.path.dirname(__file__), 'D:\\Test_Appium\\KakaogameSDK', 'KakaoGameSDK_Test_App_3.8.0.1.apk')
        app = os.path.abspath(app)

        # Set up appium
        # Appium 서버의 포트는 4001로 지정합니다.
        # 그리고 desired_capabilities에 연결하려는 디바이스(V10)의 정보를 넣습니다.
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4001/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'Android',
                'platformVersion': '6.0',
                'deviceName': 'V10',
                'automationName': 'Appium',
                'appPackage': 'com.kakaogame.sample',
                'appActivity': 'com.kakaogame.sample.SampleActivity',
                'udid': 'LGF600Kb1134738'
            })

    def test_search_field(self):

        # appiun의 webdriver를 초기화 합니다.
        driver = self.driver

        # selenium의 WebDriverWait을 사용합니다. element가 나올때 까지 최고 20초까지 기다립니다.
        wait = WebDriverWait(driver, 20)
        
        # Login 버튼을 클릭(탭) 합니다.
        # Login element를 ID로 찾고 클릭할 수 있을 때까지 최대 20초까지 기다립니다.
        sdkLogin = wait.until(EC.element_to_be_clickable((By.ID, 'com.kakaogame.sample:id/login_ui_button')))
        sdkLogin.click()

        # "카카오 계정으로 로그인"을 클릭(탭)합니다.
        kakaoLogin = driver.find_element_by_id('com.kakaogame.sample:id/kakao_game_login_idp_item_name')
        kakaoLogin.click()

        # "다른 카카오계정으로 로그인"을 클릭(탭)합니다.
        # 만약 디바이스에 카카오톡이 설치되어 있지 않다면 try/except문을 사용해 처리해야 합니다.

        try:
            otherKakaoAccount = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.ListView/android.widget.LinearLayout[2]/android.widget.TextView')
            otherKakaoAccount.click()
        except NoSuchElementException:
            print('No element found')

        # 계정을 입력합니다.
        # 계정과 비밀번호 입력 화면이 나오기 전 로딩 화면이 뜨게 됩니다.
        # 로딩 할때까지 기다려야 하니 wait.until()함수를 사용합니다.
        account = wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.widget.EditText')))
        account.click()
        account.send_keys('dejavuwing@gmail.com')

        # 비밀번호를 입력합니다.
        password = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.widget.EditText')
        password.click()
        password.send_keys('qwert1234%')

        # 로그인 버튼을 클릭(탭)합니다.
        signin = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[2]')
        signin.click()

        # Kakao Game SDK Test App 화면에서 logout 버튼을 클릭(탭)합니다.
        appLogout = wait.until(EC.element_to_be_clickable((By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.support.v4.view.ViewPager/android.widget.ListView/android.widget.FrameLayout[7]/android.widget.Button')))
        appLogout.click()

        # 다시한번 로그아웃을 확인합니다.
        conformLogout = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.TextView[2]')
        conformLogout.click()

        # Start 버튼을 클릭합니다.
        start = driver.find_element_by_id('com.kakaogame.sample:id/start_button')
        start.click()

        sleep(30)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(KakaoGameSDKLoginOutTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
