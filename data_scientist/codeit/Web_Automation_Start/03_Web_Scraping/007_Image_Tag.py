import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/ratings/index")

soup = BeautifulSoup(response.text, 'html.parser')


print(soup.select_one('img'))