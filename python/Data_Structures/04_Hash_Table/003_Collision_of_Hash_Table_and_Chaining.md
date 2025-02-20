## Chaining

+ 해시 테이블 충돌을 링크드 리스트를 통해서 방지한다.

+ 링크드 리스트에 key - value를 저장해서 다음 노드를 연결

+ 마치 쇠사슬로 묶여 있는 것처럼 연결해 둔다.

+ 따라서 충돌이 일어나도 링크드 리스트에 값을 주면 원하는 key-value 쌍을 모두 저장할 수 있다.

```python
class Node:

    def __init(self, key, value):
        self.key = key
        self.value = value
        self.next = None
```

---

+ 전 레슨에서도 보았듯이 Chaining을 이용하면 해시 테이블에서 충돌이 일어나도 key - value 쌍들을 모두 저장할 수 있습니다. 

+ 이번 챕터에서는 해시 테이블의 개념을 배우고 직접 구현해볼 건데요. 지난 챕터에서 만들었던 링크드 리스트 클래스도 한 번 해시 테이블에서 사용할 수 있게 바꿔볼게요.

+ 더블리 링크드 리스트를 이용하겠습니다.

## Node 클래스

+ 여기서는 크게 바꿀 건 없는데요. 영상에서 본 것처럼 그냥 링크드 리스트 노드가 변수 data 대신 key와 value를 저장하도록 해줄게요.

```python
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None  # 전 노드에 대한 레퍼런스
```

## LinkedList 클래스
+ 링크드 리스트 클래스에서는 필요한 메소드들만 가지고 와서 쓰면 됩니다. 노드 클래스랑 마찬가지로 그대로 사용할 수는 없고요. 조금씩 고쳐서 써야합니다.

+ 다행히 __init__ 메소드는 바꾸지 않아도 됩니다.

```python
class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드
```

## 탐색 메소드

```python
def find_node_with_key(self, key):
    """링크드 리스트에서 주어진 데이터를 갖고있는 노드를 리턴한다. 단, 해당 노드가 없으면 None을 리턴한다"""
    iterator = self.head   # 링크드 리스트를 돌기 위해 필요한 노드 변수

    while iterator is not None:
        if iterator.key == key:
            return iterator

        iterator = iterator.next

    return None
```

+ 탐색 메소드는 이제 특정 데이터를 갖은 노드를 찾는 게 아니라 **특정 key를 갖는 노드**를 찾습니다. 

+ 이에 맞게 링크드 리스트를 처음부터 끝까지 돌면서 원하는 key를 갖는 노드를 리턴해주도록 수정해줍니다. 코드에서는 기존에 data 변수를 다 key로 바꿔주면 되죠.

## 추가 (맨 뒤 삽입) 메소드

```python
def append(self, key, value):
    """링크드 리스트 추가 연산 메소드"""
    new_node = Node(key, value)

    # 빈 링크드 리스트라면 head와 tail을 새로 만든 노드로 지정
    if self.head is None:
        self.head = new_node
        self.tail = new_node
    # 이미 노드가 있으면
    else:
        self.tail.next = new_node  # tail의 다음 노드로 추가
        new_node.prev = self.tail
        self.tail = new_node  # tail 업데이트
```

+ 추가 메소드 append는 이제 파라미터로 data 변수 대신 key와 value를 받습니다. 

+ 링크드 리스트에 데이터를 더해줄 때는 항상 새로운 노드를 만들어줘야 되는데요. 파라미터로 받은 정보를 key와 value를 갖는 새로운 노드를 만들어줍니다. 

+ 새 노드를 링크드 리스트에 연결해주는 부분 코드는 똑같습니다.

## 삭제 메소드

```python
def delete(self, node_to_delete):
    """더블리 링크드 리스트 삭제 연산 메소드"""

    # 링크드 리스트에서 마지막 남은 데이터를 삭제할 때
    if node_to_delete is self.head and node_to_delete is self.tail:
        self.tail = None
        self.head = None

    # 링크드 리스트 가장 앞 데이터 삭제할 때
    elif node_to_delete is self.head:
        self.head = self.head.next
        self.head.prev = None

    # 링크드 리스트 가장 뒤 데이터 삭제할 떄
    elif node_to_delete is self.tail:
        self.tail = self.tail.prev
        self.tail.next = None

    # 두 노드 사이에 있는 데이터 삭제할 때
    else:
        node_to_delete.prev.next = node_to_delete.next
        node_to_delete.next.prev = node_to_delete.prev
```

+ 원래 링크드 리스트 삭제 메소드에서는 노드를 삭제할 때 삭제하는 노드의 데이터를 리턴했는데요. 이 부분을 빼줄게요.

+ 나머지 부분은 바꿔줄 필요 없습니다. 더블리 링크드 리스트 삭제 메소드는 어차피 노드가 주어졌을 때 그 노드를 링크드 리스트에서 삭제해주죠? 

+ 기존 data 변수나 key, value 변수와 전혀 관계가 없는 메소드기 때문에 나머지 코드를 바꿀 필요가 없는 거죠.

## 문자열 메소드

+ 문자열 메소드는 출력 형식을 조금 바꿔줄게요.

```python
def __str__(self):
    """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
    res_str = ""

    # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
    iterator = self.head

    # 링크드 리스트 끝까지 돈다
    while iterator is not None:
        # 각 노드의 데이터를 리턴하는 문자열에 더해준다
        res_str += "{}: {}\n".format(iterator.key, iterator.value)
        iterator = iterator.next # 다음 노드로 넘어간다

    return res_str
```

+ 원래는 링크드 리스트에 2, 3, 5, 7, 11이 들어있으면 이런 식으로 링크드 리스트의 모든 data 변수를 한 줄에 순서대로 출력했잖아요?

```
2 | 3 | 5 | 7 | 11
```

+ 이제는 key - value 쌍을 저장하니까 출력 형식도 바꿔주는 거죠.

+ 링크드 리스트에 `101: “최지웅”, 204: “강영훈”, 305: “성태호”`이 들어 있다고 할게요. 

+ 그러면 아래와 같이 이 링크드 리스트를 출력했을 때 한 줄에 한 key, value 쌍 하나씩 나오도록 바꿔준 거죠.

```
101: 최지웅
204: 강영훈
305: 성태호
```