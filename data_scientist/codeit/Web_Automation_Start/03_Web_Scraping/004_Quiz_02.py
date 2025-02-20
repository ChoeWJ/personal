import requests
from bs4 import BeautifulSoup

response = requests.get("https://workey.codeit.kr/orangebottle/index")

soup = BeautifulSoup(response.text, 'html.parser')

branch_infos = []

branch_tags = soup.select('div.branch')

for branch in branch_tags:
    branch_name = branch.select_one('p.city').get_text()
    address = branch.select_one('p.address').get_text()
    phone_number = branch.select_one('span.phoneNum').get_text()
    branch_infos.append([branch_name, address, phone_number])

# 테스트 코드
print(branch_infos)
