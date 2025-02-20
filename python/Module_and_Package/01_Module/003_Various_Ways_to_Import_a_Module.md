
# 함수 불러오기

```python
# test.py의 circle 함수를 불러오기
from test import circle, square 



# test.py에서 정의한 원의 면적 구하기 함수 실행
print(circle(2))    # 12.56

print(square(2))    # 4
```

# 모듈 이름 지정

```python
# test 모듈을 가져와서 이름을 T로 지정한다.
import test as T



# test.py에서 정의한 원의 면적 구하기 함수 실행
print(T.circle(2))    # 12.56

print(T.square(2))    # 4
```

# 함수 이름 지정

```python
# test 모듈을 가져와서 이름을 T로 지정한다.
from test import square as sq
from test import circle as cr



# test.py에서 정의한 원의 면적 구하기 함수 실행
print(cr(2))    # 12.56

print(sq(2))    # 4
```

# 모듈 내의 모든 함수 불러오기

```python 
from test import *
```