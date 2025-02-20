# 스크립트 vs 모듈

+ `스크립트`는 **실제로 프로그램을 작동시키는 코드를 담은, 실행 용도의 파일**을 뜻합니다.

+ `모듈`은 프로그램에 **필요한 변수들이나 함수들을 정의해 놓은, 임포트 용도의 파일**을 뜻합니다.

+ 우리가 이전 영상에서 봤던 면적 계산기 프로그램은 두 파일로 구성돼 있습니다.

```python
# area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length
```

+ `area 파일`에서는 프로그램에 필요한 함수들을 정의하기만 하고 함수들을 사용하지는 않습니다.

```python
# run.py

import area

x = float(input('원의 지름을 입력해 주세요: '))
print('지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area.square(y)))
```

+ 실제로 함수들을 사용하는 코드는 `run`파일에 있습니다. 

+ 이 파일을 실행시키면 프로그램이 작동합니다.

+ 따라서 `area` 파일은 `모듈`이고 `run` 파일은 `스크립트`라고 할 수 있습니다.

+ 그런데 `스크립트`와 `모듈`은 우리가 그 안에 어떤 내용을 담을지 정한 것일 뿐 파일 자체에 특별한 차이가 있는 건 아니기 때문에 어떤 파이썬 파일이든 직접 실행할 수도 있고 다른 곳에서 불러올 수도 있습니다. 

+ 그러니까 어떤 파일은 **상황에 따라 `모듈`이 될 수도 있고 `스크립트`가 될 수도 있는 거죠.** 

+ 예를 들어 아래와 같은 코드를 `area.py`에 추가하면:

```python
# area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

# circle 함수 테스트
print(circle(2) == 12.56)
print(circle(5) == 78.5)

# square 함수 테스트
print(square(2) == 4)
print(square(5) == 25)
```

+ `area` 파일을 함수들을 테스트해 주는 `스크립트`로 사용할 수도 있습니다.

+ 하지만 여기서 문제가 생기는데 그건 `area` 모듈을 임포트해도 위 테스트 코드가 실행된다는 겁니다. 

+ `모듈`을 임포트하면 `모듈` 안에 있는 코드가 처음부터 끝까지 모두 실행되기 때문이죠. 

+ 이 문제를 해결하기 위해서는 `__name__`이라는 특수 변수를 사용해야 합니다.

# name 특수 변수

## name 이란?

+ `__name__`은 **`모듈`의 이름을 저장해 놓은 변수**입니다.

+ `__name__`의 값은 파이썬이 알아서 정해 주는데요.

+ 파일을 직접 실행하면 `__name__`은 `__main__`으로 설정됩니다

+ 파일을 임포트하면 `__name__`은 모듈 이름으로 설정됩니다.

+ 예를 들어 `area` 파일에서 `__name__`을 아래처럼 출력해 보면:

```python
# area.py

print(__name__)
```

+ `area` 파일을 직접 실행할 경우 `__main__`이라고 나오고:

```python
__main__

"""
area
"""
```

+ `area` 파일을 임포트할 경우 `area`라고 나오는 거죠:


# if __name__ == '__main__'

+ `__name__`을 사용하면 파일이 직접 실행되냐 아니면 임포트되냐에 따라서 코드의 흐름을 제어할 수 있습니다.

+ 파일이 직접 실행될 때만 실행하고 싶은 코드는 `if __name__ == '__main__'`이라는 조건문 안에 넣어주면 됩니다.

```python
# area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

if __name__ == '__main__':
     # circle 함수 테스트
    print(circle(2) == 12.56)
    print(circle(5) == 78.4)

    # square 함수 테스트
    print(square(2) == 4)
    print(square(5) == 25)
```

+ `area` 파일을 직접 실행시키면 파일의 `__name__`은 `__main__`이 되기 때문에 조건문 안에 있는 코드가 실행되지만 `area` 파일을 임포트하면 `__name__`은 `area`가 되기 때문에 조건문 안에 있는 코드가 실행되지 않습니다.