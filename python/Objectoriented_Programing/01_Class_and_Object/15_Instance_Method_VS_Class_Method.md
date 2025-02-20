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
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"

    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다")


user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")
user3 = User("서혜린", "lisa@codeit.kr", "123abc")

# 클래스 메소드 사용
User.print_number_of_users()
```

# 클래스 메소드를 쓰는 이유

+ 이전 영상에서 클래스 메소드 print_number_of_users()를 작성해 봤습니다. 
+ 그런데 print_number_of_users() 메소드는 사실 인스턴스 메소드로 작성해도 됩니다. 이렇게요.
```python
    def print_number_of_users(self):
        print(f"총 유저 수는: {User.count}입니다")
```

+ 인스턴스 메소드에서도 클래스 변수 count를, User.count로 가져올 수 있습니다.

+ 두 메소드를 모두 사용해 볼게요.
```python
user1 = User("강영훈", "younghoon@codeit.kr", "123456")
user2 = User("이윤수", "yoonsoo@codeit.kr", "abcdef")

User.print_number_of_users(user1)
user1.print_number_of_users()
```
실행해 보면

```python
총 유저 수는: 3입니다
총 유저 수는: 3입니다
```
잘 출력됩니다.

+ 그럼 처음에 print_number_of_users() 메소드를 왜 클래스 메소드로 만든 걸까요? 
+ 인스턴스 변수의 값을 읽거나 설정하지 않기 때문이죠. 
+ 실제로 인스턴스 메소드의 바디를 살펴보면 지금 self 파라미터가 한 번도 사용되지 않죠?

+ 하지만 클래스 변수 User.count는 사용하고 있습니다. 
+ 이렇게 인스턴스 변수 말고 클래스 변수만 사용하는 메소드라면 클래스 메소드로 작성해야 합니다.

# 인스턴스 변수 클래스 변수를 둘 다 쓸 때

+ 그럼 인스턴스 변수와 클래스 변수를 둘 다 쓴다면 어떤 메소드를 써야 할까요? 
+ 이건 쉽습니다. 인스턴스 메소드는 인스턴스 변수, 클래스 변수 둘 다 가져올 수 있습니다.

+ 인스턴스 변수는 self를 통해, 클래스 변수는 그냥 클래스 이름에 점을 붙여 가져오면 됩니다. 이렇게요. 

`User.count`

+ 하지만 클래스 메소드에서는 인스턴스 변수를 가져올 수 없습니다. 
+ 클래스가 자동 전달되는 파라미터 cls를 통해 클래스 변수는 가져올 수 있지만, 
+ 인스턴스 변수는 가져올 방법이 없습니다. 
+ 그러니까 인스턴스 변수, 클래스 변수가 둘 다 필요할 때는 인스턴스 메소드를 사용해야 합니다.

# 인스턴스가 없을 때도 사용해야 되는 메소드

+ 인스턴스가 없을 때도, 필요한 메소드면 꼭 클래스 메소드를 사용해야 합니다. 
+ 예를 들어 User.count는 인스턴스가 하나도 없더라도 필요한 정보입니다. 
+ 유저 인스턴스의 개수가 0이라 정보를 사용하고 싶을 수 있으니까요. 
+ `print_number_of_users()` 메소드 또한 유저 인스턴스가 하나도 없더라도 필요하다는 뜻입니다.

한번 확인해 볼게요.

먼저, `print_number_of_users()` 메소드를 다시 클래스 메소드로 바꿔줍시다.
```python
    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다")
```

+ 인스턴스를 생성 코드를 지우고 실행시키면
```python
User.print_number_of_users()
```
```python
총 유저 수는: 0입니다
```

+ 유저 인스턴스 수가 0개라고 잘 출력됩니다. 
+ 지금 인스턴스가 하나도 없는데도 결과가 잘 나왔죠?
+ 이렇게 인스턴스가 하나도 없을 때에도, 사용할 가능성이 있으면 클래스 메소드로 만들어야 합니다.