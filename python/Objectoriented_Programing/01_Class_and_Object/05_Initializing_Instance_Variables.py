class User:
    
    """
    인스턴스 변수는 항상 사용하기 전에 미리 초기화를 해야 한다.
    그래서 새로운 유저 인스턴스를 만들때마다 일일이 변수들을 다 만들어 줬었는데
    번거롭다
    따라서 변수를 초기화하는 메소드를 구현해서 좀 더 편리하게 접근할 수 있다.
    """
    
    # Magic or Special_Method
    # 특정상황에서 자동으로 호출된다
    # __init__ 메소드는 인스턴스 변수를 초기화할때 자동으로 호출된다
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    """""
    def initialize(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    """
        
    
    def say_hello(self):
        print(f"안녕하세요! 저는 {self.name}입니다!")
    
        # 유저를 로그인시키는 인스턴스 메소드를 추가
    def login(self, email, password):
        if self.email == email and self.password == password:
            print("로그인 성공, 환영합니다")
            self.say_hello()
        else:
            print("로그인 실패, 없는 아이디이거나 잘못된 비밀번호입니다.")
        
        
user1 = User("최우진", "qhdksapdlf117@gmail.com", "12345")
user2 = User("코드잇", "codeit@codeit.com", "abcde")

print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
            
"""
user1 = User()
user1.initialize("최우진", "qhdksapdlf117@gmail.com", "12345")
print(user1.name, user1.email, user1.password)

# user1.name = "최우진"
# user1.email = "qhdksapdlf117@gmail.com"
# user1.password = "12345"

user2 = User()
user2.initialize("코드잇", "codeit@codeit.com", "abcde")
print(user2.name, user2.email, user2.password)

# user2.name = "코드잇"
# user2.email = "codeit@codeit.com"
# user2.password = "abcde"
"""
