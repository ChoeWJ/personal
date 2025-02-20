class User:
    
    # 인스턴스 변수 초기화
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
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
    
    # 출력할 내용을 담은 특수메소드 함수
    # __str__ 메소드는 인스턴스가 문자열로 형 변환 될 때 자동으로 호출된다
    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"
        
        
user1 = User("최우진", "qhdksapdlf117@gmail.com", "12345")
user2 = User("코드잇", "codeit@codeit.com", "abcde")

"""
__str__ 함수 생성전

print(user1)    # <__main__.User object at 0x0000019E37612AB0>
print(user2)    # <__main__.User object at 0x0000019E37612B10>
"""

print(str(user1))   # 사용자: 최우진, 이메일: qhdksapdlf117@gmail.com   
print(str(user2))   # 사용자: 코드잇, 이메일: codeit@codeit.com 

# str 함수를 삭제해도 위와 같이 동일한 결괏값을 얻을 수 있다.
print(user1)    # 사용자: 최우진, 이메일: qhdksapdlf117@gmail.com   
print(user2)    # 사용자: 코드잇, 이메일: codeit@codeit.com 