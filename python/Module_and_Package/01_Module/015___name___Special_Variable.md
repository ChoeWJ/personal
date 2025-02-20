+ 실행 파일에서 모듈에 있는 코드가 출력되는 문제를 해결하기 위해서는

+ `__name__`이라는 특수 변수를 활용하면 된다.

+ `__name__`은 **모듈의 이름을 저장해 해둔 변수**

+ `__name__`의 값은 파이썬에서 알아서 정해주는데, 만약 파이썬 파일을 직접 실행하면

+ 그 파일을 `__name__`은 `__main__`으로 설정이 되고,

+ 파일을 다른곳에서 `import` 해서 사용하면 `__name__`은 원래 모듈 이름으로 설정된다.

+ 즉, `Test.py`의 파일을 직접 실행하면, 

+ `Test.py` 파일의 `__name__`는 `__main__`으로 설정되고

+ 다른 곳에서 불러와서 사용하면 `__name__`은 `Test.py`가 된다

```python
# Example.py

print(f"Example 모듈 이름: {__name__}")

PI = 3.14

def circle(radius):
    return PI * radius * radius

def square(side):
    return side * side

print(circle(2) == 12.56)
print(circle(5) == 78.5)

print(square(4) == 16)
print(square(7) == 49)

"""
Example 모듈 이름: __main__
True
True
True
True
"""
```

```python
# Test.py

print(f"Test.py의 모듈 이름: {__name__}")

import Example


print("Example 파일 실행")

"""
Test.py의 모듈 이름: __main__
Example 모듈 이름: Example
True
True
True
True
Example 파일 실행
"""
```

+ 코드의 출력 순서도 확인할 수 있다.

+ 만약 `Example.py` 파일이 직접 실행될 때만 코드를 실행시키고 싶다면,

```python
# Example.py

if __name__ == '__main__':
    print(circle(2) == 12.56)
    print(circle(5) == 78.5)

    print(square(4) == 16)
    print(square(7) == 49)
```
+ 위와 같이 `if`문을 넣어주면 된다.

+ `Test.py` 파일을 다시 실행시켜서 확인해 보면 위와는 다른 출력 결과를 확인할 수 있다.

```python
"""
Test.py의 모듈 이름: __main__
Example 모듈 이름: Example
Example 파일 실행
"""
```