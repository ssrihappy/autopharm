from selenium import webdriver

# Chrome 브라우저를 자동으로 설치하여 WebDriver를 설정
import chromedriver_autoinstaller

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep

#import pandas as pd
from selenium.webdriver.common.keys import Keys

## 주의사항 : nprotect online security 항상 실행

##24년 7월 1일 이후 일반결제 자동화


id_pico = '아이디 입력하세요'
pw_pico = '비밀번호'
id_bp = '아이디'
pw_bp = '비밀번호'


def picomall(id, pw):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 표시 제거
    options.add_experimental_option('useAutomationExtension', False)  # 자동화 확장 기능 사용 안 함

    chromedriver_autoinstaller.install()
    #options.add_argument('headless')  
    driver = webdriver.Chrome(options=options)     

    url_bp = 'https://www.picomall.co.kr/member/login.do'
    url_bp_charge = 'https://www.picomall.co.kr/order/deposit_buying.do?paytype=04'

    driver.get(url_bp)
    driver.find_element(By.XPATH, '//*[@id="member_id"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="member_pw"]').send_keys(pw)
    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="Frm"]/article/input[3]').click()
    sleep(2)
    driver.implicitly_wait(5)
    driver.get(url_bp_charge)
    sleep(2)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="container"]/section/div/div/article/ul/li[2]/button').click()
    sleep(1)
    driver.implicitly_wait(5)

    driver.switch_to.alert.accept()

    driver.implicitly_wait(5)

    sleep(1)
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])

    #iframe 이지페이
    iframe_element = driver.find_element(By.ID, 'frame_content')
    driver.switch_to.frame(iframe_element)

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div[1]').click() # 동의하기
    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div[2]/a[2]').click() #확인
    sleep(2)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btn_029"]').click() # 신한카드
    sleep(2)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="div_cardArea"]/div[8]/a[2]').click() # 다음

    sleep(1)
    driver.implicitly_wait(5)

    driver.switch_to.default_content()
    sleep(1)
    driver.implicitly_wait(5)

    #iframe 신한
    iframe_element2 = driver.find_element(By.ID, 'KICC_LAYER_TARGET')
    driver.switch_to.frame(iframe_element2)
    sleep(1)
    driver.implicitly_wait(5)
    iframe_element3 = driver.find_element(By.ID, 'v3dframe')
    driver.switch_to.frame(iframe_element3)

    ###
    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="fanView"]/div[2]/ul/li[2]/a').click() #일반결제

    #패스워드 결제(사전등록)

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="otherView"]/div[3]/ul/li[3]/a').click() #패스워드결제

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="e2e_smartId_useyn_toggle"]').click() #가상키보드
    sleep(1)

    #!!!!!가상키보드 매핑작업 하세요, img[0~45] - 결제비밀번호!!!!!!
    driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-smartId"]/div/div[2]/img[??]').click() 
    
    sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-smartId"]/div/div[4]/img[45]').click() #완료
    sleep(1.5)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click() #결제클릭

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btnNext"]').click() #결제클릭

    sleep(1)
    driver.implicitly_wait(5)

    driver.switch_to.default_content()
    sleep(1)
    driver.implicitly_wait(5)
    driver.switch_to.frame(iframe_element)

    driver.find_element(By.XPATH, '//*[@id="ckcs3"]').click() #결제클릭

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div[3]/div[3]/a[2]').click() #동의클릭

    sleep(1)
    driver.implicitly_wait(5)
    driver.switch_to.alert.accept()


    driver.quit()


    return driver

def baropharm(id, pw):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("disable-blink-features=AutomationControlled")  # 자동화 탐지 방지
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 표시 제거
    options.add_experimental_option('useAutomationExtension', False)  # 자동화 확장 기능 사용 안 함

    chromedriver_autoinstaller.install()
    #options.add_argument('headless')  
    driver = webdriver.Chrome(options=options)     

    url_bp = 'https://www.baropharm.com/login'
    url_bp_charge = 'https://www.baropharm.com/charge'

    driver.get(url_bp)
    driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(pw)
    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="__next"]/div/div/div[1]/div/div[2]/form/div[2]/button').click()
    sleep(2)
    driver.implicitly_wait(5)
    driver.get(url_bp_charge)
    sleep(2)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/main/article/div/div/div/div[1]/div[3]/ul/li[7]/div/label').click() # 일반결제 클릭
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/div[12]/div[2]/main/article/div/div/div/div[2]/button/span').click() # 충전하기
    sleep(2)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '/html/body/div[131]/div/div[3]/button[3]').click() #확인
    sleep(2)
    driver.implicitly_wait(5)
    driver.switch_to.window(driver.window_handles[1])

    ### 페이레터 결제로 이동
    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="divAgreementList"]/div/div/div[1]/div[2]/label').click() #확인

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="divAgreementList"]/div/a').click() #확인

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="frmAuth"]/div/div[1]/div[5]/div[2]/div[1]').click() #신한

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click() #다음
    return driver

def payletter_module(driver):
    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="fanView"]/div[2]/ul/li[2]/a').click() #일반결제

    #패스워드 결제(사전등록)

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="otherView"]/div[3]/ul/li[3]/a').click() #패스워드결제

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="e2e_smartId_useyn_toggle"]').click() #가상키보드
    sleep(1)

    #!!!!!가상키보드 매핑작업 하세요, img[0~45] - 결제비밀번호!!!!!!
    driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-smartId"]/div/div[2]/img[??]').click() 
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    sleep(0.2)
    driver.find_element(By.XPATH, '//*[@id="nppfs-keypad-smartId"]/div/div[4]/img[45]').click() #완료
    sleep(1.5)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btnConfirm"]').click() #결제클릭

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btnNext"]').click() #결제클릭

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="frmAuth"]/ul/li/div/label').click() #동의클릭

    sleep(1)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="btnSubmit"]').click() #결제클릭

    driver.quit()


    

payletter_module(baropharm(id_bp, pw_bp)) #바로팜 결제


picomall(id_pico, pw_pico) #피코몰 결제
