class User:
    pass

user1 = User()
user2 = User()

# user1의 name, email, password 속성 추가
user1.name = "최우진"
user1.email = "qhdksapdlf117@gmail.com"
user1.password = "12345"

# user2의 name, email, password 속성 추가
user2.name = "코드잇"
user2.email = "codeit@codeit.com"
user2.password = "abcde"

# user1의 email을 출력
print(user1.email)  # qhdksapdlf117@gmail.com

# user2의 비밀번호를 출력
print(user2.password)   # abcde

# 정의하지 않은 인스턴스 변수를 출력하면 오류가 발생한다.
# 따라서 인스턴스 변수를 사용하려면 꼭 그 전에 정의를 해야만 한다.
print(user1.age) # AttributeError: 'User' object has no attribute 'age'

"""
인스턴스에 속성을 추가하는 것은 
변수를 만드는 것과 매우 유사하다.
User 인스턴스에 name이라는 속성을 추가하거나
이미 있는 name속성을 다른것으로 바꾸고 싶다면
위와 같이 .(점)으로 인스턴스와 속성을 연결시켜주고 등호로 값을 주면 된다.

위의 name, email, password처럼
인스턴스 안에 독립적으로 저장된 변수를 인스턴스 변수라고 부른다
따라서 저장된 인스턴스 변수를 꺼내서 사용하면 된다.
"""
