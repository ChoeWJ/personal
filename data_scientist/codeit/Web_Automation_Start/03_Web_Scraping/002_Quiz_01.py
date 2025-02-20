import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")

soup = BeautifulSoup(response.text, "html.parser")

phone_number_tags = soup.select("span.phoneNum")

phone_numbers = []
for number in phone_number_tags:
    phone_numbers.append(number.get_text())


print(phone_numbers)
