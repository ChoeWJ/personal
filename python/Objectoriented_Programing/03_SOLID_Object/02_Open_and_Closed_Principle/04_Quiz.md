# 실습 설명

+ 안드로이드 앱 개발자 영훈이는 스마트폰에서 메시지 알림 기능을 담당하는 클래스를 만들려고 하는데요. 

+ 아래와 같은 클래스 두 개를 정의했습니다.

# 메시지 알림 관리(MessageNotificationManager) 클래스

```python
class MessageNotificationManager:
    """메시지 알림 관리 클래스"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.short_message() + "\n")
```

# 카카오톡 메시지(KakaoTalkMessage) 클래스

```python
class KakaoTalkMessage:
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def short_message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str
```

+ 이 클래스들을 아래 코드와 같이 사용해 보았는데요.

# 메시지 알림 관리 인스턴스 생성

```python
message_notification_manager = MessageNotificationManager()
```

# 카카오톡 메시지 3개 생성

```python
kakao_talk_message_1 = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같애 미안!")
kakao_talk_message_2 = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 35분", "아니다 갈게 너네 어디서 놀고 있어?")
kakao_talk_message_3 = KakaoTalkMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게 나 지금 출발")
```

# 메시지 알림 관리 인스턴스에 메시지 추가

```python
message_notification_manager.add_new_message(kakao_talk_message_1)
message_notification_manager.add_new_message(kakao_talk_message_2)
message_notification_manager.add_new_message(kakao_talk_message_3)
```

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력

```python
message_notification_manager.display_message_notifications()
새로 온 메시지들:
2019년 7월 1일 오후 11시 30분
고대위
나 오늘 놀러 못갈...

2019년 7월 1일 오후 11시 35분
고대위
아니다 갈게 너네 ...

2019년 7월 2일 오전 12시 30분
이영훈
나도 놀러 갈게 나...
```

+ `MessageNotificationManager 인스턴스`가 `KakaoTalkMessage 인스턴스들`의 다음 정보들을 잘 출력합니다.

```python
"""
보낸 날짜
보낸 사람
메시지 내용
"""
```

+ 그런데 앞으로는 카카오톡 메시지 뿐만 아니라 페이스북 메시지와 문자 메시지까지도 이 클래스에서 알림 관리를 해줘야 한다고 하네요.

+ 일단 각 메시지를 나타내는 클래스를 아래처럼 만들었다고 합시다.

# 페이스북 메시지(FacebookMessage) 클래스

```python
class FacebookMessage:
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def notification_display_info(self):
       """메시지의 정보와 내용을 리턴함"""
        res_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        res_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."

        return res_str
```

# 문자 메시지(TextMessage) 클래스

```python
class TextMessage:
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def notification_string(self):
        """메시지의 정보와 내용을 리턴함"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."
        return noti_string
```

+ 이렇게 `FacebookMessage 클래스`와 `TextMessage 클래스`를 일단 만들었습니다. 

+ 그런데 `MessageNotificationManager 클래스`는 `KakaoTalkMessage 클래스`를 사용하는 것만 생각하고 작성했던 클래스입니다. 

+ 그래서 만약 새로 만든 클래스들의 인스턴스를 추가한다면 `MessageNotificationManager 클래스`의 `display_message_notifications() 메소드`를 호출할 때 

+ 아래 코드 부분의 `short_message 메소드` 부분에서 에러가 날 겁니다.

```python
for message in self.message_notifications:
            print(message.short_message() + "\n")
```

+ 왜냐하면  `FacebookMessage 클래스`와 `TextMessage 클래스`에는 `short_message라는 메소드`가 없으니까요.

+ `FacebookMessage 클래스`와 `TextMessage 클래스`의 인스턴스도 사용할 수 있으려면 

+ `MessageNotificationManager 클래스`의 코드를 좀 수정해야겠네요. 

+ 하지만 이렇게 새로운 기능을 추가할 때 기존에 썼던 코드를 수정하는 것은 **개방-폐쇄 원칙에 어긋**납니다. 

+ 지금 있는 클래스들을 개방 폐쇄 원칙에 맞게 바꿔서 `MessageNotificationManager 클래스`의 코드를 더 이상 수정하지 않아도 되는 상태로 만들어 볼까요?


# 실습 결과

```python
"""
새로 온 메시지들:
2019년 7월 1일 오후 11시 30분
고대위
나 오늘 놀러 못갈...

2019년 7월 1일 오후 11시 35분
고대위
서울시 성북구
아니다, 갈게! 너네 어디서...

이영훈, 2019년 7월 2일 오전 12시 30분
나도 놀러 갈게, 나 ...
"""
```

# 문제 풀이

```python
from abc import ABC, abstractmethod

class Message(ABC):
    
    @abstractmethod
    def message(self):
        pass

class MessageNotificationManager:
    """메시지 알림 관리 클래스"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """새로 온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새 메시지 확인"""
        print("새로 온 메시지들:")

        for message_str in self.message_notifications:
            print(message_str.message() + "\n")


class KakaoTalkMessage(Message):
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str


class FacebookMessage(Message):
    """페이스북 메시지 클래스"""
    notification_message_max_len = 15

    def __init__(self, sent_by, location, time, content):
        self.sent_by = sent_by
        self.location = location
        self.time = time
        self.content = content

    def message(self):
        """메시지를 짧은 형태로 리턴함"""
        message_str = "{}\n{}\n{}\n".format(self.time, self.sent_by, self.location)
        message_str += self.content if len(self.content) <= FacebookMessage.notification_message_max_len else self.content[:FacebookMessage.notification_message_max_len] + "..."

        return message_str   
        

class TextMessage(Message):
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def message(self):
        """메시지의 정보와 내용을 리턴함"""
        message_str = "{}, {}\n".format(self.sent_by, self.time)
        message_str += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."
        return message_str 



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
```