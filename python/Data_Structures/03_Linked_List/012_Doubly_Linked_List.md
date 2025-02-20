+ 더블리 링크드 리스트(Doubly Linked List)는 컴퓨터 과학에서 사용하는 데이터 구조 중 하나로, 각 노드가 두 개의 포인터를 가지고 있는 연결 리스트입니다. 

+ 이 포인터는 각각 이전 노드와 다음 노드를 가리킵니다. 

+ 이 구조는 단일 연결 리스트(Singly Linked List)와 달리 **양방향으로 순회가 가능**하다는 장점이 있습니다.

## 구조

+ 노드(Node): 더블리 링크드 리스트의 각 노드는 데이터 필드와 두 개의 포인터 필드를 포함합니다:

+ 데이터(data): 노드가 저장하는 실제 값.

+ 이전 포인터(prev): 이전 노드를 가리키는 포인터.

+ 다음 포인터(next): 다음 노드를 가리키는 포인터.

+ 헤드(Head): 리스트의 첫 번째 노드를 가리킵니다.

+ 테일(Tail): 리스트의 마지막 노드를 가리킵니다.

## 동작

+ 삽입(Insertion):

    + 특정 위치에 노드를 추가할 때, 이전 노드와 다음 노드의 포인터를 업데이트하여 새 노드를 연결합니다.

    + 처음(head) 또는 끝(tail)에 삽입하는 경우도 동일한 방식으로 동작하지만, 헤드 또는 테일 포인터를 업데이트해야 합니다.

    + 삭제(Deletion):

        + 특정 노드를 삭제할 때, 이전 노드와 다음 노드의 포인터를 업데이트하여 제거된 노드를 리스트에서 분리합니다.

        + 삭제할 노드가 헤드 또는 테일인 경우, 해당 포인터도 업데이트해야 합니다.

+ 순회(Traversal):

    + 앞에서 뒤로: 헤드부터 시작해 각 노드의 next를 따라갑니다.

    + 뒤에서 앞으로: 테일부터 시작해 각 노드의 prev를 따라갑니다.

+ 검색(Search):

    + 리스트를 순회하면서 원하는 값을 찾습니다. 시간 복잡도는  $O(n)$입니다.

## 장점

+ 양방향으로 순회할 수 있어 특정 상황에서 더 효율적입니다.

+ 단일 연결 리스트보다 노드 삽입 및 삭제가 유연합니다. (이전 노드에 직접 접근할 수 있으므로)

## 단점

+ 각 노드가 추가적인 포인터(이전 포인터)를 저장해야 하므로 더 많은 메모리를 사용합니다.

+ 추가적인 포인터 관리로 인해 구현이 단순 연결 리스트보다 복잡합니다.

## 예시

+ 다음은 더블리 링크드 리스트의 삽입 및 삭제 과정입니다:

    + 리스트 초기 상태:

        ```r
        NULL <- 1 <-> 2 <-> 3 -> NULL
        ```

    + 노드 4를 끝에 삽입:
        ```rust
        NULL <- 1 <-> 2 <-> 3 <-> 4 -> NULL
        ```

    + 노드 2를 삭제:
        ```r
        NULL <- 1 <-> 3 <-> 4 -> NULL
        ```

+ 이 구조는 스택, 큐, 데크, 그리고 캐시 구현 등 다양한 응용에서 사용됩니다.

## Python 코드 예시

```python
class Node:
    """노드를 정의하는 클래스"""
    def __init__(self, data):
        self.data = data  # 데이터 저장
        self.prev = None  # 이전 노드 포인터
        self.next = None  # 다음 노드 포인터

class DoublyLinkedList:
    """더블리 링크드 리스트 구현 (tail 포함)"""
    def __init__(self):
        self.head = None  # 첫 번째 노드
        self.tail = None  # 마지막 노드

    def append(self, data):
        """리스트 끝에 노드 추가"""
        new_node = Node(data)
        if not self.head:  # 리스트가 비어 있는 경우
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node  # 기존 tail의 다음 노드를 새 노드로 설정
        new_node.prev = self.tail  # 새 노드의 이전 노드를 기존 tail로 설정
        self.tail = new_node       # tail을 새 노드로 업데이트

    def delete(self, data):
        """특정 데이터를 가진 노드 삭제"""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:  # 이전 노드가 있을 경우
                    current.prev.next = current.next
                else:  # 삭제할 노드가 head일 경우
                    self.head = current.next
                if current.next:  # 다음 노드가 있을 경우
                    current.next.prev = current.prev
                else:  # 삭제할 노드가 tail일 경우
                    self.tail = current.prev
                return  # 삭제 완료
            current = current.next

    def display(self):
        """리스트를 출력"""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements



dll = DoublyLinkedList()

# 노드 추가
dll.append(1)
dll.append(2)
dll.append(3)

# 초기 상태 출력
print("Initial list:", dll.display())  # [1, 2, 3]

# 노드 삭제
dll.delete(3)  # tail 노드 삭제
print("After deleting tail:", dll.display())  # [1, 2]

# 추가 노드 삽입
dll.append(4)  # 새로운 tail 추가
print("After adding new tail:", dll.display())  # [1, 2, 4]
```
