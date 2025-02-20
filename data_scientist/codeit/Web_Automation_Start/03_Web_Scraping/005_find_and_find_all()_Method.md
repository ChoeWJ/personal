## Beautiful Soup에는 필요한 태그를 선택하는 방법이 크게 두 가지 있습니다:

1. `.select_one()`, `.select()` 메소드 활용

2. `.find()`, `.find_all()` 메소드 활용

+ 1번, 2번 다 기능이 비슷하기 때문에 둘 중 하나만 아셔도 무방한데요, 2번 방법도 많이 쓰이기 때문에 이번 레슨에서 설명드리겠습니다.

### **find()와 find_all()**

+ find()는 select_one()과 비슷하고, find_all()은 select()와 비슷합니다.

+ find()는 매칭되는 태그를 (최대) 하나만 가져오는 데 쓰이고 find_all()은 매칭되는 태그를 모두 가져오는 데 쓰이는 거죠. 

+ 리턴값의 형식도 똑같습니다. find()는 태그 자체나 None을 리턴하고 find_all()은 리스트를 리턴합니다.
 
+ 하지만 find(), find_all()은 **CSS 선택자를 쓰지 않고 여러 파라미터를 활용**합니다. 

+ 지금부터 find(), find_all()의 문법을 설명드릴 텐데, 둘 다 문법이 똑같기 때문에 find_all() 위주로 예시를 들게요.

### 태그 이름 사용

+ find(), find_all()도 soup에도 쓸 수 있고, 태그에도 쓸 수 있습니다.

```python
soup.find_all('tagname')
# 예: soup.find_all('p')

soup.find_all(['tagname1', 'tagname2'])
# 예: soup.find_all(['p', 'a'])
```

+ 태그 이름으로 태그를 선택하려면 태그 이름을 파라미터로 넣어 주거나, 여러 태그 이름을 리스트로 넣어 줍니다.

+ 첫 번째 예시는 HTML 문서에서 모든 `<p>` 태그를 찾는 것이고, 두 번째 예시는 HTML 문서에서 모든 `<p>` 태그와 `<a>` 태그를 찾는 겁니다.

+ 참고로 모든 태그를 선택할 수도 있는데 이건 태그 안에 있는 모든 태그를 가져올 때 유용하겠죠?

```python
tag.find_all(True)
```

+ 모든 태그를 가져오려면 find_all() 안에 True를 넣어 줍니다.

### 속성 사용

```python
soup.find_all('tagname', attr1='val1', attr2='val2', ...)
# 예: soup.find_all('p', id="some-id", class_="some-class")
```

+ 태그를 찾는 데 태그의 속성을 이용해서 필터를 하고 싶다면 속성 이름과 속성 값을 쭉 써 주면 됩니다.

+ id와 class도 일반 속성처럼 써 주면 되는데 *(CSS 선택자는 id와 class 속성을 위한 특수 문법 #과 .이 있었던 것 기억하시죠?)* 유일하게 속성 중 class는 class_로 써 줘야 합니다. 

+ 파이썬에서 class는 클래스를 만드는 데 사용되는 이미 예약된 단어이기 때문이죠.

+ 위 예시는 id가 some-id이고 class가 some-class인 `<p>` 태그를 모두 찾는다는 뜻입니다.

+ 참고로 속성만으로 필터를 할 수도 있습니다. 그냥 태그 이름을 안 써 주면 됩니다.

```python
soup.find_all(attr1='val1', attr2='val2', ...)
# 예: soup.find_all(id="some-id", class_="some-class")
```

+ 위 예시는 id가 some-id이고 class가 some-class인 모든 태그를 찾는다는 뜻입니다.

+ 마지막으로 find(), find_all()은 특정 속성이 있는지 없는지를 조건으로 사용할 수 있습니다. 속성 값 대신 True나 False를 써 주면 됩니다.

```python
# 예: soup.find_all('p', id=True, class_=False)
```

+ 위 예시는 id 속성은 있지만 class 속성은 없는 `<p>` 태그를 모두 찾는다는 뜻입니다.

### 중첩 태그

+ find(), find_all()은 중첩에 대한 문법이 없기 때문에, 태그 안에 중첩된 태그를 찾으려면 태그에 find(), find_all()을 사용해야 합니다.

```python
...
    <div class="some-class">
      <p>Paragraph 1</p>
      <p>Paragraph 2</p>
      <p>Paragraph 3</p>
    </div>
...
```

```python
# select - 선택자로 중첩된 <p> 태그 선택
soup.select('div.some-class p')

# find_all - 먼저 <div> 태그를 가져온 후 <div> 태그에 find_all()
div_tag = soup.find('div', class_='some-class')
div_tag.find_all('p')
```

+ 앞서 말씀드렸듯이 두 방식의 기능은 거의 똑같기 때문에 더 편하신 방식을 사용하시면 됩니다. 

+ 하지만 다음 챕터에서는 Selenium이라는 도구에 대해 배워 볼 건데, Selenium을 사용할 때는 CSS 선택자를 계속 쓸 겁니다. 이 점 유의해 주세요.

