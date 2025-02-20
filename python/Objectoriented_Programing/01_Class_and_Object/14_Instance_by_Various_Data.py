"""
실습 설명
인스턴스를 생성할 때 필요한 정보들이 항상 우리가 원하는 형태로 존재할까요? 
우리는 다양한 형태의 정보에서 필요한 부분을 뽑아내서 인스턴스를 생성할 수 있어야 합니다.
예를 들어 유저 인스턴스 생성에 필요한 정보가 문자열일 수도 있고 리스트일 수도 있습니다. 
어떻게 각각의 형태에 대응할 수 있을까요? 아래와 같은 User 클래스가 있다고 해보죠.

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

그리고 아래와 같이 서로 다른 형태의 정보를 갖고 유저 인스턴스를 만들어야 한다면?

info_string = "강영훈,younghoon@codeit.kr,123456"
info_list = ["이윤수", "yoonsoo@codeit.kr", "abcdef"]

다양한 형태의 정보로 유저 인스턴스 만들기

# 유저 인스턴스 만들기 (1): 문자열로 인스턴스 만들기
parameter_list = info_string.split(",") # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다

# 각 변수에 분리된 문자열 각각 저장
younghoon_name = parameter_list[0]
younghoon_email = parameter_list[1]
younghoon_password = parameter_list[2]

younghoon = User(younghoon_name, younghoon_email, younghoon_password)

# 유저 인스턴스 만들기 (2): 리스트로 인스턴스 만들기
yoonsoo_name = info_list[0]
yoonsoo_email = info_list[1]
yoonsoo_password = info_list[2]

yoonsoo = User(yoonsoo_name, yoonsoo_email, yoonsoo_password)

# 인스턴스가 제대로 생성되었는지 확인
print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)
"""
# User 클래스 생성
class User:
    # User 클래스의 인스턴스 변수 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # classmethod 데코레이터 생성
    @classmethod
    def from_string(cls, string_params):
        params_list = string_params.split(",")  # 문자열을 ,(쉼표)를 기준으로 분리흐 저장
        
        name = params_list[0]               # 이름은 0번 인덱스
        email = params_list[1]              # 이메일은 1번 인덱스
        password = params_list[2]           # 비밀번호는 2번 인덱스
        
        return cls(name, email, password)   # 인스턴스 생성 후 리턴

    @classmethod
    def from_list(cls, list_params):
        name = list_params[0]
        email = list_params[1]
        password = list_params[2]
        
        return cls(name, email, password)

# 유저 생성 및 초기값 설정
younghoon = User.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo = User.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)