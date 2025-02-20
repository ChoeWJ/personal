# 더블리 링크드 리스트 겹치는 연산들

+ 사실 더블리 링크드 리스트는 __init__ 메소드 말고도 싱글리 링크드 리스트에서 안 바꿔도 되는 메소드들이 좀 있는데요.

+ 구체적으로 말하면 `find_node_at(접근 연산)`, `find_node_with_data(탐색 연산)`, 그리고 `__str__`  메소드가 싱글리 링크드 리스트랑 겹칩니다.

+ 그래서 더블리 링크드 리스트를 배울 때도 이 메소드들은 이미 있다는 가정하에 배울 건데요. 참고하시기 편하게 아래에 메소드 별로 적어놨습니다.

+ 혹시 이번 노트에서 보시는 메소드 중에서 이해가 안 되는 부분이 있으면 챕터 앞 부분의 레슨들을 복습하시고 넘어가시는 걸 추천드릴게요.

## 접근

```python
def find_node_at(self, index):
    """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정한다"""
    
    iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
    
    # index 번째 있는 노드로 간다
    for _ in range(index):
        iterator = iterator.next
    
    return iterator
```

## 탐색

```python
def find_node_with_data(self, data):
    """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
    iterator = self.head  # 링크드 리스트를 돌기 위해 필요한 노드 변수
    
    while iterator is not None:
        if iterator.data == data:
            return iterator

        iterator = iterator.next

    return None
```

## __str__ 메소드

```python
def __str__(self):
    """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
    res_str = "|"

    # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
    iterator = self.head

    # 링크드 리스트 끝까지 돈다
    while iterator is not None:
        # 각 노드의 데이터를 리턴하는 문자열에 더해준다
        res_str += " {} |".format(iterator.data)
        iterator = iterator.next  # 다음 노드로 넘어간다

    return res_str
```