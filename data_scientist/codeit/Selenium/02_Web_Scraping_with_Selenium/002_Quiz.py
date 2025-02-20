from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/orangebottle/index")
sleep(1)

branch_infos = []

for element in driver.find_elements(by=By.CSS_SELECTOR, value='div.branch'):
    branch_name = element.find_element(by=By.CSS_SELECTOR, value='p.city').text
    address = element.find_element(by=By.CSS_SELECTOR, value='p.address').text
    phone_number = element.find_element(by=By.CSS_SELECTOR, value='span.phoneNum').text
    branch_infos.append([branch_name, address, phone_number])

print(branch_infos)

sleep(5)
driver.quit()