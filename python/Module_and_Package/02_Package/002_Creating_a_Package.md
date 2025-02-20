```python
# Example.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(side):
    return side * side
```
```python
# Volume.py

PI = 3.14

# 구의 부피를 구해 주는 함수
def sphere(radius):
    return (4/3) * PI * radius * radius  * radius

# 정육면체의 부피를 구해 주는 함수
def cube(length):
    return length * length * length
```
+ 위 두 모듈을 합쳐서 `Package`를 만들어 보자.

    1. 기존의 `Practice` 디렉토리에 새로운 `Shapes`라는 디렉토리를 추가한다

    2. `Shapes` 디렉토리에 위 두 모듈을 넣어준다

    3. `Shapes` 디렉토리 안에 `__init__.py` 라는 새로운 파일을 만들어 준다.
