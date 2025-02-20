```python
class User:
    count = 0

    def __init__(self, name, email, pw):
        self.name = name
        self.email = email
        self.pw = pw

        User.count += 1

    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")

    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"


user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")
```

# 클래스 변수를 읽거나 설정하는 법

+ 사실 클래스 변수는 모든 인스턴스들이 공유하는 값이라고 했는데요. 
+ 그렇기 때문에 클래스뿐만 아니라 인스턴스를 통해서도 읽어올 수 있습니다.

```python
print(User.count)   # 출력: 3
print(user1.count)  # 출력: 3
print(user2.count)  # 출력: 3
```
+ 실행해 보면 세 줄 모두 3이 출력됩니다. 
+ 가지고 오는 건 문제가 없는데요. 설정하는 건 인스턴스를 통해서 할 수 없습니다. 
+ user1을 통해서 count에 접근한 후 5를 넣겠습니다.

```python
user1.count = 5

print(User.count)   # 출력: 3
print(user1.count)  # 출력: 5
print(user2.count)  # 출력: 3
```
+ 출력 결과를 보면 user1의 count만 5로 출력되고 나머지는 그대로 3입니다. 왜 그런 걸까요?

+ 생각해 보면 user1.count = 5 이 문법은 인스턴스 변수를 설정할 때 사용하는 문법입니다. 

+ 이렇게 하면, user1 인스턴스에 count라는 새로운 인스턴스 변수가 생기고 그 값이 5로 설정됩니다. 

+ 그러니까 이 코드는 클래스 변수의 값을 설정하는 게 아니라, 

+ 그냥 같은 이름의 인스턴스 변수를 추가하는 거죠.

+ 같은 이름의 클래스 변수와 인스턴스 변수가 둘 다 있으면, 인스턴스 변수가 읽어집니다. 

+ 그래서  user1.count는 클래스 변수 count가 아니라, user1의 인스턴스 변수 count를 나타내는 거죠.

+ 이렇게 헷갈릴 수 있기 때문에, **클래스 변수에 값을 설정할 때는 꼭 클래스를 통해서 해야 합니다.**