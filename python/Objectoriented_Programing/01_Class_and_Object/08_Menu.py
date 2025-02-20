"""
실습 설명
올해 코드잇 대학교를 졸업한 영훈이는 배달 어플 회사 "여기오"에 취직했습니다. 
"여기오"는 고객들이 배달 음식을 주문할 수 있는 어플을 만들려고 합니다. 
영훈이가 맡게 된 업무는 어플에서 각 배달 음식 메뉴를 나타낼 클래스를 작성하는 건데요.

MenuItem 클래스가 가져야할 다음 조건들을 보고 배달 음식 메뉴를 나타내는 MenuItem 클래스를 정의해 보세요.

인스턴스 변수(타입):

name(문자열): 메뉴 이름
price(숫자): 메뉴 가격
인스턴스 메소드:

__init__: MenuItem 클래스의 모든 인스턴스 변수를 초기화한다.
__str__: MenuItem 인스턴스의 정보를 문자열로 리턴한다. 단, 리턴 형식은 아래의 출력 예시와 같은 형식이어야 한다.
"""
class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} 가격: {self.price}"

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)