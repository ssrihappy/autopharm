import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
from datetime import datetime
import pandas as pd

"""
Version_1.0.0, 2023-05-08
    지원하는 거래처
    1. 백제
    2. 바로팜
    3. 광동몰
    4. 동아답몰        
"""
accounts = pd.read_excel('accounts.xlsx')

#개인정보 입력 주의_계정정보가 담긴 엑셀 파일을 절대 그대로 공유하지 마세요#
########################################################
card_kakao = accounts.loc[0][1]     #카드번호 16자리    #
card_verify = accounts.loc[1][1]    #월/년             #
########################################################
id_bj = accounts.loc[2][1]          # 백제 아이디       #
pw_bj = accounts.loc[3][1]          # 백제 비밀번호     #
########################################################
########################################################
id_bp = accounts.loc[4][1]          # 바로팜 이메일     #
pw_bp = accounts.loc[5][1]          # 바로팜 비밀번호   #
########################################################
########################################################
id_kd = accounts.loc[6][1]          # 광동몰 이메일     #
pw_kd = accounts.loc[7][1]          # 광동몰 비밀번호   #
########################################################
########################################################
id_da = accounts.loc[8][1]          # 동아몰 아이디     #
pw_da = accounts.loc[9][1]          # 동아몰 비밀번호   #
########################################################


def pharm_bj(id, pw, card_kakao, card_verify): #백제 도매상
    options = Options()
    chromedriver_autoinstaller.install()
    options.add_argument('headless')  
    driver = webdriver.Chrome(options=options)     


    url_bj = 'http://ibjp.co.kr/login.act'
    #url_bj_account = 'https://ibjp.co.kr/payment/payment.act'

    driver.get(url_bj)
    driver.find_element(By.XPATH, '//*[@id="loginId"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="pwd"]').send_keys(pw)
    driver.find_element(By.XPATH, '//*[@id="loginBox"]/div[2]/a[3]').click()
    sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gnbPayment"]/a').click()

    driver.find_element(By.XPATH, '//*[@id="CARD_GB1"]').click() #신한 클릭

    driver.find_element(By.XPATH, '//*[@id="CARD_NO1"]').send_keys(card_kakao.split('-')[0])
    driver.find_element(By.XPATH, '//*[@id="CARD_NO2"]').send_keys(card_kakao.split('-')[1])
    driver.find_element(By.XPATH, '//*[@id="CARD_NO3"]').send_keys(card_kakao.split('-')[2])
    driver.find_element(By.XPATH, '//*[@id="CARD_NO4"]').send_keys(card_kakao.split('-')[3])
    driver.find_element(By.XPATH, '//*[@id="CARD_M"]').send_keys(card_verify.split('/')[0])
    driver.find_element(By.XPATH, '//*[@id="CARD_Y"]').send_keys(card_verify.split('/')[1])
    driver.find_element(By.XPATH, '//*[@id="PAYMENT_AMOUNT_TI"]').send_keys('5000')
    sleep(1)
    driver.find_element(By.XPATH, '//*[@id="creditForm"]/div/div/a').click()
    sleep(1)
    try:
        driver.switch_to.alert.accept()
        print('거래처:백제,  결제 성공')
        driver.quit()
    except:
        print('거래처:백제,  결제 실패')
        driver.quit()

def pharm_bp(id, pw): #바로팜
    try:
        options = Options()
        chromedriver_autoinstaller.install()
        options.add_argument('headless')  
        driver = webdriver.Chrome(options=options)     

        url_bp = 'https://www.baropharm.com/login'
        url_bp_account = 'https://www.baropharm.com/charge'

        driver.get(url_bp)
        driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(id)
        driver.find_element(By.XPATH, '//*[@id="userPwd"]').send_keys(pw)
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div/form/button').click()
        sleep(2)
        driver.get(url_bp_account)
        sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[56]/div[2]/main/article/div/div[7]/div[2]/div[2]/div[2]/button/span').click()
        sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[61]/div/div[3]/button[3]').click()
        print('거래처:바로팜, 결제 성공')
        driver.quit()
    except:
        print('거래처:바로팜, 결제 실패')
        driver.quit()

def pharm_kd(id, pw): #광동몰
    options = Options()
    chromedriver_autoinstaller.install()
    options.add_argument('headless')  
    driver = webdriver.Chrome(options=options)     

    url_kd = 'https://kdshop.co.kr/member/login.do'
    url_kd_account = 'https://kdshop.co.kr/mypage/deposit_charge_pop.do'

    driver.get(url_kd)
    driver.find_element(By.XPATH, '//*[@id="member_id"]').send_keys(id)
    driver.find_element(By.XPATH, '//*[@id="member_pw"]').send_keys(pw)
    driver.find_element(By.XPATH, '//*[@id="fromDataField"]/div[1]/div[2]/button').click()
    sleep(2)
    driver.get(url_kd_account)
    sleep(1)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/dl/dd[1]/input').send_keys('5000')

    driver.find_element(By.XPATH, '//*[@id="Frm"]/dl/dd/ul/li[1]/span/label').click()
    driver.find_element(By.XPATH, '/html/body/div[4]/button[2]').click()
    sleep(3)
    try:
        driver.switch_to.alert.accept()
        print('거래처:광동,  결제 성공')
        driver.quit()
    except:
        print('거래처:광동,  결제 실패')
        driver.quit()

def pharm_da(id, pw): #동아답몰
    try:
        options = Options()
        chromedriver_autoinstaller.install()
        #options.add_argument('headless')  
        driver = webdriver.Chrome(options=options)     

        url_da = 'https://www.dapmall.com/mypage/benefit/pscash/list'
        url_da_account = 'https://www.dapmall.com/mypage/benefit/pscash/list'

        driver.get(url_da)
        driver.find_element(By.XPATH, '//*[@id="userId"]').send_keys(id)
        driver.find_element(By.XPATH, '//*[@id="userPw"]').send_keys(pw)
        driver.find_element(By.XPATH, '//*[@id="login-form"]/button').click()
        sleep(2)
        driver.get(url_da_account)
        sleep(1)
        driver.find_element(By.XPATH, '//*[@id="list-form"]/div[2]/p/a').click()
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="amt"]').send_keys('5000')
        driver.find_element(By.XPATH, '//*[@id="pscash-form"]/div[3]/button').click()
        print('거래처:동아몰, 결제 성공')
        driver.quit()
    except:
        print('거래처:동아몰, 결제 실패')
        driver.quit()

counter = 0
pharm_bj(id_bj, pw_bj, card_kakao, card_verify)
try:
    pharm_bj(id_bj, pw_bj, card_kakao, card_verify)
    counter = counter + 1
except:
    print("백제 결제 실패")

msg = '1/4 진행 중, ' + str(counter) + '회 성공'
print(msg)

try:
    pharm_bp(id_bp, pw_bp)
    counter = counter + 1
except:
    print("바로팜 결제 실패")

msg = '2/4 진행 중, ' + str(counter) + '회 성공'
print(msg)

try:
    pharm_kd(id_kd, pw_kd)
    counter += 1
except:
    print("광동몰 결제 실패")

msg = '3/4 진행 중, ' + str(counter) + '회 성공'
print(msg)

try:
    pharm_da(id_da, pw_da)
    counter += 1
except:
    print("동아몰 결제 실패")

msg1 = "오늘은 " + str(datetime.today().date()) + ', ' + str(datetime.today().time())[0:8]
msg2 = '카카오뱅크 신한카드 자동결제 '+ str(counter) + '회 성공'
print(msg1 + '\n' + msg2)

