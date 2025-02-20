# 파이썬 데코레이터

+ 파이썬 **데코레이터**에 대해 알아봅시다.

## 데코레이터란

+ **데코레이트**(decorate)는 영어로 ***꾸며주다***라는 뜻을 갖는데요. 

+ 이 단어가 어원인 파이썬 **데코레이터**(decorator)는 다른 함수의 기능을 확장시켜주는, 혹은 꾸며주는 특별한 함수입니다. 

+ 정의만으로는 바로 이해하기 힘들 수 있기 때문에 바로 예시를 통해서 무슨 말인지 볼게요.

## 데코레이터 정의

+ `add_introduction()`이란 함수를 정의했습니다.

```python
def add_introduction(original_function):
    def new_function():
        print("안녕하세요")
        original_function()
        print("잘 부탁드립니다\n")
    return new_function
```

+ 파라미터로는 어떤 함수 `original_function`을 받고요. 

+ 바디 부분에서는 새로운 함수 `new_function`을 정의해서 리턴해줍니다.

+ 함수를 함수 안에서 정의한다거나, 파라미터로 받고 리턴한다는 게 조금 낯설 수도 있는데요. 

+ 일단은 파이썬에서는 함수가 정수형, 문자열, 리스트 등 다른 자료형들과 똑같이 취급되기 때문에 가능하다고만 알고 계시면 충분합니다.

+ `add_introduction()` 함수 안에 정의된 `new_function()`을 살펴볼까요? 

+ `new_function()`은 파라미터를 받지 않습니다. 

+ 그리고 바디 부분에서는 "안녕하세요"라는 메세지를 출력하고  `original_function()`을 호출한 뒤, 다음에는 "잘 부탁드립니다"라는 메세지를 출력합니다.

+ 데코레이터는 어떤 함수의 기능을 확장시켜주는 특별한 함수라고 했는데요. 

+ `add_introduction()`은 함수 `original_function()`을 파리미터로 받아 앞 뒤로 메세지를 출력하는 기능이 추가된 새로운 함수를 리턴해줍니다. 데코레이터 정의에 부합하죠.

## 데코레이터 사용

+ `add_introduction()`를 사용해볼까요? 아래와 같이 새로운 함수를 정의했다고 할게요.

```python
def print_young():
    print("저는 강영훈입니다")
```

+ 이걸  `add_introduction()` 함수의 아규먼트로 넘겨준 후,

+ 리턴되는 새로운 함수를 `new_print_young()`이라는 변수에 저장할게요.

```python
new_print_young = add_introduction(print_young)
```

+ 그리고 이 함수를 호출하면

```python
new_print_young()
```

+ 아래 내용이 출력되는데요.

```markdown
안녕하세요
저는 강영훈입니다
잘 부탁드립니다
```

+ `print_young()` 함수의 기존 출력 내용 "저는 강영훈입니다" 앞뒤로 내용이 추가됐는데요. 
+ 함수의 기능이 기존 거에 더해져 확장된 걸 확인할 수 있습니다.

## 데코레이터 Syntactic Sugar

+ 데코레이터를 좀 더 쉽게 사용할 수 있는 문법 하나를 배워볼게요.

+ 아규먼트로 넘겨주는 함수의 정의 부분 바로 위에  @를 쓰고 사용할 데코레이터로 사용할 함수를 써주면 됩니다.

```python
@add_introduction
def print_young():
    print("저는 강영훈입니다")
```

+ 그럼 이제 `print_young()` 함수는 `add_introduction()`함수를 통해서 기능이 추가된 상태로 정의되는데요.
+ `print_young()`을 호출해보면 위에서 했던 거와 똑같이 함수 안에 정의한 기능뿐만 아니라, 데코레이터도 추가된 기능도 잘 실행되는 걸 확인할 수 있습니다.

```markdown
안녕하세요
저는 강영훈입니다
잘 부탁드립니다
```

