"""
객체를 만들기 위해서는 그 안에 무슨 속성과 행동들을 저장할지 정하는 
모델링이라는 것을 활용한다.

예를 들어 

    - 하나의 User는 name, email, password, following, followers라는 속성을 가지고
    - 행동으로는 소개메시지와 로그인을 할 수 있다라고 한다
    - 또한 이것은 하나의 유저만이 가지는 것이 아니라 모든 유저들이 가지고 있어야 한다.

때문에 많은 언어들에서는 객체에 대한 어떤 설명서 혹은 틀을 정의하고
그 내용을 바탕으로 객체를 만든다'

python에서는 

객체를 만드는 틀을 클래스라고 하고
이것으로 만든 객체는 인스턴스라고 한다.
"""

# User 클래스 생성
# 클래스의 첫 글자는 항상 대문자로 작성해야 한다.
class User: 
    pass

# User 클래스의 인스턴스를 생성한 값을 user1 인스턴스에 저장
user1 = User()
user2 = User()

# type 함수는 자료형의 argument를 리턴하는데
# python에서는 자료형과 클래스는 거의 동일하다
# 따라서 type 함수는 argument로 넘겨준 데이터의 클래스를 리턴해 주는 함수이다.
print(type(user1))  # <class '__main__.User'>
print(type(user2))  # <class '__main__.User'>