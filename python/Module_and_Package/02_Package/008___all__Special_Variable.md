# `Shapes 패키지 구조`

```python
# Shapes/
    __init__.py
    area.py
    volume.py
```

```python
# Shapes/Example.py

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length
```

```python
# Shapes/Volume.py

PI = 3.14

# 구의 부피를 구해 주는 함수
def sphere(radius):
    return (4/3) * PI * radius * radius * radius

# 정육면체의 부피를 구해 주는 함수
def cube(length):
    return length * length * length
```

# `import *`

+ 모듈을 임포트할 때 `from <module> import *`를 하면 **모듈의 모든 내용이 임포트**됩니다.

+ 하지만 모듈 대신 패키지에 `from <package> import *`를 하면 패키지 안에 있는 게 아무것도 임포트되지 않습니다.

# `__all__ 특수 변수`

+ `__all__` 특수 변수는 우리가 `import *`를 했을 때 **임포트 대상에서 어떤 것들을 가져와야 하는지를 정해 주는 변수**입니다. 

+ 임포트 대상에서 내용 전체를 가져오라고 했을 때 **'전체'가 무엇인지 정의**해 주는 거죠. 

+ `__all__` 은 모듈에도 적용되고 패키지에도 적용됩니다.

# `__all__ 과 모듈`

+ 모듈의 `__all__` 은 모듈에 해당하는 파일에서 정의합니다. 

+ 예를 들어 `area.py`에 아래와 같은 코드를 추가해 주면:

```python

# Shapes/Example.py

# __all__ 정의
__all__ = ['circle', 'square'] 

PI = 3.14

# 원의 면적을 구해 주는 함수
def circle(radius):
    return PI * radius * radius  

# 정사각형의 면적을 구해 주는 함수
def square(length):
    return length * length
```

+ `from shapes.area import *`를 했을 때 `area` 모듈의 모든 내용이 임포트되지 않고 `circle` 과 `square` 함수만 임포트됩니다.

# `__all__ 과 패키지`

+ 패키지의 `__all__` 은 패키지에 해당하는 `init` 파일에서 정의합니다. 

+ 예를 들어 `shapes` 패키지의 `init` 파일에 아래와 같은 코드를 추가해 주면:

```python
# Shapes/__init__.py

__all__ = ['area', 'volume']
```

+ 이제 `from shapes import *`를 하면 `area` 모듈과 `volume` 모듈이 임포트됩니다.

+ `__all__`을 사용하면 패키지나 모듈에 `import *`를 했을 때 **어떤 것들이 임포트되는지를 제어**할 수 있습니다. 

+ 그래도 여전히 `import *` 만 봐서는 정확히 어떤 것들이 임포트되는지를 알 수 없기 때문에 `import *`는 프로그램에서 정의되는 이름들, 

+ ***즉 네임스페이스를 완벽히 이해하고 있을 때만 사용하는 것을 추천***드립니다.