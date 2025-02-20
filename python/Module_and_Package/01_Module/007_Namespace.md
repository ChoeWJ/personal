+` 네임스페이스(Namespace)`는 파일에서 정의된 모든 이름들을 의미한다.

+ 따라서 `dir 함수`는 파이썬의 `네임스페이스`를 리턴해 주는 것이다.

```python
import Example

print(dir())

"""
['Example', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 'help', 'howdoi', 'input']
"""
```

+ 여기서 `Example 모듈`에 추가로 또 다른 `square 함수`를 정의한다면 어떻게 될 것인가?

```python
# Test.py

from Example import circle, square

def square(side):
    return side * 4

print(dir())

print(square(4))

"""
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 'circle', 'help', 'howdoi', 'input', 'square']
16
"""
```

+ 출력값을 확인해 보면 새롭게 `Test.py`에서 정의한 함수의 결괏값으로 출력된다.

+ 파이썬에서 이렇게 똑같은 이름을 여러 함수가 정의되었을 때 **가장 나중에 정의된 함수**를 사용한다.

+ 따라서 한 네임스페이스안에서는 같은 이름이 중복되지 않는 것이 좋다.

+ 그렇다면 이것들이 중복되지 않게 하는 방법이 있을까?

    1. from Example import circle, square as sq

        ```python
        from Example import circle, square as sq

        def square(side):
            return side * 4

        print(dir())

        print(square(4))

        print(sq(3))
        ```

    2. 모듈을 그대로 import
        ```python
        import Example

        def square(side):
            return side * 4

        print(dir())

        print(square(4))

        print(Example.sq(3))
        ```
+ 두 가지 방식 모두 출력 결과를 확인해보면

```python

"""
['__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 'circle', 'help', 'howdoi', 'input', 'sq', 'square']
16
9
"""
```

+ 위 두 가지 경우 모두 동일한 결괏값이 출력되는 것을 확인할 수 있다.

+ 참고로 `import *` 가 권장되지 않는 이유를 출력 결과로 확인해 보면,

```python

from Example import*
 
def square(side):
    return side * 4

print(dir())

"""
['PI', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', 'circle', 'help', 'howdoi', 'input', 'square']
"""
```

+ 위와 같이 모듈에서 정의된 모든 이름들을 네임스페이스에 추가하고,

+ 그렇게되면 네임스페이스에 어떤 이름들이 추가되었는지 파악하기 힘들고,

+ 중복이 될 확률이 높아진다. 따라서 위와 같은 방식은 권장되지 않는다.