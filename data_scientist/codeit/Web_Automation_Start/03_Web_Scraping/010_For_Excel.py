import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)  # 새로운 Workbook 객체 생성 / 파일의 데이터를 쓰기만 하기 위한 write_only 모듈사용
ws = wb.create_sheet('TV Ratings') # 새로운 워크시트 생성
ws.append(['순위', '채널', '프로그램', '시청률']) # 행 추가


response = requests.get(" https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')

for tr_tag in soup.select('tr')[1:]:   # 두 번째 행부터 슬라이싱
    td_tags = tr_tag.select('td')
    row = [
        td_tags[0].get_text(),    # 순위
        td_tags[1].get_text(),    # 채널
        td_tags[2].get_text(),    # 프로그램
        td_tags[3].get_text(),    # 시청률
    ]
    ws.append(row)

wb.save('시청률_2010년1월1주차.xlsx')
