"""
클래스를 만들고 실행하다보면 간혹 민감한 정보가 드러나거나, 
나오면 안되는 값이 나오는 경우가 있다
이런 문제들이 발생하는 가장 기본적인 이유는
클래스를 사용하는 개발자가 함부로 다루면 안되는 객체의 일부 내용을 마구잡이로 사용하고 있기 떄문이다.
이것을 캡슐화라는 개념을 사용해서 이러한 문제를 방지한다

캡슐화는 두 가지의 정의를 갖는다
    1. 객체의 일부 구현 내용에 대한 외부로부터의 접근을 차단하는 것
    2. 객체의 속성과 그걸 사용하는 행동을 하나로 묶는 것
"""

class Citizen:
    """주민 클래스"""
    drinking_age = 19
    
    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self._age = age                     # _(언더바)를 사용해서 이 기능을 사용하는 개발자에게 접근을 하지 말라고 알려준다.
        self.__resident_id = resident_id    # __(언더바 + 언더바)를 사용하면 조금 더 직접적인 접근을 차단할 수 있다.
        
    def authenticate(self, resident_id):
        """본인 인증 메소드"""
        return self.__resident_id == resident_id
    
    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self._age) + "살입니다!"
    
    
citizen = Citizen("최우진", 32, "12312312")
print(citizen.__resident_id)    # AttributeError: 'Citizen' object has no attribute '__resident_id'

citizen._age = -13
print(citizen._age) # -13