+ `add_introduction()`으로 기능을 추가해야 되는 함수가 하나가 아니라 여러 개가 있으면 어떨까요? 
+ 그냥 전부 @를 사용하면 됩니다. 예를 들어 이렇게 세 개의 함수가 있다면

```python
def print_young():
    print("저는 강영훈입니다")

def print_yoonsoo():
    print("저는 이윤수입니다")

def print_dongwook():
    print("저는 손동욱입니다")
```

+ 그냥 호출하면

```python
print_young()
print_yoonsoo()
print_dongwook()
```

+ 이렇게 출력물이 나올텐데요.

```markdown
저는 강영훈입니다
저는 이윤수입니다
저는 손동욱입니다
```

+ 이 세 함수에 모두 데코레이터를 추가해준 후 호출하면

```python
@add_introduction
def print_young():
    print("저는 강영훈입니다")

@add_introduction
def print_yoonsoo():
    print("저는 이윤수입니다")

@add_introduction
def print_dongwook():
    print("저는 손동욱입니다")
```

+ `add_introduction()`의 기능을 여러 함수에 손쉽게 추가시킬 수 있습니다.

```markdown
안녕하세요
저는 강영훈입니다
잘 부탁드립니다

안녕하세요
저는 이윤수입니다
잘 부탁드립니다

안녕하세요
저는 손동욱입니다
잘 부탁드립니다
```

+ 여러 함수에 동일한 기능을 추가하고 싶을 때 데코레이터를 사용하면 중복되는 내용 없이 깔끔하게 코드를 쓸 수 있겠죠?

## 데코레이터 빌트인 예시

+ 지금까지 본 것과 같이 데코레이터를 직접 정의해서 사용하는 경우들도 많긴한데요. 

+ 파이썬이 빌트인으로 제공하는 것들도 많습니다. 

+ 개발자들은 이걸 가지고 객체 지향 프로그래밍에 활용한다거나 다양한 자료형이나 함수들의 기능을 손쉽게 확장시키죠.

+ 파이썬에서 제공하는 빌트인 데코레이터 한 가지만 예시로 보게요.

+ 바로 functools 모듈에 있는 cache 데코레이터입니다. 

+ cache는 함수의 특정 아규먼트에 대한 결과를 저장해놨다가 같은 아규먼트가 넘어왔을 때 함수를 다시 실행시키는 게 아니라 이미 저장한 결과를 가지고오는 기능을 더해주는 데코레이터입니다.

+ 예를 들어 아래와 같이 어떤 정수 n의 팩토리얼(1부터 n까지의 곱)을 계산해주는 함수 factorial이 있다고 할게요.

```python
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
```

+ **cache 데코레이터**를 입히면 이렇게 되는데요.

```python
from functools import cache

@cache
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1
```

+ 위와 같이 함수를 정의하고 아래와 같이 동일한 아규먼트 100을 사용해서 함수를 호출하면 작성자 컴퓨터 기준 실행 시간이 무려 100배나 차이납니다.

```python
factorial(100)
factorial(100)
```

+ 설명드린 것과 같이 factorial() 함수를 두 번째로 호출할 때 실제로 팩토리얼을 계산하는 게 아니라, 
+ 아규먼트가 100 일 때의 저장해놓은 결과를 그냥 가지고 오고 있기 때문이죠.

+ 한번 호출될 때 오랜 시간이 걸리면서 여러 번 호출되는 함수들은 cache 데코레이터를 활용하면 불필요한 연산 낭비를 줄일 수 있습니다.

+ 파이썬에는 cache 말고도 유용한 데코레이터들이 많습니다. 

+ 빌트인이 아니어도 웹 개발이나, 데이터 사이언스 분야에서도 데코레이터를 많이 사용합니다.

+ 데코레이터가 뭐고 어떻게 사용하는지 알고 있으면 훨씬 더 코드를 쉽고 효율적이게 쓸 수 있겠죠?