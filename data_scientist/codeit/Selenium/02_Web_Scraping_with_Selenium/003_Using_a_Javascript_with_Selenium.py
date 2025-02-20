from time import sleep
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# 엑셀 파일 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이리스트')
ws.append(['제목', '해시태그', '좋아요 수', '노래 수'])

options = Options()
options.add_argument('--window-size=1980,1000')

# Selenium WebDriver 초기화
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(3)

# 웹페이지 접속
driver.get("https://workey.codeit.kr/music")
sleep(3)


# 현재 scrollHeight 가져오기
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # 스크롤을 가장 아래로 이동
    driver.execute_script('window.scrollBy(0, document.body.scrollHeight);')

    # 새로운 내용 로딩될 때까지 기다림
    sleep(0.5)

    # 새로운 scrollHeight 가져오기
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

# 플레이리스트 데이터 수집
playlists = driver.find_elements(by=By.CSS_SELECTOR, value='div.playlist__meta')

for playlist in playlists:
    title = playlist.find_element(by=By.CSS_SELECTOR, value='h3.title').text
    hashtags = playlist.find_element(by=By.CSS_SELECTOR, value='p.tags').text
    like_count = playlist.find_element(by=By.CSS_SELECTOR, value='span.data__like-count').text
    music_count = playlist.find_element(by=By.CSS_SELECTOR, value='span.data__music-count').text
    ws.append([title, hashtags, like_count, music_count])

# WebDriver 종료 및 엑셀 저장
driver.quit()
wb.save('플레이리스트.xlsx')