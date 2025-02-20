from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3) # 사이트가 로딩될 떄 까지 대기시간

driver.get("https://workey.codeit.kr/costagram")
sleep(1)

driver.find_element(by=By.CSS_SELECTOR, value="#app > nav > div > a").click()
sleep(1)

driver.find_element(by=By.CSS_SELECTOR, value="#app > div > div > div > form > input.login-container__login-input").send_keys('codeit')
driver.find_element(by=By.CSS_SELECTOR, value="#app > div > div > div > form > input.login-container__password-input").send_keys('datascience')
driver.find_element(by=By.CSS_SELECTOR, value="#app > div > div > div > form > input.login-container__login-button").click()

sleep(5)

driver.quit()