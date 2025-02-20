import requests
from bs4 import BeautifulSoup

response = requests.get(" https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')    # rating_page 내의 html을 parser(정리)

tr_tag = soup.select('tr')[1]
td_tags = tr_tag.select('td') # == td_tags = tr_tag.select('*')

# print(td_tags)

for tag in td_tags:
    print(tag.get_text())

""" 슬라이싱
td_tags = soup.select('td')[:4]
for tag in td_tags:
    print(tag.get_text())
"""