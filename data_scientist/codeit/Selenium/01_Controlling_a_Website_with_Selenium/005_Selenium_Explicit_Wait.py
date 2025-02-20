from time import sleep  # sleep 함수를 사용해 프로그램을 일정 시간 동안 정지시킬 수 있음
from selenium import webdriver  # Selenium의 webdriver를 불러와 브라우저를 제어함
from selenium.webdriver.common.by import By  # 요소를 찾기 위한 다양한 속성(By)을 사용함
from selenium.webdriver.support import expected_conditions as EC  # 조건이 만족될 때까지 기다리는 기능을 지원함
from selenium.webdriver.support.ui import WebDriverWait  # 요소가 조건을 만족할 때까지 대기하는 기능을 제공함

# Chrome 웹 드라이버를 사용해 브라우저 실행
driver = webdriver.Chrome()

# 최대 3초 동안 특정 조건이 만족될 때까지 기다리는 객체 생성
wait = WebDriverWait(driver, 3)

# 특정 URL(웹페이지)로 이동
driver.get("https://workey.codeit.kr/costagram")

# ".top-nav__login-link" 요소가 클릭 가능할 때까지 기다린 후 클릭 (로그인 페이지로 이동)
login_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".top-nav__login-link")))
login_link.click()

# ".login-container__login-input" 요소가 화면에 표시될 때까지 기다린 후, ID 입력 필드에 접근
id_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-container__login-input")))
id_box.send_keys("codeit")  # ID 입력 필드에 "codeit" 입력

# ".login-container__password-input" 요소가 화면에 표시될 때까지 기다린 후, 비밀번호 입력 필드에 접근
pw_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-container__password-input")))
pw_box.send_keys("datascience")  # 비밀번호 입력 필드에 "datascience" 입력

# ".login-container__login-button" 요소가 클릭 가능할 때까지 기다린 후 클릭 (로그인 시도)
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".login-container__login-button")))
login_button.click()

# 프로그램 실행을 5초 동안 일시 정지 (로그인 결과 확인용)
sleep(5)

# 브라우저 종료
driver.quit()