class User:
    
    """
    user 인스턴스는 항상 자동으로 함수의 첫 번째 파라미터로 전달된다
    python에서는 이것을 self를 사용하기를 권장하고 있다
    따라서 이전에 some_user로 사용하던 것을 
    모두 아래와 같이 self로 바꾸어 주었다
    """
    
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
    """
    인스턴스 변수와 파라미터 이름이 같아도 문제가 발생하지 않는다
    오른쪽의 email은 파라미터로 넘겨받은 email, password이고
    왼쪽의 경우에는 self 즉, 인스턴스의 email, password 이기 때문이다
    둘은 엄연히 다른 변수이다
    심지어 같은 종류의 변수가 있을 때에도 이렇게 작성하는 것이 매우 일반적이다
    """
    # 유저를 로그인시키는 인스턴스 메소드를 추가
    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
            self.say_hello()
            """
            위와 같은 경우 self를 사용해서 인스턴스 변수만을 사용했는데
            사실 메소드 안에서 다른 메소드를 호출해서 사용할 수도 있다
            예를 들어서
            login 메소드에서 로그인에 성공하게 되면
            각 유저에 맞는 인사 메시지를 출력하고 싶다면
            이미 정의해놓은 메소드를 사용하면 된다.
            
            메소드 안에서는 다른 메소드를 활용할 일이 많은데
            이때는 위와 같이 이미 정의해 놓은 메소드를 활용하면 된다.
            """
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")
            
    
            


user1 = User()

user1.name = "최우진"
user1.email = "qhdksapdlf117@gmail.com"
user1.password = "12345"

user1.login("qhdksapdlf117@gmail.com", "12345") # 로그인 성공, 환영합니다
                                                # 안녕하세요! 저는 최우진입니다!