class User:
    
    """
    클래스 변수는 하나의 인스턴스가 갖고 있는 값이 아니라 서로 공유하는 값이다
    어떤 User 인스턴스라도 똑같은 값을 가져야 한다는 의미이다
    클래스 변수 바로 아래에 변수를 지정한다
    """
    
    # 클래스 변수 생성
    count = 0
    
    # 인스턴스 변수 초기화
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        
        User.count += 1
    
    # 유저의 기본 인사말 함수
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
    # 유저를 로그인시키는 인스턴스 메소드를 추가
    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")
    
    # 인스턴스를 문자열로 형 변환
    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"
    

user1 = User("최우진", "qhdksapdlf117@gmail.com", "12345")
user2 = User("코드잇", "codeit@codeit.com", "abcde")

# 클래스 변수값을 가져온다
print(User.count)   # 2