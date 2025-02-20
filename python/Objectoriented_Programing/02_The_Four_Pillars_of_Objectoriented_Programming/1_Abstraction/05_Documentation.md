+ 문서화의 형식에 관해 꼭 지켜야 할 규칙은 없습니다. 하지만 흔히 사용하는 포맷은 있습니다.

+ 유저를 위한 추천 영상을 찾는 find_suggestion_videos 메소드의 docstring을 작성한다고 해봅시다. 

+ 널리 쓰이는 포맷 3가지로 각각 문서화를 해볼게요.

```python
def find_suggestion_videos(self, number_of_suggestions=5):
```

# Google Docstring:
```python
"""유저에서 추천할 영상을 찾아준다
Parameters:
number_of_suggestions (int): 추천하고 싶은 영상 수. 기본값은 5

Returns:
list: 추천할 영상 주소가 담긴 리스트
"""
```

# reStructuredText (파이썬 공식 문서화 기준):
```python
"""유저에서 추천할 영상을 찾아준다
:param number_of_suggestions: 추천하고 싶은 영상 수. 기본값은 5
:type number_of_suggestions: int

:returns: 추천할 영상 주소가 담긴 리스트
:rtype: list
"""
```

# NumPy/SciPy
```python
"""유저에서 추천할 영상을 찾아준다

Parameters
----------
number_of_suggestions: int
  추천하고 싶은 영상 수 (기본값은 5)

Returns
-------
list 
  추천할 영상 주소가 담긴 리스트
"""
```
+ 한 가지 메소드의 정보를 3가지 포맷으로 문서화한 것을 보았습니다. 
+ 문서화에서 가장 중요한 것은 프로그램을 함께 만드는 팀원들과 이러한 문서화 포맷에 관해 미리 약속을 하고 이를 잘 지키는 것입니다. 
+ 혼자서 만드는 프로그램이라도 자신만의 포맷을 일관성 있게 사용한다면 나중에 프로그램을 수정할 때 도움이 되겠죠?