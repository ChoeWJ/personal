# 해설

## 알림 가능한 메시지(NotifiableMessage) 추상 클래스

+ 이 과제에서 개방 폐쇄 원칙을 지키려면 **코드에 다형성을 적용**하면 됩니다. 

+ 여러 종류의 메시지 클래스들이 하나의 추상 클래스를 상속받도록 하면 되는데요. 

+ 먼저 모든 메시지 클래스가 가져야 할 공통 메소드를 생각해 보겠습니다. 

+ 힌트에서 제시된 `NotifiableMessage`라는 이름으로 `추상 클래스`를 정의하고 그 안에 알림 내용을 리턴하는 `추상 메소드`를 만들겠습니다. 

+ `추상 메소드`의 이름은 `get_notification_message()`라고 하겠습니다.

```python
from abc import ABC, abstractmethod

class NotifiableMessage(ABC):
    """알림 가능한 메시지를 나타내는 추상 클래스"""
    @abstractmethod
    def get_notification_message(self) -> str:
        """알림 내용에 들어갈 문자열을 리턴하는 메소드"""
        pass
```

+ 이제 모든 종류의 메시지 클래스들이 이 `NotifiableMessage 추상 클래스`를 상속받게 하면 됩니다.

## 카카오톡(KakaoTalkMessage) 클래스

```python
class KakaoTalkMessage(NotifiableMessage):
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_notification_message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str
```

## 페이스북 메시지(FacebookMessage) 클래스

```python
class FacebookMessage(NotifiableMessage):
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def get_notification_message(self):
        """메시지의 정보와 내용을 리턴함"""
        res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."

        return res_str
```

## 문자 메시지(TextMessage) 클래스

```python
class TextMessage(NotifiableMessage):
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_notification_message(self):
        """메시지의 정보와 내용을 리턴함"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."

        return noti_string
```

+ `KakaoTalkMessage 클래스`

+ `FacebookMessage 클래스`

+ `TextMessage 클래스`

+ 모두 `NotifiableMessage 추상 클래스`를 상속받도록 정의했습니다. 

+ 그리고 메시지 알림 내용을 리턴하기 위해 각자 다름 이름으로 갖고 있던 메소드의 이름을 모두 `get_notification_message`로 수정했습니다.

## 메시지 알림 매니저(MessageNotificationManager) 클래스

+ 이제 `MessageNotificationManager 클래스`의 `add_new_message 메소드`가 `NotifiableMessage 클래스`의 인스턴스만 파라미터로 받아야한다는 의미를 나타내는 `type hinting`을 합니다. 

+ 그리고 `display_message_notifications 메소드`에서 `message 인스턴스`의 `get_notification_message 메소드`를 호출하면 됩니다.  

+ 이렇게 하면 `MessageNotificationManager 클래스`에 어떤 종류의 메시지 인스턴스가 추가되더라도 그 인스턴스는 `get_notification_message 메소드`를 갖고 있을테니 새로운 메시지 클래스가 생긴다고 하더라도 `MessageNotificationManager 클래스`는 그 코드를 수정할 필요가 없습니다.

```python
class MessageNotificationManager:
    """메시지 알림 관리 클래스"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message: NotifiableMessage):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.get_notification_message() + "\n")
```

# 모범 답안

```python
from abc import ABC, abstractmethod

class NotifiableMessage(ABC):
    """알림 가능한 메시지를 나타내는 추상 클래스"""
    @abstractmethod
    def get_notification_message(self) -> str:
        """알림 내용에 들어갈 문자열을 리턴하는 메소드"""
        pass


class MessageNotificationManager:
    """메시지 알림 관리 클래스"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message: NotifiableMessage):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.get_notification_message() + "\n")


class KakaoTalkMessage(NotifiableMessage):
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_notification_message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str


class FacebookMessage(NotifiableMessage):
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def get_notification_message(self):
        """메시지의 정보와 내용을 리턴함"""
        res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."

        return res_str
        

class TextMessage(NotifiableMessage):
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def get_notification_message(self):
        """메시지의 정보와 내용을 리턴함"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."

        return noti_string


# 메시지 알림 관리 인스턴스 생성
message_notification_manager = MessageNotificationManager()

# 서로 다른 종류의 메시지 3개 생성
kakao_talk_message = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같아, 미안!")
facebook_message = FacebookMessage("고대위", "서울시 성북구", "2019년 7월 1일 오후 11시 35분", "아니다, 갈게! 너네 어디서 놀고 있어?")
text_message = TextMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게, 나 지금 출발")

# 메시지 알림 관리 인스턴스에 3개의 메시지를 추가
message_notification_manager.add_new_message(kakao_talk_message)
message_notification_manager.add_new_message(facebook_message)
message_notification_manager.add_new_message(text_message)

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
message_notification_manager.display_message_notifications()  
          
"""
실습 결과
새로 온 메시지들:
2019년 7월 1일 오후 11시 30분
고대위
나 오늘 놀러 못갈...

2019년 7월 1일 오후 11시 35분
고대위
서울시 성북구
아니다, 갈게! 너네 어디서...

이영훈, 2019년 7월 2일 오전 12시 30분
나도 놀러 갈게, 나...
"""
```
