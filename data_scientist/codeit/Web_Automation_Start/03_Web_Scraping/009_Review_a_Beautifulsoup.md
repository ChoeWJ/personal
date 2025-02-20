# Beautiful Soup 라이브러리

+ Beautiful Soup은 HTML 코드에서 필요한 정보를 추출해 주는 라이브러리입니다. 

+ Beautiful Soup을 이용하면 HTML 문서에서 필요한 태그를 쉽게 찾을 수 있고, 태그 안에 있는 다양한 정보도 쉽게 가져올 수 있습니다.

[Beautiful Soup 공식 문서](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Beautiful Soup 임포트

```python
import requests
from bs4 import BeautifulSoup
```

+ 파이썬에서는 Beautiful Soup 라이브러리를 bs4라고 하는데요. bs는 Beautiful Soup을 줄인 것이고, 4는 라이브러리 버전을 뜻합니다. 4가 가장 최신 버전입니다.

+ bs4에서 BeautifulSoup이라는 걸 가져와 줍니다.

+ Beautiful Soup 라이브러리로는 웹에 요청을 보낼 수 없기 때문에 requests 라이브러리도 임포트해 줍니다.

# BeautifulSoup 만들기

```python
# URL에 요청 보내기
response = requests.get(URL) 

# 받아온 HTML 코드로 BeautifulSoup 만들기
soup = BeautifulSoup(response.text, 'html.parser')
```

+ 라이브러리를 임포트해 주었으면, 원하는 웹사이트에 요청을 보내고, 받아온 HTML 코드로 BeautifulSoup이라는 걸 만들어 줍니다. 

+ BeautifulSoup을 만들 때 쓰이는 html.parser는 HTML 코드를 정리해 줍니다. 

+ 일반적으로 parser는 문서를 읽어 들여서 프로그램이 쉽게 사용할 수 있는 형식으로 변환시켜 주는 툴입니다.

+ 이제 soup을 통해 필요한 태그를 쉽게 가져올 수 있습니다.

# 필요한 태그 가져오기

+ .select()와 .select_one() 메소드는 선택자를 통해 필요한 태그를 가져옵니다.

### .select()

+ .select()는 선택자에 매칭되는 모든 태그를 리스트 형식으로 리턴해 줍니다. 매칭되는 태그가 없거나, 하나뿐이어도 리스트를 리턴합니다.
```python
soup.select(selector)
# 리턴값: [tag1, tag2, ...]
```

### .select_one()

+ .select_one()은 선택자에 매칭되는 태그 중 HTML 문서에서 가장 먼저 나타나는 태그를 리턴해 줍니다. 

+ .select()와 달리 태그 자체를 리턴해 줍니다(매칭되는 태그가 없는 경우 None을 리턴합니다).

```python
soup.select_one(selector)
# 리턴값: tag or None
```

##### 웹사이트의 HTML 구조가 복잡해서 필요한 태그를 가져오는 것이 어려운 경우:

+ 태그 선택 범위를 넓게 잡고 슬라이싱 등으로 필요한 태그들만 가져오거나

+ 태그 선택 과정을 나눠서 바깥쪽 태그를 선택하고, 태그 안에서 또 태그를 찾습니다. 태그에도 .select()와 .select_one()을 사용할 수 있습니다.

# 태그에서 필요한 정보 가져오기

### 텍스트 가져오기

+ 태그의 텍스트를 가져오는 방법은 여러 가지가 있습니다.

```python
tag.get_text()
list(tag.strings)
list(tag.stripped_strings)
```

### .get_text()

+ .get_text()는 태그 안에 있는 모든 텍스트를 하나로 합쳐서 리턴해 줍니다. 

+ 사실 .get_text()안에는 파라미터를 넣을 수도 있는데요. 파라미터를 넣어 주면, 텍스트를 합칠 때 파라미터로 넣은 문자열을 텍스트 사이에 넣어 줍니다.

```python
...
    <tag>
      Hello <b>World<b>!
    </tag>
...
```

```python
# tag 안에 텍스트: 'Hello ', 'World', '!'

tag.get_text()
# 리턴값: 'Hello World!'

tag.get_text(' ')
# 리턴값: 'Hello  World !'

tag.get_text(',')
# 리턴값: 'Hello ,World,!'
```

### .strings

+ .strings는 태그 안에 있는 텍스트를 따로 리턴해 줍니다. 태그 안에 있는 텍스트 일부만 필요할 때 유용하겠죠? 

+ .strings를 쓸 때는 결괏값을 list()로 감싸 줘야 합니다.

```python
# tag 안에 텍스트: 'Hello ', 'World', '!'

list(tag.strings)
# 리턴값: ['Hello ', 'World', '!']
```

### .stripped_strings

+ .stripped_strings는 .strings와 똑같지만 각 텍스트 요소의 양옆의 공백을 제거해 줍니다. 아예 공백인 텍스트는 .stripped_strings에 포함되지 않습니다.

```python
# tag 안에 텍스트: 'Hello ', 'World', '!'

list(tag.stripped_strings)
# 리턴값: ['Hello', 'World', '!']
```

### 속성 가져오기

```python
tag['attr']
```

+ 태그의 속성은 tag[]를 사용해서 가져옵니다. []안에 속성 이름을 넣어 줍니다.

```python
tag.attrs
```

+ 태그의 모든 속성은 .attrs로 확인할 수 있습니다.

