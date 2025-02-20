import requests
from bs4 import BeautifulSoup

response = requests.get(" https://workey.codeit.kr/ratings/index")
rating_page = response.text

soup = BeautifulSoup(rating_page, 'html.parser')    # rating_page 내의 html을 parser(정리)

program_title_tages = soup.select('td.program')

progrma_titles = []
for tag in program_title_tages:
    progrma_titles.append(tag.get_text())

print(progrma_titles)


    