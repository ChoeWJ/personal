class User:
    
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
    
    """
    클래스 메소드에는 꼭 알아야 하는 규칙이 있다
        - 클래스 메소드는 인스턴스 대신 클래스가 자동 전달된다.
        - 따라서 인스턴스 메소드에서 사용한 self 대신에 cls라는 이름을 사용한다.
    """
    # 클래스 변수를 사용하는 클래스메소드 생성
    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다.")
        
        
    

user1 = User("최우진", "qhdksapdlf117@gmail.com", "12345")
user2 = User("코드잇", "codeit@codeit.com", "abcde")

# 클래스 메소드 실행
User.print_number_of_users()    # 총 유저 수는: 2입니다.