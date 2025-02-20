# 1. "추상" 클래스와 "추상"화?

+ 추상화는 변수, 함수, 클래스 등을 사용해 사용자가 **꼭 알아야만 하는 부분만 겉으로 드러내고, 그렇지 않은 내용은 숨기는 것**
+ 그런 의미에서 **추상 클래스를 사용하는 것도 추상화의 일부**라고 할 수 있는데요. 

---
+ `Paint` 클래스를 만드는 개발자는 프로그램에서 도형 클래스가 `Shape` 클래스를 상속받기만 하면 무조건 `draw()` 메소드를 구현하고 있다는 걸 알고 있습니다. 
+ 따라서 정확히 어떤 도형 클래스들이 있을 거고, 이 클래스들이 각각 어떤 방식으로 시각화를 구현했는지에 대해서 생각하지 않고 프로그램을 만들 수 있습니다.

+ 도형 클래스를 만드는 개발자는 `Paint` 클래스에서 본인이 만든 클래스가 어떻게 사용되는지, 
+ 더 나아가 아예 클래스 자체가 어떤 방식으로 구현돼 있는지 알 필요가 없습니다. 
+ 그냥 `Shape` 클래스에 명시된 조건, `draw()` 메소드를 통해서 표현하는 도형을 시각화하기만 하면 되는 거죠.

+ `Shape` 클래스를 통해 일반 도형 클래스는 `draw()` 메소드를 구현해야 되는 걸 겉으로 드러내고, 
+ `Paint` 클래스 개발자에게는 일반 도형 클래스들의 구현을 숨기고, 
+ 일반 도형 클래스들에게는 `Paint` 클래스 구현을 숨겨서 쉽고 안전하게 협업할 수 있게 됩니다.

# 2. 자식 클래스에 인스턴스 변수 갖게 하기

+ 추상 클래스를 사용하면 자식 클래스가 추상 클래스의 추상 메소드를 오버라이딩하도록 
+ 즉, 해당 메소드를 갖도록 강제할 수 있습니다. 
+ 하지만 추상 클래스로 자식 클래스가 특정 변수를 갖도록 유도할 수 있는 방법이 있습니다.

+ 그림판에서 사용할 모든 도형 클래스는 좌표를 나타내는 인스턴스 변수 `x`와 `y`를 반드시 가져야 한다고 가정합시다. 
+ 어떻게 하면 추상 클래스를 사용해 각 자식 클래스가 이 변수를 갖도록 유도할 수 있을까요?

```python
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def draw(self):
        """콘솔에 도형을 그린다"""
        pass

    @property
    @abstractmethod
    def x(self):
        """도형의 x 좌표 getter 메소드"""
        pass

    @property
    @abstractmethod
    def y(self):
        """도형의 y 좌표 getter 메소드"""
        pass

```

+ `Shape` 클래스는 지금 `x` 메소드와 `y` 메소드를 getter 메소드이자 추상 메소드로 갖고 있습니다.

+ 이렇게 `@property`와 `@abstractmethod` 데코레이터를 메소드 이름 위에 연달아 적어주면 이 함수는 **getter 메소드이자 추상 메소드**가 됩니다. 
+ 즉, 어떤 변수에 대한 getter 메소드를 뜻하지만 아직 내용이 비어있어 어떤 변수를 리턴하는지는 결정되지 않은 것이죠. 
+ 이때 `Shape` 클래스를 상속받는 자식 클래스에서 어떤 변수를 리턴하는지 
+ **즉, 이 getter 메소드가 어떤 변수에 대한 것인지를 나타내도록 오버라이딩해야 하는 것입니다.

+ `Shape` 클래스를 상속받는 정삼각형 클래스인 `EquilateralTriangle` 클래스를 정의했습니다.

```python
class EquilateralTriangle(Shape):
    """장삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    def draw(self):
        """도형을 콘솔에 그린다"""
        result = '\n'
        for i in range(1, self.side+1):
            result += ' ' * (self.side - i) + '* ' * i + '\n'
        print(result)

    def __str__(self):
        """도형 정보를 문자열로 리턴한다"""
        return f'변이 {self.side}인 정삼각형'

equilateral_triangle = EquilateralTriangle(4)

```

+ getter 메소드들을 오버라이드하지 않으니 다음과 같은 에러가 뜨네요.

```python
TypeError: Can't instantiate abstract class EquilateralTriangle with abstract methods x, y
```

+ 그렇다면 각 getter 함수는 어떻게 오버라이딩하면 될까요? 
+ 보통 인스턴스 변수의 이름은 예를 들어 `_apple`처럼 캡슐화를 적용한 것으로 나타내고 
+ getter 함수의 이름은 `apple`처럼 변수 이름 앞에서 밑줄을 뺀 이름으로 한다고 배웠습니다. 
+ 이 경우에도 `x`는 인스턴스 변수 `_x`의 getter 함수로, `y`는 인스턴스 변수 `_y`의 getter 함수로 해주면 좋을 것 같네요.

```python
    @property
    def x(self):
        """_x getter 메소드"""
        return self._x

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

```

+ 그럼 이때까지 설명한 조건에 부합하는 `EquilateralTriangle` 클래스를 완성한 결과를 봅시다.

```python
class EquilateralTriangle(Shape):
    """장삼각형 클래스"""
    def __init__(self, side):
        self.side = side

    def draw(self):
        """도형을 콘솔에 그린다"""
        result = '\n'
        for i in range(1, self.side+1):
            result += ' ' * (self.side - i) + '* ' * i + '\n'
        print(result)

    @property
    def x(self):
        """_x getter 메소드"""
        return self._x

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

    @property
    def y(self):
        """_y getter 메소드"""
        return self._y

    @y.setter
    def y(self, value):
        """_y setter 메소드"""
        self._y = value

    def __str__(self):
        """도형 정보를 문자열로 리턴한다"""
        return f'변이 {self.side}인 정삼각형'

equilateral_triangle = EquilateralTriangle(4)

```

