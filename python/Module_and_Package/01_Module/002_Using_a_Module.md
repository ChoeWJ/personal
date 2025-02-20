## 여러 도형의 면적을 구하는 모듈

```python
# Python/test.py


PI = 3.14 # 원주율


def circle(radius):
    """원의 면적을 구하는 함수"""
    return PI * radius *radius

def square(length):
    """정사각형의 면적을 구하는 함수"""
    return length * length
```

```python
# Python/run.py


import test # test.py 불러오기

print(test.circle(2))   # test.py에서 정의한 원의 면적 구하기 함수 실행

print(test.square(2))   # test.py에서 정의한 정사각형의 면적 구하기 함수 실행

print(test.PI)  # test.py에서 정의한 상수 파이(PI)의 면적 구하기 함수 실행

"""
출력 결과

12.56
4
3.14
"""
```