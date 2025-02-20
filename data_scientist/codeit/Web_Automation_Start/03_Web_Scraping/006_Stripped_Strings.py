import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/music")
soup = BeautifulSoup(response.text, 'html.parser')


populat_artists = []
for tag in soup.select('ul.popular__order li'):
    populat_artists.append(list(tag.stripped_strings)[1])

print(populat_artists)


# populat_artists = []
# for tag in soup.select('ul.popular__order li'):
#     populat_artists.append(tag.get_text().strip())

# print(populat_artists)


# for tag in soup.select('ul.popular__order li'):
#     print(tag.get_text().strip())
    