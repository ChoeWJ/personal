import requests

# https://workey.codeit.kr/ratings/index?year=2016&month=1&weekIndex=0

rating_pages = []
for i in range(5):
    url = f"https://workey.codeit.kr/ratings/index?year=2016&month=1&weekIndex={i}"
    
    response = requests.get(url)
    rating_page = response.text
    rating_pages.append(rating_page)


print(i)
print(rating_pages[0])

