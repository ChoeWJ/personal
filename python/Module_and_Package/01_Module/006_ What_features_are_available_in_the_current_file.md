```python
# Example.py

PI = 3.14

def circle(radius):
    return PI * radius * radius

def square(side):
    return side  * side
```

```python
# Test.py

import Example

print(dir(Example))

"""
[
    'PI', 
    '__builtins__', 
    '__cached__', 
    '__doc__', 
    '__file__', 
    '__loader__', 
    '__name__', 
    '__package__', 
    '__spec__', 
    'circle', 
    'square'
]
"""
```
+ `dir 함수`는 어떤 파일 안에서 정의도니 모든 이름들을 알려주는 함수이다

+ `dir 함수`를 사용해서 `Example 모듈`을 출력하면

+ `Example 모듈`에서 정의한 `circle`, `PI`, `square`가 나온다. 

+ 이외에 이름 양옆에 **_(언더스코어)가 두 개씩 있는 것**을 볼 수 있다.

+ 읽을 때는 **던더** 라고 읽고 이것은 **더블언더스코어**의 줄임말이고 이것들은 파이썬의 특수 변수들이다.

+ 특수변수들은 파이썬에서 내부적으로 관리하는 변수들이다.

+ `dir 함수`의 파라미터에 아무것도 넣지 않는다면 어떻게 될까?

```python
import Example

print(dir())

"""
['Example', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 'help', 'howdoi', 'input']
"""
```

+ 실행을 해보면 위와 같이 다양한 특수 변수들이 나온다.

+ 모듈을 임포트 하면 이 파일에서는 모듈의 이름만 정의되고

+ 모듈 안에 있는 함수나 변수에 이름들은 정의되지 않는다.

+ `dir 함수`를 이용하면 프로그램에서 관리하는 이름들을 조금 더 쉽게 관리할 수 있다.