+ 물론 `Shape` 클래스에서 자식 클래스에 getter 메소드를 오버라이드하도록 강제한다고 해도 
+ 자식 클래스에서 이 메소드를 엉뚱한 내용으로 오버라이딩할 수도 있습니다. 
+ 하지만 파이썬의 문화를 잘 따르는 개발자라면 자식 클래스를 만들더라도 getter/setter 메소드를 적절하게 오버라이드할 것입니다. 
+ 이처럼 부모 클래스에서 추상 메소드인 getter 메소드를 만드는 것으로 자식 클래스에서 관련 인스턴스 변수를 갖도록 유도할 수 있는 것입니다!

# 3. 추상 클래스와 일반 메소드

+ 추상 클래스에 꼭 추상 메소드만 있어야 하는 것은 아닙니다. 
+ `@abstractmethod` 데코레이터가 없는 일반적인 메소드가 있어도 상관없습니다. 
+ 이 메소드들 또한 자식 클래스가 물려받아 그대로 사용하거나 오버라이딩하여 사용할 수 있습니다.

```python
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def draw(self):
        """도형을 콘솔에 그린다"""
        pass

    def draw_line(self, shape):
        """콘솔에 줄을 출력한다"""
        print('-----------------------------------')

```

+ 추상 클래스 `Shape` 에 일반 메소드 `draw_line()`을 추가했습니다.

```python
class Circle(Shape):
    """원 클래스"""
    def __init__(self, diameter):
        self.diameter = diameter

    def draw(self):
        """도형을 콘솔에 그린다"""
        radius = self.diameter / 2 - .5
        r = (radius + .25)**2 + 1
        result = '\n'
        for i in range(self.diameter):
            y = (i - radius)**2
            for j in range(self.diameter):
                x = (j - radius)**2
                if x + y <= r:
                    result += '* '
                else:
                    result += '  '
            result += '\n'
        print(result)

circle = Circle(6)
circle.draw()
circle.draw_line()

```

+ `Shape`를 상속받는 `Circle` 클래스의 인스턴스를 만들고, 
+ 상속받은 일반 메소드 `draw_line()`을 호출해 보면, 잘 출력되는 걸 확인할 수 있습니다.

```python
    * * *     
  * * * * *   
* * * * * * * 
* * * * * * * 
* * * * * * * 
  * * * * *   
    * * *     

-----------------------------------

```

+ 추상 클래스에는 꼭 추상 메소드뿐만 아니라 일반 메소드도 정의할 수 있고 
+ 이것도 똑같이 자식 클래스가 물려받습니다. 
+ 하지만 반드시 오버라이딩해야 하는 추상 메소드와 달리 일반 메소드는 물려받은 그대로 사용할지, 오버라이드할지 선택할 수 있습니다.

# 4. 추상 메소드의 바디

```python
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def draw(self):
        """도형을 콘솔에 그린다."""
        print('도형을 그리는 중!')

```

+ 추상 메소드 `draw()` 바디 부분에 메시지를 출력하는 코드를 썼습니다.
+ 그런데 좀 이상하죠? 어차피 추상 클래스를 상속받는 자식 클래스에서 추상 메소드들은 반드시 오버라이딩해야 한다고 했는데요. 
+ 이렇게 어차피 무시될 추상 메소드의 내용이 왜 필요한지 조금 의문이군요.

+ 하지만 사실 이 내용은 경우에 따라 유용할 때가 있습니다. 
+ 보통 추상 메소드에 내용을 쓸 때는 모든 자식 클래스에 해당하는 공통 내용을 써줍니다. 
+ 모든 일반 도형 인스턴스가 그려지기 전 메시지를 출력해야 된다고 할게요. 
+ 이 내용을 위 추상 클래스 바디에 써놓으면 다른 일반 도형 클래스들에 중복 코드를 쓸 필요 없이, 그냥 `super()` 함수를 통해서 가지고 올 수 있습니다. 이렇게요.

```python
class Circle(Shape):
    """원 클래스"""
    def __init__(self, diameter):
        self.diameter = diameter

    def draw(self):
        """도형을 콘솔에 그린다"""
        super().draw()  # Shape 클래스의 draw() 메소드를 실행시킨다
        radius = self.diameter / 2 - .5
        r = (radius + .25)**2 + 1
        result = '\n'
        for i in range(self.diameter):
            y = (i - radius)**2
            for j in range(self.diameter):
                x = (j - radius)**2
                if x + y <= r:
                    result += '* '
                else:
                    result += '  '
            result += '\n'
        print(result)

circle = Circle(7)
circle.draw()

```

```python
도형을 그리는 중!

    * * *     
  * * * * *   
* * * * * * * 
* * * * * * * 
* * * * * * * 
  * * * * *   
    * * *

```
+ 물려받은 추상 메소드를 오버라이딩하는데

> + `super()` 함수를 통해 추상 메소드의 기존 내용을 포함함과 동시에
이와 별도로 자신만의 내용을 또 추가한 거죠.



+ 이렇게 모든 자식 클래스에서 공통적으로 사용할 부분을 추상 메소드의 내용으로 써주고 
+ 자식 클래스에서 이를 `super()` 함수로 접근하는 방법은 꽤 자주 쓰는 방법이기 때문에 필요할 때 꼭 떠올려보세요.
