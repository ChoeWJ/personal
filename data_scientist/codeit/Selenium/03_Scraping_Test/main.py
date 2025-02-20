from time import sleep
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.by import By

# 엑셀 파일을 생성하고, 데이터를 작성할 새로운 시트를 생성합니다.
wb = Workbook(write_only=True)
ws = wb.create_sheet()
# 엑셀 파일의 첫 번째 행에 데이터의 제목(열 이름)을 추가합니다.
ws.append(['이미지 주소', '제목', '해시태그', '좋아요 수', '댓글 수'])

# Selenium 웹 드라이버를 설정하고, 암묵적 대기 시간을 3초로 설정합니다.
driver = webdriver.Chrome()
driver.implicitly_wait(3)

# 코스타그램 메인 페이지를 엽니다.
driver.get('https://workey.codeit.kr/costagram/index')
# 페이지 로딩을 위해 1초 동안 대기합니다.
sleep(1)

# 로그인 버튼을 클릭하여 로그인 화면으로 이동합니다.
driver.find_element(by=By.CSS_SELECTOR, value='.top-nav__login-link').click()
# 로그인 화면이 로드될 시간을 위해 1초 동안 대기합니다.
sleep(1)

# 로그인 화면에서 아이디 입력란에 아이디를 입력합니다.
driver.find_element(by=By.CSS_SELECTOR, value='.login-container__login-input').send_keys('codeit')
# 로그인 화면에서 비밀번호 입력란에 비밀번호를 입력합니다.
driver.find_element(by=By.CSS_SELECTOR, value='.login-container__password-input').send_keys('datascience')

# 로그인 버튼을 클릭하여 로그인합니다.
driver.find_element(by=By.CSS_SELECTOR, value='.login-container__login-button').click()
# 페이지가 로드될 시간을 위해 1초 동안 대기합니다.
sleep(1)

# 페이지 끝까지 스크롤하기 위해 현재 문서의 초기 scrollHeight를 가져옵니다.
last_height = driver.execute_script("return document.body.scrollHeight")

# 페이지 끝까지 스크롤을 반복적으로 수행합니다.
while True:
    # 현재 페이지의 맨 아래로 스크롤합니다.
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # 새로운 콘텐츠가 로드될 시간을 위해 0.5초 대기합니다.
    sleep(0.5)

    # 스크롤 이후 문서의 새로운 scrollHeight를 가져옵니다.
    new_height = driver.execute_script("return document.body.scrollHeight")
    # 새로운 scrollHeight와 이전 scrollHeight가 같으면 스크롤 종료합니다.
    if new_height == last_height:
        break
    # 이전 scrollHeight 값을 업데이트합니다.
    last_height = new_height

# 페이지에 로드된 모든 포스팅 썸네일 요소를 찾습니다.
posts = driver.find_elements(by=By.CSS_SELECTOR, value='.post-list__post')

# 각 포스팅 썸네일을 클릭하여 세부 정보를 가져옵니다.
for post in posts:
    # 포스팅 썸네일을 클릭하여 상세 페이지를 엽니다.
    post.click()
    # 상세 페이지가 열릴 시간을 위해 0.5초 대기합니다.
    sleep(0.5)

    # 상세 페이지에서 이미지의 style 속성을 가져옵니다.
    style_attr = driver.find_element(by=By.CSS_SELECTOR, value='.post-container__image').get_attribute('style')
    # style 속성에서 이미지 경로를 추출합니다.
    image_path = style_attr.split('"')[1]
    # 전체 이미지 URL을 생성합니다.
    image_url = 'https://workey.codeit.kr' + image_path

    # 상세 페이지에서 제목(본문 텍스트)을 가져옵니다.
    content = driver.find_element(by=By.CSS_SELECTOR, value='.content__text').text.strip()
    # 상세 페이지에서 해시태그를 가져옵니다.
    hashtags = driver.find_element(by=By.CSS_SELECTOR, value='.content__tag-cover').text.strip()
    # 상세 페이지에서 좋아요 수를 가져옵니다.
    like_count = driver.find_element(by=By.CSS_SELECTOR, value='.content__like-count').text.strip()
    # 상세 페이지에서 댓글 수를 가져옵니다.
    comment_count = driver.find_element(by=By.CSS_SELECTOR, value='.content__comment-count').text.strip()

    # 추출한 데이터를 엑셀 파일에 추가합니다.
    ws.append([image_url, content, hashtags, like_count, comment_count])

    # 상세 페이지의 닫기 버튼을 클릭하여 창을 닫습니다.
    driver.find_element(by=By.CSS_SELECTOR, value='.close-btn').click()
    # 창이 닫히는 시간을 위해 0.5초 대기합니다.
    sleep(0.5)

# 웹 드라이버를 종료하여 브라우저를 닫습니다.
driver.quit()

# 작성된 데이터를 엑셀 파일로 저장합니다.
wb.save('코스타그램.xlsx')