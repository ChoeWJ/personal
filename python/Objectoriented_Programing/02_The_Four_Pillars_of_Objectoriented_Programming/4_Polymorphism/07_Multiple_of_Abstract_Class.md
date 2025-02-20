+ 추상 클래스 여러개를 상속받는 것은 문제가 되지 않는다

---
```python
from abc import ABC, abstractmethod

class Message(ABC):
    @abstractmethod
    def print_message(self):
        pass

class Sendable(ABC):
    @abstractmethod
    def send(self, destination):
        pass

class Email(Message, Sendable):
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email

    def print_message(self):
        print(f"이메일 내용입니다:\n{self.content}")

    def send(self, destination):
        print(f"이메일을 주소 {self.user_email}에서 {destination}로 보냅니다!")

```

```python
email = Email("안녕? 오랜만이야 잘지내니?", "young@codeit.xyz")
email.print_message()
email.send("yoonsoo@codeit.xyz")

```

```python
이메일 내용입니다:
안녕? 오랜만이야 잘지내니?
이메일을 주소 young@codeit.xyz에서 yoonsoo@codeit.xyz로 보냅니다!
```

+ 자식 클래스는 어차피 상속받는 모든 추상 메서드를 오버라이딩해야한다.
+ 부모에 같은 이름의 추상 메서드들이 있다해도`mro()` 순서상 자식 클래스가 먼저 실행되기 때문에 먼저 오버라이딩 된다.
+ 때문에 주상 메서드들로만 이루어져 있으면 추상 메서드 이름이 아무리 겹친다고 해도 문제없이 잘 동작이 가능하다.

# 추상 클래스에 일반 메소드가 있을 때

```python
class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

    def __str__(self):
        return "메시지 클래스의 인스턴스"

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:
        pass

    def __str__(self):
        return "보내질 수 있는 것 클래스의 인스턴스"

```

+ 물론 위와 같이 추상 클래스에 추상 메서드가 아닌 **일반 메서드** 도 같이 있다면
+ 일반 메서드의 다중 상속과 마찬가지로 주의해야 한다.
+ 이유는 일반 메서드를 오버라이드하지 않으면 어느 추상 클래스의 것을 실행해야 하는지 애매하다는 문제가 있기 때문이다.