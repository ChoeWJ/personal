# 링크드 리스트(Linked List)란?

+ **링크드 리스트**(Linked List)는 데이터를 **노드**(Node)로 구성하여 연결하는 **선형 자료 구조**입니다. 

+ 각 노드는 데이터와 다음 노드에 대한 **참조**(포인터)를 포함하고 있습니다.

## 구조

+ 노드(Node):

    + 데이터(Data): 저장할 값.

    + 참조(Reference): 다음 노드(또는 이전 노드)의 주소를 저장.

### 종류
1. 단일 링크드 리스트(Singly Linked List):

    + 각 노드가 다음 노드를 가리킴.

    + 마지막 노드의 참조는 null 또는 None(Python)으로 설정됨.

2. 이중 링크드 리스트(Doubly Linked List):

    + 각 노드가 이전 노드와 다음 노드를 모두 가리킴.

    + 양방향 탐색이 가능.

3. 환형 링크드 리스트(Circular Linked List):

    + 마지막 노드가 첫 번째 노드를 가리켜 순환 구조를 형성.

## 특징

+ 유연성: 배열과 달리, 크기가 고정되지 않아 동적 크기 조정이 가능.

+ 메모리 할당: 노드가 필요할 때마다 힙 메모리에 동적으로 생성됨.

+ 삽입/삭제:

    + 특정 위치에서 삽입/삭제가 빠름 ($O(1)$, 참조만 변경).

    + 그러나, 탐색 시에는 느림 ($O(n)$).

## 장단점

### 장점

+ 크기가 유동적이라 메모리 낭비가 적음.

+ 삽입과 삭제가 배열에 비해 유리함(중간에서 데이터 추가/삭제 시).

### 단점

+ 순차 접근만 가능(랜덤 접근이 불가능).

+ 노드마다 추가적인 참조(포인터)를 저장해야 하므로 메모리 오버헤드 발생.

+ 탐색 속도가 배열보다 느림.

## 예제1: 단일 링크드 리스트 (Python)
```python
class Node:
    def __init__(self, data):
        self.data = data  # 데이터 저장
        self.next = None  # 다음 노드의 참조 초기화

class LinkedList:
    def __init__(self):
        self.head = None  # 링크드 리스트의 첫 노드

    # 노드 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # 리스트가 비었을 경우
            self.head = new_node
            return
        current = self.head
        while current.next:  # 마지막 노드까지 이동
            current = current.next
        current.next = new_node

    # 노드 출력
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 사용 예시
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()  # 출력: 10 -> 20 -> 30 -> None
```

## 예제2: 이중 링크드 리스트
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # 이전 노드
        self.next = None  # 다음 노드

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드

    # 노드 추가 (끝에 추가)
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # 리스트가 비어 있는 경우
            self.head = new_node
            return
        current = self.head
        while current.next:  # 마지막 노드로 이동
            current = current.next
        current.next = new_node
        new_node.prev = current  # 이전 노드 참조 설정

    # 노드 출력 (앞에서 뒤로)
    def display_forward(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    # 노드 출력 (뒤에서 앞으로)
    def display_backward(self):
        current = self.head
        if not current:
            print("List is empty")
            return
        while current.next:  # 마지막 노드로 이동
            current = current.next
        while current:  # 뒤에서 앞으로 출력
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

# 사용 예시
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display_forward()  # 출력: 10 <-> 20 <-> 30 <-> None
dll.display_backward()  # 출력: 30 <-> 20 <-> 10 <-> None
```

## 예제3: 환형 링크드 리스트
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 다음 노드

class CircularLinkedList:
    def __init__(self):
        self.head = None  # 리스트의 첫 번째 노드

    # 노드 추가
    def append(self, data):
        new_node = Node(data)
        if not self.head:  # 리스트가 비어 있는 경우
            self.head = new_node
            new_node.next = self.head  # 첫 노드를 자기 자신으로 연결
            return
        current = self.head
        while current.next != self.head:  # 마지막 노드 찾기
            current = current.next
        current.next = new_node
        new_node.next = self.head  # 새 노드를 첫 노드로 연결

    # 노드 출력
    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:  # 다시 첫 노드로 돌아오면 종료
                break
        print("(Back to head)")

# 사용 예시
cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()  # 출력: 10 -> 20 -> 30 -> (Back to head)
```

## 활용 사례


+ 스택과 큐 구현.

+ 해시 테이블에서 충돌 해결(체이닝 방식).

+ 그래프의 인접 리스트 표현.

+ 캐시 시스템에서 LRU(Least Recently Used) 알고리즘 구현.

## 링크드 리스트는 데이터 구조의 기본 개념을 배우고, 다양한 응용 프로그램에서 활용할 수 있는 중요한 구조입니다!