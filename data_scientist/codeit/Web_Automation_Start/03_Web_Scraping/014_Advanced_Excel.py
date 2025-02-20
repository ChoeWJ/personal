import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

wb = Workbook(write_only=True)

for year in range(2010, 2019):
    ws = wb.create_sheet(f"{year}")
    ws.append(['기간', '순위', '채널', '프로그램', '시청률'])

    for month in range(1, 13):
        for weekIndex in range(0, 5):
            url = f"https://workey.codeit.kr/ratings/index?year={year}&month={month}&weekIndex={weekIndex}"
            response = requests.get(url)
            rating_pages = response.text
            soup = BeautifulSoup(rating_pages, 'html.parser')

            for tr_tag in soup.select('tr')[1:]:
                td_tags = tr_tag.select('td')
                period = f"{year}년 {month}월 {weekIndex + 1}주차"
                row = [
                    period,
                    td_tags[0].get_text(),
                    td_tags[1].get_text(),
                    td_tags[2].get_text(),
                    td_tags[3].get_text()
                ]
                ws.append(row)


wb.save("시청률.xlsx")