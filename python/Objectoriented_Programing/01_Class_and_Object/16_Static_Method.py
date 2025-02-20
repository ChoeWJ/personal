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
    
    
    # 클래스 메소드 생성
    @classmethod
    def print_number_of_users(cls):
        print(f"총 유저 수는: {cls.count}입니다.")
        
    """
    정적 메소드는 인스턴스와 클래스의 관련 내용이 전혀 필요하지 않은 메소드이다
    필요하지는 않지만 직접적인 연관이 있어서
    이를 묶어서 클래스 안에 제공하는 게 좋을 것 같을 때 사용한다.

    또한 self나 cls 처럼 자동으로 전달되는 파라미터가 필요 없다.
    따라서 자동으로 아무거나 전달받기 위해서는 
    클래스 메소드와 비슷하게 decorator를 사용해 주어야 한다.
    """
    # 정적 메소드 생성
    @staticmethod
    def valid_email(email):
        return "@" in email
        
        
    

user1 = User("최우진", "qhdksapdlf117@gmail.com", "12345")
user2 = User("코드잇", "codeit@codeit.com", "abcde")


# 정적 메소드를 호출할때는 클래스를 통해서 호출하는게 더 일반적인 방법이다.
print(User.valid_email("qhdksapdlf117@gmail.com"))  # True
print(User.valid_email("최우진"))   # False