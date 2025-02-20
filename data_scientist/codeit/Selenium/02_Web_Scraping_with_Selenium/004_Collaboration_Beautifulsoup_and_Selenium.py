from time import sleep

from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By

# 엑셀 파일 생성
wb = Workbook(write_only=True)
ws = wb.create_sheet('플레이리스트')
ws.append(['제목', '해시태그', '좋아요 수', '노래 수'])

# Selenium WebDriver 초기화
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 웹페이지 접속
driver.get("https://workey.codeit.kr/music")
sleep(3)

# 초기 스크롤 및 scrollHeight 확인
driver.execute_script('window.scrollTo(0, 200);')
scroll_height = driver.execute_script('return document.body.scrollHeight')
print(scroll_height)

# 현재 scrollHeight 가져오기
last_height = driver.execute_script('return document.body.scrollHeight')

while True:
    # 스크롤을 가장 아래로 이동
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

    # 새로운 내용 로딩될 때까지 기다림
    sleep(0.5)

    # 새로운 scrollHeight 가져오기
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height

# 스크롤 완료

# 현재 웹 페이지의 html코드를 가져온다
music_page = driver.page_source
driver.quit()

# 가져온 html로 Beautifulsoup 활용
soup = BeautifulSoup(music_page, 'html.parser')

playlists = soup.select('.playlist__meta')

for playlist in playlists:
    title = playlist.select_one('h3.title').get_text()
    hashtags = playlist.select_one('p.tags').get_text()
    like_count = playlist.select_one('span.data__like-count').get_text()
    music_count = playlist.select_one('span.data__music-count').get_text()
    ws.append([title, hashtags, like_count, music_count])



wb.save('플레이리스트.xlsx')