from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(3)

driver.get("https://workey.codeit.kr/music")
sleep(1)

popular_artists = []

for element in driver.find_elements(by=By.CSS_SELECTOR, value = 'ul.popular__order li'):
    popular_artists.append(element.text.strip())
     
print(popular_artists)

sleep(5)

driver.quit()




# Beautifulsoup
#
# import requests
# from bs4 import BeautifulSoup

# response = requests.get('https://workey.codeit.kr/music')
# music_page = response.text

# soup = BeautifulSoup(music_page, 'html.parser')

# popular_artists = []

# for tag in soup.select('ul.popular__order li'):
#     popular_artists.append(tag.get_text().strip())

# print(popular_artists)