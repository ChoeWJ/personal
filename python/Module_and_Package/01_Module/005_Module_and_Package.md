+ 우리가 만든 area 모듈에는 아래와 같이 변수와 함수들이 있습니다.

```python
# area.py

PI = 3.14
```

# 원의 면적을 구해 주는 함수

```python
def circle(radius):
    return PI * radius * radius
```

# 정사각형의 면적을 구해 주는 함수

```python
def square(length):
    return length * length
```

+ 그런데 모듈에는 '클래스'라는 것이 있는 경우도 많습니다. 

+ 클래스는 어떤 프로그래밍 객체를 생성하기 위한 설계도인데요. 

+ 아직 객체 지향 프로그래밍을 안 배우신 분들은 

+ 그냥 **'모듈 안에는 꼭 변수랑 함수만 있는 게 아니라 클래스가 있을 수도 있다'** 이 정도만 기억하시고 넘어가면 될 것 같습니다.

+ 예를 들어 어떤 프로그램에서는 원과 정사각형의 면적만 계산해야 하는 게 아니라 원과 정사각형을 직접 만들어서 사용해야 한다고 합시다. 

+ 그러면 새로운 파일을 만들고 파일에서 원과 정사각형 클래스들을 정의해 주면 됩니다.

```python
# shapes2d.py

# 원 클래스
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

# 정사각형 클래스
class Square:
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
```

+ 그리고 다른 파일에서 이 클래스들을 사용하려면 이전과 같이 `import 키워드`를 사용하면 됩니다.

```python
# run.py

# import <module>
import shapes2d

circle = shapes2d.Circle(2)
print(circle.area())

# from <module> import <member(s)>
from shapes2d import Square

square = Square(3)
print(square.area())
```

+ 물론 as 키워드를 사용해서 임포트하는 것의 이름을 바꿔줄 수도 있습니다.

```python
# run.py

from shapes2d import Square as Sq

square = Sq(3)
print(square.area())
```