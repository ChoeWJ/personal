```python
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
True
True
True
True
"""
```
+ 위와 같이 모듈에서도 작동이 잘 되는것을 알 수 있는데 한 가지 문제점이 발생한다.

+ 스크립트에서 파일을 실행시켜보면 모듈의 값이 그대로 같이 출력되면서 진행되는데

+ 이유는 import한 모듈 내의 함수를 모두 실행한 뒤에 스크립트 파일을 실행하기 때문이다.

+ 따라서 모듈은 가져오지만 모듈 내의 특정부분의 것들은 가져오지 않으려면....