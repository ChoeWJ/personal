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

+ 위 두 모듈에서는 현재 상수 `PI`가 사용되고 있다.

+ 이처럼 패키지에 있는 여러 모듈이 필요로 하는 것들은 각 모듈에서 정의하기 보다는 

+ `__init__.py`를 활용해서 한번에 정의해주면 된다.

```python
# __init__.py

PI = 3.14
```

```python
# Example.py

from Shapes import PI

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(side):
    return side * side
```

```python
# Volume.py

from Shapes import PI

# 구의 부피를 구해 주는 함수
def sphere(radius):
    return (4/3) * PI * radius * radius  * radius

# 정육면체의 부피를 구해 주는 함수
def cube(length):
    return length * length * length
```
