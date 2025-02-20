# .tagname 문법

+ 첫 번째는 .select_one('tagname'), 즉 태그 이름으로 태그를 찾는 코드를 더 간결하게 쓰는 방법입니다.

+ 태그 이름으로 태그를 찾는 방법은 워낙 많이 쓰이기 때문에 더 간결한 문법이 존재하는데요. 바로 `.tagname`입니다. 아래와 같이 쓰면 됩니다.

```python
soup.tagname # soup.select_one('tagname')과 동일
tag.tagname # tag.select_one('tagname')과 동일
```

+ 예를 들어, 아래 `<div>` 태그에서 `<h2>`,` <p>`, `<a>` 태그의 정보를 가져와야 한다고 합시다.

```python
...
    <div class="data">
      <h2>제목</h2>
      <p>내용</p>
      <a href="www.example.com">링크</a>
    </div>
...
```

+ `select`를 이용하면 아래와 같이 코드를 써야 하는데요.

```python
div_tag = soup.select_one('div.data')
title = div_tag.select_one('h2').get_text()
content = div_tag.select_one('p').get_text()
link = div_tag.select_one('a')['href']
```

+ `.tagname` 문법을 쓰면, 아래와 같이 코드가 바뀌는 거죠.

 ```python
div_tag = soup.select_one('div.data')
title = div_tag.h2.get_text()
content = div_tag.p.get_text()
link = div_tag.a['href']
```

+ 코드가 더 간단해졌죠?

# 메소드 체이닝

+ 두 번째는 **메소드 체이닝**(Method Chaining)입니다.

+ 체인(Chain)은 사슬을 뜻하죠? 메소드 체이닝은 메소드의 리턴값을 변수에 저장하지 않고, 리턴값에 바로 또 다른 메소드를 호출하는 것을 뜻합니다. 

+ 메소드를 사슬처럼 연결하기 때문에 메소드 체이닝이라고 부르는 거죠.

+ 예를 들어 select_one() 메소드는 태그를 리턴하는데요. select_one() 바로 뒤에 태그에 쓰는 메소드를 호출해 주면 됩니다.  select_one(), select(), get_text() 같은 것들이 있겠죠?

```python
# 1. selector1에 매칭되는 태그를 찾은 다음 그 안에서 selector2에 매칭되는 태그 선택
soup.select_one(selector1).select_one(selector2)

# 2. selector1에 매칭되는 태그를 찾은 다음 그 안에서 selector2에 매칭되는 모든 태그 선택
soup.select_one(selector1).select(selector2) 

# 3. selector1에 매칭되는 태그를 찾은 다음 그 안에서 텍스트 추출
soup.select_one(selector1).get_text()
```

+ 메소드 체이닝을 사용하면 코드가 더 간결해지지만, 코드의 가독성은 떨어질 수 있으니까 주의해 주세요. 특히 체인이 너무 길어지면 코드의 가독성이 떨어질 겁니다.

+ 참고로 이번 레슨 첫 부분에서 본 .tagname 문법도 체이닝을 할 수 있습니다. 태그를 계속 타고 들어가야 할 때 .tagname을 계속 붙여 써 주면 됩니다.

```python
...
    <div class="data">
      <div>
        <h2>제목</h2>
        <p>내용<b>키워드</b>내용</p>
        <a href="www.example.com">링크</a>
      </div>
    </div>
...
```

+ 예를 들어 위와 같은 HTML 구조에서 `<b>` 태그 안에 있는 키워드를 가져와야 한다면. 아래와 같은 코드를 쓸 수 있습니다.

```python
div_tag = soup.select_one('div.data')
keyword = div_tag.div.p.b.get_text()
print(keyword)
```

```
키워드
```