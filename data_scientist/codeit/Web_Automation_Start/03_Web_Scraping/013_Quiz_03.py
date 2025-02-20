import requests
from bs4 import BeautifulSoup
import csv

response = requests.get("https://workey.codeit.kr/orangebottle/index")

csv_file = open('오렌지_보틀.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['지점 이름', '주소', '전화번호'])

soup = BeautifulSoup(response.text, 'html.parser')

branch_tag = soup.select('div.branch')

branch_infos = []
for tag in branch_tag:
    branch_name = tag.select_one('p.city').get_text()
    address = tag.select_one('p.address').get_text()
    phone_number = tag.select_one('span.phoneNum').get_text()
    csv_writer.writerow([branch_name, address, phone_number])
    
csv_file.close()
    




# import requests
# from bs4 import BeautifulSoup
# from openpyxl import Workbook


# response = requests.get("https://workey.codeit.kr/orangebottle/index")

# wb = Workbook(write_only=True)
# ws = wb.create_sheet("오린제 보틀 정보")
# ws.append(['지점 이름', '주소', '전화번호'])

# soup = BeautifulSoup(response.text, 'html.parser')

# branch_tag = soup.select('div.branch')

# branch_infos = []
# for tag in branch_tag:
#     branch_name = tag.select_one('p.city').get_text()
#     address = tag.select_one('p.address').get_text()
#     phone_number = tag.select_one('span.phoneNum').get_text()
#     row =[
#         branch_name,
#         address,
#         phone_number
#     ]
#     ws.append(row)

# wb.save("오렌지_보틀.xlsx")