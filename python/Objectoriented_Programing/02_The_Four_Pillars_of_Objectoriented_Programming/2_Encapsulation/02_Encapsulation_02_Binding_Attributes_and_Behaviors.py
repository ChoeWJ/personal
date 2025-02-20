"""
숨긴 변수들을 아예 사용하지 못하면, 클래스 안에 정의한 의미가 없어진다
이때 캡슐화의 두 번째 정의
객체의 속성과 그걸 사용하는 행동을 하나로 묶는 것을 사용하면 된다.

인스턴스 변수를 사용해야 될 때는 가능하면 메소드를 통해서 사용하라는 것
즉, 아래의 authenticate 메소드처럼 숨기고 싶은 변수를 사용해야 할 때는 메소드로 정의해 놓고
이 메소드를 통해서 기능들을 사용할 수 있게 한다.
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
    
    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age
    
    """
    property 데코레이터를 사용하면 메소드를 호출하는 방식이 아니라
    인스턴스 변수에 접근하는 방식으로
    age getter 메소드를 호출할 수 있다.
    """
    @property
    def age(self):
        print("나이에 접근합니다")
        return self._age
    
    @age.setter
    def age(self, value):
        if value < 0:
            print("나이는 0보다 작을 수 없습니다")
        else:
            print("나이를 설정합니다")
            self._age = value
    
    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는" + str(self._age) + "살입니다!"
    
    
citizen = Citizen("최우진", 32, "12312312")
#print(citizen.__resident_id)    # AttributeError: 'Citizen' object has no attribute '__resident_id'

if citizen.can_drink():
    print(f"{citizen.name}은 음주 가능 나이입니다.")    # 최우진은 음주 가능 나이입니다.
    
if citizen.can_drink():
    print(f"{citizen.name}에게 술을 판매할 수 있습니다.") # 최우진에게 술을 판매할 수 있습니다.
    
"""
클래스와 인스턴스를 만들고 아래와 같이
그 안에 있는 변수들에 아무렇게나 접근해서 사용하는 것은 메소드를 사용하는 이유가 없다.

if citizen._age >= 19:
    print(f"{citizen.name}은 음주 가능 나이입니다.")
    
if citizen._age >= 10:
    print(f"{citizen.name}에게 술을 판매할 수 있습니다.")
"""

"""
변수를 사용할 때 항상 메소드로 어떤 구체적인 작업을 하는 게 아니라
그냥 가지고 오거나 수정해야 되는 경우들도 있다

이런경우에 캡슐화를 적용해 본다.
print(citizen.get_age())    # 나이에 접근합니다
                            # 32
"""

print(citizen.age)  # 나이에 접근합니다
                    # 32
                    
citizen.age = -1

print(citizen.age)  # 나이는 0보다 작을 수 없습니다
                    # 나이에 접근합니다
                    # 32

citizen.age = 26

print(citizen.age)  # 나이를 설정합니다
                    # 나이에 접근합니다
                    # 26