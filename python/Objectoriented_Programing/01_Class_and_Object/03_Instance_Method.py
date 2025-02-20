class User:
    
    """
    함수를 사용해서 객체의 행동을 정의하는 법
    이러한 함수들을 인스턴스 메소드, 짧게는 메소드라고 부른다.
    
    아래의 say_hello 함수는
    모든 인스턴스가 공유하는 행동이기는 하지만 
    각 User 인스턴스의 고유 속성을 활용해서 결과가 다 다르게 나오기 때문에
    인스턴스 메소드라고 부른다.
    """
    # say_hello 함수를 만들고 파라미터로는 임의의 user를 받는다
    def say_hello(some_user):
        # 각 유저에 맞는 인사 메시지를 출력
        print(f"안녕하세요! 저는 {some_user.name}입니다!")
        """
        say_hello 메소드에 user1 인스턴스를 넘기면
        say_hello 파라미터 some_user부분에 user1이 입력되게 되고
        some_user -> user1이 되었으므로
        print 에서 some_user.name 이 user1.name으로 바뀌게 된다
        """

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

# 클래스 안의 메소드를 실행
User.say_hello(user1)   # 안녕하세요! 저는 최우진입니다!
User.say_hello(user2)   # 안녕하세요! 저는 코드잇입니다!

# 인스턴스를 통해서 메소드를 호출
user1.say_hello()  # 안녕하세요! 저는 최우진입니다!
"""
인스턴스 메소드에는 특별한 규칙이 있는데
클래스가 아닌 인스턴스의 메소드를 호출하면
따로 코드를 작성하지 않아도 인스턴스가 메소드의 첫 번째 argument로 자동 전달된다.
따라서 user1을 괄호 안에 따로 작성해줄 필요는 없다.
"""

user1.say_hello(user1)  # TypeError: User.say_hello() takes 1 positional argument but 2 were given
"""
만약 클래스 메소드와 같이 user1을 argument로 넘겨주게 되면
say_hello 메소드는 argument를 하나만 받는데 두 개가 넘어왔다는 오류가 발생한다.

인스턴스를 메소드로 호출할 때 argument로 인스턴스를 또 넘겨주는 코드는 아래와 같다
User.say_hello(user1, user1)
"""