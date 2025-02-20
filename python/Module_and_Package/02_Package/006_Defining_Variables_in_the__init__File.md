+ 패키지만 가져와서 안에 있는 모듈들을 사용하려고 하면 

+ 안에 있는 모듈들은 같이 임포트 되지 않기 떄문에 오류가 나게 된다.

+ 패키지를 임포트할 때 안에 있는 모듈들도 같이 가져오려면

+ `__init__.py` 파일을 활용하면 된다.

```python
# Test.py

import Shapes

print(Shapes.Example.square(2))
print(Shapes.Volume.cube(2))
```

```python
# __init__.py

from Shapes import Example, Volume
```
+ 이렇게 `__init__.py` 파일에 먼저 임포트를 해주면 오류가 나지 않는다.

