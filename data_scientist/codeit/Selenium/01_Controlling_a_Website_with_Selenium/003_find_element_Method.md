+ Selenium에는 CSS 선택자를 `find_element()` 함수로 가져올 때 사용하는 By.CSS_SELECTOR 말고도 웹 요소를 찾는 다양한 조건들이 있습니다.

#### 태그 이름으로 찾기

+ 태그 이름으로 요소를 찾습니다. 

+ 파라미터로 태그 이름을 그대로 써 주면 됩니다.

```python
driver.find_element(by=By.TAG_NAME, value='tag_name')
```

#### id로 찾기

+ id 값으로 요소를 찾습니다. 

+ value 파라미터로 id 값을 그대로 써 주면 됩니다. 

+ 예를 들어서 id 값이 id-name이라면, #id-name이 아닌 id-name을 그대로 넣어 주시면 됩니다.

```python
driver.find_element(by=By.ID, value='id-name')
```

#### class로 찾기
+ class 이름으로 요소를 찾습니다. 

+ 파라미터로 class 이름을 . 없이 그대로 써 주면 됩니다.

```python
driver.find_element(by=By.CLASS_NAME, value='class-name')
```

+ 간단하게 태그 이름이나, id 값, 또는 class 이름으로만 요소를 찾을 수 있다면 이런 함수들을 쓰는 게 더 편리할 수도 있겠죠?

#### 매칭되는 모든 요소 찾기

+ `find_element()` 메소드는 매칭되는 웹 요소 하나를 리턴해 줍니다. 

+ HTML 문서에서 가장 먼저 나타나는 요소인데요. 

+ 만약 매칭되는 모든 요소를 찾고 싶다면 어떻게 해야 할까요? 

+ 그럴 땐 find_element`s`()라는 메소드를 쓰면 됩니다.

```python
# CSS 선택자
driver.find_elements(by=By.CSS_SELECTOR, value='selector')

# 태그 이름
driver.find_elements(by=By.TAG_NAME, value='tag_name')

# class 이름
driver.find_elements(by=By.CLASS_NAME, value='class-name')
```

+ Beautiful Soup처럼 `find_element()` 메소드는 웹 요소 자체를 리턴하고 find_element`s`() 메소드는 웹 요소 리스트를 리턴합니다.