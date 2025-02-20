+ 일반적으로 클래스를 정의할 때는 클래스를 정의하는 코드와, 

+ 그 클래스 및 인스턴스를 사용하는 코드를 다른 파일들에 분리해 놓습니다.

+ 생각해 보면 정수형, 문자열, 불린, 리스트, 사전 등 파이썬에서 정말 자주 사용하는 클래스들이지만, 

+ 각 클래스들이 모두 실행시키는 파일 안에 있다면 꽤 복잡하고 번거롭겠죠?

+ 직접 정의한 클래스들도 마찬가지입니다. 

+ 하나가 아니라 여러 클래스를 가지고 와서 사용하는 경우들도 많기 때문에 

+ 일반적으로 각 클래스마다 하나의 파일, 또는 연관 있는 클래스들을 한 파일에 묶어서 저장하고, 실행하기 위한 파일을 따로 만듭니다.

+ 이번 토픽에서 만들어본 `User` 클래스를 `user.py`라는 파일에 저장했다고 할게요.

```python
class User:
    count = 0

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, email, password):
        # 로그인 메소드
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"

    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다")
```

+ 그럼 이 파일에는 딱 이 클래스 하나, 또는 유저 클래스와 같이 사용하는 클래스들만 정의를 해놓고요. 

+ 다른 파일에서 이 클래스를 가지고 와서 사용하면 됩니다.

+ 예를 들어 같은 폴더 안에 `driver.py`라는 파일을 만들고, 

+ 여기에 `User` 클래스 및 인스턴스를 사용하는 코드를 작성해서 실행시키면 됩니다.

```python
from user import User

user1 = User("강영훈", "younghoon@codeit.xyz", "123456")
user2 = User("이윤수", "yoonsoo@codeit.xyz", "abcdef")
user3 = User("오종훈", "jonghoon@codeit.xyz", "123abc")

User.print_number_of_users()
```

+ 가장 첫 번째 줄처럼 같은 폴더 안에 있는 `user.py` 파일에서 `User` 클래스를 가지고 오고 싶을 때는 `from`키워드를 쓰고 `.py` 익스텐션을 제외한 파일 이름을 적고, 

+ 그 뒤에 `import` 키워드를 쓰고, 가지고 오고 싶은 클래스 이름, `User`를 써주면 됩니다. 

+ 다 합치면 `from user import User` 가 되는데요. 

+ 그냥 영어로 "파일 user에서 클래스 User를 가지고 와라"와 의미가 같죠?

+ `user.py` 파일 안에 클래스 정의가 아닌 실행하는 코드가 있으면 `driver.py`에서 임포트 해올 때 실행코드도 실행이 됩니다. 

+ 이걸 방지하기 위해서는 실행 코드를 아래와 같이 `if __name__ == "__main__":` 조건문 안에 넣으셔야 합니다.

```python
if __name__ == "__main__":
    user1 = User("강영훈", "younghoon@codeit.xyz", "123456")
    user2 = User("이윤수", "yoonsoo@codeit.xyz", "abcdef")

    print(user1.name, user1.email, user1.password)
    print(user2.name, user2.email, user2.password)
```

+ 지금 이게 뭘 의미하는지 설명을 드리기엔 객체와 클래스 토픽의 주제를 벗어나는데요.

+ 위 코드의 의미나, 다른 폴더 안에 있는 클래스를 사용하는 방법 등 파이썬의 모듈과 패키지의 작동법에 대해서 더 자세하게 알고 싶으신 분들은 꼭 코드잇 [파이썬 모듈과 패키지](https://www.codeit.kr/topics/python-module-and-package) 토픽을 수강하시는 걸 추천드립니다.