# Selenium 라이브러리

+ Selenium은 **웹 브라우저를 자동화하는 도구**입니다. 

+ Selenium을 활용하면 클릭이나 스크롤, 키보드 입력 같은 사용자의 동작을 제어할 수 있습니다. 

+ 코드로 작성된 내가 원하는 동작들이 브라우저에서 자동으로 실행되는 거죠. 

+ Selenium을 활용하면 로그인, 검색, 버튼 클릭 같은 작업을 자동화할 수 있기 때문에, 데이터 수집 등 웹을 다방면으로 응용하는 데 쓸 수 있습니다.

# Selenium 임포트

+ selenium 라이브러리에서 webdriver를 임포트해 줍니다.

```python
from selenium import webdriver
```

# 웹 드라이버 생성

+ 웹 드라이버는 웹 브라우저를 운전(drive)하는 도구입니다. 

+ 웹 드라이버가 사용자 동작을 실행해 줍니다. 먼저 웹 드라이버를 생성해 줍니다. 

+ 크롬 브라우저를 사용하니까, 크롬 드라이버를 만들어 줍니다.

```python
driver = webdriver.Chrome()
```

+ 그리고 get() 메소드를 활용하면 원하는 웹사이트에 접속할 수 있습니다.

```python
driver.get('https://www.example.com')
```

# 웹 요소 찾기

+ 먼저 제어하려는 웹 요소를 찾아야 합니다. 

+ 웹 요소를 찾기 위해선 get_element() 메소드를 쓸 수 있습니다. 

+ 이때 By 값을 써서 CSS 선택자로 요소를 찾을 수 있어요.

```python
from selenium.webdriver.common.by import By

...

driver.get_element(by=By.CSS_SELECTOR, value='selector')
```

+ 선택자 selector에 매칭되는 웹 요소가 선택됩니다.

# 웹 요소 제어하기

+ 웹 요소에 가장 많이 쓰이는 동작은 클릭과 키보드 입력입니다. 

+ click()과 send_keys() 메소드를 활용하면 됩니다.

```python
driver.get_element(by=By.CSS_SELECTOR, value='selector').click()
driver.get_element(by=By.CSS_SELECTOR, value='selector').send_keys('input')
```

+ 필요한 웹 요소를 찾고, 그걸 클릭하거나 키보드 인풋을 전달해 줍니다.

---

# Wait 설정하기

+ 웹은 로딩되는 데 시간이 걸립니다. 

+ 웹 요소가 로딩되지 않았는데 그걸 찾으려고 하거나, 클릭하려고 하면 오류가 납니다. 

+ Selenium을 사용할 때는 웹 요소의 로딩을 기다려 주는 것이 중요합니다. 

+ 두 가지 wait 방식을 영상으로 알아봤습니다.

# implicit wait
+ 웹 드라이버에 implicit wait을 설정해 주면 찾으려고 하는 웹 요소가 없을 때, 최대 설정해 준 기간만큼 기다려 줍니다.

```python
driver = webdriver.Chrome()
driver.implicitly_wait(3)
```

+ 드라이버를 생성하고, 한 번만 설정해 주면 됩니다. 

+ 위 코드는 최대 3초를 기다려 준다는 뜻입니다. 

+ 3초가 지나도 웹 요소를 찾지 못하면 오류가 납니다. 

+ 하지만 implicitly_wait은 웹 요소가 '존재'하는지만을 확인합니다. 

+ 웹 요소는 존재하지만 아직 클릭은 못하는 상태일 수도 있습니다. 

+ 따라서 추가적인 wait 방식이 필요합니다.

### sleep()

+ time 모듈의 sleep()은 정해진 기간만큼 동작을 멈춥니다. 

+ 항상 정해진 기간만큼 기다려 주는 거죠. 

+ 먼저 time 모듈에서 sleep()을 임포트해 주고, 필요한 곳에 추가해 줍니다.

```python
from time import sleep

...

sleep(1)
```

+ 위 코드는 1초 동안 기다린다는 뜻이겠죠?

+ sleep()은 보통 웹사이트 **코드가 로딩되거나 바뀌고 난 직후에 추가**해 주는 것이 좋습니다. 

+ 예를 들어 웹사이트에 처음 접속하거나, 어떤 버튼을 클릭해서 새로운 창이 뜬다면(새로운 창에 대한 HTML 코드가 어딘가 로딩되겠죠?), 직후에 sleep()을 걸어 주는 거죠.

+ 참고로 이번 강의 영상에서는 동작을 확인하기 위해서 모든 동작이 끝나고 driver.quit()을 실행하기 전에 sleep()을 종종 추가했어요. 

+ 하지만 굳이 확인할 필요가 없는 완성된 코드라면 기다리지 않고 드라이버를 바로 종료하면 됩니다.