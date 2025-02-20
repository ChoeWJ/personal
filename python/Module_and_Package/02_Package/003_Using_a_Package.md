```python
import Shapes.Volume

print(Shapes.Volume.cube(3)) # 27
```

+ `as`를 사용해서 아래와 같이도 사용 가능하다.

```python
import Shapes.Volume as vol

print(vol.cube(3)) # 27
```
+ `from`을 사용해서도 가져올 수 있다

```python
from Shapes.Example import square

print(square(3)) # 9
```

```python
from Shapes import Volume

print(Volume.cube(3)) # 27
```
+ 단순하게 패키지만 임포트 할 경우는 오류가 발생한다

```python
import Shapes

print(Shapes.Example.circle(3))

"""
AttributeError: module 'Shapes' has no attribute 'Example'
"""

print(Shapes.Volume.circle(3))
"""
AttributeError: module 'Shapes' has no attribute 'Volume'
"""
```

+ 위와 같은 오류가 발생하는 이유는

+ 파이썬에서는 패키지를 임포트하면 패키지 안에 있는 내용들은 임포트가 되지 않는다.

+ 따라서 패키지 안에 있는 모듈들도 같이 임포트 하려면 `__init__.py` 파일을 사용해야 한다.