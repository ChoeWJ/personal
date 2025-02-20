from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# 크롬 드라이버 생성
driver = webdriver.Chrome()

# 페이지 로딩이 완료되기까지 대기 시간
driver.implicitly_wait(3)

# 사이트 접속하기
driver.get("https://workey.codeit.kr/costagram")

# == Beautifulsoup
driver.find_element(by=By.CSS_SELECTOR, value='.top-nav__login-link').click()
driver.find_element(by=By.CSS_SELECTOR, value='.login-container__login-input').send_keys('codeit')
driver.find_element(by=By.CSS_SELECTOR, value='.login-container__password-input').send_keys('datascience')
driver.find_element(by=By.CSS_SELECTOR, value='.login-container__login-button').click()

# 5초 기다리기
sleep(5)

# 크롬 드라이버 종료
driver.quit()