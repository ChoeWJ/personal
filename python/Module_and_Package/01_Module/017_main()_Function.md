+ 파이썬에서는 모든 파일을 실행할 수 있습니다. 

+ 파일을 실행하면 **파일에 있는 모든 코드가 처음부터 끝까지 실행**됩니다. 

+ 하지만 `Java`나 `C`, `C++` 같은 언어들은 그렇지 않습니다. 

+ `Java`나 `C`, `C++` 같은 언어들에서는 어떤 파일을 실행하기보다는 파일 안에 있는 `'main()'`이라는 함수를 실행합니다. 

+ `main 함수`는 말 그대로 `'주요' 함수`로서 프로그램을 작동시키는 코드를 담고 있습니다.

+ 예를 들어 `Java`의 'Hello World!' 프로그램은 아래와 같이 생겼습니다.

```java
HelloWorld.java

class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello World!"); 
    }
}
```

+ 프로그램이 더 복잡해지면 `main 함수` 안에서 다른 함수들을 호출하겠죠?

+ 파이썬에서도 이 프로그래밍 패턴을 사용할 수 있습니다. 

+ 파일에서 어떤 프로그램을 작동시키는 부분을 그냥 `main`이라는 함수 안에 넣어 주는 거죠. 

+ 예를 들어 우리의 `area` 파일과 `run` 파일에 `main 함수`를 추가해 주면 아래와 같이 바뀝니다.

```python
# area.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length

# 함수들을 테스팅 하는 메인 함수
def main():
    # circle 함수 테스트
    print(circle(2) == 12.56)
    print(circle(5) == 78.4)

    # square 함수 테스트
    print(square(2) == 4)
    print(square(5) == 25)

if __name__ == '__main__':
    main()
```
```python
# run.py

import area

# 면적 계산기 프로그램
def main():
    x = float(input('원의 지름을 입력해 주세요: '))
    print('지름이 {}인 원의 면적은 {}입니다.\n'.format(x, area.circle(x)))

    y = float(input('정사각형의 변의 길이를 입력해 주세요: '))
    print('변의 길이가 {}인 정사각형의 면적은 {}입니다.'.format(y, area.square(y)))

if __name__ == '__main__':
    main()
```

+ `if __name__ == '__main__'` 안에 있는 코드는 파일이 직접 실행될 때만 실행되니까 그 안에서 `main 함수`를 호출해 주면 됩니다.

+ 이렇게 `main 함수`를 사용하면 파일에서 프로그램을 작동시키는 코드가 어디 있는지 쉽게 알 수 있기 때문에 코드의 가독성이 올라갑니다. 

+ 코드의 흐름과 의도를 더 쉽게 이해할 수 있는 거죠. 

+ 따라서 파이썬에서는 `main 함수`가 요구되지 않더라도 `if __name__ == '__main__'`과 `main()`을 사용하는 것을 추천드립니다.